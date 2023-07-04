---
summary: Set up a Redis Cluster for Production environments
guid: b010b104-71ae-48cf-9fe9-ac6c39cd9614
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Set up a Redis Cluster for Production environments

<div class="info" markdown="1">

Applies to OutSystems self-managed infrastructures.

</div>

<div class="info" markdown="1">

Before you start, make sure you meet the [system requirements](requirements.md) for using Redis with OutSystems.

</div>

<div class="info" markdown="1">

The following instructions show how to set up a dedicated Redis Cluster with three servers, each of them running Ubuntu 20.04.1 LTS. 
You may need to adapt these instruction for different operating systems.

</div>

## Install and configure three Redis server machines for the cluster

Follow these steps **for each server node** in the Redis Cluster:

1. Connect to the server using SSH with an account with super-user privileges.

1. Run the following commands:

        sudo apt-get update
        sudo apt-get install redis-server
        sudo systemctl disable redis-server.service
        sudo ufw allow 7000
        sudo ufw allow 7001
        sudo ufw allow 17000
        sudo ufw allow 17001

1. Create and edit the `/etc/rc.local` file by running the following command:

        sudo nano /etc/rc.local

1. Add the following content to the file:

        #!/bin/sh -e
        #
        # rc.local
        #
        # This script is executed at the end of each multiuser runlevel.
        # Make sure that the script will "exit 0" on success or any other
        # value on error.
        #
        # In order to enable or disable this script just change the execution
        # bits.
        #
        # By default this script does nothing.
        echo never > /sys/kernel/mm/transparent_hugepage/enabled
        sysctl -w net.core.somaxconn=65535

        exit 0

1. Save the file and exit (if you're using `nano`, press **Ctrl+X** followed by **Y**).

1. Give executable permissions to the `/etc/rc.local` file by running the following command:

        sudo chmod +x /etc/rc.local

1. Edit the `/etc/sysctl.conf` by running the following command:

        sudo nano /etc/sysctl.conf

1. Add the following line at the end of the file:

        vm.overcommit_memory=1

1. Create some required folders by running the following commands (remember to use `sudo`):

        sudo mkdir /etc/redis/cluster
        sudo mkdir /etc/redis/cluster/7000
        sudo mkdir /var/lib/redis/7000
        sudo mkdir /etc/redis/cluster/7001
        sudo mkdir /var/lib/redis/7001

1. Create and edit the file `/etc/redis/cluster/7000/redis_7000.conf` by running the following command:

        sudo nano /etc/redis/cluster/7000/redis_7000.conf

1. Add the following content to the `redis_7000.conf` file, replacing `[ACCESSKEY]` with a long password (longer than 16 characters):

        port 7000
        dir /var/lib/redis/7000/
        appendonly no
        protected-mode no
        cluster-enabled yes
        cluster-node-timeout 5000
        cluster-config-file /etc/redis/cluster/7000/nodes_7000.conf
        pidfile /var/run/redis/redis_7000.pid
        logfile /var/log/redis/redis_7000.log
        loglevel notice
        requirepass [ACCESSKEY]
        masterauth [ACCESSKEY]

1. Create and edit the file `/etc/redis/cluster/7001/redis_7001.conf` by running the following command:

        sudo nano /etc/redis/cluster/7001/redis_7001.conf

1. Add the following content to the `redis_7001.conf` file, replacing `[ACCESSKEY]` with the same password you used before:

        port 7001
        dir /var/lib/redis/7001
        appendonly no
        protected-mode no
        cluster-enabled yes
        cluster-node-timeout 5000
        cluster-config-file /etc/redis/cluster/7001/nodes_7001.conf
        pidfile /var/run/redis/redis_7001.pid
        logfile /var/log/redis/redis_7001.log
        loglevel notice
        masterauth [ACCESSKEY]
        requirepass [ACCESSKEY]

1. Create a `redis` user and a `redis` group for the Redis Server services and give them the correct permissions by running the following commands:

        sudo chown redis:redis -R /var/lib/redis
        sudo chmod 770 -R /var/lib/redis
        sudo chown redis:redis -R /etc/redis

1. Create and edit the file `/etc/systemd/system/redis_7000.service` by running the following command:

        sudo nano /etc/systemd/system/redis_7000.service

    This is the configuration of the daemon service for the Master `redis-server` process used when the system restarts.

1. Add the following content to the `redis_7000.service` file:

        [Unit]
        Description=Redis key-value database on 7000
        After=network.target
        [Service]
        ExecStart=/usr/bin/redis-server /etc/redis/cluster/7000/redis_7000.conf --supervised systemd
        ExecStop=/bin/redis-cli -h 127.0.0.1 -p 7000 shutdown
        Type=notify
        User=redis
        Group=redis
        RuntimeDirectory=redis
        RuntimeDirectoryMode=0755
        LimitNOFILE=65535
        [Install]
        WantedBy=multi-user.target

1. Create and edit the file `/etc/systemd/system/redis_7001.service` by running the following command:

        sudo nano /etc/systemd/system/redis_7001.service

1. Add the following content to the `redis_7001.service` file.

        [Unit]
        Description=Redis key-value database on 7001
        After=network.target
        [Service]
        ExecStart=/usr/bin/redis-server /etc/redis/cluster/7001/redis_7001.conf --supervised systemd
        ExecStop=/bin/redis-cli -h 127.0.0.1 -p 7001 shutdown
        Type=notify
        User=redis
        Group=redis
        RuntimeDirectory=/etc/redis/cluster/7001
        RuntimeDirectoryMode=0755
        LimitNOFILE=65535
        [Install]
        WantedBy=multi-user.target

    This is the configuration of the daemon service for the Replica `redis-server` process used when the system restarts.

1. Tell `systemd` to start the two services `redis_7000.service` and `redis_7000.service` automatically at boot by running the following commands:

        sudo systemctl enable /etc/systemd/system/redis_7000.service
        sudo systemctl enable /etc/systemd/system/redis_7001.service

1. Reboot the server by running the following command:

        sudo reboot

1. Repeat the previous steps for all servers in the cluster.

<div class="info" markdown="1">

Note that, with this configuration, the log files configured in the `redis_7000.conf` and `redis_7001.conf` files **will grow indefinitely**.

OutSystems recommends that you implement some sort of house-keeping policy, either through the use of `logrotate` daemon, or through any other mechanism available in Linux.

</div>

## Validate the installation of the Redis servers

After rebooting all servers, check if everything is running and configured correctly. You shouldn't have any warnings in the logs files.

Perform these steps **on each server**:

1. Open an SSH connection to the server.

1. Check the content of the log file (last 100 lines) for the `redis-server` service running on port 7000 by running the following command:

        sudo tail -n 100 /var/log/redis/redis_7000.log

    The information messages in the logs should be similar to the following, with no warnings or errors:

        2917:C 25 Sep 2019 08:14:15.752 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
        2917:C 25 Sep 2019 08:14:15.752 # Redis version=5.0.7, bits=64, commit=00000000, modified=0, pid=2917, just started
        2917:C 25 Sep 2019 08:14:15.752 # Configuration loaded
        2917:C 25 Sep 2019 08:14:15.752 * supervised by systemd, will signal readiness
        systemd[1]: Started Redis persistent key-value database.
        2917:M 25 Sep 2019 08:14:15.754 * No cluster configuration found, I'm ff3e4300bec02ed4bd1be9af5d83a5b44249c2b2
        2917:M 25 Sep 2019 08:14:15.756 * Running mode=cluster, port=7000.
        2917:M 25 Sep 2019 08:14:15.756 # Server initialized
        2917:M 25 Sep 2019 08:14:15.756 * Ready to accept connections

1. Check the content of the log file (last 100 lines) for the `redis-server` service running on port 7001 by running the following command:

        sudo tail -n 100 /var/log/redis/redis_7001.log

    The information messages in the logs should be similar to the following, with no warnings or errors:

        2917:C 25 Sep 2019 08:14:15.752 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
        2917:C 25 Sep 2019 08:14:15.752 # Redis version=5.0.7, bits=64, commit=00000000, modified=0, pid=2917, just started
        2917:C 25 Sep 2019 08:14:15.752 # Configuration loaded
        2917:C 25 Sep 2019 08:14:15.752 * supervised by systemd, will signal readiness
        systemd[1]: Started Redis persistent key-value database.
        2917:M 25 Sep 2019 08:14:15.754 * No cluster configuration found, I'm ff3e4300bec02ed4bd1be9af5d83a5b44249c2b2
        2917:M 25 Sep 2019 08:14:15.756 * Running mode=cluster, port=7001.
        2917:M 25 Sep 2019 08:14:15.756 # Server initialized
        2917:M 25 Sep 2019 08:14:15.756 * Ready to accept connections

1. Check the status of the `redis-server` service running on port 7000 by running the following command:

        sudo systemctl status redis_7000.service

    If everything is configured correctly, the output should be similar to the following:

        redis_7000.service - Redis persistent key-value database
            Loaded: loaded (/etc/systemd/system/redis_7000.service; enabled; vendor preset: enabled)
            Active: active (running) since Wed 2020-09-16 17:13:15 UTC; 22min ago
        Main PID: 472 (redis-server)
            Tasks: 4 (limit: 4710)
            Memory: 544.3M
            CGroup: /system.slice/redis_7000.service
                    └─472 /usr/bin/redis-server *:7000 [cluster]

1. Repeat the previous command for the `redis-server` service running on port 7001:

        sudo systemctl status redis_7001.service

    If everything is configured correctly, the output should be similar to the following:

        redis_7001.service - Redis persistent key-value database
            Loaded: loaded (/etc/systemd/system/redis_7001.service; enabled; vendor preset: enabled)
            Active: active (running) since Wed 2020-09-16 17:13:15 UTC; 21min ago
        Main PID: 474 (redis-server)
            Tasks: 4 (limit: 4710)
            Memory: 5.3M
            CGroup: /system.slice/redis_7001.service
                    └─474 /usr/bin/redis-server *:7001 [cluster]

After checking that all servers are well configured, you can proceed with the cluster configuration.

## Configure the Redis Cluster

In the following instructions, consider that the IP addresses of the three Redis servers are the following:

* Server 1: 172.31.6.35
* Server 2: 172.31.11.176
* Server 3: 172.31.3.184

We'll use the `redis-cli` command, a command-line utility installed along with Redis that allows you to send commands to Redis.

Do the following:

1. Open an SSH connection to one of the Redis server machines.

1. Create a cluster from several Redis Server processes by running the following command:

        redis-cli --cluster create 172.31.6.35:7000 172.31.11.176:7000 172.31.3.184:7000 172.31.6.35:7001 172.31.11.176:7001 172.31.3.184:7001 --cluster-replicas 1 -a [ACCESSKEY]

    The first 3 addresses are the Master nodes and the next 3 addresses are the Replica nodes. The `--cluster-replicas 1` argument indicates that each Master will have 1 Replica. It will be a cross-node replication as depicted before.

    The output should be similar to the following:

        >>> Performing hash slots allocation on 6 nodes...
        Master[0] -> Slots 0 - 5460
        Master[1] -> Slots 5461 - 10922
        Master[2] -> Slots 10923 - 16383
        Adding replica 172.31.11.176:7001 to 172.31.3.184:7000
        Adding replica 172.31.3.184:7001 to 172.31.11.176:7000
        Adding replica 172.31.3.184:7001 to 172.31.3.184:7000
        M: ff3e4300bec02ed4bd1be9af5d83a5b44249c2b2 172.31.3.184:7000
        slots:[0-5460] (5461 slots) master
        M: 314038a48bda3224bad21c3357dbff8305735d72 172.31.11.176:7000
        slots:[5461-10922] (5462 slots) master
        M: 19a2c81b7f489bec35eed474ae8e1ad787327db6 172.31.3.184:7000
        slots:[10923-16383] (5461 slots) master
        S: 896b2a7195455787b5d8a50966f1034c269c0259 172.31.3.184:7001
        replicates 19a2c81b7f489bec35eed474ae8e1ad787327db6
        S: 89206df4f41465bce81f44e25e5fdfa8566424b8 172.31.11.176:7001
        replicates ff3e4300bec02ed4bd1be9af5d83a5b44249c2b2
        S: 20ab4b30f3d6d25045909c6c33ab70feb635061c 172.31.3.184:7001
        replicates 314038a48bda3224bad21c3357dbff8305735d72
        Can I set the above configuration? (type 'yes' to accept):

1. Type `yes` and press **Enter** to accept the proposed configuration.

    You get the configuration details in the output:

        Can I set the above configuration? (type 'yes' to accept): yes
        >>> Nodes configuration updated
        >>> Assign a different config epoch to each node
        >>> Sending CLUSTER MEET messages to join the cluster
        Waiting for the cluster to join
        ..
        >>> Performing Cluster Check (using node 172.31.6.35:7000)
        M: ff3e4300bec02ed4bd1be9af5d83a5b44249c2b2 172.31.6.35:7000
        slots:[0-5460] (5461 slots) master
        1 additional replica(s)
        S: 20ab4b30f3d6d25045909c6c33ab70feb635061c 172.31.3.184:7001
        slots: (0 slots) slave
        replicates 314038a48bda3224bad21c3357dbff8305735d72
        M: 314038a48bda3224bad21c3357dbff8305735d72 172.31.11.176:7000
        slots:[5461-10922] (5462 slots) master
        1 additional replica(s)
        M: 19a2c81b7f489bec35eed474ae8e1ad787327db6 172.31.3.184:7000
        slots:[10923-16383] (5461 slots) master
        1 additional replica(s)
        S: 89206df4f41465bce81f44e25e5fdfa8566424b8 172.31.11.176:7001
        slots: (0 slots) slave
        replicates ff3e4300bec02ed4bd1be9af5d83a5b44249c2b2
        S: 896b2a7195455787b5d8a50966f1034c269c0259 172.31.6.35:7001
        slots: (0 slots) slave
        replicates 19a2c81b7f489bec35eed474ae8e1ad787327db6
        [OK] All nodes agree about slots configuration.
        >>> Check for open slots...
        >>> Check slots coverage...
        [OK] All 16384 slots covered.

After creating the cluster there are 16384 hash slots, divided by the 3 servers:

* Server 1 contains hash slots from 0 to 5500
* Server 2 contains hash slots from 5501 to 11000
* Server 3 contains hash slots from 11001 to 16383

Your Redis Cluster is now created and ready to accept connections.

## Checking the status of the Redis Cluster

Start by inspecting the information about the nodes that belong to the Redis Cluster, and then perform some basic set/get operations to see if everything is working properly.

Do the following:

1. Open an SSH connection to one of the Redis Cluster nodes (Server 1, Server 2, or Server 3).

1. run the following command in the terminal:

        redis-cli -c -h 172.31.6.35 -p 7000 -a [ACCESSKEY]

    `[ACCESSKEY]` is the password you previously configured in the Redis configuration file. The `-c` option activates basic cluster support in `redis-cli`.

1. On the `redis-cli` prompt, run the `CLUSTER NODES` command:

        172.19.33.7:7000> CLUSTER NODES
        20ab4b30f3d6d25045909c6c33ab70feb635061c 172.31.3.184:7001@17001 slave 314038a48bda3224bad21c3357dbff8305735d72 0 1569402961000 6 connected
        314038a48bda3224bad21c3357dbff8305735d72 172.31.11.176:7000@17000 master - 0 1569402961543 2 connected 5461-10922
        19a2c81b7f489bec35eed474ae8e1ad787327db6 172.31.3.184:7000@17000 master - 0 1569402960538 3 connected 10923-16383
        ff3e4300bec02ed4bd1be9af5d83a5b44249c2b2 172.31.6.35:7000@17000 myself,master - 0 1569402959000 1 connected 0-5460
        89206df4f41465bce81f44e25e5fdfa8566424b8 172.31.11.176:7001@17001 slave ff3e4300bec02ed4bd1be9af5d83a5b44249c2b2 0 1569402960000 5 connected
        896b2a7195455787b5d8a50966f1034c269c0259 172.31.6.35:7001@17001 slave 19a2c81b7f489bec35eed474ae8e1ad787327db6 0 1569402959936 4 connected

From the command output you can observe the following (analyzing the output line by line):

* The Replica process with node ID 20ab4b30f3d6d25045909c6c33ab70feb635061c on Server 3 (172.31.3.184) is monitoring or connected to the Master process with node ID 314038a48bda3224bad21c3357dbff8305735d72 on Server 2 (172.31.11.176).

* There are three Master processes on the cluster, running on Server 2 (172.31.11.176), Server 3 (172.31.3.184), and on Server 1 (172.31.6.35).

* The Replica process with node ID 89206df4f41465bce81f44e25e5fdfa8566424b8 on Server 2 (172.31.11.176) is monitoring or connected to the Master process with node ID ff3e4300bec02ed4bd1be9af5d83a5b44249c2b2 on Server 1 (172.31.6.35).

* The Replica process with node ID 896b2a7195455787b5d8a50966f1034c269c0259 on Server 1 (172.31.6.35) is monitoring or connected to the Master process with node ID 19a2c81b7f489bec35eed474ae8e1ad787327db6 on Server 3 (172.31.3.184).

Since everything looks OK, perform a few `SET` and `GET` operations to test if the Redis Cluster behaves as expected.

Do the following:

1. Connect to the Redis Master process (7000) on Server 1 (172.31.6.35) by running the following command:

        redis-cli -c -h 172.31.6.35 -p 7000 -a [ACCESSKEY]

    Replace `[ACCESSKEY]` with the password you configured previously.

1. Run a few `SET` and `GET` commands to check the behavior of Redis:

        172.31.6.35:7000> set a 1
        -> Redirected to slot [15495] located at 172.31.3.184:7000
        OK
        172.31.3.184:7000> set b 2
        -> Redirected to slot [3300] located at 172.31.6.35:7000
        OK
        172.31.6.35:7000> set c 3
        -> Redirected to slot [7365] located at 172.31.11.176:7000
        OK
        172.31.11.176:7000> set d 4
        -> Redirected to slot [11298] located at 172.31.3.184:7000
        OK
        172.31.3.184:7000> get b
        -> Redirected to slot [3300] located at 172.31.6.35:7000
        "2"
        172.31.6.35:7000> get a
        -> Redirected to slot [15495] located at 172.31.3.184:7000
        "1"
        172.31.3.184:7000> get c
        -> Redirected to slot [7365] located at 172.31.11.176:7000
        "3"
        172.31.11.176:7000> get d
        -> Redirected to slot [11298] located at 172.31.3.184:7000
        "4"
        172.31.3.184:7000>

From the output, you can see that Redis sends the keys to the correct hash slots in each server, even though you're connected to a specific Master process (on Server 1).

## Next steps

* After setting up a Redis Cluster, you should [test its failover behavior](cluster-failover-test.md).

* To scale the Redis Cluster you just created, check [Scaling a Redis Cluster by adding more nodes](cluster-add-nodes.md).
