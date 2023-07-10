---
summary: Configure Platform Server to use SSL when connecting to Redis 6.x by defining environment variables and enabling SSL in the Configuration Tool.
guid: f69f6130-df05-468b-aabf-5414ba06e384
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Enable SSL for Redis

<div class="info" markdown="1">

Applies to OutSystems self-managed infrastructures.

</div>

<div class="info" markdown="1">

SSL/TLS support is only available in Redis 6.x, and only if the Redis binaries were compiled with this feature enabled. 
Check OutSystems system [requirements](requirements.md) page for the supported versions.

</div>

## Prerequisites

* You have a supported Redis installation **with SSL/TLS enabled**. Check the [Redis documentation](https://redis.io/topics/encryption) for more information.

## Configure Platform Server to support SSL connections to Redis

To configure Platform Server to use SSL when connecting to Redis, you must:

1. Define required environment variables on every front-end server of your OutSystems environment.
1. Use the Configuration Tool to enable SSL support.
1. Apply the new settings to your apps.

Check the next sections for details.

### 1. Define required environment variables

Define the following environment variables on every front-end server of your OutSystems environment. You must define a value at least for the environment variables that are mandatory:

`SERedis_ClientCertPfxPath`
:   **Mandatory**. Defines the **local** Secure Sockets Layer (SSL) certificate used for authentication. Set this environment variable to the full path of a X.509 `.PFX` certificate file.

`SERedis_IssuerCertPath`
:   **Optional**. Defines the **remote** Secure Sockets Layer (SSL) certificate used for authentication. This parameter must only be used if the Issuer of the Redis server certificate **is not trusted** by the frontend. Set this environment variable to the full path of a `.CRT` certificate file.
  
`SERedis_ClientCertPassword`
:   **Optional**. Password of the certificate for the local certificate used for authentication. Set this environment variable to the certificate password.  
    If the certificate doesn't have a password, you don't need to define this environment variable.

`SERedis_ClientCertStorageFlags`
:   **Optional**. Integer value that represents the sum of the values that control where and how to import the local certificate used for authentication.  
    Examples:

    * If the flag is "UserKeySet", set the value to **1**
    * If the flags are "UserKeySet" and "UserProtected", set the value to **9**
    * If the flags include every possible combination, set the value to **63**

    For more information, check Microsoft's documentation on the [X509KeyStorageFlags Enum](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.x509certificates.x509keystorageflags).

    If there are no restrictions on how to import the local certificate, you don't need to define this environment variable.

### 2. Enable SSL in Configuration Tool

In each front-end server of your OutSystems environment do the following:

1. Open the Configuration Tool and select the **Session** tab.

1. Select the **Redis** Session Provider, if it's not selected.

1. Enable the **Use SSL** option.

1. _(Optional)_ Enter the **SSL Host**. If not specified, OutSystems determines the SSL host from the **Hosts** field value.

1. Click **Test Connection** to verify if the configuration is correct.

1. Click **Apply and Exit**.

### 3. Apply the new Redis settings to your OutSystems apps

If you were already using Redis with Platform Server, update the Redis connection string for each application by doing the following:

1. Open the Service Center management console of one of the front-end servers of your OutSystems environment.

1. Navigate to **Factory** > **Solutions**.

1. Select an existing solution (or create a new one, if it doesn't exist) containing all the modules in the factory.

1. In the solution details page, click **Apply Settings**.

If you weren't using Redis with Platform Server before configuring SSL, you must republish the factory. Check [Creating and using an "all components" solution](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Creating_and_using_an_%22All_Components%22_solution) for more information on using a solution to republish your factory.
