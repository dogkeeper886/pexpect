import pexpect
import sys

# argument check
if len(sys.argv) != 2:
    print('[VSZ_IP_ADDRESS]')
    exit(1)

# input vszIp
vszIp = sys.argv[1]
print('vszIp:', vszIp)

# start vsz conect
con = 'ssh admin@' + vszIp
child = pexpect.spawn(con, encoding='utf-8', logfile=sys.stdout)
child.timeout = 1800

# login vsz
child.expect('password:')
child.sendline('admin')
child.expect('>')
child.sendline('enable')
child.expect('Password:')
child.sendline('admin')
child.expect('#')

# start setup
child.sendline('setup')

# skip network setup
child.expect('Do you want to setup network\? \(y/n\)')
child.sendline('N')

# create cluster
child.expect('\(C\)reate a new cluster or \(J\)oin an exist cluster \(c/j\):')
child.sendline('c')
child.expect('Cluster Name \(cluster name can contain letters \(a-z, A-Z\), numbers \(0-9\), and dashes \(-\)\):')
child.sendline('Cluster-vSZ-1')
child.expect('Controller Description:')
child.sendline('vSZ-1')
child.expect('Are these correct \(y/n\):')
child.sendline('y')
child.expect('Is this controller behind NAT\? \(y/n\)')
child.sendline('n')
child.expect('NTP Server \([a-zA-Z0-9.-]\): [ntp.ruckuswireless.com]')
child.sendline('tock.stdtime.gov.tw')
child.expect('Convert ZoneDirector APs in factory settings to vSZ APs automatically \(y/n\) [N]')
child.sendline('N')
child.expect('Enter admin password:')
child.sendline('admin\!234')
child.expect('Enter admin password again:')
child.sendline('admin\!234')
child.expect('Enter the CLI enable command password:')
child.sendline('admin\!234')
child.expect('Enter the CLI enable command password again:')
child.sendline('admin\!234')
child.expect('Setup configurations done. Starting setup process after 5 seconds...')
child.sendline('')

child.expect('Press the enter key to continue.')
child.sendline('')

# log out
#child.sendline('exit')

# end vsz connect
if child.isalive():
    child.close()
