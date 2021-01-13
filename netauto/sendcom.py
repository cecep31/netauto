import paramiko
import time
import routeros_api
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

def show_ipactive(parameter_list):
    host = "192.168.31.1"

    conn = routeros_api.RouterOsApiPool(host, username="admin", password="", plaintext_login=True)
    api= conn.get_api()

    list_ip = api.get_resource('ip/address')
    show_ip = list_ip.get()

    data = json.dumps(show_ip, indent=3)
    conn.disconnect()
    return show_ip
    pass