import requests

for i in range(10):
    proxies = {
        'https': 'https://125.59.109.103:8080',
    }
    session = requests.Session()
    session.proxies.update(proxies)

    data = session.get('https://devcrawlers.com/ip')
    print(data.content)
