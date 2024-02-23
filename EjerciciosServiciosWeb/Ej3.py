import socket
import ipwhois

def get_country(ip):
    try:
        domain = socket.gethostbyaddr(ip)[0]
        obj = ipwhois.IPWhois(domain)
        results = obj.lookup_whois()
        country = results.get('nets')[0].get('country')
        return country
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    ip = input("Enter IP address: ")
    country = get_country(ip)
    if country:
        print(f"The IP address {ip} is registered in {country}.")
    else:
        print("Unable to retrieve country information.")

if __name__ == "__main__":
    main()
