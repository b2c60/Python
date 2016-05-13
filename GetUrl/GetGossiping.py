import requests
payload = {'form': '/bbs/Gossiping/index.html', 'yes': 'yes'}
rs = requests.session()
res = requests.post('https://www.ptt.cc/ask/over18', verify=False, data=payload)
res = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', verify=False)
print(res.text)