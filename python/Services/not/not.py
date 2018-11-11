#!~/Python-3.6.5 python
#/usr/bin/env python3
#s9408574 Sean Michael Murray

import sys,json

def main():
    # print(sys.argv)
    # stdInp =open(sys.stdin)
    inp = getInput()
    # print(inp)
    if(inp['data'] == 'False'):
        print('{"data":"True"}')
    elif(inp['data'] == 'True'):
        print('{"data":"False"}')
    else:
        print('{"error":"Input not valid"}')
        sys.exit(1)

def getInput():
    inp = sys.stdin.read()
    inp = inp.strip()
    inp = json.loads(inp)
    return inp

main()
sys.exit(0)
