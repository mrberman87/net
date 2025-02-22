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

    
def instantiateComponent(tcpipBerkeleyApiComponent):
    print("TCPIP Berkeley Api Component")
    configName = Variables.get("__CONFIGURATION_NAME")
    
    # Enable Berkeley API
    tcpipBerkeleyApi = tcpipBerkeleyApiComponent.createBooleanSymbol("TCPIP_STACK_USE_BERKELEY_API", None)
    tcpipBerkeleyApi.setHelp("mcc_h3_bsd_configurations")
    tcpipBerkeleyApi.setLabel("Berkeley API")
    tcpipBerkeleyApi.setVisible(False)
    tcpipBerkeleyApi.setDescription("Enable Berkeley API")
    tcpipBerkeleyApi.setDefaultValue(True)

    # Maximum Number of Simultaneous Sockets Supported
    tcpipBerkeleyBsdSktsMaxNum = tcpipBerkeleyApiComponent.createIntegerSymbol("TCPIP_BSD_MAX_BSD_SOCKETS", None)
    tcpipBerkeleyBsdSktsMaxNum.setHelp("mcc_h3_bsd_configurations")
    tcpipBerkeleyBsdSktsMaxNum.setLabel("Maximum Number of Simultaneous Sockets")
    tcpipBerkeleyBsdSktsMaxNum.setVisible(True)
    tcpipBerkeleyBsdSktsMaxNum.setDescription("Maximum Number of Simultaneous Sockets Supported")
    tcpipBerkeleyBsdSktsMaxNum.setDefaultValue(4)

    tcpipBerkeleyheapdependency = ["TCPIP_BSD_MAX_BSD_SOCKETS", "tcpipStack.TCPIP_STACK_HEAP_CALC_MASK"]    
        
    # Berkeley Heap Size
    tcpipBerkeleyHeapSize = tcpipBerkeleyApiComponent.createIntegerSymbol("TCPIP_BSD_HEAP_SIZE", None)
    tcpipBerkeleyHeapSize.setLabel("BSD Heap Size (bytes)") 
    tcpipBerkeleyHeapSize.setVisible(False)
    tcpipBerkeleyHeapSize.setDefaultValue(tcpipBerkeleyHeapCalc())
    tcpipBerkeleyHeapSize.setReadOnly(True)
    tcpipBerkeleyHeapSize.setDependencies(tcpipBerkeleyHeapSizeHeapUpdate, tcpipBerkeleyheapdependency) 

    # Add berkeley_api.c file
    tcpipBerkeleyApiSourceFile = tcpipBerkeleyApiComponent.createFileSymbol(None, None)
    tcpipBerkeleyApiSourceFile.setSourcePath("tcpip/src/berkeley_api.c")
    tcpipBerkeleyApiSourceFile.setOutputName("berkeley_api.c")
    tcpipBerkeleyApiSourceFile.setOverwrite(True)
    tcpipBerkeleyApiSourceFile.setDestPath("library/tcpip/src/")
    tcpipBerkeleyApiSourceFile.setProjectPath("config/" + configName + "/library/tcpip/src/")
    tcpipBerkeleyApiSourceFile.setType("SOURCE")
    tcpipBerkeleyApiSourceFile.setEnabled(True)

    tcpipBerkeleyApiHeaderFtl = tcpipBerkeleyApiComponent.createFileSymbol(None, None)
    tcpipBerkeleyApiHeaderFtl.setSourcePath("tcpip/config/berkeley_api.h.ftl")
    tcpipBerkeleyApiHeaderFtl.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
    tcpipBerkeleyApiHeaderFtl.setMarkup(True)
    tcpipBerkeleyApiHeaderFtl.setType("STRING") 
    
def tcpipBerkeleyApiMenuVisible(symbol, event):
    if (event["value"] == True):
        print("BerkeleyApi Menu Visible.")      
        symbol.setVisible(True)
    else:
        print("BerkeleyApi Menu Invisible.")
        symbol.setVisible(False)    
        
def tcpipBerkeleyApiGenSourceFile(sourceFile, event):
    sourceFile.setEnabled(event["value"])
    

def tcpipBerkeleyHeapCalc(): 
    maxNumSkt = Database.getSymbolValue("tcpipBerkeleyApi","TCPIP_BSD_MAX_BSD_SOCKETS")
    heap_size = maxNumSkt * 64
    return heap_size    
    
def tcpipBerkeleyHeapSizeHeapUpdate(symbol, event): 
    heap_size = tcpipBerkeleyHeapCalc()
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
    Database.setSymbolValue("tcpipBerkeleyApi", "TCPIP_STACK_USE_BERKELEY_API", False, 2)
