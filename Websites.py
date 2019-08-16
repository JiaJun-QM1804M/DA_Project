import requests
url = 'http://172.18.58.238/varsity/'
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t*", r.status_code)
h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t" , x, ":", h.headers[x])
print("**********")
headers = {
    'User_Agent' : "Mobile"
}

url2 = 'http://172.18.58.238/headers.php'
rh = requests.get(url2, headers=headers)
print(rh.text)
