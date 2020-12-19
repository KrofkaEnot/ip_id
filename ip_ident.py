import requests
import re

from requests.exceptions import SSLError


def ip_ramziv():
    try:
        ramziv_requests = requests.get("https://ramziv.com/ip").text
        rri = ramziv_requests_ip = re.search('\d+\.\d+\.\d+\.\d+', ramziv_requests).group()
        return rri
    except SSLError:
        return ('Недоступен!')
    except:
        return ('Ошибка запроса!')


def ip_yandex():
    try:
        yandex_requests = requests.get("https://yandex.ru/internet/").text
        yri = yandex_requests_ip = re.search('\d+\.\d+\.\d+\.\d+', yandex_requests).group()
        return yri
    except SSLError:
        return ('Недоступен!')
    except:
        return ('Ошибка запроса!')


def ip_beget():
    try:
        beget_requests = requests.get("https://ip.beget.ru/").text
        bri = beget_requests_ip = re.search('\d+\.\d+\.\d+\.\d+', beget_requests).group()
        return bri
    except SSLError:
        return ('Недоступен!')
    except:
        return ('Ошибка запроса!')


def ip_2ip():
    try:
        ip2_requests = requests.get("https://2ip.ru").text
        ip2 = re.search('\d+\.\d+\.\d+\.\d+', ip2_requests).group()
        return ip2
    except SSLError:
        return ('Недоступен!')
    except:
        return ('Ошибка запроса!')

