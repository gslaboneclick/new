import requests
import json
import urllib3
import veemTonbu
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
content_type = "application/vnd.netbackup+json; version=1.0"
X = "true"
import migration

#****************************************************************************************************

# get login or session Token.

#****************************************************************************************************


def perform_login(username, password, base_url, domain_name, domain_type):
	url = base_url + "/login"

	if domain_name != "" and domain_type != "":
		req_body = {"userName": username, "password": password, "domainName": domain_name, "domainType": domain_type}
	else:
		req_body = {"userName": username, "password": password}

	headers = {'Content-Type': content_type}

	print("performing POST on {} for user '{}'\n".format(url, req_body['userName']))

	resp = requests.post(url, headers=headers, json=req_body, verify=False)

	if resp.status_code != 201:
		raise Exception('Login API failed with status code {} and {}'.format(resp.status_code, resp.json()))
	
	return resp.json()['token']


#****************************************************************************************************

#get list of available policies in NBU.

#****************************************************************************************************


def get_netbackup_policies(jwt, base_url):
	url = base_url + "/config/policies"
	headers = {'Content-Type': content_type, 'Authorization': jwt, 'X-NetBackup-Policy-Use-Generic-Schema': X}
	
	# print("\nMaking GET Request to list policies ")
	
	resp = requests.get(url, headers=headers, verify=False)

	
	jsonData = json.loads(resp.content)
	n=jsonData['data']
	
	# print(jsonData['data'][1]['id'])
	poli=[]
	for i in n:
		poli.append(i['id']) 
	
	
	
	
	VMware = []
	Oracle = []

	for i in poli:
			
		url = base_url + "/config/policies/" + i
		global etag
		headers = {'Content-Type': content_type, 'Authorization': jwt}
		resp = requests.get(url, headers=headers, verify=False)
		jsonData = json.loads(resp.content)
		n = jsonData['data']
		n1=n['attributes']
		n2=n1['policy']
		
		if (n2['policyType']=='VMware'):
			VMware.append(n2['policyName'])
		if (n2['policyType']=='Oracle'):
			Oracle.append(n2['policyName'])
	
	
	print("VMware type Policy")
	print("*************************************************")
	for i in VMware:
		print(i)

	# print("*************************************************")
	# print("Oracle type Policy")
	# for i in Oracle:
	# 	print(i)

	
#****************************************************************************************************

#get perticular policy details.

#****************************************************************************************************


def get_netbackup_policy(jwt, base_url):
	
	url = base_url + "/config/policies/" + "datta_1"
	global etag
	headers = {'Content-Type': content_type, 'Authorization': jwt}
	
	print("\nperforming GET on {}\n".format(url))
	
	resp = requests.get(url, headers=headers, verify=False)
	if resp.status_code != 200:
		print('GET Policy API failed with status code {} and {}\n'.format(resp.status_code, resp.json()))
	
	print("\nGet policy details on {} succeeded with status code: {}\n".format("policy1", resp.status_code))
	print("\n The E-tag for the get policy : {}\n".format(resp.headers['ETag']))
	etag = resp.headers['ETag']
	print("\n Json Response body for get policy : \n{}\n".format(json.loads(resp.content)))

#****************************************************************************************************

#Get Storage Units.

#****************************************************************************************************
def get_netbackup_storage(jwt,base_url):

	url = base_url + "/storage/storage-units"
	
	headers = {'Content-Type': content_type, 'Authorization': jwt}
	
	print("\nperforming GET on {}\n".format(url))
	
	resp = requests.get(url, headers=headers, verify=False)
	if resp.status_code != 200:
		print('GET Policy API failed with status code {} and {}\n'.format(resp.status_code, resp.json()))
	
	jsonData = json.loads(resp.content)
	jsonData = jsonData['data']	
	storageUnit=[]
	for i in jsonData:
		storageUnit.append(i['attributes']['storageUnitName'])
	print(storageUnit)

#****************************************************************************************************

#Create VMware policy.

#****************************************************************************************************



def post_netbackup_VMwarePolicy(jwt, base_url,policyType,vmwarePolicyName,storageName,client):
	
	
	vmwarePolicyName=vmwarePolicyName
	storageName=client  
	client=client
	policyType=policyType
	url = base_url + "/config/policies/"
	req_body = {
					"data": {
						"type": "policy",
						"id": vmwarePolicyName,
						"attributes": {
							"policy": {
								"policyName": vmwarePolicyName,
								"policyType": policyType,
								"policyAttributes": {
									"active": True,
									"applicationConsistent": True,
									"applicationDiscovery": True,
									"applicationProtection": [],
									"autoManagedLabel": None,
									"autoManagedType": 0,
									"backupHost": "MEDIA_SERVER",
									"blockIncremental": True,
									"dataClassification": None,
									"disableClientSideDeduplication": False,
									"discoveryLifetime": 28800,
									"effectiveDateUTC": "2018-06-13T18:56:07Z",
									"jobLimit": 2147483647,
									"keyword": "testing",
									"mediaOwner": "*ANY*",
									"priority": 0,
									"secondarySnapshotMethodArgs": None,
									"snapshotMethodArgs": "skipnodisk=0,post_events=1,multi_org=0,Virtual_machine_backup=2,continue_discovery=0,exclude_swap=1,nameuse=0,tags_unset=0,ignore_irvm=1,rLim=10,snapact=3,enable_quiesce_failover=0,drive_selection=0,file_system_optimization=1,disable_quiesce=0,enable_vCloud=0,rTO=0,rHz=10,trantype=san:hotadd:nbd:nbdssl",
									"storage": storageName,
									"storageIsSLP": False,
									"useAccelerator": False,
									"useReplicationDirector": False,
									"volumePool": "NetBackup"
								},
								"clients": [
									{
										"hardware": "VMware",
										"hostName": client,
										"OS": "VMware"
									}
								],
								"schedules": [
									{
										"acceleratorForcedRescan": False,
										"backupCopies": {
											"copies": [
												{
													"failStrategy": None,
													"mediaOwner": None,
													"retentionPeriod": {
														"value": 2,
														"unit": "WEEKS"
													},
													"storage": None,
													"volumePool": None
												}
											],
											"priority": -1
										},
										"backupType": "Full Backup",
										"excludeDates": {
											"lastDayOfMonth": False,
											"recurringDaysOfMonth": [],
											"recurringDaysOfWeek": [],
											"specificDates": []
										},
										"frequencySeconds": 604800,
										"includeDates": {
											"lastDayOfMonth": False,
											"recurringDaysOfMonth": [],
											"recurringDaysOfWeek": [],
											"specificDates": []
										},
										"mediaMultiplexing": 1,
										"retriesAllowedAfterRunDay": False,
										"scheduleName": "test-1",
										"scheduleType": "Frequency",
										"snapshotOnly": False,
										"startWindow": [
											{
												"dayOfWeek": 1,
												"startSeconds": 0,
												"durationSeconds": 0
											},
											{
												"dayOfWeek": 2,
												"startSeconds": 0,
												"durationSeconds": 0
											},
											{
												"dayOfWeek": 3,
												"startSeconds": 0,
												"durationSeconds": 0
											},
											{
												"dayOfWeek": 4,
												"startSeconds": 0,
												"durationSeconds": 0
											},
											{
												"dayOfWeek": 5,
												"startSeconds": 0,
												"durationSeconds": 0
											},
											{
												"dayOfWeek": 6,
												"startSeconds": 0,
												"durationSeconds": 0
											},
											{
												"dayOfWeek": 7,
												"startSeconds": 0,
												"durationSeconds": 0
											}
										],
										"storageIsSLP": False,
										"syntheticBackup": False
									}
								],
								"backupSelections": {
									"selections": [
										"vmware:/?filter=Displayname Equal \"Example-Test\""
									]
								}
							}
						}
					}
				}
	headers = {'Content-Type':content_type, 'Authorization': jwt}
	
	print("\n Making POST Request to create VMware Policy with  out defaults")
	
	resp = requests.post(url, headers=headers, json=req_body, verify=False)
	
	if resp.status_code != 204:
		print('Create Policy API failed with status code {} and {}\n'.format(resp.status_code, resp.json()))
	
	print("\n {} with out defaults is created with status code : {}\n".format("+vmwarePolicyName+",resp.status_code))
	

