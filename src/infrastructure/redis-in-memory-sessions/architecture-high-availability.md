---
summary: Explore the 3-node Master/Replica Redis Cluster high availability architecture in OutSystems 11 (O11) for self-managed infrastructures.
guid: 8325ebdd-9bc8-445f-bd9b-5d41a435a841
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/o7Rkyuxm89D6KrjD7AOYCU/Infrastructure?node-id=1242:242
tags: high availability, redis, cluster configuration, infrastructure, master-replica architecture
audience:
  - platform administrators
  - backend developers
  - infrastructure managers
  - architects
  - full stack developers
outsystems-tools:
  - none
content-type:
  - procedure
---

# Redis Cluster high availability architecture

<div class="info" markdown="1">

Applies to OutSystems self-managed infrastructures.
</div>

The following diagram depicts the architecture of a 3-node Master/Replica Redis Cluster infrastructure:

![Diagram showing the 3-node Master/Replica Redis Cluster architecture with ports 7000 and 7001 for Master and Replica processes respectively.](images/redis-arch-3-node-diag.png "Redis Cluster 3-Node Architecture Diagram")

In this infrastructure there are 3 cluster nodes, running on 3 server machines. Each server machine has two `redis-server` processes running, a Master process and a Replica process. Since there are two `redis-server` processes running, they must listen in different ports. In this article, we'll use port 7000 for the Master `redis-server` process, and port 7001 for the Replica `redis-server` process.

Additionally, cluster nodes communicate with each other using ports 17000 and 17001. To obtain these port numbers, add 10000 to each data port, as detailed in the [Redis documentation](https://redis.io/topics/cluster-tutorial).

Note that, in this architecture, the Replica processes monitoring the Master are crossed, meaning that they don't run on the same server machine. With this setup, if a server machine fails completely, a Replica process running on a different machine takes over the Master process of the failed server. Redis handles this cross-node assigment automatically when creating the Redis Cluster.

For example, if Server 3 fails and becomes unavailable, the Replica process running on Server 1 takes over, becoming the new Master (blue) listening on port 7001.

![Diagram illustrating the failover process in a Redis Cluster where the Replica on Server 1 becomes the new Master for Server 3.](images/redis-arch-3-node-failover-diag.png "Redis Cluster Failover Scenario Diagram")
