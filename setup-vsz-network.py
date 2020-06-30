import pexpect
import sys

# argument check
if len(sys.argv) != 3:
    print('[VSZ_IP_ADDRESS] [VSZ_PROFILE(E|H)]')
    exit(1)

# input vszIp
vszIp = sys.argv[1]
print('vszIp:', vszIp)

# input vszProfile
vszProfile = sys.argv[2]
print('vszProfile:', vszProfile)


# start vsz conect
con = 'ssh admin@' + vszIp
child = pexpect.spawn(con, encoding='utf-8', logfile=sys.stdout)

# login vsz
child.expect('password:')
child.sendline('admin')
child.expect('>')
child.sendline('enable')
child.expect('Password:')
child.sendline('admin')
child.expect('#')

# setup vsz profile
child.sendline('setup')
child.expect('Select vSZ Profile \(1/2\):')
if vszProfile in ['E', 'e']:
    child.sendline('1')
if vszProfile in ['H', 'h']:
    child.sendline('2')
child.sendline('Y')

# setup vsz ip address
child.expect('Select address type: \(1/2\)')
child.sendline('1')
child.expect('Select IP configuration: \(1/2\)')
child.sendline('2')
child.expect('Primary DNS:')
child.sendline('10.10.10.10')
child.expect('Secondary DNS:')
child.sendline('10.10.10.106')
child.expect('Do you want to apply the settings\? \(y/n\)')
child.sendline('y')
child.expect('#')

# log out
child.sendline('exit')

# end vsz connect
if child.isalive():
    child.close()
