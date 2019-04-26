import dynamic

obj = {
    "name": "Laura",
    "age": 25,
    "email": "laurajquinchia@gmail.com"
}

r= dynamic.callApi('https://jsonplaceholder.typicode.com/posts/1', 'delete', obj)

print(r.text)