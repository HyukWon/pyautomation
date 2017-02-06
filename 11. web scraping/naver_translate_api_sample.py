from requests import Request, Session

s = Session()

headers = {
    'X-Naver-Client-Id': 'j58SbrPz_PIM5yY5Idna',
    'X-Naver-Client-Secret': 'OmrbJ9_v6y',
}
text = "Specifically, you'll work with NumPy, Pandas and Matplotlib."
payload = {
    'source': 'en',
    'target': 'ko',
    'text': text,
}
url = 'https://openapi.naver.com/v1/language/translate'

req = Request('POST', url, data=payload, headers=headers)
prepped = req.prepare()

res = s.send(prepped)
res_json = res.json()
print(res_json)
print(res_json['message']['result']['translatedText'])
