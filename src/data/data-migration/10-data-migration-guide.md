---
summary: A guide to migrate data of an OutSystems Application
tags: data-migration-of-outsystems-applications;
---

# Introduction to Data Migration

This guide is a starting point to support migrating data of an OutSystems Application. You must define each specific solution in a case-by-case scenario.

## Data migration goal

The goal of this guide is to migrate pure application data and hybrid data of one application (or solution) from a source Production Environment to a destination Non-Production Environment.

### Recommendations (between source and destination Environment)

* Platform versions: OutSystems recommends having the same Platform version between Source and Destination to avoid any risk, but depending on the solution tool, it's not mandatory to have the same version.

* The database Engine and versions have to be the same.

* Database Definition: It's preferable to have the same Database definition between Source and Destination, but if the definition isn't the same, you have to manage the differences between them. For example, check what do to with new attributes on the destination with or without default values and soft-deleted attributes. Also, don´t forget what to do with new Entities or soft-deleted Entities on the destination.

* Business Process Technology (BPT) Processes Definition Differences: While it's still possible to migrate processes and activities data having different definitions between environments, there is a high probability to migrate data no longer needed or missing data for new BPT definitions.

* Destination Entities Data - Option to delete before migrate: if the goal is to have the same data from Production to Non-Production environment for testing purposes, it's important to not have dirty data or duplicates that can change calculations, metrics, dashboards, etc. One of the options is to have a migration process's first step for deleting the destination data and its dependencies. In this case, don't forget that there might be data consumers that you may also have to delete.

* Destination Applications Downtime: It's recommended, but not mandatory, that you disable the relevant applications in the Destination environment while the migration process is running, both to prevent users from accessing the Application and to stop all the application activity that can impact the business and applicational data. This means Timers, Processes, and Integrations that shouldn't run while the migration process is running. In this case, be sure to disable the Applications in the Service Center.

### Other notes and awarenesses

* Don’t migrate site properties, settings, configuration, and integration endpoints from Production to Non-Production.

* If the data isn't deleted from the destination, the migration process has to take care of unique indexes that can't be repeated.

* In Cloud the permissions are limited to Data-reader and Data-writer.

* Be aware that Soft-Keys (SKs) aren't mapped and replaced automatically like the Foreign-Keys (FKs) and this may affect the application behavior in runtime.

## Migrating data

### Applicational and Hybrid Data Entities Domain

For the migration process start by inspecting and getting the list of all entities that are the source of data to migrate to the destination.

The migration Data Domain includes the normal business applicational data, and also hybrid data like the business processes instances and user and group info.

This can be based on a Solution, or on a set of Applications, just one application or even just an Espace, but has to include all the producers on which it depends.

Refer to the [How To Migrate Data](11-how-to-migrate-data.md) document to see how you can get this information.

### Match Entities and Attributes Physical Names

In the current step, the process has to match the active entities and their attributes.

The active Entities and their attributes can have different physical names between environments. It is possible not only to mismatch names, but also to have duplicated entities or attributes inside the entities, but only one entity and attribute are active and matching between environments.

It's extremely important to keep in mind this match if using any query to push data from source entities and source attributes to their corresponding destination-related entities and source attributes. The match is done using the `SS_key` or Entity `Attribute SS_Keys` always combined with the related Espace `SS_key` (it is possible to have repeated Entities SS_Keys but not if combined with the Espace `SS_Key`).

Find more details about the Platform Factory Management on the [Factory Application Modules](sections/02-factory-application-modules.md) and [Factory Database](sections/03-factory-database.md) sections.

### Match System Static Entities Records Identifiers 

Now, the process has to match the Static Entities Records Data Identifiers being used has foreign keys on the Entities Data that are to be migrated.

Static Entities are managed by the OutSystems Platform and must not be changed. Considering the same Application version published between environments, then the same active Static Entities’ Records exist in both environments and the corresponding identifier exists in the physical `OSUSR` table.

The enumerated Entity Records correspondent Identifiers can be different between environments, so these have to match to be manipulated and changed on the migrating data migrating, to match the same business concept or meaning between environments.

Based on the data that you are going to migrate, the process has to:

1. Get the list of all Static Entities used has foreign keys
1. Match the Static Records Identifier using the Entity Records `SS_Key` and Espace `SS_Key`.
1. Keep the matched identifier values to replace the foreign keys, if different between environments.

For more details refer to the [Static Entities](sections/06-static-entities.md) section.

### Disable BPT Triggers

The Entities being triggered by BPT have a  directly related `Triggered` and a corresponding `OSEVT` entity where all the entity’ events are subscribed.

One solution to stop the BPT Triggers is to search for all the BPT Triggered entities and delete all the data on the destination OSEVTs entities. In this case the trigger runs (not the best solution) but checks for BPT event subscriptions and will not find anything, so nothing is inserted on the System Event Queues for processing by the scheduled systems.
This workaround does not disable System Triggers, but tries to get the same result and behavior as if they were disabled.

In a forward step, the Event entities data is migrated and the normal behavior reestablished.

### Create or Update Users & Groups

In this step the migration process checks if all Users related to the applications and data being migrated are created in the destination environment. 

Users usually are the most used foreign key all over applicational data and the Applications behavior can change based on Users' Roles and permissions, and the User can belong to Groups with assigned Roles.

To achieve this goal the migration process has to:

* Get the domain of Users used by the Application to migrate
* It is then possible to have different approaches to User migration:

    1. If the User data is somehow used in the Application and can be changed (for example, phone numer or email) the user that already exists on the destination might need to be updated, so a good aproach could be deleting all matched users in the destination and create them again.
    1. If the Users are only used for login and having foreign keys on the applicational data, then it's possible to check which users need to be created on the destination.

Depending on the approach, create or update:

* Users
* User Roles - Roles directly assigned Users
* Groups
* Group Roles - Roles assigned to Groups
* Group Users - Users assigned to Groups resulting on Roles assigned to groups, and so being indirectly assigned to Users

Match User by username, and Groups by name, and keep the mapped identifiers between environment so these can be used to replace the foreign keys on the consumers entities when being migrated in a future step.

For more details on Users and  Groups Metamodel, refer to the [Application User Groups](sections/05-application-users-groups-roles.md) section.

### Migrate Application Data

In this step, the migration process starts getting entities' data from the source and pushing it to the destination environment.

Previously, you set a list of Entities to migrate. Start by getting all the Entities related to:

* One Espace - all Entities related to the Espace
* One or more Applications - all Entities related to all Espaces related to the Applications
* One Solution - all Entities related to Espaces related to the Solution

Having the Domain of Entities to migrate (`OSUSR*`) and clearing the Event Entities (`OSEVT*`) related to this domain, the process can then start the data migration.

Based on the previous steps, and for this data migration guide purpose, consider that th data migration process has an auxiliar supporting table (temporary or not) mapping and matching entity identifiers between source and destination environment. This can be used to replace the foreign keys on the destination accordingly to the map. This Foreign Keys Map (also know as FKs-Map) can be processed in differents steps depending on each type:

* Static Entities Records Identifiers.

    The Static Identifiers matching can be done in an early step since the data is managed by the platform and only changes if the developed solution changes,

* Users Identifiers

    The Users Identifiers matching can be done in the step where the Users are aligned between environments.

* All other Foreign Keys Map

    This Identifiers match only occurs while the process of data migration is running and progressing.

Depending on how the data migration process is implemented, the Entities need to follow a precedence order based on the foreign keys dependency. That is caused by the Foreign keys precedency where it's not possible to insert records with foreign keys that weren't already migrated and mapped on FK-Map. This means that the migration solution has to find the best way to deal with the dependencies between entities and indirect cyclic dependencies. One way to deal with the entities cyclic dependencies in the migration process is to find the optional foreign keys (FK), leave that FK empty upon insert (1st step) and update it later on (2nd step).

#### General Process to Migrate an Entity Data

For each Entity Ordered by Foreign Keys dependencies:

* Consider the match for Physical Table Name and Attributes between environments

* Get a Record from the Source and:

    * Insert the Source Id on the FKs-Map, with the corresponding Espace `SS_Key`, Entity `SS_Key` and Attribute `SS_Key`
    * Replace All Foreign Keys from the Source Id to the Destination Id found on the FKs-Map
    * If the Record has a Foreign Key to its own Id, after the insertion, the Record has to be updated with the new Id
    * Insert the new Destination Id on the FKs-Map, for the same Espace SS_Key, Entity SS_Key and Attribute SS_Key

The process can be improved depending on the DB Entities Relationship complexity level, by trying to do bulk foreign keys replacements over temporary tables before processing each record.

### Migrate Hybrid BPT Instances Data (OSSYS_BPM_* Instances)

This is the step of the process where the Process Application Instances Data is migrated. The definitions are keeped by the platform and must not be changed.

The following list shows the BPT Hybrid tables:

* OSSYS_BPM_PROCESS
* OSSYS_BPM_PROCESS_INPUT
* OSSYS_BPM_PROCESS_OUTPUT
* OSSYS_BPM_ACTIVITY
* OSSYS_BPM_ACTIVITY_OUTPUT

Before migrating the BPT Instances data, if the data migration process has not mapped already, then it needs to map the source identifier with the destination identifiers to the Foreign Keys Map (a.k.a. FKs-Map):

* Process Definitions Identifiers
* Process Input Definitions Identifiers
* Process Output Definitions Identifiers
* Activity Definitions
* Activity Output Definitions Identifiers
* Roles Identifiers
* Tenant Identifiers

The step-by-step procedure to migrate BPT Instances is the same as for Applications Data. For each Entity Ordered by Foreign Keys dependencies:

* Consider the match for Physical Table Name and Attributes between environments

* Get a Record from the Source and:

    * Insert the Source Id on the FKs-Map, with the corresponding Espace `SS_Key`, Entity `SS_Key` and Attribute `SS_Key`
    * Replace all Foreign Keys from the Source Id to the Destination Id found on the FKs-Map
    * If the Record has a Foreign Key to its own Id, after the insertion, the Record has to be updated with the new Id <sup>(&#42;)</sup>
    * Insert the new Destination Id on the FKs-Map, for the same Espace SS_Key, Entity SS_Key and Attribute SS_Key
    * Insert the new Destination Id on the FKs-Map, for the same Espace `SS_Key`, Entity `SS_Key` and Attribute `SS_Key`

<p style="font-size:12px" markdown="1">

(*) Note: Be aware of some special foreign keys on the Process instance entity `PARENT_ACTIVITY_ID` with FKs:

* `PARENT_ACTIVITY_ID` - which is migrated after the process migration. In this case the process has to be updated after the Activities migration.
* `TOP_PROCESS_ID` - On a root process, the Top Process Id is itself. In this case it means that the Top Process Id have to be updated after the process record migration.

</p>

### "Enable" BPT Trigger - Migrate Hybrid BPT Events Data (OSEVT_*)

Search for every possible OSEVT table that has data to be migrated.

These OSEVT Entities don't have their owned Identifiers and have a well defined common structure:

* `_ESPACE_ID`
* `_TENANT_ID`
* `_ACTIVITY_ID`
* `_PROCESS_DEF_ID`
* `_IS_UPDATE`
* `_IS_LIGHT`

followed by some particular fields of the related Entity:

* Entity ID
* Entity Foreigh keys (multiple fields)

Now the migration process is similar to the previous ones, getting the data from the source environment, replacing the foreign keys (`_ID`) with the known mapped identifier to the destination environment.

## Final Steps

After the migration, don't forget to enable the applications on the destination environments.

Now the users can login into Applications, call Integrations, and Timers and Processes run again.
