#!~/Python-3.6.5 python
#/usr/bin/env python3
#s9408574 Sean Michael Murray

import sys, json
from datetime import datetime

def main():
    # print(sys.argv)
    # stdInp =open(sys.stdin)
    timeStamp = getTimeInput()
    if(timeStamp < datetime.strptime('12:00:00','%H:%M:%S').time()):
        print('{"data":"True"}')
    else:
        print('{"data":"False"}')

def getTimeInput():
    try:
        inp = sys.stdin.read()
        inp = json.loads(inp)
        time_obj = datetime.strptime(inp['data'],'%H:%M:%S').time()
    except ValueError:
        print('{"error":"Input not valid"}')
        sys.exit(1)

    return time_obj

main()
sys.exit(0)
