import requests

r = requests.get('https://imgs.xkcd.com/comics/python.png')

# print(r.content)   
print(r.status_code)
print(r.headers)

# with open('comic.png','wb') as f:
#     f.write(r.content)



