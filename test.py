import os
import time
import pexpect

server = '203.151.106.139'
port = '10443'
username = 'punyapat.pl'
password = '1Net@Infra01'
pid = os.getpid()
# f = open('test_file.pid', 'r')
# f = f.readline().strip()

cmd = './forticlientsslvpn/64bit/forticlientsslvpn_cli --server serveraddress:port --vpnuser username'

vpn = peexpect.spawn(cmd)
print(vpn.expect_exact("Password for VPN:"))
