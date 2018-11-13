#!/usr/bin/env python3.6
# usage testing.php "{varName: [variableName], deviceID: [deviceID], accessToken: [accessToken]}"

import sys
import particleCommunication

def main():
    data = particleCommunication.getArgObj(sys.argv[1])
    responce = particleCommunication.particleVariable(data)
    if responce != 'error':
        print(responce)
        # return responce
    else:
        sys.exit(1)
    # print(particleCommunication.particleVariable(data))

#     data = getArgObj()
#     url = "https://api.particle.io/v1/devices/" + data['deviceID'] + "/" + data['varName']
#     params = {"access_token": data['accessToken']}
#
#     # print(url)
#     # print(params)
#
#     data = urllib.parse.urlencode( params )
#     # data = query_string.encode( "ascii" )
#
#     with urllib.request.urlopen( url + '?' + data ) as response:
#         response_text = response.read()
#         responceObj = json.loads(response_text)
#         # print(response_text)
#         # print("Result: " + str(responceObj['result']))
#         print(responceObj['result'])
#
# def getArgObj():
#     try:
#         args = sys.argv[1]
#     # try:
#     #     return json.loads(sys.argv[1])
#     except:
#         args = sys.stdin.read()
#
#     try:
#         return json.loads(args)
#     except:
#         print("args not valid json format")
#         print(args)
#         sys.exit(1)
main()
sys.exit(0)
