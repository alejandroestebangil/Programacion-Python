import requests
import time

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is up.")
        else:
            print(f"{url} is down (status code: {response.status_code}).")
    except Exception as e:
        print(f"Error: {e}")
        print(f"{url} is down.")

def main():
    url = input("Enter the URL to monitor: ")
    interval = int(input("Enter the interval in seconds between checks: "))

    while True:
        check_website(url)
        time.sleep(interval)

if __name__ == "__main__":
    main()
