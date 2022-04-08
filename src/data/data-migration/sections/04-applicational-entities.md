---
summary: A guide to migrate from Production to Non-Production environments in OutSystems - Applicational Entities
tags: data-migration-between-outsystems-installation; data-migration-between-production-and-non-production-outsystems; applicational-entities
---

# Applicational Entities

There are numerous possibilities to design the data model, depending on the business request requirements and features, for different applications, customers, and so on.
Usually, you need to address this in a case-to-case analysis approach or by doing an initial assessment to check if the migration is possible for a particular scenario.
This section provides a guideline for migrating application data with some awareness and technical considerations to keep in mind before starting the migration.

## OutSystems Platform Dependencies

Start by identifying the OutSystems Platform dependencies on your applicational entities. 
Applicational entities usually have foreign keys to the systems model. Be aware of the following list with some of the most used entities that might cause dependencies and have to be mapped and aligned between environments in order to migrate final applicational entities:

* Users (Find more about User data migration in the [Application Users, Groups and Roles](05-application-users-groups-roles.md) section).
    * Audits (for example, Foreign Keys for attributes CreatedBy or UpdatedBy)
    * Using Groups on the application
    * Other

* Tenants

* Multi-Tenant Entities

* BPTs - (Find more about BPT data migration in the [Business Process Technology (BPT)](07-business-process-technology-bpt.md) section).
    * BPT definitions IDs on Application Entities (Extended configurations etc.) 
    * Process Instances and Activity Instances foreign keys

* Other OS Platform Entities referred by Application Entities
    * Systems Entities exposed to be referenced can be foreign keys in a final application
    * Extending System Entities with more attributes (for example, ``UserExtended``, BPT ``ActivityDefenitionExtended``, and so on.)


## Applicational Dependencies

Search and identify other dependencies inside your application, such as:

* Primary Keys & Foreign Keys

* Other Constraints - Mandatory attributes

* External Integrated Systems IDs 
    * Attributes that are not Keys but can be used by your application over an integration to get or set data in an external system that might not be present or integrated by the migration destination environment.

* Extension Integrated Entities 
    * IDs in Applicational Entities (Delete Rule Ignored)

* Be careful with “Entities cyclic dependencies”, 
    *   Entities referencing themselves (for example, tree reference, like a parent node and child node, where all records have a foreign key to the top node even the top node itself)
    * Entities referencing each other, for example, Entity ``A`` with a foreign key of Entity ``B`` with a foreign key of Entity ``A``
    * Reference loop over multiple entities, for example, Entity ``A`` with a foreign key of Entity ``B``, with a foreign key of Entity ``C``, with a foreign key of Entity ``A``
    
* Be aware of the "Soft Keys" in use. This is not a database stopper but may affect the final application behavior for tests (for example, SS_Keys, GUIDs, Usernames and other business concepts that may relate different entities) 
    

## Other topics

There are several other topics you must consider when you plan data migration, such as:
 
* Personal and Sensitive Data - Make sure that any data migration process is GDPR compliant or any other rules that the business may have.

* Data Scrambling / Masking - Related to the previous point, to be GDPR compliant or to follow any rules required by the business, it might be required that the data migration process includes specific processes for data obfuscation to hide the original characters or data.

* Date Formats - Understand the necessary work to prepare the data migration in the appropriate format (note that the Production and Non-Production Environment can have different date formats).

* Date Timezones - Please note that in the OutSystems Cloud all servers are set to work in the UTC time zone. This configuration cannot be changed. Applications that need to deal with time zone differences from UTC need to consider that from the early phases of development.

* Database Catalog - A data catalog belongs to a database instance and is comprised of metadata containing database object definitions like base tables, synonyms, views or synonyms and indexes. The SQL standard lays down a regular method for accessing the data catalog known as the information schema, though not all databases use this.

* Migration of Binary Data - typically here we have images, audio, video or other multimedia objects which are called a Binary Large object (BLOB). Note that database support for blobs is not universal. 
Entity Attributes Delete Rule - if the migration solution will try to delete something

* Bootstraps - Be careful if we don’t want to bootstrap data from inside an Espace module just by publishing a solution or Espace.

[Proceed to the next section](05-application-users-groups-roles.md)
