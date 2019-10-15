import requests
from bs4 import BeautifulSoup as bs4
import os
import shutil
import sys
import json

session = requests.get("https://www.cubetutor.com")
cookies = session.cookies.get_dict()
try:
    cardSet = sys.argv[1]
except IndexError:
    cardSet = "10E"

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://www.cubetutor.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,es-419;q=0.8,es;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': f'https://www.cubetutor.com/topcardsbyset/1;jsessionid={cookies["JSESSIONID"]}',
}

data = {
    't:ac': '1',
    't:formdata': 'byjWim5rtLJcD8P4BWZe94Mn6II=:H4sIAAAAAAAAAJWOPQ4BQRSAH4lCdBIRPe1oaKiQqEQkywHezj5rZOxM5j1/l3ECcQmFzh0cQKtS2DiARPsV3/edn1DaN6A+d36EIeHhMSLpMQmTJS0coOtCqtCjXpES9MQSjl2lXSBrYhUjkxrEOUQtY0M2aeaCrW8trpVH7fYuQmECFe0yCc5OcUMC1ckad9i2mKXtSILJ0v7BC5TzaPSN/v4Z/PszC04Tc7SNN4bZuOx6STrL1+leBDj4DxyMK0MBAQAA',
    'setSelect': cardSet,
    't:zoneid': 'topCardsZone'
}
response = bs4(requests.post('https://www.cubetutor.com/topcardsbyset.topcardsform', headers=headers, cookies=cookies, data=data).json()['content'], 'html.parser')
cards = {}

try:
    os.mkdir("cardImages")
except:
    shutil.rmtree("cardImages")
    os.mkdir("cardImages")

for col in response.find_all(class_='compareCubeColumn'):
    card_type = " ".join(col.text.split('\n')[:1])
    links = col.find_all('a')
    for i, line in enumerate(col.text.split('\n')[1:]):
        name = " ".join(line.split(' ')[1:-2])
        occ = "".join(line.split(' ')[-1])
        cards[name] = {
            'occurence': occ,
            'type': card_type,
            'card_url': links[i]['data-image']
        }
        img = requests.get(links[i]['data-image'])
        img_name = "".join(line.split(' ')[1:-2])
        with open(f'cardImages/{img_name}.jpg', 'wb') as i:
            i.write(img.content)

if carrds == {}:
    raise ValueError("It looks like that card set doesn't exist!")
    
with open('cards.txt', 'w') as cr:
    cr.write(json.dumps(cards))
