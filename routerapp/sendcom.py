import paramiko
import time
import routeros_api
import json
from .models import Routerm
from paramiko.ssh_exception import NoValidConnectionsError


class Remote:
    def __init__(self, host, user, passw, speeddown, speedup):
        self.host = host
        self.user = user
        self.passw = passw
        self.speeddown = speeddown
        self.speedup = speedup

    def connectssh(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(hostname=self.host, username=self.user,
                    password=self.passw)

        return ssh

    def scanip(self, host):
        import networkscan
        network = host+"/24"
        # net = ipaddress.ip_network(network, strict=False)
        myscan = networkscan.Networkscan(network)
        myscan.run()
        j = 0
        for i in myscan.list_of_hosts_found:
            j += 1
        return j

    def autocon1(self):

        # stdin, stdout, stderr = self.connectssh().exec_command("ip address print \n interface print ")
        try:
            # stdin, stdout, stderr = self.connectssh().exec_command(
            # "queue simple add target=ether2 name=pcq1 queue=pcq-upload-default/pcq-download-default")
            command = "queue type add name=pcqdown kind=pcq pcq-rate={}k pcq-classifier=dst-address \n queue type add name=pcqup kind=pcq pcq-rate={}k pcq-classifier=src-address \n queue simple add target=ether2 name=pcq1 queue=pcqup/pcqdown \n".format(
                self.speeddown, self.speedup)
            stdin, stdout, stderr = self.connectssh().exec_command(command)
            time.sleep(1)
        except paramiko.AuthenticationException:
            return "Gagal untuk login pastikan username dan password benar"
        except paramiko.BadHostKeyException:
            return "Proses gagal roueter tidak terhubung"
        except NoValidConnectionsError:
            return "Proses gagal roueter tidak terhubung"
        except TimeoutError:
            return "Proses gagal karena router tidak menangapi"

        if "already" in stdout.read().decode("ascii"):
            return "Sudah Di Set sebelumnya"
        else:
            return "berhasil di set"

    def addmangel(self):
        try:
            mgldown = "ip firewall mangle add chain=forward dst-address=192.168.1.0/24 action=mark-packet new-packet-mark=down_user passthrough=no"
            mglupl = "ip firewall mangle add chain=forward src-address=192.168.1.0/24 action=mark-packet new-packet-mark=upl_user passthrough=no"
            command = "ip firewall mangle add chain=forward dst-address=192.168.1.0/24 action=mark-packet new-packet-mark=down_user passthrough=no \n ip firewall mangle add chain=forward src-address=192.168.1.0/24 action=mark-packet new-packet-mark=upl_user passthrough=no"
            stdin, stdout, stderr = self.connectssh().exec_command(command)
            time.sleep(1)
        except paramiko.AuthenticationException:
            return "Gagal untuk login pastikan username dan password benar"
        except paramiko.BadHostKeyException:
            return "Proses gagal roueter tidak terhubung"
        except NoValidConnectionsError:
            return "Proses gagal roueter tidak terhubung"
        except TimeoutError:
            return "Proses gagal karena router tidak menangapi"
        outnya = stdout.read().decode("ascii")
        if "already" in outnya:
            return "Sudah Di Set sebelumnya"
        else:
            return outnya

    def tampunganauto2(self):
        mgldown = "ip firewall mangle add chain=forward dst-address=192.168.1.0/24 action=mark-packet new-packet-mark=down_user passthrough=no"
        mglupl = "ip firewall mangle add chain=forward src-address=192.168.1.0/24 action=mark-packet new-packet-mark=upl_user passthrough=no"
        pcqdown = "queue type add name=pcq_down kind=pcq pcq-classifier=dst-address,dst-port"
        pcqupl = "queue type add name=pcq_upl kind=pcq pcq-classifier=src-address,src-port"
        qtdown = "queue tree add name=download parent=ether3 max-limit={}k".format(self.speeddown)
        qtdownc = "userdown parent=download packet-mark=down_user queue=pcq_down limit-at={}k max-limit={}k".format(limitatdown,self.speedup)
        qtupl = "queue tree add name=upload parent=ether1 max-limit={}k".format(self.speedup)
        qtuplc = "userupl parent=upload packet-mark=upl_user queue=pcq_upl limit-at={}k max-limit={}k".format(limiatup,self.speedup)
    
    def autocon2(self, limitatdown):
        limitatd=int(limitatdown)
        limiatup = (limitatd/self.speeddown)*self.speedup
        
        self.addmangel()

        return 
        

    def command(self, command):
        try:
            stdin, stdout, stderr = self.connectssh().exec_command(command)
            time.sleep(1)
        except paramiko.AuthenticationException:
            return "Gagal untuk login pastikan username dan password benar"
        except paramiko.BadHostKeyException:
            return "Proses gagal roueter tidak terhubung"
        except NoValidConnectionsError:
            return "Proses gagal roueter tidak terhubung"
        except TimeoutError:
            return "Proses gagal karena router tidak menangapi"
        except paramiko.SSHException:
            return "gagal disebabkan ndak tau mungkin config manual commad"

        return stdout.read().decode('ascii')


def show_ip(ip_add, username, password):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname=ip_add, username=username, password=password)

    stdin, stdout, stderr = ssh.exec_command("ip address print")

    time.sleep(1)

    output = stdout.read().decode("ascii").strip("\n")
    return output, stderr
    pass

# this commant


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
