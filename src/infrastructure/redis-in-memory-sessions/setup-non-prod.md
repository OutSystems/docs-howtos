---
summary: Set up a dedicated Ubuntu 20.04.1 LTS virtual machine or Docker container with Redis Server, allowing inbound connections on port 6379/TCP, and configure OutSystems platform to use it for non-productive environments.
guid: 22ce1e5d-5169-4b6c-934a-92e6b6817783
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Set up a Redis server for non-productive environments

<div class="info" markdown="1">

Applies to OutSystems self-managed infrastructures.

</div>

<div class="info" markdown="1">

Before you start, make sure you meet the [system requirements](requirements.md) for using Redis with OutSystems.

</div>

You can use a single Redis server for all non-productive environments (for example, for Development, QA, and Test), since the expected load of concurrent users is much lower than in the Production environment.

For a single Redis server, you can use the default TCP port 6379.

OutSystems recommends that you deploy the single Redis server in a subnet different from all the OutSystems platform environment front-end servers. Assuming that each environment (DEV, QA, etc.) has its own subnet for the environment's front-end servers, make sure that the deployed Redis virtual machine is reachable from all these subnets.

Additionally, your configuration must allow **inbound connections** on port 6379/TCP for the Redis virtual machine.

The following diagram depicts this network deployment:

![Redis Server network diagram (1 node)](images/redis-arch-1-node-network-diag.png)

### Install and configure Redis Server

<div class="info" markdown="1">

The following instructions assume that you have a server running with Ubuntu 20.04.1 LTS where you wish to install Redis Server. 
You may need to adapt these instructions on a different operating system.

</div>

Do the following:

1. Connect to the Ubuntu server using SSH.

1. Run the following commands:

        sudo apt-get update
        sudo apt-get install redis-server
        sudo ufw allow 6379

1. Edit the `/etc/redis/redis.conf` file with your preferred editor (we'll use `nano`, which is already installed in Ubuntu), by running the following command:

        sudo nano /etc/redis/redis.conf

1. In the `redis.conf` file, perform the following changes:

    * Comment the line with the `bind` directive by adding a `#` character at the beginning of the line
    * Change `protected-mode` from `yes` to `no`
    * Uncomment the `requirepass` directive
    * In the `requirepass` line, define a strong password, replacing `[STRONG_PASSWORD]` with a password that's at least 16 characters long

    Here are the relevant file sections:

        # ~~~ WARNING ~~~ If the computer running Redis is directly exposed to the
        # internet, binding to all the interfaces is dangerous and will expose the
        # instance to everybody on the internet. So by default we uncomment the
        # following bind directive, that will force Redis to listen only into
        # the IPv4 loopback interface address (this means Redis will be able to
        # accept connections only from clients running into the same computer it
        # is running).
        #
        # IF YOU ARE SURE YOU WANT YOUR INSTANCE TO LISTEN TO ALL THE INTERFACES
        # JUST COMMENT THE FOLLOWING LINE.
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #bind 127.0.0.1
        
        (...)

        #
        # By default protected mode is enabled. You should disable it only if
        # you are sure you want clients from other hosts to connect to Redis
        # even if no authentication is configured, nor a specific set of interfaces
        # are explicitly listed using the "bind" directive.
        protected-mode no

        (...)

        # Require clients to issue AUTH <PASSWORD> before processing any other
        # commands.  This might be useful in environments in which you do not trust
        # others with access to the host running redis-server.
        #
        # This should stay commented out for backward compatibility and because most
        # people do not need auth (e.g. they run their own servers).
        #
        # Warning: since Redis is pretty fast an outside user can try up to
        # 150k passwords per second against a good box. This means that you should
        # use a very strong password otherwise it will be very easy to break.
        #
        requirepass [STRONG_PASSWORD]

1. Reboot the redis service to apply configurations

        systemctl restart redis

After performing these steps, your server is ready to accept connections from OutSystems front-end servers.

## Next steps

* Follow the instructions in [Configure Platform Server to use Redis for sessions](setup-platform-server-redis.md) to configure your non-productive OutSystems environment to use Redis for in-memory session storage.
