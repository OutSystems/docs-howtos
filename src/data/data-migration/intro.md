---
summary: A guide to migrate from Production to Non-Production environments in OutSystems - Introduction
tags: data-migration-between-outsystems-installation; data-migration-between-production-and-non-production-outsystems;
locale: en-us
guid: 02fd2efb-6799-4656-8cdb-8043dbeff6bf
---

# Data migration from production to non-production environment

When there is the need to migrate data between different OutSystems installations, there are many factors to consider and steps to follow, for several different uses cases.
The ultimate goal of this document is to guide through the process of data migration, providing the guidelines and best practices per use case.


<div class="info" markdown="1">
Note: The current instructions apply to self-managed and OutSystems Cloud installations, and base on the following versions:

* OutSystems Platform Server version: 11.0.128.0
* Database engine: Microsoft SQL Server 2016 (SP2) (KB4052908) - 13.0.5026.0 (X64)
</div>

<div class="info" markdown="1">
Disclaimer: The database engine used to build this documentation was MSSQL. Although most of the considerations fit for different database engine types, some of them might not be completely applicable for Oracle or other database engines.
</div>

The following guidelines are related to the process of migrating data from Production to Non-Production environments, for single, multiple, or all the applications of an environment.

**The production environment** is defined as an environment, whose main purpose is to make applications available to your end-users. In 
Production environments, reliability is a top priority so the 1-Click Publish process optimizations are disabled; as a consequence, publishing an application in a Production environment can take longer than publishing the same application in a Development environment.

**The non-production environment** is defined as an environment whose main purpose is to provide a real scenario (similar to Production) where developers can test your applications and mitigate the risk of deploying them to Production while keeping features that can assist developers with debugging. In Non-Production environments, the 1-Click Publish process optimizations are disabled (like Production environments) and it's still possible to test SQL Queries and preview data in Aggregates and SQL Queries (like Development environments).

For more details, refer to the [Configure your OutSystems environment](https://success.outsystems.com/Documentation/11/Setting_Up_OutSystems/Configure_your_OutSystems_environment) documentation.

[Proceed to the next section](sections/01-entity-types-classification.md)


