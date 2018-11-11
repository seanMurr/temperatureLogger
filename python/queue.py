#!/usr/bin/env python3.6
import sys, json, time, math, os
import particleCommunication
import urllib.error

workingDir = "/var/www/html/GardenWatering/python/"
configFile = "/var/www/html/GardenWatering/python/config.txt"
queueFile = "/var/www/html/GardenWatering/python/queue.txt"
logFile = "/var/www/html/GardenWatering/python/queue.log"

def main():
    # print(time.time())
    appendLog("Service Started")
    # loop indefinaitaly
    while(True):
        # test time, and sleep for remaining seconds of current minute
        # i.e hold here until next minute ticks over
        # time.sleep(5)
        time.sleep(getRemainingSecondsInMinute())
        appendLog("")

        # get config object
        configObj = getConfigObj()

        # run next queued job for each devices
        # print("Running job queue")
        # for each devices
        for device in configObj['devices']:
            # appendLog("Checking jobs for " + device['name'])
            checkQueueForDevice(device, configObj)

        # update device status files
        # print("Updating device files")
        # for each devices
        for device in configObj['devices']:
            updateDeviceFile(device,configObj)

        # print(time.strftime("%b %d %Y %H:%M:%S", time.localtime(time.time())))

def appendLog(message):
    # open log file to append
    # create timestamp
    timeStamp = time.strftime("%b %d %Y %H:%M:%S", time.localtime(time.time()))
    # print(timeStamp + ', ' + message)
    with open(logFile, "a") as log:
        # write message
        log.write(timeStamp + ', ' + message + '\n')

def checkQueueForDevice(device, configObj):
    # open queue file
    # print("Opening 'queue.txt'")
    with open(queueFile,"r") as queue_file:
        # get array of jobs
        queue = queue_file.readlines()
        queue = [line.strip() for line in queue]
        # for each job
        for jobIndex in range(len(queue)):
        # for job in queue:
            job = queue[jobIndex].strip()
            # print(job)
            if job == '':
                # print("Empty line")
                removeJob(queue,jobIndex)
                return
            job = json.loads(job)
            # if this job is not for this devices
            if job['deviceID'] != device['deviceID']:
                # get next job
                # print("This job is not for me")
                continue

            # is this job allowed at the moment
            # (only 1 job using solenoid[0] is allowed at any time)
            # this is due to water pressure requirements
            deviceFileObj = getDeviceFileObj(device)
            # print(json.dumps(deviceFileObj['pinValues']))
            jobPinValues = decodePinValues(job['solenoid'], deviceFileObj['numSolenoids'])
            # print(json.dumps(jobPinValues))
            if not ((deviceFileObj['pinValues'][0] == 1) and (jobPinValues[0]==1)):
                # job is allowed
                # print("Job is allowed")
                # create comms object to send to particleFunction()
                comms = {"functName":job['functName']}
                comms['deviceID'] = job['deviceID']
                comms['accessToken'] = configObj['accessToken'][device['accessID']]
                comms['data'] = str(job['solenoid']) + ',' + str(job['time'])
                appendLog(json.dumps(comms))
                # send this job to devices
                try:
                    appendLog(particleCommunication.particleFunction(comms).decode("utf-8"))
                    # remove this job from queue
                    removeJob(queue,jobIndex)
                    # update device file for this device
                    updateDeviceFile(device,configObj)
                    # exit out of queue while loop
                except urllib.error.HTTPError:
                    appendLog("device '" + device['name'] + "' not found")
                except Exception as e:
                    appendLog("unmanaged exception: " + str(e))
                    raise

                return

            else:
                None
                # job is not allowed
                # print("Job is NOT allowed")
                # check next job


def removeJob(queue,jobIndex):
    # remove item from queue
    for i in range(jobIndex,len(queue)-1):
        queue[i] = queue[i+1]
    # pop the last element off the queue
    queue.pop(len(queue)-1)

    # open queue for writing
    with open(queueFile,"w") as queue_file:
        for job in queue:
            queue_file.write(job)
            queue_file.write('\n')

def updateDeviceFile(device, configObj):
    # print("Updating " + device['name'])
    # get numSolenoids from devices
    numSolenoids = getNumSolenoids(device, configObj)
    # get pinValues from devices
    if validateNumSolenoids(numSolenoids):
        pinIntValue = getPinValues(device, configObj, numSolenoids)
        if pinIntValue != 'error':
            pinValue = decodePinValues(pinIntValue,numSolenoids)
            # print("getPinValues() " + json.dumps(pinValue))
            # save into json into file [deviceID].txt
            deviceFileObj = getDeviceFileObj(device)
            # # TODO: only update if details have changed
            deviceFileObj['pinIntValue'] = pinIntValue
            deviceFileObj['pinValues'] = pinValue
            deviceFileObj['numSolenoids'] = numSolenoids
            writeToDeviceFile(device, deviceFileObj)
        else:
            pinValue = 'error'

    else:
        pinValue = 'error'

def getDeviceFileObj(device):
    # return object from the json in object files
    # if file not exist the return empty object
    fileName = workingDir + device['deviceID']+".txt"
    if os.path.exists(fileName):
        # print("File exists")
        fh = open(fileName, "r")
        deviceFileObj = fh.read()
        fh.close()
    else:
        # print("File does NOT exist")
        # create empty json string
        deviceFileObj = "{}"
    # return object from json
    return json.loads(deviceFileObj)

def writeToDeviceFile(device, deviceFileObj):
    # '{"pinValues":[0,0,0,0,0,0,0,0]}'
    # open file and read json contents to object if file exists

    # open file to write
    fileName = workingDir + device['deviceID']+".txt"
    fh = open(fileName, "w")
    # write json.dumps()
    fh.write(json.dumps(deviceFileObj))
    # close file
    fh.close()

def getNumSolenoids(device, configObj):
    comms = {"varName":"numSolenoids"}
    comms['deviceID'] = device['deviceID']
    comms['accessToken'] = configObj['accessToken'][device['accessID']]
    try:
        numSolenoids = particleCommunication.particleVariable(comms)
        # print("numSolenoids 64: " + str(numSolenoids))
        if validateNumSolenoids(numSolenoids):
            return numSolenoids
        else:
            return 'error'
    except urllib.error.HTTPError:
        appendLog("device '" + device['name'] + "' not found")
        return 'error'
    except Exception as e:
        appendLog("unmanaged exception: " + str(e))
        raise

def getPinValues(device, configObj, numSolenoids):
    comms = {"varName":"pinValues"}
    comms['deviceID'] = device['deviceID']
    comms['accessToken'] = configObj['accessToken'][device['accessID']]
    # print(json.dumps(data))
    # "{varName: [variableName], deviceID: [deviceID], accessToken: [accessToken]}"
    pinValue = (particleCommunication.particleVariable(comms))
    # print("pinValue 59: " + str(pinValue))
    # if pinValue != 'error':
    #     pinValue = decodePinValues(pinValue,numSolenoids)
    #     # print("getPinValues() " + json.dumps(pinValue))
    return pinValue

def decodePinValues(pinIntValue,numSolenoids):
    # print("decodePinValues(" + str(pinValue) + ", " +str(numSolenoids) + ")")
    # TO-DO
    # for($i=0;$i<$numDevices;$i++){
    pinValue = int(pinIntValue)
    numSolenoids = int(numSolenoids)
    pinArray = [0] * numSolenoids
    for i in range(numSolenoids-1,-1,-1):
        # print(i)
        indexPow = math.pow(2,i)
        if(pinValue/indexPow>=1):
            pinArray[i] = 1
        else:
            pinArray[i] = 0
        pinValue = pinValue % indexPow
    # print("decodePinValues() " + json.dumps(pinArray))
    return pinArray

def validateNumSolenoids(numSolenoids):
    if numSolenoids == 'error':
        return False
    return True

def getRemainingSecondsInMinute():
    # get current local time
    nowLocal = time.localtime(time.time())

    # return 60 - number of seconds in local time
    return 60-nowLocal[5]

def getConfigObj():
    # read config.txt and return object from the json encode
    try:
        with open(configFile) as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
        lines = ''.join(lines)
        # print(lines)
        return json.loads(lines)
    except:
        appendLog("Failed to load from " + configFile +". Exiting")
        sys.exit(1)

try:
    main()
except KeyboardInterrupt:
    appendLog('Service stopped: Keyboard interupt received. Exiting.')
    sys.exit(0)
except Exception as e:
    appendLog('Service stopped: ' + str(e))
    raise
    sys.exit(1)
