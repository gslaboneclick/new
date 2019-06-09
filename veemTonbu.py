import veeamUtility
import nbuUtility1
import requests
from configparser import ConfigParser
import json
content_type="application/xml; charset=utf-8"


def migrate(ip,user,passwd):
    
    veeamIp= ip
    veeamUsername= user
    veeamPassword= passwd
    
    #get veem Jobs Names
    jobs = veeamUtility.getJobs(veeamIp,veeamUsername,veeamPassword)
    
    #get veem Jobs Names
    jobDetails = veeamUtility.getJobinfo(veeamIp,veeamUsername,veeamPassword)
    
    policyType=jobDetails['Platform']
    
    vmwarePolicyName=jobDetails['Name']
    
    storageName=""# call getStorage method from nbuMain file.
    
    client= jobDetails['JobInfo']['BackupJobInfo']['Includes']['ObjectInJobs']   
    for i in client:
        client=i['Name']








































#     protocol = "https"
#     nbmaster = ip
#     username = user
#     password = passwd
#     domainname = ""
#     domaintype = ""
#     port = 1556
    
#     base_url = protocol + "://" + nbmaster + ":" + str(port) + "/netbackup"

#     jwt = nbuUtility1.perform_login(username, password, base_url, domainname, domaintype)
        
    
#     nbuUtility1.post_netbackup_VMwarePolicy(jwt, base_url,policyType,vmwarePolicyName,storageName,client)
    

# # migrate()