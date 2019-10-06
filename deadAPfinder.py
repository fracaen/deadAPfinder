import requests
import json


### This function gets a list of switches from DNAC
def buildSwitchList():
    return switches

### This function collects inline power data using Restconf
def collectSwitchPOEData(switch):
    return

### This function collects CDP Neighbor info using Restconf
def collectSwitchCDPData():
    pass

### This function collects LLDP Neighbor info using Restconf
def collectSwitchLLDPData():
    pass

### This function collects VLAN  data (VLANs on device and port membership) using Restconf
def collectSwitchVLANs():
    pass

### This function collects MAC address table using Restconf
def collectSwitchMACTable():
    pass

### This function starts data collection a single switches
def collectSwitchData(switch):
    collectSwitchPOEData()
    collectSwitchCDPData()
    collectSwitchLLDPData()
    collectSwitchVLANs()
    collectSwitchMACTable()
    pass

### This function evaluates if switch does not have enough power to fully power an additional AP
def checkLowPower(switch_data):
    pass

### This function reports that a switch has a low power scenario
def reportLowPowerSwitch():
    return switchOutput

### This function reports list of ports that are supplying power via POE
def checkPowerPorts(switch_data):
    pass

### This function check if the port providing power does not have a link state of up
def checkPortDown(port):
    pass

### This function reports ports providing POE but not with link state of up
def reportPOEPortDownPOEUP(port):
    pass

### This function checks if the AP CDP info is currently reported as managed by a WLC.
def checkPreviouslyManaged(dpData):
    pass

### This reports that the AP on this port was previously managed
def reportPreviousManaged(dpData, port):
    pass

### This function returns both CDP and LLDP data
def getDPData(port):
    pass

### This function checks if the device pulling power is reporting CDP/LLDP data
def checkDPAP(dpData):
    pass

### This function reports a possible AP on port
def reportPossibleAP(port):
    pass


def main():
    switches = buildSwitchList()
    ReportList = []
    # Iterate through switches
    for switch in switches:
        switch_data = (collectSwitchData(switch))
        # Check if switch has insufficient power budget for additional APs
        if checkLowPower(switch_data):
            reportLowPowerSwitch(switch)

        # Iterate through ports providing POE Power
        for port in checkPowerPorts(switch_data):
            # Check if port shows link status up
            if checkPortDown(port):
                reportPOEPortDownPOEUP(port)

            # Collect CDP/LLDP Data for port
            dpData = getDPData(port)

            # Check if (C|LL)DP info shows AP device info
            if checkDPAP(dpData):

                # Check if AP has  been previously discovered by DNAC or WLC
                if checkPreviouslyManaged(dpData):
                    reportPreviousManaged(dpData, port)

            # Check if CDP/LLDP data is empty, then this could a potential
            elif dpData == "":
                reportPossibleAP(port)




if __name__ == '__main__':
    main()
