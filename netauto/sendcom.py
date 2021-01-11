import paramiko
import time

import json

def show_ip(ip_add,username,password):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname=ip_add,username=username,password=password)

    stdin, stdout, stderr = ssh.exec_command("ip address print")

    time.sleep(1)

    output=stdout.read().decode("ascii").strip("\n")
    return output
    pass
