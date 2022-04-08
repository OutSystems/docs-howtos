---
summary: A guide to migrate from Production to Non-Production environments in OutSystems - Factory Application Modules
tags: data-migration-between-outsystems-installation; data-migration-between-production-and-non-production-outsystems; factory-application-modules
---

# Factory Application Modules

To create a process or tool to move data between different OutSystems environments, it is important to understand how the OutSystems platform manages the development factory, such as Applications, Modules, Espaces, and Extensions; and also how the OutSystems Platform manages the factory applicational database info, such as Entities, Entities Records of Static Entities, and Entities Attributes and Types.

## Entity-Relationship Model

The following diagram shows the relationships between Applications, Espaces, Modules, and Extensions.

![Relationships between Applications, Espaces, Modules, and Extensions](images/relationships-applications-espaces-modules-extensions.png?\width=750)

The records for the entities in the diagram above can be generated from the following sources:

* Service Studio 
    * Creating new Applications
    * Creating or Cloning Espace Modules
    * Updating Applications or Espace Modules

* Integration Studio
    * Creating or Updating Extensions 

* Service Center
    * Uploading and Publishing Applications, Solutions, Espaces and Extensions

* Lifetime
    * Pushing Applications to another Environment

* User Applications
    * References to the Exposed Entities and methods

* APIs
    * [DB Cleaner API](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/DbCleaner_API)
    * [Lifetime API](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/LifeTime_API_v2)

## Considerations

Take the following considerations into account:

* SS_Keys 
    * The Espace / Extension always have a unique ``SS_Key`` generated and stored in the metamodel and is e equal in all environments.

    * Other SS_Keys - Entity, Entity_Attr, and so on - **are not unique** and always need to be compared using the Espace ``SS_Key`` as a unique pair of SS_Keys (for example, Cloned Espace generates a new ``SS_Key`` for the Espace but all other objects keep the ``SS_Key``)

* Check the `Is Active` flag to include or exclude inactive - soft-deleted - Applications, Espaces, and Extensions

* Be aware of Exposed Systems Entities that can be referenced and used on User Applications (Entity extended attributes, etc.)

* The Module type can be Espace or Extension. This means that the Module Espace Identifier or the Extension Identifier have exclusive values or Null value. Identifiers with null values or both Identifiers with an existing identifier cannot exist at the same time. 

* A Cloned Espace gets a new SS_Keys, and is not related with the source Espace application or any other application, and can be found on the “Independent Modules”. The same happens with cloned Extensions.

* Deleting an Espace or Extension results on the change of the `Is Active` flag  set to false, updating the name on the database with an added suffix `(deleted0)` and changing the ``SS_Key`` (This allows someone to upload and publish the same previous Espace or Extension from another source, for example, Forge). The relation of the Extension with the Application is also removed.

* Deleting an Application also results in the change of the `Is Active` flag set to false, and changing the ``SS_Key``. In this case, the Application name does not change, but the relation between the application and the modules is deleted and the modules are soft deleted, having the same behavior as if they were deleted individually.

## System Entities Description

### Applications

* Application Mobile
     
|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|ApplicationMobile |OSSYS_APPLICATIONMOBILE |Mobile apps specific settings |

|**Producers**    |
|-----------------|
|OSSYS_APPLICATION|

|**Consumers**    |
|-----------------|
|-                |
 
* Application
  
|**Name**          |**Physical Table Name** |**Description**                                                         |
|------------------|------------------------|------------------------------------------------------------------------|
|ApplicationMobile |OSSYS_APPLICATION       |Applications in this environment. Old applications are kept as inactive |

|**Producers**    |
|-----------------|
|OSSYS_USER       |


|**Consumers**    |
|-----------------|
|OSSYS_APP_CSP    |
|OSSYS_APP_DBCONFIG |
|OSSYS_APP_DEFINITION_MODULE |
|OSSYS_APP_FORGE |
|OSSYS_APP_MOBILE_BASE |
|OSSYS_APP_PARAMETER |
|OSSYS_APP_SECURITY |
|OSSYS_APP_VERSION |
|OSSYS_APPLICATION_ICON |
|OSSYS_APPLICATION_ICONHIGHRES |
|OSSYS_APPLICATIONMOBILE |
|OSSYS_APPOVERREXTCONFIG |
|OSSYS_NATIVEPLUGINS |

### Modules

* Definition Module

|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|App_Definition_Module |OSSYS_APP_DEFINITION_MODULE |Modules for a specific application definition. Internal use only |

|**Producers**     |
|------------------|
|OSSYS_APPLICATION |
|OSSYS_MODULE      |

|**Consumers**    |
|-----------------|
|OSSYS_APP_DEFINITION_MODULE |

*  Module
    
|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|Module            |OSSYS_MODULE            |An Espace or an Extension     |


|**Producers**     |
|------------------|
|OSSYS_MODULE_KIND |
|OSSYS_ESPACE      |
|OSSYS_EXTENSION   |


|**Consumers**    |
|-----------------|
|OSSYS_APP_DEFINITION_MODULE |


* Module Kind
     
|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|Module_Kind       |OSSYS_MODULE_KIND       |Espace and Extension          |

|**Producers**     |
|------------------|
|-                 |

|**Consumers**    |
|-----------------|
|OSSYS_APP_VERSION_MODULE_VERSI |
|OSSYS_MODULE     |

### Espace Modules

* Espace
     
|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|Espace            |OSSYS_ESPACE            |Espaces defined in Service Studio. Older and deleted Espaces are kept as inactive |

|**Producers**        |
|---------------------|
|OSSYS_ESPACE_VERSION |
|OSSYS_DBCATALOG      |
   
|**Consumers**    |
|-----------------|
|OSSYS_AREA       |
|OSSYS_ASSEMBLY |
|OSSYS_ASSEMBLY_DEPENDENCY |
|OSSYS_ASYNC_OP_DBCATALOG |
|OSSYS_AUTHPROVIDER |
|OSSYS_BPM_PROCESS_DEFINITION |
|OSSYS_CALLBACK |
|OSSYS_DEBUG_SESSION_DATA |
|OSSYS_DEVELOPER_ESPACE |
|OSSYS_EMAIL_DEFINITION |
|OSSYS_ENTITY |
|OSSYS_ENTITY_RECORD |
|OSSYS_ESPACE_CONFIGURATION |
|OSSYS_ESPACE_ENTITY |
|OSSYS_ESPACE_EXTENSION |
|OSSYS_ESPACE_FRAGMENTS |
|OSSYS_ESPACE_MOBILE_CONFIGS |
|OSSYS_ESPACE_PRODUCTINFO |
|OSSYS_ESPACE_REFERENCE_STATUS |
|OSSYS_ESPACE_RUNNING_PROD_VER |
|OSSYS_ESPACE_RUNTIME |
|OSSYS_ESPACE_SCREEN |
|OSSYS_ESPACE_SHAREDCONFIG |
|OSSYS_ESPACE_VERSION |
|OSSYS_ESPACE_VERSION_PTA |
|OSSYS_LICENSINGEMAILLOG |
|OSSYS_META_CYCLIC_JOB |
|OSSYS_MODULE |
|OSSYS_NATIVEPLUGINS |
|OSSYS_PAGEMETARULE |
|OSSYS_RECOMPILATION_ERROR_LOG |
|OSSYS_REPORT_SLOWSRVAPI |
|OSSYS_REST_EXPOSE |
|OSSYS_REST_WEB_REFERENCE |
|OSSYS_ROLE |
|OSSYS_SAPCONFIG |
|OSSYS_SITE_PROPERTY_DEFINITION |
|OSSYS_SOAP_CONSUME |
|OSSYS_SOLUTION_REFERENCE |
|OSSYS_SRVAPI_CONFIGS |
|OSSYS_TENANT |
|OSSYS_TENANT_VIEW |
|OSSYS_TEST_CASE |
|OSSYS_TRANSLATIONOVERRIDE |
|OSSYS_WEB_REFERENCE |
|OSSYS_WEB_SERVICE|

## Extension Modules

* Extension
     
|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|Extension         |OSSYS_EXTENSION         |Extensions published in the environment |
    
|**Producers**        |
|---------------------|
|OSSYS_EXTENSION_VERSION |
    
|**Consumers**    |
|-----------------|
|OSSYS_ASSEMBLY   |
|OSSYS_ASSEMBLY_DEPENDENCY |
|OSSYS_ASYNC_OP_LOGICALDATABASE |
|OSSYS_DEVELOPER_EXTENSION |
|OSSYS_ENTITY |
|OSSYS_ESPACE_EXTENSION |
|OSSYS_EXTENSION_CONFIGURATION |
|OSSYS_EXTENSION_DBCONNECTION |
|OSSYS_EXTENSION_DEPENDENCY |
|OSSYS_EXTENSION_VERSION |
|OSSYS_MODULE |
|OSSYS_SOLUTION_REFERENCE |

* Espace Extension
     
|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|Espace_Extension  |OSSYS_ESPACE_EXTENSION  |Extensions referred by each Espace as defined in Service Studio add/remove references |

|**Producers**        |
|---------------------|
|OSSYS_ESPACE         |
|OSSYS_EXTENSION      |
    
|**Consumers**    |
|-----------------|
|-                |

[Proceed to the next section](03-factory-database.md)
