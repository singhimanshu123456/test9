import time
def aa(client):
    remote_conn = client.invoke_shell()
    remote_conn.send("ifconfig\n")
    time.sleep(1)
        
    output1 = remote_conn.recv(99999)
    while(remote_conn.recv_ready()):
        time.sleep(1)
        print("hey")
        output1 += remote_conn.recv(999)
    
    return output1