/*******************************************************************************
  SMSC LAN8700 definitions

  Company:
    Microchip Technology Inc.
    
  File Name:
    drv_extphy_smsc8700.h

  Summary:
    SMSC LAN8700 definitions

  Description:
    This file provides the SMSC LAN8700 definitions.

*******************************************************************************/
// DOM-IGNORE-BEGIN
/*****************************************************************************
 Copyright (C) 2012-2018 Microchip Technology Inc. and its subsidiaries.

Microchip Technology Inc. and its subsidiaries.

Subject to your compliance with these terms, you may use Microchip software 
and any derivatives exclusively with Microchip products. It is your 
responsibility to comply with third party license terms applicable to your 
use of third party software (including open source software) that may 
accompany Microchip software.

THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER 
EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED 
WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR 
PURPOSE.

IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, 
INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND 
WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS 
BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE 
FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN 
ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY, 
THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************/

// DOM-IGNORE-END

#ifndef _SMSC_8700_H_

#define _SMSC_8700_H_

typedef enum
{
    /*
    // basic registers, accross all registers: 0-1
    PHY_REG_BMCON       = 0,
    PHY_REG_BMSTAT      = 1,
    // extended registers: 2-15
    PHY_REG_PHYID1      = 2,
    PHY_REG_PHYID2      = 3,
    PHY_REG_ANAD        = 4,
    PHY_REG_ANLPAD      = 5,
    PHY_REG_ANLPADNP    = 5,
    PHY_REG_ANEXP       = 6,
    PHY_REG_ANNPTR      = 7,
    PHY_REG_ANLPRNP     = 8,
    */
    // specific vendor registers: 16-31
    PHY_REG_SILICON_REV     = 16,
    PHY_REG_MODE_CTRL       = 17,
    PHY_REG_SPECIAL_MODE    = 18,
    PHY_REG_SYMBOL_ERR_CNT  = 26,
    PHY_REG_SPECIAL_CTRL    = 27,
    PHY_REG_INT_SOURCE      = 29,
    PHY_REG_INT_MASK        = 30,
    PHY_REG_PHY_CTRL        = 31,
    //
    //PHY_REGISTERS     = 32    // total number of registers
}ePHY_VENDOR_REG;
// updated version of ePHY_REG


// vendor registers
//
typedef union {
  struct {
    unsigned              :6;
    unsigned SILICON_REV  :4;
    unsigned              :6;
  };
  struct {
    unsigned short w      :16;
  };
} __SILICONREVbits_t;   // reg 16: PHY_REG_SILICON_REV
#define _SILICONREV_SILICON_REV_MASK        0x03c0


typedef union {
  struct {
    unsigned                  :1;
    unsigned ENERGYON         :1;
    unsigned FORCE_GOOD_LINK  :1;
    unsigned PHYADPB          :1;
    unsigned                  :2;
    unsigned ALTINT           :1;
    unsigned                  :2;
    unsigned FAR_LOOPBACK     :1;
    unsigned MDPREPB          :1;
    unsigned LOWSQEN          :1;
    unsigned                  :1;
    unsigned EDPWRDOWN        :1;
    unsigned                  :2;
  };
  struct {
    unsigned short w:16;
  };
} __MODECTRLbits_t; // reg 17: PHY_REG_MODE_CTRL
#define _MODECTRL_ENERGYON_MASK         0x0002
#define _MODECTRL_FORCE_GOOD_LINK_MASK  0x0004
#define _MODECTRL_PHYADPB_MASK          0x0008
#define _MODECTRL_ALTINT_MASK           0x0040
#define _MODECTRL_FAR_LOOPBACK_MASK     0x0200
#define _MODECTRL_MDPREPB_MASK          0x0400
#define _MODECTRL_LOWSQEN_MASK          0x0800
#define _MODECTRL_EDPWRDOWN_MASK        0x2000


typedef union {
  struct {
    unsigned PHYAD    :5;
    unsigned MODE     :3;
    unsigned          :6;
    unsigned MIIMODE  :1;
    unsigned          :1;
  };
  struct {
    unsigned short w  :16;
  };
} __SPECIALMODEbits_t;  // reg 18: PHY_REG_SPECIAL_MODE
#define _SPECIALMODE_PHYAD_MASK     0x001f
#define _SPECIALMODE_MODE_MASK      0x00e0
#define _SPECIALMODE_MIIMODE_MASK   0x4000




typedef union {
  struct {
    unsigned Sym_Err_Cnt  :16;
  };
  struct {
    unsigned short w      :16;
  };
} __SYMBOLERRCNTbits_t; // reg 26: PHY_REG_SYMBOL_ERR_CNT


typedef union {
  struct {
    unsigned            :4;
    unsigned XPOL       :1;
    unsigned            :6;
    unsigned SQEOFF     :1;
    unsigned            :1;
    unsigned CH_SELECT  :1;
    unsigned            :1;
    unsigned AMDIXCTRL  :1;
  };
  struct {
    unsigned short w    :16;
  };
} __SPECIALCTRLbits_t;  // reg 27: PHY_REG_SPECIAL_CTRL
#define _SPECIALCTRL_XPOL_MASK       0x0010
#define _SPECIALCTRL_SQEOFF_MASK     0x0800
#define _SPECIALCTRL_CH_SELECT_MASK  0x2000
#define _SPECIALCTRL_AMDIXCTRL_MASK  0x8000




typedef union {
  struct {
    unsigned          :1;
    unsigned INT1     :1;
    unsigned INT2     :1;
    unsigned INT3     :1;
    unsigned INT4     :1;
    unsigned INT5     :1;
    unsigned INT6     :1;
    unsigned INT7     :1;
    unsigned          :8;
  };
  struct {
    unsigned short w  :16;
  };
} __INTSOURCEbits_t;    // reg 29: PHY_REG_INT_SOURCE

typedef union {
  struct {
    unsigned          :1;
    unsigned INT1     :1;
    unsigned INT2     :1;
    unsigned INT3     :1;
    unsigned INT4     :1;
    unsigned INT5     :1;
    unsigned INT6     :1;
    unsigned INT7     :1;
    unsigned          :8;
  };
  struct {
    unsigned short w  :16;
  };
} __INTMASKbits_t;  // reg 30: PHY_REG_INT_MASK


typedef union {
  struct {
    unsigned SCRMBL_DISBL  :1;
    unsigned               :1;
    unsigned SPEED         :3;   // 1: 10MbpsHD; 5:10MbpsFD; 2: 100MbpsHD; 6: 100MbpsFD;
    unsigned               :1;
    unsigned ENABLE_4B5B   :1;
    unsigned GPO           :3;
    unsigned               :2;
    unsigned AUTODONE      :1;
    unsigned               :3;
  };
  struct {
    unsigned short w       :16;
  };
} __PHYCTRLbits_t;  // reg 31: PHY_REG_PHY_CTRL
#define _PHYCTRL_SCRMBL_DISBL_MASK  0x0001
#define _PHYCTRL_SPEED_MASK         0x001c
#define _PHYCTRL_SPEED_FDUPLX_MASK  0x0010
#define _PHYCTRL_SPEED_100_10_MASK  0x000c
#define _PHYCTRL_SPEED_100_MASK     0x0008
#define _PHYCTRL_ENABLE_4B5B_MASK   0x0040
#define _PHYCTRL_GPO_MASK           0x0380
#define _PHYCTRL_AUTODONE_MASK      0x1000



#endif  // _SMSC_8700_H_

