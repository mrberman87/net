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

def instantiateComponent(tcpipIperfComponent):
    print("TCPIP IPERF Component")
    configName = Variables.get("__CONFIGURATION_NAME")
    # Use iperf Benchmark Tool
    tcpipIperf = tcpipIperfComponent.createBooleanSymbol("TCPIP_USE_IPERF", None)
    tcpipIperf.setHelp("mcc_h3_iperf_configurations")
    tcpipIperf.setLabel("Use iperf Benchmark Tool")
    tcpipIperf.setVisible(False)
    tcpipIperf.setDescription("Use iperf Benchmark Tool")
    tcpipIperf.setDefaultValue(True) 

    # Number of Iperf Instances
    tcpipIperfInstancesMax = tcpipIperfComponent.createIntegerSymbol("TCPIP_IPERF_MAX_INSTANCES", None)
    tcpipIperfInstancesMax.setHelp("mcc_h3_iperf_configurations")
    tcpipIperfInstancesMax.setLabel("Number of Iperf Instances")
    tcpipIperfInstancesMax.setVisible(True)
    tcpipIperfInstancesMax.setDescription("Number of Iperf Instances")
    tcpipIperfInstancesMax.setDefaultValue(1)
    
    # Socket TX Buffer Size
    tcpipIperfTxBuffSize = tcpipIperfComponent.createIntegerSymbol("TCPIP_IPERF_TX_BUFFER_SIZE", None)
    tcpipIperfTxBuffSize.setHelp("mcc_h3_iperf_configurations")
    tcpipIperfTxBuffSize.setLabel("Socket TX Buffer Size")
    tcpipIperfTxBuffSize.setVisible(True)
    tcpipIperfTxBuffSize.setDescription("Socket TX Buffer Size")
    tcpipIperfTxBuffSize.setDefaultValue(4096)

    # Socket RX Buffer Size
    tcpipIperfRxBuffSize = tcpipIperfComponent.createIntegerSymbol("TCPIP_IPERF_RX_BUFFER_SIZE", None)
    tcpipIperfTxBuffSize.setHelp("mcc_h3_iperf_configurations")
    tcpipIperfRxBuffSize.setLabel("Socket RX Buffer Size")
    tcpipIperfRxBuffSize.setVisible(True)
    tcpipIperfRxBuffSize.setDescription("Socket RX Buffer Size")
    tcpipIperfRxBuffSize.setDefaultValue(4096)
            
    # Advanced Settings
    tcpipIperfAdvSettings = tcpipIperfComponent.createMenuSymbol("TCPIP_IPERF_ADV_SETTING", None)
    tcpipIperfAdvSettings.setLabel("Advanced Settings")
    tcpipIperfAdvSettings.setDescription("Advanced Settings")
    tcpipIperfAdvSettings.setVisible(True)

    # Time-out for TX Channel to Become Ready in ms
    tcpipIperfTxWaitTimeout = tcpipIperfComponent.createIntegerSymbol("TCPIP_IPERF_TX_WAIT_TMO", tcpipIperfAdvSettings)
    tcpipIperfTxWaitTimeout.setHelp("mcc_h3_iperf_configurations")
    tcpipIperfTxWaitTimeout.setLabel("Timeout for TX Channel to Become Ready (in msec)")
    tcpipIperfTxWaitTimeout.setVisible(True)
    tcpipIperfTxWaitTimeout.setDescription("Time-out for TX Channel to Become Ready in ms")
    tcpipIperfTxWaitTimeout.setDefaultValue(100)

    # Maximum Number of UDP TX Packet Queue
    tcpipIperfTxQueueLimit = tcpipIperfComponent.createIntegerSymbol("TCPIP_IPERF_TX_QUEUE_LIMIT", tcpipIperfAdvSettings)
    tcpipIperfTxQueueLimit.setHelp("mcc_h3_iperf_configurations")
    tcpipIperfTxQueueLimit.setLabel("Maximum Number of UDP TX Packet Queue")
    tcpipIperfTxQueueLimit.setVisible(True)
    tcpipIperfTxQueueLimit.setDescription("Maximum Number of UDP TX Packet Queue")
    tcpipIperfTxQueueLimit.setDefaultValue(2)

    # Iperf timing error in ms
    tcpipIperfTimingError = tcpipIperfComponent.createIntegerSymbol("TCPIP_IPERF_TIMING_ERROR_MARGIN", tcpipIperfAdvSettings)
    tcpipIperfTimingError.setHelp("mcc_h3_iperf_configurations")
    tcpipIperfTimingError.setLabel("Iperf Timing Error (in msec)")
    tcpipIperfTimingError.setVisible(True)
    tcpipIperfTimingError.setDescription("Iperf timing error in ms")
    tcpipIperfTimingError.setDefaultValue(0)

    # TX Default Bandwidth in Mbps
    tcpipIperfTxBwLimit= tcpipIperfComponent.createIntegerSymbol("TCPIP_IPERF_TX_BW_LIMIT", tcpipIperfAdvSettings)
    tcpipIperfTxBwLimit.setHelp("mcc_h3_iperf_configurations")
    tcpipIperfTxBwLimit.setLabel("Default TX Bandwidth(in Mbps)")
    tcpipIperfTxBwLimit.setVisible(True)
    tcpipIperfTxBwLimit.setDescription("TX Default Bandwidth in Mbps")
    tcpipIperfTxBwLimit.setDefaultValue(1)

    #Add to system_config.h
    tcpipIperfHeaderFtl = tcpipIperfComponent.createFileSymbol(None, None)
    tcpipIperfHeaderFtl.setSourcePath("tcpip/config/iperf.h.ftl")
    tcpipIperfHeaderFtl.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
    tcpipIperfHeaderFtl.setMarkup(True)
    tcpipIperfHeaderFtl.setType("STRING")

    # Add iperf.c file
    tcpipIperfSourceFile = tcpipIperfComponent.createFileSymbol(None, None)
    tcpipIperfSourceFile.setSourcePath("tcpip/src/iperf.c")
    tcpipIperfSourceFile.setOutputName("iperf.c")
    tcpipIperfSourceFile.setOverwrite(True)
    tcpipIperfSourceFile.setDestPath("library/tcpip/src/")
    tcpipIperfSourceFile.setProjectPath("config/" + configName + "/library/tcpip/src/")
    tcpipIperfSourceFile.setType("SOURCE")
    tcpipIperfSourceFile.setEnabled(True)
    
def tcpipIperfMenuVisible(symbol, event):
    if (event["value"] == True):
        print("Telnet Menu Visible.")       
        symbol.setVisible(True)
    else:
        print("Telnet Menu Invisible.")
        symbol.setVisible(False)
        
def tcpipIperfGenSourceFile(sourceFile, event):
    sourceFile.setEnabled(event["value"])

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
    Database.setSymbolValue("tcpipIperf", "TCPIP_USE_IPERF", False, 2)
