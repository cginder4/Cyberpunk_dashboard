skyline = r"""
   |       ____________        
   ||     /            \       
   |||   (    ______    ) 
  |||||   \__/      \__/  
|| SECTOR: 312 || SYSTEM: ONLINE ||
===================================
"""
#custom ascii art in skyline. Default is chicago
import subprocess
import platform
import re
import psutil

def nmap_scan(subnet="192.168.0.0/24"):
    #checking which OS, won't work using sudo on windows & must have for Linux
    if platform.system() == "Windows":
        cmd = [r"C:\Program Files (x86)\Nmap\nmap.exe", "-sn", subnet]
    else:
        cmd = ["sudo", "nmap", "-sn", subnet]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    # Print for debugging
    #print(result.stdout)

    devices = []
    lines = result.stdout.splitlines()
    current_device = {}

    for line in lines:
        if line.startswith("Nmap scan report for"):
            # Start of a new device
            match = re.match(r"Nmap scan report for (.+) \(([\d.]+)\)", line)
            if not match:
                match = re.match(r"Nmap scan report for ([\d.]+)", line)
                if match:
                    hostname = "Unknown"
                    ip = match.group(1)
                else:
                    continue
            else:
                hostname = match.group(1)
                ip = match.group(2)
            current_device = {"IP": ip, "Hostname": hostname}
        elif current_device:
            devices.append(current_device)
            current_device = {}

    return devices

def display_nmap_results():
    devices = nmap_scan()
    output_list = []
    dev_count = 0
    for dev in devices:
        hostname = dev.get("Hostname", "Unknown")
        ip = dev.get("IP", "-")
        macaddress = dev.get("MAC", "no MAC found")
        if hostname == "Unknown" and ip == "-":
            continue
        else:
            dev_count += 1
            output_list.append(f"D{dev_count}: {ip}\nMAC- {macaddress}")
    return output_list

output = display_nmap_results()

def get_system_stats():
    stats = []

    cpu = psutil.cpu_percent(interval=1)
    stats.append(f"CPU Usage: {cpu}%")

    mem = psutil.virtual_memory()
    total_ram = round(mem.total / (1024**3), 2) #byte to GB conversion
    used_ram = round(mem.used / (1024**3), 2)
    stats.append(f"RAM: {used_ram} GB / {total_ram} GB")

    disk = psutil.disk_usage('/')
    total_disk = round(disk.total / (1024**3), 2)
    used_disk = round(disk.used / (1024**3), 2)
    stats.append(f"Disk: {used_disk} GB / {total_disk} GB")

    return stats
