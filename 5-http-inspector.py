import urllib.request

def inspect_website(url):
    print(f"\n[+] Auditing URL: {url}")
    try:
        # Create request with a standard User-Agent header
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        
        with urllib.request.urlopen(req) as response:
            print(f"[*] Status Code: {response.getcode()} OK")
            print("[*] Response Headers:")
            for header, value in response.getheaders():
                print(f"    - {header}: {value}")
                
    except Exception as e:
        print(f"[-] Error fetching URL: {e}")

if __name__ == "__main__":
    target = "https://httpbin.org/get"
    inspect_website(target)