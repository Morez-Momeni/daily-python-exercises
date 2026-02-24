"""
Problem #12: Validate IPv4 Address and Identify Famous DNS


Problem Statement:
Write a function to check if a given string is a valid IPv4 address.
An IPv4 address consists of four decimal numbers separated by dots,
each in the range 0-255, with no leading zeros (optional constraint).
Additionally, if the IP matches a well-known DNS server, identify it.

"""


def ip_check(ip):
    
    FAMOUS_DNS = {
    "8.8.8.8": "Google Public DNS",
    "8.8.4.4": "Google Public DNS (secondary)",
    "1.1.1.1": "Cloudflare DNS",
    "1.0.0.1": "Cloudflare DNS (secondary)",
    "208.67.222.222": "OpenDNS Home",
    "208.67.220.220": "OpenDNS Home (secondary)",
    "9.9.9.9": "Quad9",
    "149.112.112.112": "Quad9 (secondary)",
    }


    if ip in FAMOUS_DNS:
        return True , f"reconize as {FAMOUS_DNS[ip]}"
    ip = ip.split('.')
    if len(ip) == 4:
        for i in ip:
            if 0 <= int(i) <= 255 :
                continue
            else:
                return False
        return True
    else:
        return False


ip = "1.1.1.1"
print(ip_check(ip))
            
    
        
        
