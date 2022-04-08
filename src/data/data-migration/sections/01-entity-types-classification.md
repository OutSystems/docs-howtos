---
summary: A guide to migrate from Production to Non-Production environments in OutSystems - Classification of Entity Types
tags: data-migration-between-outsystems-installation; data-migration-between-production-and-non-production-outsystems; entity-types-classification
en_title: OutSystems Platform Metamodel
locale: en-us
guid: dce526c4-9948-404e-a2a5-c55ef13747d7
---

# OutSystems Platform Metamodel

Consider the following explanation, classifications and topics, to better understand the OutSystems Platform metamodel, from the data migration point of view.

## Classification of Entity Types

Entities (tables) can be grouped into three main types:

* System Entities
* Application Entities
* Hybrid Entities

### System Entities

While creating an entity you give the logical name and the OutSystems Platform creates a physical name for it internally. The mapping between the physical table name and the logical name is in the OSSYS_ENTITY table. Systems Entities are usually recognized by the prefix “OSSYS_” in their names and are pure system tables that are used in the metamodel of the OutSystems Platform.

Depending on the data migration type these entities must be used just to READ information and it is strictly not allowed to change/write in these entities to maintain the OutSystems Platform integrity and health.

Note that there are special exceptions like scenarios where some System entities need to be also migrated to keep configurations, endpoints, and so on (for example, data migration from Production to Production - which is not covered in this use case).

The categorized System Entities can be subgrouped by different topics:

* Support the OutSystems Platform Factory
    * Applications & Modules
    * Espaces and Extensions
    * Solutions, Versions and Publication Traces
    * Entities, Attributes, and Records

*   Support the Applications
    * BPT definitions
    * Tenants
    * Timers
    * Site properties
    * Integrations
    * Email definitions
    * Other

* Support the OS Platform Engine & other Configurations
    * Parameter
    * Other

#### Examples
The following table shows an examples of system entities:

| **System Entities** |
|----------|
| OSSYS_APP_DEFINITION_MODULE |
| OSSYS_APPLICATION |
| OSSYS_BPM_ACTIVITY_DEFINITION |
| OSSYS_BPM_ACTIVITY_OUTPUT_DEF |
| OSSYS_BPM_EVENT |
| OSSYS_BPM_EVENT_QUEUE |
| OSSYS_BPM_PROCESS_DEFINITION |
| OSSYS_BPM_PROCESS_INPUT_DEF |
| OSSYS_BPM_PROCESS_OUTPUT_DEF |
| OSSYS_ENTITY |
| OSSYS_ENTITY_ATTR |
| OSSYS_ENTITY_RECORD |
| OSSYS_ESPACE |
| OSSYS_ESPACE_ENTITY |
| OSSYS_ESPACE_TENANT |
| ... |

The following tables shows an examples of system application settings:

| **System Application Settings** |
|-----------|
| OSSYS_CYCLIC_JOB |
| OSSYS_CYCLIC_JOB_SHARED |
| OSSYS_META_CYCLIC_JOB |
| OSSYS_SITE_PROPERTY |
| OSSYS_TENANT |
| OSSYS_WEB_REFERENCE |
| OSSYS_WEB_SERVICE |

### Application Entities

These tables are usually recognized by the prefix `OSUSR_`in their name and relate directly to the application development. Applicational entities relate to the business and do not exist until the application is created. 

The data migration process must be allowed to read and write on these entities, except for the physical static entities’ info that should not be changed because it is normally being consumed in other entities as foreign keys in one or more applications.
The nature of these tables is very flexible and it depends on how the code was developed.

Contrary to the Systems Entities, we are not able to list the Application Entities here, as these are only created when an application is developed in OutSystems.

### Hybrid Entities

These are the tables that are managed by the OutSystems Platform (similar to pure system tables). However, as the applications are created, they interact with these tables (that is, create records on them). Based on this, these are the tables that require more attention and work from a data migration perspective.

You must have a good understanding of these types of tables because in a data migration process it is required to read them, and to write on them as well - however under certain conditions.
These entities can be subgrouped by categories:

* Users 
* BPT Processes Instances 
* BPT Activities Instances
* BPT Events
* Emails

[Proceed to the next section](02-factory-application-modules.md)
