---
summary: Explore the entity relationships and data migration considerations for Users, Groups, and Roles in OutSystems 11 (O11).
locale: en-us
guid: 4cc52c9d-17cb-4c79-b17d-69bb3ef1de4a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/5uD7gg1CIy1jlOE2BNFdsU/Data?node-id=1142:245
tags: data migration, entity relationships, outsystems platform, user management, security model
audience:
  - full stack developers
  - platform administrators
  - architects
outsystems-tools:
  - service studio
  - service center
  - lifetime
coverage-type:
  - apply
---

# Application Users Groups and Roles

Another important topic regarding data migration is the application Users, Groups and Roles. This section provides explanations about how the entities in these areas relate to each other.

## Entity-Relationship Model

The following diagram shows the relationships between Entities Users, Roles and Groups.

![Diagram illustrating the relationships between Users, Roles, Groups, and their associative entities in OutSystems.](images/relationships-entities-users-roles-groups.png "Entity-Relationship Diagram for Users, Roles, and Groups")

The records for the entities in the diagram above can be generated from the following sources:

* Service Studio 
    * Publishing modules with new or changed Roles
    * Updating apps or modules

* Service Center
    * Uploading and publishing apps, solutions, or modules with Roles

* LifeTime
    * Pushing apps to another environment with Roles

* User apps
    * References to the exposed Entities and methods
    * Bootstraps for Users, Groups, and Roles 

## Considerations

Take into account the following considerations:

* Users, Groups, and Roles are not managed by the OutSystems Platform. Only by applications (By default there is the User Application Tool to manage it)

* Roles don’t have to be migrated since they are created when publishing an app, solution, or module.

* LifeTime syncronizes IT users across environments. In this case, Users from Service Center user provider (typically, ``tenant_id = 1``) don´t need to be migrated.

* If LifeTime is not being used to manage the infrastructure and applications lifecycle, the Service Center manages the IT users in each environment. In this case, if the applications being migrated utilize Service Center as User Provider, you should take these users into consideration to be migrated.

* The way to relate these entities between environments is:
Users - the attribute Username (and Tenant ID) (Note: Being different environments, and application it is possible that a user named `john.doe` in production may not be the same `john.doe` in pre-production).

* Groups - the attribute Name (and Tenant ID)

* Roles - the attribute ``SS_Key`` and the related module ``SS_Key`` attribute

* User IDs, Role IDs, and Group IDs
    * Search for Users, Groups, and Roles dependencies, where they can be used:
        * User Application Entities consuming references
        * BPT Activity Definitions - Activity Role Permission, User that toke role in Processes and Activities

* Applicational data typically has references to the User entity (for example, ``CreatedBy`` type of audit columns) So, a step of the migration process has to traverse all foreign keys and understand all records that are holding said user records, to align the corresponding User between environment and then, taking that in consideration when migrating, the application data with the changed foreign keys

* User Roles & User Groups Configurations
    * Configurations must be migrated and aligned between the source and destination environments to have the same applicational results and behavior between environments. That stands for roles assigned to users, roles assigned to groups, and groups assigned to users

* Other topics to be aware of:
    * User Passwords (Encryption)
    * Authentication Model (Different User Providers, IdP, AD, etc)
    * Tenant - if different User Providers are being used (that means different User Tenant IDs)

## Entities Description

### Users

|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|User              |OSSYS_USER              |End-user of the applications. Shared between eSpaces with the same user provider (defined in Service Studio) |

|**Producers**    |
|-----------------|
|-                |


|**Consumers**    |
|-----------------|
|OSSYS_APP_VERSION |
|OSSYS_APPLICATION |
|OSSYS_AREA |
|OSSYS_BPM_ACTIVITY |
|OSSYS_DEBUG_SESSION_DATA |
|OSSYS_DEVELOPER |
|OSSYS_ESPACE_VERSION |
|OSSYS_ESPACE_VERSION_PTA |
|OSSYS_GROUP_USER |
|OSSYS_RECOMPILATION_LOG |
|OSSYS_SERVICECENTER_USER |
|OSSYS_SESSIONTOKEN |
|OSSYS_SOLUTION |
|OSSYS_SOLUTION_PACK_REFERENCE |
|OSSYS_SOLUTION_VERSION |
|OSSYS_SOLUTIONAPPLYSETTINGS |
|OSSYS_USER_DEVELOPER |
|OSSYS_USER_OPTION |
|OSSYS_USER_ROLE |
|OSSYS_USER_USERPOOL |
|OSSYS_USERSERVICEACCOUNT |
|-----------------|

### Roles
   
|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|Role              |OSSYS_ROLE              |Espace specific roles as defined in Service Studio. Old roles are kept as inactive |

|**Producers**    |
|-----------------|
|OSSYS_ESPACE     |
    
|**Consumers**    |
|-----------------|
|OSSYS_BPM_ACTIVITY_DEF_ROLE |
|OSSYS_GROUP_ROLE |
|OSSYS_USER_ROLE |

### User Role
   

|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|User_Role         |OSSYS_USER_ROLE         |Roles for each end user       |


|**Producers**    |
|-----------------|
|OSSYS_ROLE       |
|OSSYS_USER       |
    
|**Consumers**    |
|-----------------|
|-                |

#### Groups
   
|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|Group             |OSSYS_GROUP             |Set of users managed in runtime |

|**Producers**    |
|-----------------|
|-                |

|**Consumers**    |
|-----------------|
|OSSYS_BPM_ACTIVITY |
|OSSYS_GROUP_ROLE |
|OSSYS_GROUP_USER |

### Group Role
   
|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|Group_Role        |OSSYS_GROUP_ROLE        |Roles shared for a specific user group |
    
|**Producers**    |
|-----------------|
|OSSYS_GROUP      |
|OSSYS_ROLE       |

|**Consumers**    |
|-----------------|
|-                |

### Group User
   
|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|Group_User        |OSSYS_GROUP_USER        |Users of a specific group     |

|**Producers**    |
|-----------------|
|OSSYS_GROUP      |
|OSSYS_USERS      |
   
|**Consumers**    |
|-----------------|
|-                |

## End Users Authentication - Data & Synchronization

Regarding this topic, it is relevant to read the [End-Users Authentication](https://success.outsystems.com/Documentation/11/Developing_an_Application/Secure_the_Application/End_Users/End_Users_Authentication) documentation.

[Proceed to the next section](06-static-entities.md)
