import requests
import time
import numpy as np
import params as p

from motors import Motors


if __name__ == '__main__':
    m = Motors()
    while True:
        try:
            response = requests.get("http://localhost:5000/get_cmd")
            if response.ok:
                data = response.json()
                m.set(data['forward'], data['turn'])
            else:
                print('Status Code {}'.format(response.status_code))
                m.set(0, 0)

        except requests.ConnectionError:
            print('Request failed.')
            m.set(0, 0)


        time.sleep(0.05)

    m.stop()