"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
"""
import requests
import fake_useragent
from bs4 import BeautifulSoup

session = requests.Session()

url = "https://e-schools.info/m/login"
user = fake_useragent.UserAgent().random

header = {
    "user-agent": user
}

data = {
    'form-sent': "1",
    'username': "Nimod",
    'password': "22072007Dimon"
}

response = session.post(url, data=data, headers=header, verify=False).text

print(response)

# TODO: Авторизация
# TODO: Парсинг
# TODO: Flask

