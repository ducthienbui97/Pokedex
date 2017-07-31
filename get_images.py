import requests
import json
import os
from io import BytesIO
from PIL import Image

def getPokemon(name, offset = 0, count = 150):
    url = 'https://api.cognitive.microsoft.com/bing/v5.0/images/search'
    params = {'q': name,'count': count,'aspect':'Square'}
    headers = {'Ocp-Apim-Subscription-Key':'REPLACE WITH YOUR KEY'}
    r = requests.get(url, headers=headers,params = params)
    return json.loads(r.text)['value']
def saveImage(url, name):
    r = requests.get(url, timeout = 20)
    image = Image.open(BytesIO(r.content))
    image.save(name)
pokenumber = 0
with open('pokemons.txt','r+') as p:
    for pokemon in p.readlines():
        pokenumber += 1
        cnt = 0
        res = getPokemon(pokemon[:-1] + " pokemon")
        folder = os.path.join('data','train','{:03d}'.format(pokenumber) + '_' +pokemon[:-1])
        if not os.path.exists(folder):
            os.makedirs(folder)
        for data in res:
            try:
                if data['encodingFormat'] in set(['png','jpeg']):
                    saveImage(data['contentUrl'], os.path.join(folder,str(cnt) + '.' + data['encodingFormat']))
                    cnt += 1
            except:
                pass
        print(pokemon[:-1],cnt)