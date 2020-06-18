import time
import sys
import ibmiotf.application # to install pip install ibmiotf
import ibmiotf.device

#Provide your IBM Watson Device Credentials
organization = "8ymz8u" #replace the ORG ID
deviceType =  "Receiver"#replace the Device type wi
deviceId = "0408"#replace Device ID
authMethod = "token"
authToken = "9876543210" #Replace the authtoken

def myCommandCallback(cmd): # function for Callback
        #print("Command received: %s" % cmd.data)
        if cmd.data['command']=='motor_on':
                print("Motor is Running...")
                          
        elif cmd.data['command']=='motor_off':
                print("Motor has Turned OFF..!")
                
        if cmd.command == "setInterval":
                
                if 'interval' not in cmd.data:
                        print("Error - command is missing required information: 'interval'")
                else:
                        interval = cmd.data['interval']
        elif cmd.command == "print":
                if 'message' not in cmd.data:
                        print("Error - command is missing required information: 'message'")
                else:
                        output=cmd.data['message']
                        print(output)

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
           
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()