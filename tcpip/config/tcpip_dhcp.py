"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

    
def instantiateComponent(tcpipDhcpComponent):
    print("TCPIP DHCP Client Component")
    configName = Variables.get("__CONFIGURATION_NAME")
    
    # Enable DHCP Client
    tcpipDhcpc = tcpipDhcpComponent.createBooleanSymbol("TCPIP_STACK_USE_DHCP_CLIENT", None)
    tcpipDhcpc.setHelp("mcc_h3_dhcp_configurations")
    tcpipDhcpc.setLabel("DHCP Client")
    tcpipDhcpc.setVisible(False)
    tcpipDhcpc.setDescription("Enable DHCP Client")
    tcpipDhcpc.setDefaultValue(True)

    # DHCP Client Request Time-out in seconds
    tcpipDhcpcReqTimeout = tcpipDhcpComponent.createIntegerSymbol("TCPIP_DHCP_TIMEOUT", None)
    tcpipDhcpcReqTimeout.setHelp("mcc_h3_dhcp_configurations")
    tcpipDhcpcReqTimeout.setLabel("DHCP Request Time-out (in sec)")
    tcpipDhcpcReqTimeout.setVisible(True)
    tcpipDhcpcReqTimeout.setDescription("DHCP Request Time-out in seconds")
    tcpipDhcpcReqTimeout.setDefaultValue(10)
    
    # DHCP Client Host name maximum size
    tcpipDhcpcHostNameSize = tcpipDhcpComponent.createIntegerSymbol("TCPIP_DHCP_HOST_NAME_SIZE", None)
    tcpipDhcpcHostNameSize.setHelp("mcc_h3_dhcp_configurations")
    tcpipDhcpcHostNameSize.setLabel("DHCP Host Name Maximum Size")
    tcpipDhcpcHostNameSize.setVisible(True)
    tcpipDhcpcHostNameSize.setDescription("DHCP Client Host name maximum size")
    tcpipDhcpcHostNameSize.setDefaultValue(20)
    
    # Enable DHCP Client Console Command
    tcpipDhcpcCmdEnable = tcpipDhcpComponent.createBooleanSymbol("TCPIP_DHCP_CLIENT_CONSOLE_CMD", None)
    tcpipDhcpcCmdEnable.setHelp("mcc_h3_dhcp_configurations")
    tcpipDhcpcCmdEnable.setLabel("Enable Console Commands")
    tcpipDhcpcCmdEnable.setVisible(True)
    tcpipDhcpcCmdEnable.setDescription("Enable DHCP Client Console Commands")
    tcpipDhcpcCmdEnable.setDefaultValue(True)
    
    # Advanced Settings
    tcpipDhcpcAdvSettings = tcpipDhcpComponent.createMenuSymbol("TCPIP_DHCP_ADV_SETTING", None)
    tcpipDhcpcAdvSettings.setLabel("Advanced Settings")
    tcpipDhcpcAdvSettings.setDescription("Advanced Settings")
    tcpipDhcpcAdvSettings.setVisible(True)
    
    # DHCP Client Tick Rate in msec
    tcpipDhcpcTickRate = tcpipDhcpComponent.createIntegerSymbol("TCPIP_DHCP_TASK_TICK_RATE", tcpipDhcpcAdvSettings)
    tcpipDhcpcTickRate.setHelp("mcc_h3_dhcp_configurations")
    tcpipDhcpcTickRate.setLabel("DHCP Client Task Rate (in msec)")
    tcpipDhcpcTickRate.setVisible(True)
    tcpipDhcpcTickRate.setDescription("DHCP Tick Rate in msec")
    tcpipDhcpcTickRate.setDefaultValue(5)
    
    # DHCP Client port
    tcpipDhcpcConnectPort = tcpipDhcpComponent.createIntegerSymbol("TCPIP_DHCP_CLIENT_CONNECT_PORT", tcpipDhcpcAdvSettings)
    tcpipDhcpcConnectPort.setHelp("mcc_h3_dhcp_configurations")
    tcpipDhcpcConnectPort.setLabel("Client Port for DHCP Client Transactions")
    tcpipDhcpcConnectPort.setVisible(True)
    tcpipDhcpcConnectPort.setDescription("Client Port for DHCP Client Transactions")
    tcpipDhcpcConnectPort.setDefaultValue(68)

    # Remote Server Port for DHCP Server Messages
    tcpipDhcpcServerListenPort= tcpipDhcpComponent.createIntegerSymbol("TCPIP_DHCP_SERVER_LISTEN_PORT", tcpipDhcpcAdvSettings)
    tcpipDhcpcServerListenPort.setHelp("mcc_h3_dhcp_configurations")
    tcpipDhcpcServerListenPort.setLabel("Remote Server Port for DHCP Server Messages")
    tcpipDhcpcServerListenPort.setVisible(True)
    tcpipDhcpcServerListenPort.setDescription("Remote Server Port for DHCP Server Messages")
    tcpipDhcpcServerListenPort.setDefaultValue(67)
    
    # Time Server Options + Maximum Number Time Servers to Store
    tcpipDhcpcTimeServerMax = tcpipDhcpComponent.createIntegerSymbol("TCPIP_DHCP_OPTION_TIME_SERVER_MAX", tcpipDhcpcAdvSettings)
    tcpipDhcpcTimeServerMax.setHelp("mcc_h3_dhcp_configurations")
    tcpipDhcpcTimeServerMax.setLabel("Maximum Number of Time Servers to Store")
    tcpipDhcpcTimeServerMax.setVisible(True)
    tcpipDhcpcTimeServerMax.setDescription("Maximum Number of Time Server Addresses that Can Be Stored")
    tcpipDhcpcTimeServerMax.setDefaultValue(0)

    # NTP Server Options + Maximum Number NTP Servers to Store
    tcpipDhcpcNtpServerMax = tcpipDhcpComponent.createIntegerSymbol("TCPIP_DHCP_OPTION_NTP_SERVER_MAX", tcpipDhcpcAdvSettings)
    tcpipDhcpcNtpServerMax.setHelp("mcc_h3_dhcp_configurations")
    tcpipDhcpcNtpServerMax.setLabel("Maximum Number of NTP Servers to Store")
    tcpipDhcpcNtpServerMax.setVisible(True)
    tcpipDhcpcNtpServerMax.setDescription("Maximum Number of NTP Server Addresses that Can Be Stored")
    tcpipDhcpcNtpServerMax.setDefaultValue(0)
    
    tcpipDhcpcheapdependency = ["tcpipNetConfig.TCPIP_STACK_NETWORK_INTERAFCE_COUNT", "tcpipStack.TCPIP_STACK_HEAP_CALC_MASK"]    
        
    # DHCPC Heap Size
    tcpipDhcpcHeapSize = tcpipDhcpComponent.createIntegerSymbol("TCPIP_DHCP_HEAP_SIZE", None)
    tcpipDhcpcHeapSize.setLabel("DHCPC Heap Size (bytes)") 
    tcpipDhcpcHeapSize.setVisible(False)
    tcpipDhcpcHeapSize.setDefaultValue(tcpipDhcpcHeapCalc())
    tcpipDhcpcHeapSize.setReadOnly(True)
    tcpipDhcpcHeapSize.setDependencies(tcpipDhcpcHeapUpdate, tcpipDhcpcheapdependency)    
    
    # Add to system_config.h
    tcpipDhcpcHeaderFtl = tcpipDhcpComponent.createFileSymbol(None, None)
    tcpipDhcpcHeaderFtl.setSourcePath("tcpip/config/dhcp.h.ftl")
    tcpipDhcpcHeaderFtl.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
    tcpipDhcpcHeaderFtl.setMarkup(True)
    tcpipDhcpcHeaderFtl.setType("STRING")
        
def tcpipDhcpMenuVisibleSingle(symbol, event):
    if (event["value"] == True):
        print("DHCP Client Menu Visible.")      
        symbol.setVisible(True)
    else:
        print("DHCP Client Menu Invisible.")
        symbol.setVisible(False)    

# make DHCP Client option visible
def tcpipDhcpcMenuVisible(tcpipDependentSymbol, tcpipIPSymbol):
    tcpipIPv4 = Database.getSymbolValue("tcpipIPv4","TCPIP_STACK_USE_IPV4")
    tcpipUdp = Database.getSymbolValue("tcpipUdp","TCPIP_USE_UDP")
    print("DHCP IPv4 UDP  Menu On.")
    if(tcpipIPv4 and tcpipUdp):
        tcpipDependentSymbol.setVisible(True)
        print("DHCP IPv4 UDP  Menu On.")
    else:
        tcpipDependentSymbol.setVisible(False)  
        print("DHCP IPv4 UDP  Menu Off.")       

def tcpipDhcpcHeapCalc(): 
    numInterface = Database.getSymbolValue("tcpipNetConfig","TCPIP_STACK_NETWORK_INTERAFCE_COUNT")
    heap_size = 0
    if (numInterface != None):
        heap_size = numInterface * 88
    return heap_size    
    
def tcpipDhcpcHeapUpdate(symbol, event): 
    heap_size = tcpipDhcpcHeapCalc()
    symbol.setValue(heap_size)
    if(event["id"] == "TCPIP_STACK_HEAP_CALC_MASK"):
        symbol.setVisible(event["value"])

#Set symbols of other components
def setVal(component, symbol, value):
    triggerDict = {"Component":component,"Id":symbol, "Value":value}
    if(Database.sendMessage(component, "SET_SYMBOL", triggerDict) == None):
        print "Set Symbol Failure" + component + ":" + symbol + ":" + str(value)
        return False
    else:
        return True

#Handle messages from other components
def handleMessage(messageID, args):
    retDict= {}
    if (messageID == "SET_SYMBOL"):
        print "handleMessage: Set Symbol"
        retDict= {"Return": "Success"}
        Database.setSymbolValue(args["Component"], args["Id"], args["Value"])
    else:
        retDict= {"Return": "UnImplemented Command"}
    return retDict
    
def destroyComponent(component):
    Database.setSymbolValue("tcpipDhcp", "TCPIP_STACK_USE_DHCP_CLIENT", False, 2)

