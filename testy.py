import urllib3

http = urllib3.PoolManager()

response = http.request("GET", "https://django-vue-js.auth0.com/.well-known/jwks.json")

print(response.data.decode("utf-8"))