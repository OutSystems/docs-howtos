---
summary: A guide to migrate from Production to Non-Production environments in OutSystems - Static Entities
tags: data-migration-between-outsystems-installation; data-migration-between-production-and-non-production-outsystems; static-entities
locale: en-us
guid: 23483ef2-7c45-48af-9a05-977eaadbc72f
---

# Static Entities

Migrating data from Static Entities requires some considerations. Firstly, it's important to understand how the OutSystems Platform manages Static Entity Records and how they relate with the corresponding Physical Table.

## Considerations

Take into account the following considerations:

* When a new Static Entity is published, the OutSystems Platform creates:
    * Entity info for the new Static Entity (``OSSYS_ENTITY``)
    * Entity Attributes info (``OSSYS_ENTITY_ATTR``)
    * Entity Records (``OSSYS_ENTITY_RECORD``), with special attribute Data ID with the corresponding value of the Physical Application Table ID 
    * The Physical applicational Table with the attribute values set for each record
    * Static Entities are managed by the OutSystems Platform and can be consumed by other applications when exposed. This info should not be changed directly in the database.
    * Since the Static Entity Records can have different Data IDs for each Environment (meaning different IDs on the Physical Table), this information should match between environments and taken into consideration when migrating applicational info using static entities foreign keys.
    * The Entity Record ``SS_Key`` is not unique. To be unique, it has to be combined with the related Espace ``SS_Key`` and that is the way to match and map the same Entity Record between two different environments
    * Check the flag ``Is_Active`` to include or exclude inactive - soft-deleted info
    * Deleting records from the Static Entity sets the ``Is_Active`` flag, and will not delete the info from the Entity Record~


## How the OutSystems Platform Manages Static Entities - Example

This section shows an example of how the OutSystems Platform Manages Static Entities.

### Create Static Entity

Create an Espace named ``CityManager`` and a Static Entity Named ``CitySize`` with two Integer Attribute: ``MinSize`` and ``MaxSize``. Add four Records ``Small``, ``Medium``, ``Big``, and ``Huge`` like in the following table:

|**Record Name**   |**Min Size**            |**Max Size**                  |
|------------------|------------------------|------------------------------|
|Small             |0                       |5000                          |
|Medium            |5001                    |100000                        |
|Big               |100001                  |1000000                       |
|Huge              |1000001                 |99999999                      |

After publishing the Espace you can search for the created Entity info:

```
SELECT 
	OSSYS_ENTITY.NAME,
	OSSYS_ENTITY.DATA_KIND,
	OSSYS_ENTITY.PHYSICAL_TABLE_NAME
FROM OSSYS_ENTITY
WHERE OSSYS_ENTITY.NAME = 'CitySize' 
	AND OSSYS_ENTITY.ESPACE_ID = (
		SELECT ID FROM OSSYS_ESPACE WHERE NAME = 'CityManager'
	)
```

|Id|Data_Id|Name|SS_Key|Entity_SS_Key|Espace_Id|Is_Active|
|--- |--- |--- |--- |--- |--- |--- |
|8567|1|Huge|6fac2fbc-ea92-46e3-9402-6332b7bf3f13|b2257cc9-9454-40cd-845f-dc065e5e5551|679|1|
|8568|2|Medium|a7123828-b174-4959-a1d3-04ea47d5d081|b2257cc9-9454-40cd-845f-dc065e5e5551|679|1|
|8569|3|Small|b4e90a62-b31c-46ea-bd22-74103b86e600|b2257cc9-9454-40cd-845f-dc065e5e5551|679|1|
|8570|4|Big|d4364e1a-51a3-43cd-9f5e-1706831b5796|b2257cc9-9454-40cd-845f-dc065e5e5551|679|1|

And in the physical table we get the physical attributes info:

```
SELECT
	Id,
	Name,
	Order,
	Is_Active,
	MinSize,
	MaxSize
FROM OSUSR_5Z9_CITYSIZE 
ORDER BY [ORDER]
```

|Id|Name|Order|Is_Active|MinSize|MaxSize|
|--- |--- |--- |--- |--- |--- |
|3|Small|1|1|0|5000|
|2|Medium|2|1|5001|100000|
|4|Big|3|1|100001|1000000|
|1|Huge|4|1|1000000|99999999|

### Remove Static Entity Records

Remove the Small record from the CitySize Entity.

This is only possible to do if the Record to delete is not yet being used as a foreign key in another entity. If it is, all the dependencies have to be deleted before doing this operation or it will only be possible to set the record has inactive.

If it is possible to delete the record, the Entity_Record changes the attribute ``Is_Active`` to ``False`` (``0``) since it is no longer active.

|Id|Data_Id|Name|SS_Key|Entity_SS_Key|Espace_Id|Is_Active|
|--- |--- |--- |--- |--- |--- |--- |
|8569|3|Small|b4e90a62-b31c-46ea-bd22-74103b86e600|b2257cc9-9454-40cd-845f-dc065e5e5551|679|0|

And then, in the physical table, the corresponding row is deleted.

|Id|Name|Order|Is_Active|MinSize|MaxSize|
|--- |--- |--- |--- |--- |--- |
|2|Medium|2|1|5001|100000|
|4|Big|3|1|100001|1000000|
|1|Huge|4|1|1000000|99999999|

### Create Static Entity Record with the Same Name as Previous Deleted Record

Create a record named ``Small``, which is the same name as the record that was deleted before. Its size parameters are from 101 to 5000. 
After publishing the Espace, the information on the Entity Record is:

|Id|Data_Id|Name|SS_Key|Entity_SS_Key|Espace_Id|Is_Active|
|--- |--- |--- |--- |--- |--- |--- |
|8569|3|Small|b4e90a62-b31c-46ea-bd22-74103b86e600|b2257cc9-9454-40cd-845f-dc065e5e5551|679|0|
|8567|1|Huge|6fac2fbc-ea92-46e3-9402-6332b7bf3f13|b2257cc9-9454-40cd-845f-dc065e5e5551|679|1|
|8568|2|Medium|a7123828-b174-4959-a1d3-04ea47d5d081|b2257cc9-9454-40cd-845f-dc065e5e5551|679|1|
|8570|4|Big|d4364e1a-51a3-43cd-9f5e-1706831b5796|b2257cc9-9454-40cd-845f-dc065e5e5551|679|1|
|8588|5|Tiny|260e479c-5c4c-4fe7-986a-bdf116b8e4f4|b2257cc9-9454-40cd-845f-dc065e5e5551|679|1|
|8589|6|Small|611d1096-61be-4fbb-9303-66a0c56eacf7|b2257cc9-9454-40cd-845f-dc065e5e5551|679|1|

A new record has been created, and the previously deleted record has not been activated. 
The static entity physical table has a new record related with the new entity record:

|Id|Name|Order|Is_Active|MinSize|MaxSize|
|--- |--- |--- |--- |--- |--- |
|2|Medium|2|1|5001|100000|
|4|Big|3|1|100001|1000000|
|1|Huge|4|1|1000000|99999999|
|5|Tiny|5|1|0|100|
|6|Small|6|1|101|5000|

## Static Entity Records

This section shows an example of how the OutSystems Platform Manages Static Entity Records

### Entity Record

|**Name**          |**Physical Table Name** |**Description**               |
|------------------|------------------------|------------------------------|
|Entity_Record     |OSSYS_ENTITY_RECORD     |Records for each static entity defined in Service Studio. Older records are kept as inactive |

|**Producers**    |
|-----------------|
|OSSYS_ESPACE     |
   
|**Consumers**    |
|-----------------|
|-                |

[Proceed to the next section](07-business-process-technology-bpt.md)
