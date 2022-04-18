import requests                                    
pageURL='http://ipv6.ipv6-test.ch/ip/?callback=?'
content=requests.get(pageURL).text.strip("callback")
data = eval(content)
print(data['ip'])

#获取ipv6的地址，用于ddns地址更新



