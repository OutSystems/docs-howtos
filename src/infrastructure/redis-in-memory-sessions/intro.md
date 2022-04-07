---
summary:
tags: article-page
---

# Configuring OutSystems with Redis in-memory session storage

## Session storage in Traditional Web Apps

In previous versions of Platform Server, Traditional Web Application Sessions could only be stored in Relational Databases, serialized as a binary/blob column. In this case, reading and writing session information means doing many serialization and deserialization operations, which require a significant amount of hardware resources like CPU and Disk I/O. When a Traditional Web App is under load, possibly handling thousands of requests per second, session storage can be a bottleneck and stress the relational database engine. Additionally, storing sessions in the database can also increase the licensing costs of the relational database engine.

In the past few years, the approach of storing application state in memory, without persisting this information, became generally accepted for keeping session information. **Redis** is an in-memory key-value database well suited for this use case, with wide support in the industry.

Redis presents several advantages when compared with relational databases, such as the following:

* Able to scale horizontally (for example, by adding more active nodes)
* Low memory and CPU footprint
* High availability and fault tolerant
* Increased performance
* Low maintainability
* No lock contention
* Capability of operating 100% in memory

OutSystems supports in-memory session storage using one of the following configurations:

* **Redis Server** — a single server machine used for Redis, running the `redis-server` service.

* **Redis Cluster** — several machines used for Redis, each running two `redis-server` services (a Master process and a Replica process), configured for high availability.

## Next steps

* Check the [system requirements](requirements.md) for using Redis with OutSystems, both for Production environments and for other types of OutSystems environments.

* If you're just starting, learn [how to install a Redis server for non-productive OutSystems environments](setup-non-prod.md).  
    After setting up a Redis server, [configure OutSystems to use Redis for in-memory session storage](setup-platform-server-redis.md).

* When you're ready, learn more about the recommended [Redis architecture with high availability](architecture-high-availability.md) for Production environments, and check [how to set up a Redis Cluster for Production environments](setup-prod.md) with three servers.  
    You also need to [configure OutSystems to use Redis for in-memory session storage](setup-platform-server-redis.md).

* Learn how to scale your Redis infrastructure for Production environments by [adding more Redis nodes to your Redis Cluster](cluster-add-nodes.md).
