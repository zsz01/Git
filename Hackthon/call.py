from deleteset import deleteset
from getset import getset
import matplotlib.pyplot as plt
import matplotlib.image as img


API_KEY = "-PJkamhZzEUkUgv_wvopwTgVSWBVhblr"
API_SECRET = "1heuneo4ixxDAAAKmHrc_dGIP1NMhxne"


face_one = './template_file/demo1.jpg'
face_two = './template_file/demo2.jpeg'
face_three = './template_file/demo3.jpg'
face_four = './template_file/demo4.jpg'
outer_id = 'faceset'

face_search = './merge_file/zhy.jpg'

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

ret = api.faceset.create(outer_id= outer_id)
print_result("faceset create", ret)

Face = {}
res = api.detect(image_file=File(face_one))
print_result("person_one", res)
Face['person_one'] = res["faces"][0]["face_token"]

res = api.detect(image_file=File(face_two))
print_result("person_two", res)
Face['person_two'] = res["faces"][0]["face_token"]

res = api.detect(image_file=File(face_three))
print_result("person_three", res)
Face['person_three'] = res["faces"][0]["face_token"]

res = api.detect(image_file=File(face_four))
print_result("person_four", res)
Face['person_four'] = res["faces"][0]["face_token"]

api.faceset.addface(outer_id= outer_id, face_tokens=Face.itervalues())

ret = api.detect(image_file=File(face_search))
print_result("detect", ret)
search_result = api.search(face_token=ret["faces"][0]["face_token"], outer_id=outer_id)

print_result('search', search_result)
print '=' * 60
for k, v in Face.iteritems():
    if v == search_result['results'][0]['face_token']:
        print 'The person with highest confidence:', k
        break

value = {'person_one': face_one, 'person_two':face_two, 'person_three': face_three, 'person_four': face_four}
print(value[k])
dest = img.imread(value[k])
plt.imshow(dest)
plt.axis('off')
plt.show()

deleteset(outer_id)