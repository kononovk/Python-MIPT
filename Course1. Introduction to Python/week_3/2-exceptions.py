import sys
import requests

url = sys.argv[1]
try:
    response = requests.get(url, timeout=30)
except requests.Timeout:
    print("ошибка timeout, url:", url)
except requests.HTTPError as err:
    code = err.response.status_code
    print("ошибка url: {0}, code: {1}".format(url, code))
except request.RequestException:
    print("ошибка скачивания url:", url)
else:
    print(response.content)