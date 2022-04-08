---
summary: Configure your OutSystems installation to use an Apache web server as a reverse proxy. Includes configuration for Apache Web Server 2.2 or higher for HTTP and HTTPS.
tags: support-installation;support-maintenance;support-Security
en_title: 04_Configuring_an_Apache_Web_Server_as_a_Reverse_Proxy
locale: en-us
guid: c96d06e4-6dc7-4269-bb4e-726267bc75e6
---

# Configuring an Apache Web Server as a Reverse Proxy

<div class="info" markdown="1">

Applies only to **Traditional Web Apps**

</div>

## Requirements

Apache Web Server 2.2 or higher with the following modules:

* Substitute
* SSL
* Rewrite

## Example assumptions

**Old Application Path:** `http://mysite.com/myapp`

**New Application Path:** `http://mysite.com/apps/myapp`

**Proxy Server:** `mysite.com`

**OutSystems Server:** `server.local`

**Extra Path in URL:** `/apps/`

## Configuration for HTTP

This configuration can be added to the main `httpd.conf` file, or to a separate file under the user-specific configurations folder. The latter is usually the `conf.d` folder.

```
< VirtualHost *:80 >

ProxyRequests Off
ProxyPreserveHost On
RewriteEngine on

#Global Rules
ProxyPassMatch /apps/(?!LifeTimeSDK|LifeTimeCore|lifetime|PerformanceMonitor)(.*) http://server.local/$1
ProxyPassReverse /apps/ http://server.local/

#Mod rewrite rules
RewriteRule "^/(?!apps)(.*)" "http://mysite.com/apps/$1" [R]
AddOutputFilterByType SUBSTITUTE text/html
AddOutputFilterByType SUBSTITUTE text/javascript

#Fix for Service Center eSpace and Extension publish
Substitute s|http(.*)://(.*)/ServiceCenter/|http$1://$2/apps/ServiceCenter/|i

#Fix AppFeedback / ECT in Javascript
Substitute s|"/ECT_Provider/|"/apps/ECT_Provider/|i
Substitute s|'/ECT_Provider/|'/apps/ECT_Provider/|i

#LifeTime Management Console
ProxyPassMatch /apps/LifeTimeSDK/(.*) http://lifetime.server/LifeTimeSDK/$1
ProxyPassMatch /apps/LifeTimeCore/(.*) http://lifetime.server/LifeTimeCore/$1
ProxyPassMatch /apps/lifetime/(.*) http://lifetime.server/lifetime/$1

ProxyPassMatch /apps/PerformanceMonitor/(.*) http://lifetime.server/PerformanceMonitor/$1

​< / VirtualHost >
```

## Configuration for HTTPS

This configuration is added to the `ssl.conf` configuration file, which by default is the `ssl.conf` under the user-specific configurations folder, and between the virtual host tags.

```
< VirtualHost >
... 
Listen 443
... 
ProxyRequests Off 
ProxyPreserveHost On 
RewriteEngine on 

#Global Rules 
ProxyPassMatch /apps/(?!LifeTimeSDK|LifeTimeCore|lifetime|PerformanceMonitor)(.*) http://server.local/$1 
ProxyPassReverse /apps/ http://server.local/ 

#Mod rewrite rules 
RewriteRule "^/(?!apps)(.*)" "https://mysite.com/apps/$1" [R] 

AddOutputFilterByType SUBSTITUTE text/html 
AddOutputFilterByType SUBSTITUTE text/javascript 

#Fix for Service Center eSpace and Extension publish 
Substitute s|http(.*)://(.*)/ServiceCenter/|http$1://$2/apps/ServiceCenter/|i 

#Fix AppFeedback / ECT in Javascript 
Substitute s|"/ECT_Provider/|"/apps/ECT_Provider/|i
Substitute s|'/ECT_Provider/|'/apps/ECT_Provider/|i 

#LifeTime Management Console 
ProxyPassMatch /apps/LifeTimeSDK/(.*) http://lifetime.server/LifeTimeSDK/$1 
ProxyPassMatch /apps/LifeTimeCore/(.*) http://lifetime.server/LifeTimeCore/$1 
ProxyPassMatch /apps/lifetime/(.*) http://lifetime.server/lifetime/$1 

ProxyPassMatch /apps/PerformanceMonitor/(.*) http://lifetime.server/PerformanceMonitor/$1 
...
< / VirtualHost >
```
