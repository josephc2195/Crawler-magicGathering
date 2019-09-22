import requests
from bs4 import BeautifulSoup as bs4



cookies = {
    'JSESSIONID': '3F2D6C9BB4DD16EE34326FA02BBDB64E',
    '_ga': 'GA1.2.1810600194.1569118116',
    '_gid': 'GA1.2.194488843.1569118116',
    '_gat': '1',
}

headers = {
    'Pragma': 'no-cache',
    'Origin': 'http://www.cubetutor.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,es-419;q=0.8,es;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'http://www.cubetutor.com/topcardsbyset/1',
}

data = {
    't:ac': '1',
        't:formdata': 'byjWim5rtLJcD8P4BWZe94Mn6II=:H4sIAAAAAAAAAJWOPQ4BQRSAH4lCdBIRPe1oaKiQqEQkywHezj5rZOxM5j1/l3ECcQmFzh0cQKtS2DiARPsV3/edn1DaN6A+d36EIeHhMSLpMQmTJS0coOtCqtCjXpES9MQSjl2lXSBrYhUjkxrEOUQtY0M2aeaCrW8trpVH7fYuQmECFe0yCc5OcUMC1ckad9i2mKXtSILJ0v7BC5TzaPSN/v4Z/PszC04Tc7SNN4bZuOx6STrL1+leBDj4DxyMK0MBAQAA',
            'setSelect': '10E',
                't:zoneid': 'topCardsZone'
}

response = bs4(requests.post('http://www.cubetutor.com/topcardsbyset.topcardsform', headers=headers, cookies=cookies, data=data).json()['content'], 'lxml')
print(response)




