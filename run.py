import requests
import time

while True:
    try:
        response = requests.get("http://localhost:5000/get_cmd")
        if response.ok:
            data = response.json()
            print(data)
        else:
            print('Status Code {}'.format(response.status_code))

    except requests.ConnectionError:
        print('Request failed.')


    time.sleep(0.05)