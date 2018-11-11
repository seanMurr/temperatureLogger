#!/usr/bin/env python3.6

import sys
import urllib.parse
import urllib.request

def main():
    # url = "https://api.particle.io/v1/devices/200033000b47363433353735/turnOn"
    # params = {"args": "1,5", "access_token": "51d2491f8b4ec232aecfe0aa1ef33d1278dad9f0"}
    url = "https://api.particle.io/v1/devices/200033000b47363433353735/pinValues"
    params = {"access_token":"51d2491f8b4ec232aecfe0aa1ef33d1278dad9f0"}

    data = urllib.parse.urlencode( params )
    # data = query_string.encode( "ascii" )
    # print(query_string)
    print(data)

    with urllib.request.urlopen( url + '?' + data ) as response:
        response = response.read()
        print( response_text )
    # params = urllib.parse.urlencode({'@args': '1,5',
    #         '@access_token': '51d2491f8b4ec232aecfe0aa1ef33d1278dad9f0'})
    # headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    # conn = http.client.HTTPConnection("api.particle.io/v1/devices/200033000b47363433353735/turnOn")
    # conn.request("POST", "", params,headers)
    # response = conn.getresponse()
    # print(response.status, response.reason)
    # data = response.read()
    # data
    # conn.close()

main()
sys.exit(0)
