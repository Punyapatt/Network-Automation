import os
import time
import pexpect
import os, signal


count = 1
server = ''
port = ''
username = ''
password = ''
pid = os.getpid()
f = open('test_file.pid', 'w')
f.write(int(pid))
f.close


cmd = "./forticlientsslvpn/64bit/forticlientsslvpn_cli --server " + server + ":" + port + " --vpnuser " + username

print('Connect VPN')
vpn = pexpect.spawn(cmd)
print(vpn.expect_exact("Password for VPN:"))
if 0 == vpn.expect_exact("Password for VPN:"): vpn.sendline(s=password)
if 0 == vpn.expect_exact("Would you like to connect to this server? (Y/N)"): vpn.sendline(s="y")

while 1:
    if count < 6:
        print(count)
        time.sleep(1)
        count += 1
    else:
        break

f = f.readline().strip()

print('Killing...')
os.kill(int(f), signal.SIGTERM)