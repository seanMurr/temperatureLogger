#!/usr/bin/env python3.6
# usage testing.php "{data:[dataToSend], functName: [functName], deviceID: [deviceID], acessToken: [accessToken]}"

import sys, json
import urllib.parse
import urllib.request

def main():
    data = getArgObj()
    url = "https://api.particle.io/v1/devices/" + data['deviceID'] + "/" + data['functName']
    params = {"args": data['data'], "access_token": data['accessToken']}

    # print(url)
    # print(params)

    query_string = urllib.parse.urlencode( params )
    data = query_string.encode( "ascii" )

    with urllib.request.urlopen( url, data ) as response:
        response_text = response.read()
        print( response_text )

def getArgObj():
    try:
        args = sys.argv[1]
    # try:
    #     return json.loads(sys.argv[1])
    except:
        args = sys.stdin.read()

    try:
        return json.loads(args)
    except:
        print("args not valid json format")
        print(args)
        sys.exit(1)
main()
sys.exit(0)
