---
tags: version-10; bpt; 
summary: 
---

# How to archive old Business Process Technology (BPT) Processes

How can I archive old closed BPT Processes?

For example: Queries on BPT processes have become slower, because so many Processes have accumulated over time. I would like to archive these old Processes before deleting them.

## Answer

Business Process Technology relies on a set of meta-model Entities to record data required by your business Processes. When using BPT intensively, these Entities can have a high growth rate and affect the performance of BPT queries.

To archive old Processes follow these steps:

1. Create a separate set of Entities that mirror the BPT meta-model. Use this mirror set of Entities to store old Processes before deleting them. 

    ![BPTModel.png](images/BPTModel.png)

    <div class="info" markdown="1">
    If you have any Entities that reference parts of the BPT meta-model you also need to archive them or to keep track of the changes in the Entities and Foreign Keys of the archived Processes.  
    If the Foreign Keys that reference the BPT meta-model have the `Delete Rule` Property set to `Protect` you need to archive/delete them before archiving the BPT Process.
    </div>

1. To delete top level BPT Processes use the actions **Process\_Delete** or **Process\_BulkDelete** from the **BPT_API** extension.

    * **Process\_Delete** deletes processes individually.
    * **Process\_BulkDelete** deletes processes in bulk (with or without limitation on the number of Processes to be deleted) filtered by Date and/or by Process Definition. 

To better understand how to archive old Processes and any other data that may depend on those Processes check out the [BPT Sample Archiver](http://www.outsystems.com/forge/component/443/bpt-sample-archiver/) Forge Component.
