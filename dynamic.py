import requests
import json
import xmltodict, dicttoxml

def callApi(url, metodo, req=None): 
    metodo_http = getattr(requests,metodo)

    r = metodo_http(url, data = req)

    return r
    