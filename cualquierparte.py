import dynamic
import os, json

def read_folder():
    result = []
    path = 'peticiones/'
    fileList = os.listdir(path)
    for i in fileList:
        file = open('peticiones/'+ i, 'r')
        result.append(json.loads(file.read()))    
    return result


def resultado():
    result = read_folder()
    for data in result:
        r = dynamic.callApi(data["url"], data["metodo"])
        print(r.text)

resultado()