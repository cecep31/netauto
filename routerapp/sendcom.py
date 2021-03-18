import paramiko
import time
import routeros_api
import json
from .models import Routerm


class Remote:
    def __init__(self, host, user, passw, speed):
        self.host = host
        self.user = user
        self.passw = passw
        self.speed = speed

    def connectssh(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(hostname=self.host, username=self.user,
                    password=self.passw)

        return ssh

    def scanip(self):
        import networkscan

        check = "192.168.1.0/24"
        myscan = networkscan.Networkscan(check)
        myscan.run()
        data = myscan.list_of_hosts_found
        
        return data

    def pcq(self):
        stdin, stdout, stderr = self.connectssh().exec_command("ip address print \n")
        time.sleep(1)

        return stdout


def show_ip(ip_add, username, password):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname=ip_add, username=username, password=password)

    stdin, stdout, stderr = ssh.exec_command("ip address print")

    time.sleep(1)

    output = stdout.read().decode("ascii").strip("\n")
    return output, stderr
    pass


def show_ipactive(parameter_list):
    host = "192.168.31.1"

    conn = routeros_api.RouterOsApiPool(
        host, username="admin", password="", plaintext_login=True)
    api = conn.get_api()

    list_ip = api.get_resource('ip/address')
    show_ip = list_ip.get()

    data = json.dumps(show_ip, indent=3)
    conn.disconnect()
    return show_ip
    pass


def sendpcq1(id):
    r = Routerm.objects.get(id=id)
    host = r.host
    username = r.user
    password = r.password

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname=host, username=username, password=password)

    stdin, stdout, stderr = ssh.exec_command("ls \n ip address print")

    time.sleep(1)

    output = stdout.read().decode("ascii").strip("\n")

    return output
    pass
