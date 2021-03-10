---
tags: SAP; connection; security;
summary: Description of connecting to SAP
---

# SAP Connection

How is the connection made from the connector to SAP, what is the security of the communication?

## How to connect to the SAP 

## How the SAP connection works on the platform

The OutSystems platform relies on sapnco **SAP Connector for Microsoft.NET 3.0.x for Windows 64bit (Compiled with .NET Framework 4.0)** which is fully documented **[here](http://logosworld.com/docs/SAP/Connector/SAP%20Connector%20for%20Microsoft%20.NET%20%20NCo_30_ProgrammingGuide.pdf)**. Exact version of SAP connector can be find in the **[Platform Server installation checklist](http://www.outsystems.com/goto/checklist-11?_gl=1*jfriof*_ga*MTY1NzI5NTk0LjE2MTUyODQyOTg.*_ga_ZD4DTMHWR2*MTYxNTM4Nzk0NC44LjEuMTYxNTM4ODc2MC42MA..)**.
Therefore, it uses the regular username and password in the connection string. For alternative authentication mechanism more information can be found **[here](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Extensibility_and_Integration/SAP/SAP_Connection)**.

Furthermore, this connection assumes a secure network is being used, which means it doesn’t use a secure protocol (communication is performed through HTTP).
In order to add a secure layer, a custom configuration is required, including on the server side (SAP system). This is present in the documentation in SNC_MODE parameter (**[SAP .NET Connector, pp 40](http://logosworld.com/docs/SAP/Connector/SAP%20Connector%20for%20Microsoft%20.NET%20%20NCo_30_ProgrammingGuide.pdf)**).

In addition, by default the data transmitted is not encrypted, however, it can be configured on the OnBeforeConnection() callback that you can find more information in **[this article](https://success.outsystems.com/Documentation/11/Extensibility_and_Integration/SAP/Integrate_with_a_SAP_System)**, Combining this information with the **[SAP Extensibility API](https://success.outsystems.com/Documentation/10/Reference/OutSystems_APIs/SAP_Extensibility_API#SAPConnection_Class_Net)** it is possible to implement an alternative authentication mechanism. 
