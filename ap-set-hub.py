import pexpect
import sys

# argument check
if len(sys.argv) == 1:
    print('Need Argument')
    exit(1)

# input apIp
apIp = sys.argv[1]
print('apIp:', apIp)

# start ap conect
con = 'ssh ' + apIp
child = pexpect.spawn(con, encoding='utf-8', logfile=sys.stdout)
child.expect('user name')

# end ap connect
if child.isalive():
    child.close()
