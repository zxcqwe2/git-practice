import requests


def make_request(url):
    try:
        response = requests.get(url)

        status_code = response.status_code

        if 100 <= status_code < 400:
            print(f"SUCCESS - Status Code: {status_code}")
            print(f"Response Body: {response.text}\n")
        elif 400 <= status_code < 600:
            raise Exception(f"HTTP Error {status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {str(e)}")


endpoints = [
    "https://httpstat.us/200",
    "https://httpstat.us/201",
    "https://httpstat.us/301",
    "https://httpstat.us/404",
    "https://httpstat.us/500"
]

print("Starting HTTP requests to https://httpstat.us\n")

for url in endpoints:
    print(f"Making request to: {url}")
    try:
        make_request(url)
    except Exception as e:
        print(f"ERROR: {str(e)}\n")

print("All requests completed.")