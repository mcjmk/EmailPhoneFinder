import requests


def url_input(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text.strip()
