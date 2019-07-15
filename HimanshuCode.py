import paramiko
import os
import time
from datetime import datetime
from new import aa 

if __name__=='__main__':

    print(os.getcwd())
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname = "192.168.0.100", username = "hilnu", password = "Balbirsingh@0", allow_agent=False, look_for_keys=False)
    print("connected")
    try:
        os.mkdir("ios")
    except:
        pass
            
    try:
        os.chdir("ios")
    except:
        pass
            
    
    output1 = aa(client)
    print("File made")
    with open("s.txt","w") as f:
        f.write(output1.decode("utf-8"))
    client.close()
