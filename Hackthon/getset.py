import requests
from facepp import API, File
from json import JSONDecoder
import base64

def getset():
    API_KEY = "-PJkamhZzEUkUgv_wvopwTgVSWBVhblr"
    API_SECRET = "1heuneo4ixxDAAAKmHrc_dGIP1NMhxne"
    api_server_international = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets'
    api = API(API_KEY, API_SECRET)
    data = {"api_key":API_KEY, "api_secret":API_SECRET}
    response = requests.post(api_server_international, data = data)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    print(req_dict['facesets'])

if __name__ == '__main__':
    getset()