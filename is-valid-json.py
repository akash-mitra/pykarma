import json

json_string = input()

try:
    obj = json.loads(json_string)
    print ('Valid')
except ValueError:
    print ('Invalid')