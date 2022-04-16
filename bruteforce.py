import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
username = ["admin", "password"]
password = ["admin", "password"]
for i in username:
    for j in password:
        try:
            sonuc = ssh.connect("127.0.0.1", admin=i,password=j)
            sonuc.close()
            print("username : ", i,"password", j)
        except:
            pass