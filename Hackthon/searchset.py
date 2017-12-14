API_KEY = "-PJkamhZzEUkUgv_wvopwTgVSWBVhblr"
API_SECRET = "1heuneo4ixxDAAAKmHrc_dGIP1NMhxne"
from getdetail import getdetail
outer_id = 'faceset'

face_search = './template_file/demo2.jpeg'

api_server_international = 'https://api-us.faceplusplus.com/facepp/v3/'

from pprint import pformat

def print_result(hit, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(v): encode(k) for (v, k) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hit
    result = encode(result)
    print '\n'.join("  " + i for i in pformat(result, width=75).split('\n'))

from facepp import API, File

api = API(API_KEY, API_SECRET)

ret = api.detect(image_file=File(face_search))
print_result("detect", ret)
print '=' * 60
search_result = api.search(face_token=ret["faces"][0]["face_token"], outer_id=outer_id)
print_result('search', search_result)
print '=' * 60
