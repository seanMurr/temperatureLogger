#!~/Python-3.6.5 python
#/usr/bin/env python3
#s9408574 Sean Michael Murray

import sys
from subprocess import run, PIPE

command = ['date', sys.argv[1]]

# print('command: '+ str(command))

result = run(command, stdout=PIPE, input='', encoding='utf-8')
#check if proces was successful
if result.returncode == 0:
    result = result.stdout.strip()
    print('{"data":"'+str(result)+'"}')
else:
    # error in service. Send error state and message
    print('{"error":"Date command was not successful"}')
    sys.exit(1)
sys.exit(0)
