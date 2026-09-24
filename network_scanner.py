#----------- 1. Import ------------

import subprocess

#---------- 2. Nmap check funcation ----------

def check_nmap():
    result = subprocess.run("which nmap", shell=True, text=True, capture_output=True)
    if result.stdout.strip():
        print("Nmap install hai")
        return True
    else:
        print("Nmap install nahi hai")
        return False

#------------ 3. Open Ports Filter Function ----------
def ectract_open_ports(scan_output):
    open_ports = []
    for line in scan_output.split("\n"):
        if "/tcp" in line and "open" in line:
            parts = line.split()
            port = parts[0]
            service = parts[2] if len(parts) > 2 else "unknown"
            open_ports.append({"port": port, "service": service})
    return open_ports

#----------- 4. Summary Function ----------

def show_summary(target, open_ports):
    print("\n" + "=" * 40)
    print("SCAN SUMMARY:", target)
    print("=" * 40)
    if not open_ports:
        print("koi open port nahi mila.")
        return
    print("Total Open port nahi mila.")
    for item in open_ports:
        print(" ", item["port"], "->", item["service"])


#---------- 5. Mian Function -----------

def main():
    print("=" * 40 )
    print("Day 5 - Network Scanner")
    print("=" * 40)

    if not check_nmap():
        return

    target = "127.0.0.1"
    print("\nScanning", target)
    print("=" * 40)

    result = subprocess.run(
        "nmap -sV -p 22,80,443,3306 " + target,
        shell=True, capture_output=True, text=True
    )
    print(result.stdout)

    open_ports = ectract_open_ports(result.stdout)
    show_summary(target, open_ports)


if __name__ == "__main__":
    main()