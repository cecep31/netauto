import ipaddress
import paramiko
import time
import routeros_api
import json
from .models import Routerm
from paramiko.ssh_exception import NoValidConnectionsError

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
        network = self.host+"/24"
        net = ipaddress.ip_network(network, strict=False)
        myscan = networkscan.Networkscan(net)
        myscan.run()
        j = 0
        for i in myscan.list_of_hosts_found:
            j += 1
        return j, net

    def pcq(self):
        j, net = self.scanip()
        
        # stdin, stdout, stderr = self.connectssh().exec_command("ip address print \n interface print ")

       
        try:
            stdin, stdout, stderr = self.connectssh().exec_command(
            "queue simple add target=ether2 name=pcq1 queue=pcq-upload-default/pcq-download-default")
            time.sleep(1)
        except paramiko.AuthenticationException:
            return "gagal untuk login pastikan username dan password benar"
        except paramiko.BadHostKeyException:
            return "proses gagal roueter tidak terhubung"
        except NoValidConnectionsError:
            return "proses gagal roueter tidak terhubung"
        except TimeoutError:
            return "proses gagal karena router tidak menangapi"

        if "already" in stdout.read().decode("ascii"):
            return "Sudah Di Set sebelumnya"
        else:
            return "berhasil di aktifkan"


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
