import ipwhois

def whois_lookup(ip_or_host):
    try:
        obj = ipwhois.IPWhois(ip_or_host)
        results = obj.lookup_whois()
        return results
    except Exception as e:
        return f"Error: {e}"

def main():
    ip_or_host = input("Enter IP address or host address: ")
    whois_result = whois_lookup(ip_or_host)
    print(whois_result)

if __name__ == "__main__":
    main()
