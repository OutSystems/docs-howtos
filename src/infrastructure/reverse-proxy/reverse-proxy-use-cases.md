---
summary: Explore common reverse proxy configurations for OutSystems 11 (O11) to enhance security and manage web traffic effectively.
locale: en-us
guid: 4c538aa3-0623-4e86-b871-9fdd3767eb6f
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/o7Rkyuxm89D6KrjD7AOYCU/Infrastructure?node-id=1242:557
tags: security, web traffic management, reverse proxy, https, ssl
audience:
  - platform administrators
  - infrastructure managers
  - backend developers
  - full stack developers
outsystems-tools:
  - none
coverage-type:
  - apply
---

# Common use cases in reverse proxy scenarios

With many possible usages, some common use cases and the configuration to be performed to implement each scenario are detailed below.

## HTTP Redirection

<div class="info" markdown="1">

Applies only to **Traditional Web Apps**

</div>

A website exposed on the Internet and served by an internal application server. The reverse proxy delivers all requests with `http://mysite.com` as a target to the internal application server.

This scenario prevents the application servers to be directly exposed to the internet.

![Diagram showing HTTP redirection from a browser to an OutSystems front-end through a reverse proxy.](images/reverse-proxy-use-cases-httpredirect-diag.png "HTTP Redirection Diagram")

Only standard reverse proxy configuration is required on this example. Please refer to your manufacturer documentation.

## HTTPS Redirection with End-to-end SSL

A website securely exposed on the Internet and served securely by an internal application server. The reverse proxy delivers all requests in HTTPS to the internal application server, which will also serve the content in HTTPS, keeping the HTTPS protocol end-to-end.

This scenario ensures encrypted communications from the internal application server to the user browser.

![Diagram illustrating HTTPS redirection with end-to-end SSL from a browser to an OutSystems front-end via a reverse proxy.](images/reverse-proxy-use-cases-e2eSSL-diag.png "HTTPS Redirection with End-to-end SSL Diagram")

To implement this scenario, you have to perform the following configurations:

* [C1 - End-to-end SSL](reverse-proxy-config.md#ssl-offloading)
* [F - Adjust keep-alive connection timeout](reverse-proxy-config.md#keep-alive-connection) (for Mobile and Reactive Apps)

## HTTPS Redirection with SSL Offload

A website securely exposed on the Internet and served by an internal application server.

The reverse proxy encrypts the communication to the Internet while keeping a standard HTTP communication with the internal application servers.

This configuration is called SSL offload. It centralizes the certificate management on the reverse proxy that also does all the encryption, easing the load from the application servers.

![Diagram depicting HTTPS redirection with SSL offload at the reverse proxy before reaching the OutSystems front-end.](images/reverse-proxy-use-cases-offload-diag.png "HTTPS Redirection with SSL Offload Diagram")

To implement this scenario, you have to perform the following configurations:

* [C2 - SSL Offload](reverse-proxy-config.md#ssl-offloading)
* [F - Adjust keep-alive connection timeout](reverse-proxy-config.md#keep-alive-connection) (for Mobile and Reactive Apps)

## Request Header Manipulation and Referenced Content

<div class="info" markdown="1">

Applies only to **Traditional Web Apps**

</div>

A website named `mysite.com` with references to an **Images** module on the server.

Both modules, **App1** and **Images** must be exposed requiring reverse proxy configuration for each.

This scenario is used when there’s a corporate reverse proxy for several other third party applications and services.

![Diagram showing request header manipulation and referenced content handling in a reverse proxy setup for OutSystems.](images/reverse-proxy-use-cases-header-diag.png "Request Header Manipulation and Referenced Content Diagram")

To implement this scenario, you have to perform the following configurations:

* [A - Request Header Manipulation](reverse-proxy-config.md#header-manipulation)
* [B - Referenced Content Exposure](reverse-proxy-config.md#ref-content)

## SSL Offload, Request Header Manipulation and Application Path Changes

<div class="info" markdown="1">

Applies only to **Traditional Web Apps**

</div>

Serving multiple secure applications with URL and path alteration. This setup is used when the reverse proxy serves several websites and applications in a hierarchic path organization.

![Diagram representing SSL offload, request header manipulation, and application path changes in a reverse proxy configuration.](images/reverse-proxy-use-cases-path-diag.png "SSL Offload, Request Header Manipulation and Application Path Changes Diagram")

To implement this scenario, you have to perform the following configurations:

* [A - Request Header Manipulation](reverse-proxy-config.md#header-manipulation)
* [B - Referenced Content Exposure](reverse-proxy-config.md#ref-content)
* [C - End-to-end SSL and SSL Offloading](reverse-proxy-config.md#ssl-offloading)
* [D - Rewrite URLs in resources](reverse-proxy-config.md#rewrite-urls)
* [E - Disable content compression](reverse-proxy-config.md#dis-cont-compression)

## More information

To learn more about how to set up OutSystems with a reverse proxy check the [Using OutSystems in Reverse Proxy Scenarios](intro.md) guide.
