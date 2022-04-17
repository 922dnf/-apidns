import json
import requests
import time
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
client = AcsClient("LTAI5tMCDuUPxhu9fDNNav7W","yLjGO9Mr5GKTjfoVXcqco5l3Uraent","cn-hangzhou")
def get_domain_ip():
    request = DescribeDomainRecordsRequest()
    request.set_accept_format("json")
    request.set_DomainName("dengxiahei.top")
    reponse = client.do_action_with_exception(request)
    data = json.loads(str(reponse,encoding='utf-8'))
    print(data)
    ip =  data['DomainRecords']['Record'][0]['Value']
    recordID = data['DomainRecords']['Record'][0]['RecordId']
    #print(ip)
    #print(recordID)
    return ip,recordID
def get_ip():
    ip = requests.get("https://checkip.amazonaws.com").text.strip()
    return ip
def update_ip(recordid,public_ip):
    request = UpdateDomainRecordRequest()
    request.set_accept_format('json')
    request.set_RecordId(recordid)
    request.set_RR('www')
    request.set_Type('A')
    request.set_Value(public_ip)
    reqonse = client.do_action_with_exception(request)

#domain_ip,domain_recordid = get_domain_ip()
#print(domain_recordid)
domain_ip,domain_recordid = get_domain_ip()
while True:
    save_ip = domain_ip
    public_ip = get_ip()
    if save_ip == public_ip:
        print("ip一致，不更新记录")
    else:
        print("更新记录")
        update_ip(domain_recordid,public_ip)
        save_ip = public_ip
    time.sleep(20)

  

