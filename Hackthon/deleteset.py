from facepp import API

def deleteset(outer_id):
    API_KEY = "-PJkamhZzEUkUgv_wvopwTgVSWBVhblr"
    API_SECRET = "1heuneo4ixxDAAAKmHrc_dGIP1NMhxne"
    api_server_international = 'https://api-us.faceplusplus.com/facepp/v3/'
    api = API(API_KEY, API_SECRET)
    api.faceset.delete(outer_id= outer_id, check_empty=0)

if __name__ == '__main__':
    deleteset('faceset')