import requests
import base64
import matplotlib.pyplot as plt
import matplotlib.image as img
from json import JSONDecoder

http_url = "https://api-cn.faceplusplus.com/imagepp/v1/mergeface"
key = "-PJkamhZzEUkUgv_wvopwTgVSWBVhblr"
secret = "1heuneo4ixxDAAAKmHrc_dGIP1NMhxne"
rectangle = []
rectangle.append('')                                    ## 空着
rectangle.append('175,49,301,301')                      ##demo1(jpg)
rectangle.append('359,197,483,483')                     ##demo2(jpeg)
rectangle.append('339,107,296,296')                        ##demo3(jpg)
rectangle.append('282,81,348,348')                        ##demo4(jpg)
merge_file = r"C:\Users\heyon\Desktop\merge_file\zhy.jpg"
template_file = r"C:\Users\heyon\Desktop\template_file\demo2.jpeg"

opt = int(input('请输入换脸号:'))
merge_rate = input('请输入换脸程度:')
if opt == 1:
    template_file = r"C:\Users\heyon\Desktop\template_file\demo1.jpg"
elif opt == 2:
    template_file = r"C:\Users\heyon\Desktop\template_file\demo2.jpeg"
elif opt == 3:
    template_file = r"C:\Users\heyon\Desktop\template_file\demo3.jpg"
elif opt == 4:
    template_file = r"C:\Users\heyon\Desktop\template_file\demo4.jpg"
else:
    template_file = r"C:\Users\heyon\Desktop\template_file\demo2.jpg"##默认值

data = {"api_key": key, "api_secret": secret, "template_rectangle": rectangle[opt], "merge_rate": merge_rate}
files = {"template_file": open(template_file, "rb"), "merge_file": open(merge_file, "rb")}
response = requests.post(http_url, data = data, files = files)
req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)

a = base64.b64decode(req_dict['result'])
f = open('pict.jpg','wb')
f.write(a)
f.close()
dest = img.imread('pict.jpg')
plt.imshow(dest)
plt.axis('off')
plt.show()
