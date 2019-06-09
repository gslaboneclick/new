import requests
from configparser import ConfigParser
import json
content_type="application/xml; charset=utf-8"


# *************************************************************************************

# getting authorization Token

# *************************************************************************************
        
def get_authorize_token(ip, username, password):
        ip = ip
        username = username
        password = password

        base_url = "http://"+ip+":9399"
        session_id = requests.post(base_url + '/api/sessionMngr/?v=latest', auth = (username, password))
        
        # print(session_id)
        # print(session_id.headers['X-RestSvcSessionId'])

        if session_id.status_code != 201:
            print('Authorization failed')
        session_id=session_id.headers['X-RestSvcSessionId']
        # print(session_id)
        return session_id
        
# get_authorize_token()    


#*******************************************************************************************

# getting jobs from veeam

#*******************************************************************************************

def getJobs():

    # ip= ip
    # username= username
    # password= password

    ip= "10.136.59.233"
    username= "Administrator"
    password= "lc@123"

    url="http://"+ip+"/api/jobs"
    auth_token=get_authorize_token(ip,username,password)
    headers = {'Content-Type': content_type,'X-RestSvcSessionId': auth_token,'accept':'application/json' }
	
	# print("\nMaking GET Request to list policies ")
	
    resp = requests.get(url, headers=headers, verify=False)

    if resp.status_code != 200:
        raise Exception('Jobs API failed with status code {} and {}'.format(resp.status_code, resp.json()))

    jobs=[]
    jsonData = json.loads(resp.text)
    jsonData = jsonData['Refs']
    for i in jsonData:
        jobs.append(i['Name'])
    
    return jobs
    print("JOBs LIST")
    for i in jobs:
        print(i)


getJobs()

#*******************************************************************************************

# getting job details from veeam

#*******************************************************************************************

def getJobinfo(ip,username,password):
    
    ip= ip
    username= username
    password= password

    url="http://"+ip+"/api/jobs"
    auth_token=get_authorize_token()
    headers = {'Content-Type': content_type,'X-RestSvcSessionId': auth_token,'accept':'application/json' }
    
	# print("\nMaking GET Request to list policies ")
	
    resp = requests.get(url, headers=headers, verify=False)

    if resp.status_code != 200:
        raise Exception('Login API failed with status code {} and {}'.format(resp.status_code, resp.json()))

    jobs=[]
    jsonData = json.loads(resp.content)
    jsonData = jsonData['Refs']
    for i in jsonData:
        jobs.append(i['Name'])
    print("JOBs LIST")
    for i in jobs:
        print(i)

    
    url="http://10.136.59.233:9399/api/jobs"+"/a132890d-371a-42d4-b42d-631476cc18f5?format=Entity"
    # auth_token=get_authorize_token()          
    headers = {'Content-Type': content_type,'X-RestSvcSessionId': auth_token,'accept':'application/json' }
	
	# print("\nMaking GET Request to list policies ")
	
    resp = requests.get(url, headers=headers, verify=False)
    print(resp)
    if resp.status_code != 200:
        raise Exception('Login API failed with status code {} and {}'.format(resp.status_code, resp.json()))

    jsonData = json.loads(resp.content)
    return jsonData

# getJobinfo()














