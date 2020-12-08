import requests
import re


def ip_ramziv():
    ramziv_requests = requests.get("https://ramziv.com/ip").text
    rri = ramziv_requests_ip = re.search('\d+\.\d+\.\d+\.\d+', ramziv_requests).group()
    return rri


def ip_yandex():
    yandex_requests = requests.get("https://yandex.ru/internet/").text
    yri = yandex_requests_ip = re.search('\d+\.\d+\.\d+\.\d+', yandex_requests).group()
    return yri


def ip_beget():
    beget_requests = requests.get("https://ip.beget.ru/").text
    bri = beget_requests_ip = re.search('\d+\.\d+\.\d+\.\d+', beget_requests).group()
    return bri


def ip_2ip():
    ip2_requests = requests.get("https://2ip.ru").text
    ip2 = re.search('\d+\.\d+\.\d+\.\d+', ip2_requests).group()
    return ip2
