#!~/Python-3.6.5 python
#/usr/bin/env python3
#s9408574 Sean Michael Murray

import sys,json

def getInput():
    inp = sys.stdin.read()
    inp = json.loads(inp)
    return inp

def main():
    # print(sys.argv)
    # stdInp =open(sys.stdin)
    inp = getInput()
    # print(inp)
    if(inp['data'] == 'False'):
        sys.exit(1)
    else:
        sys.exit(0)



main()
sys.exit(0)
