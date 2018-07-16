/*******************************************************************************
  Microchip TCP/IP Stack Include File

  Company:
    Microchip Technology Inc.
    
  File Name:
    tcpip_private.h.ftl

  Summary:
   Private include file for the TCPIP stack

  Description:
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright ? 2012 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED ?AS IS? WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef __TCPIP_STACK_PRIVATE_H__
#define __TCPIP_STACK_PRIVATE_H__

#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
        
#include "system_config.h"
//#include "system/debug/sys_debug.h"
//#include "system/console/sys_console.h"
#include "system/sys_console_h2_adapter.h"
//#include "system/command/sys_command.h"
#include "system/sys_cmd_h2_adapter.h"
//#include "system/random/sys_random.h"
#include "system/sys_random_h2_adapter.h"
//#include "system/tmr/sys_tmr.h"
#include "system/sys_time_h2_adapter.h"

#include "osal/osal.h"

#include "tcpip/src/common/helpers.h"



// Internal adjustments - dependencies
// change signaling depends on the IPv4
#if defined(TCPIP_STACK_USE_IPV4) && (TCPIP_STACK_INTERFACE_CHANGE_SIGNALING != 0)
#define _TCPIP_STACK_INTERFACE_CHANGE_SIGNALING     1
#else
#define _TCPIP_STACK_INTERFACE_CHANGE_SIGNALING     0
#endif  // defined(TCPIP_STACK_USE_IPV4)

// alias interface support depends on IPv4
#if defined(TCPIP_STACK_USE_IPV4) && (TCPIP_STACK_ALIAS_INTERFACE_SUPPORT != 0)
#define _TCPIP_STACK_ALIAS_INTERFACE_SUPPORT     1
#else
#define _TCPIP_STACK_ALIAS_INTERFACE_SUPPORT     0
#endif  // defined(TCPIP_STACK_USE_IPV4) && (TCPIP_STACK_ALIAS_INTERFACE_SUPPORT != 0)

// public module interface
#include "tcpip/tcpip.h"

#include "tcpip/src/tcpip_types.h"
#include "tcpip/src/link_list.h"
#include "tcpip/src/tcpip_heap_alloc.h"

#include "tcpip/tcpip_mac_object.h"

// private stack manager interface
#include "tcpip/src/tcpip_manager_control.h"

#include "tcpip/src/ipv4_manager.h"
#include "tcpip/src/icmp_manager.h"
#include "tcpip/src/dhcp_manager.h"
#include "tcpip/src/arp_manager.h"
#include "tcpip/src/dns_manager.h"
#include "tcpip/src/udp_manager.h"
#include "tcpip/src/lldp_manager.h"
#include "tcpip/src/tcpip_packet.h"
#include "tcpip/src/tcpip_helpers_private.h"
#include "tcpip/src/oahash.h"
#include "tcpip/src/hash_fnv.h"
#include "tcpip/src/tcpip_notify.h"

#endif  // __TCPIP_STACK_PRIVATE_H__
