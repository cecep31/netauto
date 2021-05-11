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
            command = "queue type add name=pcq_down kind=pcq pcq-rate={}k pcq-classifier=dst-address \n queue type add name=pcq_upl kind=pcq pcq-rate={}k pcq-classifier=src-address \n queue simple add target=ether3 name=pcq1 queue=pcq_upl/pcq_down \n".format(self.speeddown, self.speedup)
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
    def pcqaddtree(self):
        try:
            pcqdown = "queue type add name=pcq_down kind=pcq pcq-classifier=dst-address,dst-port"
            pcqupl = "queue type add name=pcq_upl kind=pcq pcq-classifier=src-address,src-port"
            command = "queue type add name=pcq_down kind=pcq pcq-classifier=dst-address,dst-port \n queue type add name=pcq_upl kind=pcq pcq-classifier=src-address,src-port"
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
    
    def queueddtree(self,limitdown,limitup):
        try:
            # qtdown = "queue tree add name=download parent=ether3 max-limit={}k".format(self.speeddown)
            # qtdownc = "userdown parent=download packet-mark=down_user queue=pcq_down limit-at={}k max-limit={}k".format(limitatdown,self.speedup)
            # qtupl = "queue tree add name=upload parent=ether1 max-limit={}k".format(self.speedup)
            # qtuplc = "userupl parent=upload packet-mark=upl_user queue=pcq_upl limit-at={}k max-limit={}k".format(limiatup,self.speedup)
            command = "queue tree add name=download parent=ether3 max-limit={}k \n queue tree add name=userdown parent=download packet-mark=down_user queue=pcq_down limit-at={}k max-limit={}k \n queue tree add name=upload parent=ether1 max-limit={}k \n queue tree add name=userupl parent=upload packet-mark=upl_user queue=pcq_upl limit-at={}k max-limit={}k".format(self.speeddown,limitdown,self.speeddown, self.speedup,limitup,self.speedup)
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
            return "Berhasil di aktifkan/diperbarui"

    def tampunganauto2(self):
        # mgldown = "ip firewall mangle add chain=forward dst-address=192.168.1.0/24 action=mark-packet new-packet-mark=down_user passthrough=no"
        # mglupl = "ip firewall mangle add chain=forward src-address=192.168.1.0/24 action=mark-packet new-packet-mark=upl_user passthrough=no"
        # pcqdown = "queue type add name=pcq_down kind=pcq pcq-classifier=dst-address,dst-port"
        # pcqupl = "queue type add name=pcq_upl kind=pcq pcq-classifier=src-address,src-port"
        # qtdown = "queue tree add name=download parent=ether3 max-limit={}k".format(self.speeddown)
        # qtdownc = "userdown parent=download packet-mark=down_user queue=pcq_down limit-at={}k max-limit={}k".format(limitatdown,self.speedup)
        # qtupl = "queue tree add name=upload parent=ether1 max-limit={}k".format(self.speedup)
        # qtuplc = "userupl parent=upload packet-mark=upl_user queue=pcq_upl limit-at={}k max-limit={}k".format(limiatup,self.speedup)
        pass
    
    def autocon2(self, limitatdown):
        if limitatdown != "":
            limitd=int(limitatdown)
        else:
            limitd=1

        limiatup = (limitd/self.speeddown)*self.speedup
        
        self.addmangel()
        self.pcqaddtree()
        x=self.queueddtree(limitd,limiatup)


        return x
        

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


class Routerapi(Remote):
    def __init__(self, host, user, passw, speeddown,speedup):
        super().__init__(host,user,passw,speeddown,speedup)
    
    def connecapi(self):
        connection = routeros_api.RouterOsApiPool(self.host, username=self.user, password=self.passw, plaintext_login=True)
        api = connection.get_api()
        return api

    def manglescan(self,nama):
        api = self.connecapi()
        listmangle=api.get_resource('ip/firewall/mangle')
        showmangle=listmangle.get(new_packet_mark=nama)
        try:
            x=showmangle[0]["id"]
            
        except IndexError:
            x="ok"
       
        return x
    
    def pcqscan(self,nama):
        api = self.connecapi()
        listmangle=api.get_resource('queue/type')
        showmangle=listmangle.get(name=nama)
        try:
            x=showmangle[0]["id"]
            
        except IndexError:
            x="ok"
        return x

    def queuetreescan(self,name):
        api = self.connecapi()
        listmangle=api.get_resource('queue/tree')
        showmangle=listmangle.get(name=name)
        try:
            x=showmangle[0]["id"]
            
        except IndexError:
            x="ok"
       
        return x

    def queuesimplescan(self,name):
        api = self.connecapi()
        listmangle=api.get_resource('queue/simple')
        showmangle=listmangle.get(name=name)
        try:
            x=showmangle[0]["id"]
            
        except IndexError:
            x="ok"
        return x

    def delqueuetree(self):
        pdown=self.queuetreescan("download")
        pup=self.queuetreescan("upload")
        cdown=self.queuetreescan("userdown")
        cup=self.queuetreescan("userupl")
        if (pdown=="ok" and pup=="ok" and cdown=="ok" and cup=="ok"):
            return
        api = self.connecapi()
        listr = api.get_resource('queue/tree')
        listr.remove(id=pdown)
        listr.remove(id=pup)
        listr.remove(id=cdown)
        listr.remove(id=cup)

    def delqueuesimple(self):
        simple=self.queuesimplescan("pcq1")
        
        if (simple=="ok"):
            return
        api = self.connecapi()
        listr = api.get_resource('queue/simple')
        listr.remove(id=simple)

    def delmangle(self):
        down=self.manglescan("down_user")
        up=self.manglescan("upl_user")
        if (down=="ok" and up=="ok"):
            return
        api = self.connecapi()
        listr = api.get_resource('ip/firewall/mangle')
        listr.remove(id=down)
        listr.remove(id=up)

    def delpcq(self):
        down=self.pcqscan("pcq_down")
        up=self.pcqscan("pcq_upl")
        if (down=="ok" and up=="ok"):
            return
        api = self.connecapi()
        listr = api.get_resource('queue/type')
        listr.remove(id=down)
        listr.remove(id=up)

    def delallconfig(self):
        try: 
            self.delmangle()
        except:
            return
        self.delqueuetree()
        self.delpcq()
        self.delqueuesimple()
        return

    def deljustauto1(self):
        try: 
            self.delpcq()
        except:
            return False
        self.delqueuesimple()
        return True
    
    def deljustauto2(self):
        try: 
            self.delmangle()
        except:
            return False
        self.delpcq()
        self.delqueuetree()
        return True

    

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
