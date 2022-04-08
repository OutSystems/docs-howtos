---
summary: Instructions to guide you through the process of migrating application data in OutSystems.
tags: data-migration-of-outsystems-applications;
locale: en-us
guid: 7ba670ee-b94a-4d1c-ab09-5b44d9d6c8e9
---

# How To Migrate Data

This document is a complement to the [Data Migration Guide](10-data-migration-guide.md) for the use Case of **migrating data from Production to Non-Production environments**, for single, multiple applications or all the applications of an environment.
The goal is to provide some examples and guidance regarding the migration process. You can find questions and procedures directly related to data migration tasks, but also other questions that provide more knowledge over the database or can influence the data migration strategy and solution approach.

## General Questions

This sections shows common general questions related to data migration.

### How to Find Entities with Binary Type Attributes?

Binary types of attributes take up lots of disk space and consume time and resources when you need to migrate these. 
This is why it is important to find this type of attribute and the related Entities to prepare and have a plan to migrate this kind of data. 

The following query returns all the Entities belonging to an application containing binary types of attributes:

```
SELECT 
	  app.NAME [Application]
	, entity.NAME [Entity Name]
	, entity.PHYSICAL_TABLE_NAME [PhysicalTable Name]
	, attribute.NAME [Attribute]
FROM ossys_Entity_Attr attribute
JOIN ossys_Entity entity
	ON attribute.Entity_id = entity.id
	AND entity.IS_ACTIVE = 1 /* Active Entities*/
	AND entity.IS_SYSTEM = 0 /* Not system */
JOIN ossys_Espace espace
	ON entity.ESPACE_ID = espace.ID
JOIN ossys_Module module
	ON espace.ID = module.ESPACE_ID
JOIN OSSYS_APP_DEFINITION_MODULE appmodule
	ON module.ID = appmodule.MODULE_ID
JOIN OSSYS_Application app
	ON appmodule.APPLICATION_ID = app.ID 
WHERE 
	/* Active Entity Attributes */
	attribute.IS_ACTIVE = 1 
	/* Filter Binary Data type */
	AND attribute.TYPE = (
		select ID from OSSYS_BASIC_TYPE where NAME = 'BinaryData'
	)
ORDER BY app.NAME
	, entity.NAME
	, entity.PHYSICAL_TABLE_NAME
	, attribute.NAME
```

An example of a partial result of the the previous query:

|Application | Entity Name |PhysicalTable Name |Attribute |
|------------|-------------|-------------------|----------|
|App Feedback |FeedbackScreenshot |OSUSR_s41_FeedbackScreenshot | ImageBinary|
|App Feedback |FeedbackSoundMessage |OSUSR_s41_FeedbackSoundMessage |SoundBinary |
|App Feedback |Resource |OSUSR_s41_Resource |Content |
|App Feedback |WebpageContent |OSUSR_s41_WebpageContent |Content |

### How to Disable an Application?

Use Service Center to disable an Application. Go to the Factory, Applications list, search for the Application you want to disable and select it to go to the Application Details where you can find the Disable button.

When an Application is disabled the following happens:

* Web pages are not available - a screen message is displayed with the message “Application Temporarily Unavailable”
* Web Services are not available - the service returns the output:```{"Errors":["The Application is offline."],"StatusCode":500}```
* Timers are not running. If the timer is set to run in the meantime the application is disabled, it will run right after enabling the Application.
* BPT is stopped. The database triggers are active, but the schedule will not process the records in the system entities ``OSSYS_BPM_EVENT`` and ``OSSYS_BPM_EVENT_QUEUE``. After enabling the Application, the records in these tables are processed, meaning that the BPT Processes and Activities return to their normal flow.

## Users

### How to Get Application Users?

Searching for User Entity foreign key usage requires two steps:

1. Search for Entity attributes using the User Entity Identifier as a foreign key.
    * Example - Details about the following query:
        * Filtered by active Epaces in the Application named ``App Feedback``.
        * Filtered to return only the ``Data Kind`` entity, removing static entities info from the result
        * Filtered by the User Identifier attribute Type with the format ``‘bt’[Espace SS-Key]’*’[Entity SS-Key]``, where ``bt`` stands for business type then the ``SS_Key`` of the Espace Service Center (``OSSYS_ESPACE``) followed by ``*`` and ending on the User Entity ``SS_Key`` (``OSSYS_ENTITY``).

```
		SELECT 
	        OSSYS_APPLICATION.NAME [Application]
	        , OSSYS_ESPACE.NAME [Espace]
	        , OSSYS_ENTITY.NAME [Entity Name]
	        , OSSYS_ENTITY.PHYSICAL_TABLE_NAME [Physical Table Name]
	        , OSSYS_ENTITY_ATTR.NAME [Attribute]
        FROM OSSYS_APPLICATION
        JOIN OSSYS_APP_DEFINITION_MODULE
	        ON OSSYS_APPLICATION.ID = OSSYS_APP_DEFINITION_MODULE.APPLICATION_ID
        JOIN OSSYS_MODULE
	        ON OSSYS_APP_DEFINITION_MODULE.MODULE_ID = OSSYS_MODULE.ID
        JOIN OSSYS_ESPACE
	        ON OSSYS_MODULE.ESPACE_ID = OSSYS_ESPACE.ID
        JOIN  OSSYS_ENTITY
	        ON OSSYS_ESPACE.ID  = OSSYS_ENTITY.ESPACE_ID
        JOIN OSSYS_ENTITY_ATTR
	        ON OSSYS_ENTITY.ID = OSSYS_ENTITY_ATTR.Entity_Id 
        WHERE OSSYS_APPLICATION.IS_ACTIVE = 1 /* Active Application */
	        AND OSSYS_APPLICATION.NAME = 'App Feedback'
	        AND OSSYS_ESPACE.IS_ACTIVE = 1 /* Active Espaces */
	        AND OSSYS_ESPACE.IS_SYSTEM = 0 /* Not a System Espace */
	        AND OSSYS_ENTITY.IS_ACTIVE = 1 /* Active Entity */
	        AND OSSYS_ENTITY.Data_Kind = 'entity' /* staticEntity, entity, clientEntity */
	        AND OSSYS_ENTITY_ATTR.IS_ACTIVE = 1 /* Active Attributes */
	        AND OSSYS_ENTITY_ATTR.TYPE = 
		        CONCAT(
		        'bt', /* Business concept Type */
		        /* SS_Key of the Espace Owner of the Platform Entities */
		        (	SELECT SS_KEY 
			        FROM OSSYS_ESPACE 
			        WHERE NAME = 'ServiceCenter'), 
		        '*', /* Separator */
		        /* SS_Key of the User Entity of the corresponding Espace above */
		            (	SELECT SS_KEY 
			        FROM OSSYS_ENTITY 
			        WHERE NAME = 'User' 
				        AND ESPACE_ID = (SELECT ID FROM OSSYS_ESPACE WHERE NAME = 'ServiceCenter'))
		            )
```

|Application |Espace |Entity Name |Physical Table Name |Attribute |
|------------|-------|------------|--------------------|----------|
|App Feedback|ECT_Provider|Rule_User|OSUSR_s41_Rule_User|User_Id|
|App Feedback|ECT_Provider|FeedbackExt|OSUSR_s41_FeedbackExt|StatusChangeBy|
|App Feedback|ECT_Provider|LastFeedback|OSUSR_s41_LastFeedback|UserId|
|App Feedback|ECT_Provider|AppConfig|OSUSR_s41_AppConfig|CreatedBy|
|App Feedback|ECT_Provider|AppConfig|OSUSR_s41_AppConfig|UpdatedBy|

1. For each User Consumer Entity, it is possible to get the User Identifier values used on the application.
    * Example - Get the User Identifiers value stored on the entity ``OSUSR_s41_LastFeedback`` on the ``UserId`` attribute. Filtering the null values:
  
```
    SELECT distinct(UserId) 
    FROM OSUSR_s41_LastFeedback
    WHERE UserId IS NOT NULL
```

### How to Get Application Roles?

Get all Roles related to every Espace in an application “Users” in one environment. This query has to be executed in both environments and cross-matched using the Espace ``SS_Key`` and Role ``SS_Key`` after getting the results.

Run the following query:
```

SELECT 
  	  app.NAME [Application]
	, espace.NAME [Espace]
	, role.NAME [Role]
	, role.ID [RoleId] 
	, espace.SS_KEY [Espace SS_Key]
	, role.SS_KEY [Role SS_Key]
FROM OSSYS_APPLICATION app
JOIN OSSYS_APP_DEFINITION_MODULE appmudule
	ON app.ID = appmudule.APPLICATION_ID
JOIN OSSYS_MODULE module
	ON appmudule.MODULE_ID = module.ID
JOIN  ossys_ESPACE espace
	ON module.ESPACE_ID = espace.ID
	AND espace.IS_ACTIVE = 1 /* Active Espace */
	AND espace.IS_SYSTEM = 0 /* Not a System Espace */
JOIN ossys_Role role
	ON espace.id = role.espace_id
	AND role.IS_ACTIVE = 1 /* Active Role */
WHERE app.IS_ACTIVE = 1	/* Active Applications only */
	AND app.NAME = 'Users'
```
Example - partial result of the execution of the query:

|Application |Espace |Role        |Espace SS_Key |Role SS_Key |
|------------|-------|------------|--------------|------------|
|Users |Users |UserManager |7 |65106059-0439-4be5-b011-2f01fba4afa6 |37105987-45ed-428e-a0fa-6ec4403a3864 |
|Users |Users |SuperUser |8 |65106059-0439-4be5-b011-2f01fba4afa6 |d63e8a6e-bd39-40d2-a4c2-6e48878682d4 |


## Application Data

### How to Find Where the Application Data Is

Return all Entities and Physical Names of each returned Application Espace. Entities belonging to one Espace, which belongs to one Application. Espaces also belong to one or more Solutions. 
Espace SS Key and Entity ``SS_Key`` keep the same value between values and represent the same object between environments.

Example - searching for Entities of the Application called “App Feedback”:

```
SELECT 
	  app.NAME [Application]
	, espace.NAME [Espace]
	, entity.NAME [Entity]
	, entity.PHYSICAL_TABLE_NAME [Physical Entity Name]
	, espace.SS_KEY [Espace SS_Key]
	, entity.SS_KEY [Entity SS_Key]
FROM OSSYS_APPLICATION app
JOIN OSSYS_APP_DEFINITION_MODULE appmodule
	ON app.ID = appmodule.APPLICATION_ID
JOIN OSSYS_MODULE
	ON appmodule.MODULE_ID = OSSYS_MODULE.ID
JOIN  ossys_ESPACE espace
	ON OSSYS_MODULE.ESPACE_ID = espace.ID
		AND espace.IS_ACTIVE = 1 /* Active Espace */
		AND espace.IS_SYSTEM = 0 /* Not a System Espace */
JOIN  ossys_ENTITY entity
	ON espace.ID  = entity.ESPACE_ID
	AND entity.IS_ACTIVE = 1 /* Active Entities */
	AND entity.Data_Kind = 'entity'
WHERE app.IS_ACTIVE = 1 /* Active Application */ 	
	AND app.NAME = 'App Feedback'
```
Returns the following data:

|Application |Espace |Entity |Physical Entity Name |SS_KEY |SS_Key |
|------------|-------|-------|---------------------|-------|-------|
|App Feedback |ECT_Provider |AppConfig |OSUSR_s41_AppConfig |50957770-1dd0-42bf-9fcb-c57953b87ce1 |d43af2e2-daa1-4aec-8203-df5371aff811 |
|App Feedback |ECT_Provider |CallbackRule |OSUSR_s41_CallbackRule |50957770-1dd0-42bf-9fcb-c57953b87ce1 |37a0ee89-268b-8bed-9ba1-8a75bf145294 |

## BPT

### How to stop the BPT Trigger on the Destination Environment? 

Event Tables are used to register subscriptions that the BPT triggers. The Trigger uses data on Event tables to create entries on the BPT Event Queues. 

In Cloud infrastructures, there are no permissions to disable the BPT trigger.
One of the possible workaround solutions to stop the trigger on the destination environment is to delete all the records on the Event Entity (``OSEVT``) related to the Entity (``OSUSR``) triggered by BPT. This way the trigger is not disabled but the result is the same because nothing is created on the BPT Event Queues to be processed by the scheduler.

If needed, it’s possible to use the same workaround on the Source Environment, but there you need to be more careful to keep the original data. The Event data from the Source need to be migrated to the Destination and, in this case, would need to be inserted again to enable the trigger.

The first operation should be executed before migrating any data, like Users Data and Application Data, to avoid any trigger event to be inserted in the Event Queues.

Example - deleting all records on an Event Entity related to an ``Order``”`` Entity:

```
DELETE FROM OSEVT_ORDER 
```

### How to Get Event Tables With BPT Trigger Subscriptions?

Example - searching for the Event entities. Running the followig query:

```

select    app.NAME [Application]
	, entity.NAME [Entity]
	, entity.PHYSICAL_TABLE_NAME [Entity Physical Name]
	, entity.Event_Table_Name [Event Table Name]
from ossys_Espace espace
join ossys_entity entity
	on espace.ID = entity.ESPACE_ID
join OSSYS_MODULE module
	on espace.ID = module.ESPACE_ID
join OSSYS_APP_DEFINITION_MODULE appmodule
	on module.ID = appmodule.MODULE_ID
join OSSYS_APPLICATION app
	on appmodule.APPLICATION_ID = app.ID
where espace.IS_ACTIVE = 1
	and entity.Event_Table_Name is not null
	and entity.Expose_Process_Events = 1
	and app.IS_ACTIVE = 1
```

Returns the following data:

|Application |Entity |Entity Physical Name |Event Table Name |
|------------|-------|---------------------|-----------------|
|Service Center |TestCase |OSSYS_TEST_CASE |OSEVT_TEST_CASE |
|Service Center |Group_Role |OSSYS_GROUP_ROLE |OSEVT_GROUP_ROLE |
|Service Center |User |OSSYS_USER |OSEVT_USER |
|Service Center |Group |OSSYS_GROUP |OSEVT_GROUP |
|Service Center |Role |OSSYS_ROLE |OSEVT_ROLE |
|Service Center |Group_User |OSSYS_GROUP_USER |OSEVT_GROUP_USER |
|BPT Testing |WorldCity |OSUSR_w83_WorldCity |OSEVT_w83_WorldCity |

Example - fetching data contained on one of the Event Entities: 

```
select * 
from OSEVT_w83_WorldCity
```

Returns the followingf data:

|_ESPACE_ID |_TENANT_ID |_ACTIVITY_ID |_PROCESS_DEF_ID |_IS_UPDATE |_IS_LIGHT |ID |
|-----------|-----------|-------------|----------------|-----------|----------|---|
|26 |20 |123956 |NULL |1 |0 |2 |
|26 |20 |123958 |NULL |1 |0 |1 |
|26 |20 |123957 |NULL |1 |0 |5 |
|26 |20 |123959 |NULL |1 |0 |3 |
|26 |20 |123955 |NULL |1 |0 |4 |

* Espace Id - Espace identifier of the Espace containing the definition and development of the entity being triggered
* Tenant Id - Tenant identifier of the same User Provider of the Espace Id above
* Is_Update - defines if the event is queued to be processed by the process schedule OnUpdate or OnCreate of the entity - Used on the BPT Activity types of “wait” or “conditional start”
* Is Light - defines if the event subscription is defined on a Light BPT definition / development

### How to Get Application BPT Process Instances?

List processes that are related to an application.
The following query searches for Process Definitions and their Application and Espaces owners:

```
SELECT 
	  app.NAME [Application]
	, espace.NAME [Espace]
	, process.ID [Process Id]
FROM OSSYS_APPLICATION app
JOIN OSSYS_APP_DEFINITION_MODULE appmodule
	ON app.ID = appmodule.APPLICATION_ID
JOIN OSSYS_MODULE module
	ON appmodule.MODULE_ID = module.ID
JOIN  ossys_Espace espace
	ON module.ESPACE_ID = espace.ID
	AND espace.IS_ACTIVE = 1 /* Active Espace*/
	AND espace.IS_SYSTEM = 0 /* Not System Espace*/
JOIN ossys_BPM_Process_Definition process_def
	ON espace.id = process_def.Espace_Id 
	AND process_def.Is_Active = 1 /* Active Process Def*/
JOIN ossys_BPM_Process process
	ON process.PROCESS_DEF_ID = process_def.id
JOIN ossys_BPM_Process_Status process_status
	ON process.STATUS_ID = process_status.ID
WHERE app.IS_ACTIVE = 1	/* Active Application */
ORDER BY espace.id, process.id
```
Returns the following data:

|Application |Espace |Process Id |
|------------|-------|-----------|
|Users       |Users  |31217      |

You can add additional filters to get only the currently active process running (Process with Process Status with the flag ``Is Terminated``set to False). 

### How to Get Activities Running Instances?

List processes and activities not terminated, that are currently active and running.
The following query searches for not terminated Process Definitions, their related process instances, not terminated Activities related to the process instances, and their Application and Espaces owners:

```
SELECT 	  app.NAME [Application]
	, espace.NAME [Espace]
	, process.ID [Process Id]
	, activity.Id [Activity Id]
FROM OSSYS_APPLICATION app
JOIN OSSYS_APP_DEFINITION_MODULE appmodule
	ON app.ID = appmodule.APPLICATION_ID
JOIN OSSYS_MODULE module
	ON appmodule.MODULE_ID = module.ID
JOIN  ossys_Espace espace
	ON module.ESPACE_ID = espace.ID
	AND espace.IS_ACTIVE = 1 /* Active Espace*/
	AND espace.IS_SYSTEM = 0 /* Not System Espace*/
JOIN ossys_BPM_Process_Definition process_def
	ON espace.id = process_def.Espace_Id 
	AND process_def.Is_Active = 1 /* Active Process Def*/
JOIN ossys_BPM_Process process
	ON process.PROCESS_DEF_ID = process_def.id
JOIN ossys_BPM_Process_Status process_status
	ON process.STATUS_ID = process_status.ID
JOIN ossys_BPM_Activity activity
	ON process.Id = activity.Process_Id
JOIN ossys_BPM_Activity_Status activity_status
	ON activity.Status_Id = activity_status.ID
WHERE app.IS_ACTIVE = 1	/* Active Application */
	and process_status.IS_TERMINAL = 0
	and activity_status.IS_TERMINAL = 0
ORDER BY espace.id, process.id
```

Returns the following data:

|Application  |Espace  |Process Id  |Activity Id  |
|-------------|--------|------------|-------------|
|BPT Testing |Migration |30987 |123960 |
|BPT Testing |Migration |30987 |123958 |
|BPT Testing |Migration |30988 |123959 |
|BPT Testing |Migration |30988 |123963 |
|BPT Testing |Migration |30989 |123961 |

