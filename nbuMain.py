import sys
import nbuUtility1
import json
import texttable as tt
import migration
# import addClient

def get_policies():
	
		protocol = "https"
		nbmaster = "10.136.59.234"
		username = "Administrator"
		password = "gsLab123"
		domainname = ""
		domaintype = ""
		port = 1556
		
		base_url = protocol + "://" + nbmaster + ":" + str(port) + "/netbackup"

		jwt = nbuUtility1.perform_login(username, password, base_url, domainname, domaintype)

		

		
# get_policies()

def get_policy():
		protocol = "https"
		nbmaster = "10.136.59.234"
		username = "Administrator"
		password = "gsLab123"
		domainname = ""
		domaintype = ""
		port = 1556

		base_url = protocol + "://" + nbmaster + ":" + str(port) + "/netbackup"

		jwt = nbuUtility1.perform_login(username, password, base_url, domainname, domaintype)

		nbuUtility1.get_netbackup_policy(jwt,base_url)

# get_policy()

def getStorage():
		protocol = "https"
		nbmaster = "10.136.59.234"
		username = "Administrator"
		password = "gsLab123"
		domainname = ""
		domaintype = ""
		port = 1556

		base_url = protocol + "://" + nbmaster + ":" + str(port) + "/netbackup"

		jwt = nbuUtility1.perform_login(username, password, base_url, domainname, domaintype)

		nbuUtility1.get_netbackup_storage(jwt,base_url)

getStorage()



# def add_Cli():
# 		protocol = "https"
# 		nbmaster = "10.136.59.234"
# 		username = "Administrator"
# 		password = "gsLab123"
# 		domainname = ""
# 		domaintype = ""
# 		port = 1556

# 		base_url = protocol + "://" + nbmaster + ":" + str(port) + "/netbackup"

# 		jwt = nbuUtility1.perform_login(username, password, base_url, domainname, domaintype)

# 		addClient.post_client(jwt,base_url)

# add_Cli()
