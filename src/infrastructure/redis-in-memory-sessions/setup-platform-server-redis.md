---
summary: Learn how to configure OutSystems 11 (O11) Platform Server to use Redis for in-memory session storage in self-managed infrastructures.
guid: 5cef1f48-d700-4311-8f88-ed6ac0ded58e
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/o7Rkyuxm89D6KrjD7AOYCU/Infrastructure?node-id=1242:249
---

# Configure Platform Server to use Redis for sessions

<div class="info" markdown="1">

Applies to OutSystems self-managed infrastructures.

</div>

<div class="info" markdown="1">

You need **Platform Server version 11.23.0** to use Redis for in-memory session storage.

This article assumes that you have a Redis Cluster with three server machines, as described in [Set up a Redis Cluster for Production environments](setup-prod.md). However, the instructions are also applicable if you have a single server machine running Redis Server.

</div>

After making sure that you have a working Redis infrastructure, configure the OutSystems front-end servers of your OutSystems environment for in-memory session storage using Redis.

Do the following:
1. Run Configuration Tool as an Administrator, open the **Session** tab, and then select Redis from  the **Session Provider** dropdown.

    ![Screenshot of the Configuration Tool showing the Session tab with Redis selected as the Session Provider.](images/session-connection-string-0-ct.png "Configuration Tool Session Tab")

    In the **Hosts** element, enter the addresses and ports of all Redis Master processes in the Redis Cluster, separated by commas. If you have just one server running redis-server, enter its address and port.

    In the **Password** element, enter the password for the Redis Master or the single redis-server.

    Optionally, tick the **Use SSL** element to enable SSL configuration. If necessary, enter  the **SSL Host** element. For more information about SSL refer to [Enable SSL for Redis](setup-enable-ssl.md). 

1. To verify that the Redis server machines are reachable from the Platform Server machine and that everything works properly at runtime, Click **Test Connection**.

    ![Popup message in the Configuration Tool indicating a successful test connection to Redis.](images/session-connection-string-success-ct.png "Successful Redis Connection Test")

    If you get an error saying "It was not possible to connect to Redis server", review your firewall rules and network connections to make sure that ports 7000 and 7001 are reachable from the OutSystems front-end servers.

1. If the connection test is successful, click **Apply and Exit**.

1. If the Configuration Tool displays a popup asking you to publish the latest version of Service Center and System Components. click **OK** to accept.

    If you're configuring an existing installation, republish all modules so that they use Redis sessions.

Your front-end server is now configured to store sessions in Redis.

## Testing your configuration

When the Service Center installation finishes, test to verify the sessions are being saved in Redis by doing the following:

1. Log in to Service Center and perform some browsing in Service Center's UI.

1. To confirm that Platform Server is using Redis, open an SSH connection to one of the cluster server machines and connect to the Redis Cluster by running the following command:

        redis-cli -c -h 172.31.6.35 -p 7000 -a [ACCESSKEY]

    Alternatively, if you have a single machine running the Redis Server, open an SSH connection to your Redis server machine and run the following command:

        redis-cli -h 127.0.0.1 -p 7000 -a [ACCESSKEY]

    Replace `[ACCESSKEY]` with the Redis Server password.

1. Run the command `KEYS *` on the `redis-cli` prompt to check if your session was effectively created. You should have two keys: `{....}_Data` and `{....}_Internal`.

    Sample output:

        redis 172.31.6.35:7000> keys *
        1) "{478870b9-2d60-4f73-9eb3-7cd8b994a737_amhe3zeho1eqp5h0p0gt31ha}_Internal"
        2) "{478870b9-2d60-4f73-9eb3-7cd8b994a737_amhe3zeho1eqp5h0p0gt31ha}_Data"
