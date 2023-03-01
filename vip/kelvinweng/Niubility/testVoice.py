from aip import AipSpeech

APP_ID = '30817419'
API_KEY= '1VCfu6wxK4v2eMbREm02DsXe'
SECRET_KEY = 'ozoGHmabKzIyPFaO99V8h4kDWicNMC0U'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

result = client.synthesis(' 你真帅啊','zh',1,{
        'spd':3,
        'vol':5,
        'per':111,
    })
print (result)
if not isinstance(result,dict):
    with open('auido.mp3','wb') as f:
        f.write(result)
