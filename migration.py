import veemTonbu
import ipaddress
import getpass

def migrationOption(argument): 
    if argument==1:
        print("\n****************NBU to Veeam****************")
        nbumasterIP= input("\nEnter NBU Master IP address : ")
        nbuUsername= input("Enter NBU Master username : ")
        nbuPassword = input("Enter NBU Master password : ")
        #nbuToveeam.migrate(nbumasterIP,nbuUsername,nbuPassword)

    elif argument==2:
        print("\n***************Veeam to NBU******************")
        veeamIP= input("\nEnter Veeam IP address : ")
        veeamUsername= input("Enter Veeam username : ")
        veeamPassword = input("Enter Veeam password : ")
        veemTonbu.migrate(veeamIP,veeamUsername,veeamPassword)

    else:
        print("Invalid choice....")





# Driver program 
if __name__ == "__main__": 

    print("\n======= Migration option ======== \n\n 1. NBU to Veeam \n 2. Veeam to NBU")
   
    argument= int(input("\nEnter your choice: "))

    print (migrationOption(argument))