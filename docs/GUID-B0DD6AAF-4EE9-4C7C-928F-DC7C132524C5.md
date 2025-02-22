# DRV\_ETHPHY\_VENDOR\_MII\_CONFIGURE Type

**Parent topic:**[Ethernet PHY Driver Library](GUID-F4DF749A-0F8C-4482-8661-C005A0BE0CF4.md)

## C

```
typedef DRV_ETHPHY_RESULT (* DRV_ETHPHY_VENDOR_MII_CONFIGURE)(const struct DRV_ETHPHY_OBJECT_BASE_TYPE* pBaseObj, DRV_HANDLE handle, DRV_ETHPHY_CONFIG_FLAGS cFlags); 
```

## Returns

-   DRV\_ETHPHY\_RES\_OK - if success, operation complete

-   DRV\_ETHPHY\_RES\_PENDING - if function needs to be called again < 0 - on failure: configuration not supported or some other error


## Description

Pointer To Function: typedef DRV\_ETHPHY\_RESULT \(\* DRV\_ETHPHY\_VENDOR\_MII\_CONFIGURE\) \(const struct DRV\_ETHPHY\_OBJECT\_BASE\_TYPE\* pBaseObj, DRV\_HANDLE handle, DRV\_ETHPHY\_CONFIG\_FLAGS cFlags \);<br />This type describes a pointer to a function that configures the Ethernet PHY in one of the MII/RMII operation modes. This configuration function is PHY specific and every PHY driver has to provide their own implementation.

## Remarks

The PHY driver consists of 2 modules:

-   the main/base PHY driver which uses standard IEEE PHY registers

-   the vendor specific functionality This function provides vendor specific functionality. Every PHY driver has to expose this vendor specific function as part of its<br />interface. Traditionally the name used for this function is DRV\_EXTPHY\_MIIConfigure but any name can be used. The PHY driver will call the vendor set up functions after the communication to the PHY has been established. The function can use all the vendor specific functions to store/retrieve specific data or start SMI transactions \(see Vendor Interface<br />Routines\). The function should not block but return DRV\_ETHPHY\_RES\_PENDING if waiting for SMI transactions.


## Preconditions

Communication to the PHY should have been established.

