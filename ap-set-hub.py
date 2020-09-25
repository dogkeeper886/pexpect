import pexpect
import sys

# argument check
if len(sys.argv) != 2:
    print('[AP_IP_ADDRESS]')
    exit(1)

# input apIp
apIp = sys.argv[1]
print('apIp:', apIp)

# start ap conect
con = 'ssh ' + apIp
child = pexpect.spawn(con, encoding='utf-8', logfile=sys.stdout)

# login ap
child.expect('Please login:')
child.sendline('super')
child.expect('password :')
child.sendline('sp-admin')
child.expect('rkscli:')

# set hub
child.sendline('set hub host aprqa.ruckuswireless.com')
child.expect('OK')
child.sendline('reboot')
child.expect('OK')

# log out
child.sendline('exit')

# end ap connect
if child.isalive():
    child.close()
