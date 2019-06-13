import json

data = {}
data['song_name'] = 'Comfortably Numb'
data['artist'] = 'Pink Floyd'
data['album'] = 'The Wall'

json_string = str(json.dumps(data))
print(json_string)