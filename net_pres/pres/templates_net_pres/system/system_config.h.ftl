<#----------------------------------------------------------------------------
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
---------------------------------------------------------------------------->

<#--include "/framework/net_pres/pres/tls/templates/system_config.h.ftl"-->
<#if NET_PRES_USE>
/* MPLAB Harmony Net Presentation Layer Definitions*/
#define NET_PRES_NUM_INSTANCE 1
#define NET_PRES_NUM_SOCKETS ${NET_PRES_SOCKETS}

<#if (HarmonyCore.SELECT_RTOS)?? && HarmonyCore.SELECT_RTOS != "BareMetal">
    <#lt>/* Net Pres RTOS Configurations*/
    <#if (HarmonyCore.SELECT_RTOS)?? && HarmonyCore.SELECT_RTOS == "FreeRTOS">
        <#lt>#define NET_PRES_RTOS_STACK_SIZE                ${NET_PRES_RTOS_STACK_SIZE / 4}
    <#else>
        <#lt>#define NET_PRES_RTOS_STACK_SIZE                ${NET_PRES_RTOS_STACK_SIZE}
    </#if>
    <#lt>#define NET_PRES_RTOS_TASK_PRIORITY             ${NET_PRES_RTOS_TASK_PRIORITY}
	
	<#assign numInstance= 1>
	<#assign freertos_present= false/>
    <#list 0..(numInstance-1) as idx>
		<#assign netPresEncProviderIdx = "NET_PRES_ENC_PROVIDE"?eval>		
		<#if netPresEncProviderIdx == "WolfSSL" && (HarmonyCore.SELECT_RTOS) == "FreeRTOS">
			<#assign freertos_present=true/>
        </#if>
    </#list>
	<#if freertos_present == true>	
		<#lt>#define FREERTOS
	</#if>
</#if>
</#if>

	