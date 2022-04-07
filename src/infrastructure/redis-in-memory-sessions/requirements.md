# System requirements for using Redis

Before you can use Redis with OutSystems, check if you fulfill both OutSystems and Redis system requirements.

## Software

### Platform Server

* Using Redis for in-memory session storage requires **Platform Server version 11.11**.

### Redis server machines

Each server machine used for Redis must fulfill the following requirements:

* Ubuntu 20.04.1 LTS (Server Edition)
* Redis Server version 5.0.7

## Hardware

The recommended Redis infrastructure (and its hardware requirements) varies according to the type of OutSystems environment you are using with Redis.

### Non-productive environments

The minimum requirements of a Redis infrastructure for **non-productive OutSystems environments** are the following:

* Single Redis server with 2 CPUs (>2.6 Ghz) and 4GB of RAM (can be Virtual Machine)
* Moderate bandwith network interface card (100 Mbps)
* 10GB disk (to store the operating system, logs, etc.)

### Production environment

For Production environments, you should use a high-availability configuration of Redis Server. OutSystems recommends that you use **Redis Cluster** instead of the Sentinel alternative, since it supports multiple [Active-Active nodes](https://redislabs.com/redis-enterprise/technology/active-active-geo-distribution/) and can scale horizontally. It allows you to future-proof your Redis installation, allowing you to adjust to increased demand.

The minimum requirements of a **highly-available Redis infrastructure (Production)** are the following:

* 3 dedicated or virtualized Redis servers with 3 or 4 vCPUs each (>2.6 Ghz) and 8GB<sup>1</sup> of RAM, configured as a Redis Cluster (with high availability)
* High-bandwith network interface card (1Gbps recommended<sup>2</sup>)
* 10GB disk (to store the operating system, logs, etc.)

<sup>1</sup> You may need more RAM if your configured session expiration time allows for long sessions. Since there are 2 Redis processes per server (Master and Replica), with 8GB of RAM there's only 4GB available for session storage.

<sup>2</sup> Assumes a 20kb session and 10 000 reqs/s, which gives a bandwith of around 390MB/s (20&#215;10000&#215;2(read and write)/1024).

Check the recommended Redis infrastructure for Production environments in [Redis Cluster high availability architecture](architecture-high-availability.md). When using this architecture, ports 7000 and 7001 of the Redis servers must be reachable from the OutSystems front-end servers. For security reasons, the Redis Cluster should be on its own subnet, avoiding public exposure.

You can scale this minimal Redis infrastructure for Production by adding more servers. Repeat the Redis server installation and configuration process, and then follow the instructions on [Scaling a Redis Cluster by adding more nodes](cluster-add-nodes.md).

## Next steps

* For non-productive OutSystems environments, check how to [set up a Redis server for non-productive environments](setup-non-prod.md).

* For Production environments, check the [recommended Redis architecture for Production use](architecture-high-availability.md), and then how to [set up a Redis Cluster for Production environments](setup-prod.md).
