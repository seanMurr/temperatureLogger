#!~/Python-3.6.5 python
#/usr/bin/env python3
#s9408574 Sean Michael Murray

import sys, locale, json
from datetime import datetime

def main():
    # print(sys.argv)
    # stdInp =open(sys.stdin)
    data = getTimeInput()
    validateInput(data['data'])

    with open(sys.argv[1],'a') as logFile:
        logFile.write(data['data'])
        logFile.write('\n')

def getTimeInput():
    inp = sys.stdin.read()
    inp = json.loads(inp.strip())
    return inp

def validateInput(dateStamp):
    'try to convert input to dateStamp. exit(1) if fail '
    try:
        time_obj = datetime.strptime(dateStamp,'%H:%M:%S')
    except ValueError:
        print('{"error":"Input not valid"}')
        sys.exit(1)

main()
sys.exit(0)
