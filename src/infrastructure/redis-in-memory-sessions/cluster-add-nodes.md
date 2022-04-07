# Scale a Redis Cluster by adding more nodes { #add-node }

<div class="info" markdown="1">

Note: This article builds upon the example scenario of a dedicated Redis Cluster with three servers, initially presented in [Set up a Redis Cluster for Production environments](setup-prod.md).

</div>

You can scale an existing Redis Cluster installation by adding more Redis nodes to the cluster.

Assuming that you already have a minimal infrastructure as described in [Set up a Redis Cluster for Production environments](setup-prod.md), you must **add server machines in pairs** to maintain the recommended odd number of servers. The new server machines should have same characteristics as the other Redis server machines in the cluster.

In this example, you're scaling the minimal infrastructure with an additional pair of server machines, **Server 4** and **Server 5**. Each Replica process running on these new server machines points to the Master process of the other added server, to maintain the cross-replication architecture:

* The Replica process running on Server 4 points to the Master process running on Server 5.
* The Replica process running on Server 5 points to the Master process running on Server 4.

You should configure the Master processes first, and then set up the Replica processes.

After taking the steps described in this section, the architecture of your Redis Cluster will be the following:

![Redis Cluster architecture after adding two new server machines](images/redis-arch-5-node-diag.png)

## Step 1. Set up new Redis processes on the new server machines

Follow the process described in [Set up a Redis Cluster for Production environments](setup-prod.md), and complete the setup of the **Master** and **Replica** processes in the new Redis nodes.

Remember that you should add server machines **in pairs** to the Redis Cluster, which means that in this example you should add **Server 4** and **Server 5**, each having a Master and a Replica process.

## Step 2. Add the new Master processes to the Redis Cluster

1. Open an SSH connection to one of the new server machines (Server 4 or Server 5).

1. Run the following command to add the Master process of the current new server to the cluster:

        ubuntu@ip-172.31.6.91:~$ redis-cli --cluster add-node 127.0.0.1:7000 172.31.6.35:7000

1. Repeat the same command on the other new server machine to add it to the Redis Cluster.

## Step 3. Reshard the cluster

You must perform a reshard of the cluster to redistribute the key slots evenly among all the Master processes of the Redis Cluster, including the new Master processes running on Server 4 and Server 5.

1. Open an SSH connection to any of the Redis Cluster machines.

1. Run the following command:

        ubuntu@ip-172.31.6.91:~$ redis-cli --cluster reshard 127.0.0.1:7000

## Step 4. Add the Replica processes to the Redis Cluster

1. Add the Replica process of the first new server (Server 4, running on port 7001) to the Redis Cluster. Run the following command:

        ubuntu@ip-172.31.6.91:~$ redis-cli --cluster add-node 127.0.0.1:7001 172.31.6.35:7000 --cluster-slave --cluster-master-id [MASTER_NODE_ID]

    Replace `[MASTER_NODE_ID]` with the node ID of the Master Process you want to replicate (in this case, the Master process on Server 5). A node ID is a 40-character string (for example, `ff3e4300bec02ed4bd1be9af5d83a5b44249c2b2` for the Master process running on Server 1).

1. Repeat the last command to setup the Replica process running on Server 5. In this case, set `[MASTER_NODE_ID]` to the node ID of the Master process running on Server 4.

Repeat this process as necessary to scale the Redis Cluster infrastructure, adding servers and setting them up in pairs.
