from netmiko import ConnectHandler


def buildSwitchList():
    switches = ["10.71.154.9"]
    return switches


def buildWLCList():
    wlcs = ['10.71.154.10']
    return wlcs


def collectWLCData(wlc):
    pass


def collectSwitchPOEData():
    pass


def collectSwitchCDPData():
    pass


def collectSwitchLLDPData():
    pass


def collectSwitchVLANs():
    pass


def collectSwitchMACTable():
    pass


def collectSwitchData(switch):
    collectSwitchPOEData()
    collectSwitchCDPData()
    collectSwitchLLDPData()
    collectSwitchVLANs()
    collectSwitchMACTable()
    pass


def checkLowPower(switch_data):
    pass


def reportSwitch():
    pass


def checkPowerPorts(switch_data):
    pass


def checkPortDown(port):
    pass


def reportPOEPortDownPOEUP(port):
    pass


def checkAPManaged(port):
    pass


def reportPreviousManaged(dpData, port):
    pass


def getDPData(port):
    pass


def checkDPAP(dpData):
    pass


def reportPossibleAP(port):
    pass


def main():
    switches = buildSwitchList()
    wlc_data = []
    wlcs = buildWLCList()
    for wlc in wlcs:
        wlc_data.append(collectWLCData(wlc))
    for switch in switches:
        switch_data = (collectSwitchData(switch))
        if checkLowPower(switch_data):
            reportSwitch(switch)
        for port in checkPowerPorts(switch_data):
            if checkPortDown(port):
                reportPOEPortDownPOEUP(port)
            dpData = getDPData(port)
            if checkDPAP(dpData):
                if not checkAPManaged(dpData):
                    reportPreviousManaged(dpData, port)
            elif dpData == "":
                reportPossibleAP(port)




if __name__ == '__main__':
    main()
