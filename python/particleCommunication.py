#!/usr/bin/env python3.6
# usage testing.php "{data:[dataToSend], functName: [functName], deviceID: [deviceID], accessToken: [accessToken]}"

import sys, json, select
import urllib.parse
import urllib.request

def particleFunction(data):
    # data is an object containing the following
    #   data        - string to send to the device
    #   functName   - particleFunction to invoke
    #   deviceID    - deviceID for the recipient device
    #   accessToken - accessToken for the acount the device is attached to

    url = "https://api.particle.io/v1/devices/" + data['deviceID'] + "/" + data['functName']
    params = {"args": data['data'], "access_token": data['accessToken']}

    # print(url)
    # print(params)

    query_string = urllib.parse.urlencode( params )
    data = query_string.encode( "ascii" )

    with urllib.request.urlopen( url, data ) as response:
        response_text = response.read()
        return response_text

def particleVariable(data):
    # data is an object containing the following
    #   varName   - particleVariable to get
    #   deviceID    - deviceID for the recipient device
    #   accessToken - accessToken for the acount the device is attached to
    # print("particleVariable()")
    # print(json.dumps(data))

    url = "https://api.particle.io/v1/devices/" + data['deviceID'] + "/" + data['varName']
    params = {"access_token": data['accessToken']}

    # print(url)
    # print(params)

    data = urllib.parse.urlencode( params )
    # data = query_string.encode( "ascii" )
    # print(url + '?' + data)
    try:
        with urllib.request.urlopen( url + '?' + data ) as response:
            response_text = response.read()
            responceObj = json.loads(response_text)
            # print(response_text)
            # print("Result: " + str(responceObj['result']))
            return responceObj['result']
    except urllib.error.HTTPError:
        # print("HTTPError found")
        return "error"

def getArgObj(arg=None):
    # print("particleCommunication.getArgObj()")
    if arg:
        # print("trying sys.argv[1]")
        args = arg
    # try:
    #     return json.loads(sys.argv[1])
    else:
        # print("exception caught")
        # print("trying sys.stdin.read()")
        if select.select([sys.stdin,],[],[],0.0)[0]:
            args = sys.stdin.read()
        else:
            args = ' '

    # print(args)

    try:
        return json.loads(args)
    except:
        print("args not valid json format")
        print(args)
        sys.exit(1)
