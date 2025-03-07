# move only excel files
import os
import shutil
import paramiko
ssh_client = paramiko.SSHClient()
host = "demo.wftpserver.com"
username = "demo"
password = "demo"
port = 2222

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname=host,port=port,username=username,password=password)

print('connection established successfully') 

ftp = ssh_client.open_sftp()

files = ftp.listdir("download")

for i, file in enumerate(files):
    if file.endswith(".xlsx"):
        ftp.get(f'/download/{file}', f'C:/Users/adebb/destination_folder2/{file}')

        print(f'Moved {file}')

print("Listing all the files and Directory: ",files)

ssh_client.close()

