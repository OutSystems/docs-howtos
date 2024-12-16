---
summary: Explore how to create custom alerts in OutSystems 11 (O11) by leveraging APIs and metadata to monitor application thresholds and integrate with ITSM tools.
guid: d8e80008-11b7-43d8-804c-d99e577c7111
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/XbkdagtFJ9kxan8pAx0Qsz/DevOps?type=design&node-id=1542%3A348&mode=design&t=dN0yGLL6D8INLkOx-1
tags: custom alerts, api, monitoring, itsm tools, application performance
audience:
  - platform administrators
  - full stack developers
  - backend developers
  - frontend developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# How to create alerts based on monitoring thresholds

You can create custom alerts based on your application operations monitoring thresholds by using OutSystems APIs and metadata:

* Extend OutSystems built-in application operations
* Create your own logic for alerts with thresholds
* Integrate with external ITSM tools

![Diagram illustrating the three-step process to create alerts using OutSystems APIs: Step 1 - Gather data from OutSystems APIs, Step 2 - Consume the API data and define logic thresholds for alarms, Step 3 - Trigger email notifications or integrate with ITSM tools.](images/create-alerts-diag.png "Alerts Creation Process Diagram")


## Step 1 - gather data

OutSystems provides a set of APIs that can be used to analyze application events and even register events defined by you.

The [Monitoring API](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/PerformanceMonitoring_API) provides a **GET RequestEvents** method to gather over 100 properties of application events. 

As and example, you can gather information regarding:

* **Managed consumed resources** as a way to manage app capacity and quotas (e.g. consumed APIs)
* **Request duration** - time that passed from the moment the user made the request until the browser finished processing the response.
* **Browser load time** - time that the browser took to process the response. The load time includes for example the page rendering and the JavaScript execution.
* **Request server time** - total time the server spent serving the request.
* **Query, service action, integration, timer and extension time** - total time spent executing queries, calling service, integration, and extension actions as well as the time spent executing timers.
* Number of errors executing queries, screens, integrations, extensions and timers.

Check the [Monitoring API resources](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/PerformanceMonitoring_API#Resources) for all the details.


To gather details about each specific error, you can also [query the log data](https://success.outsystems.com/Documentation/11/Managing_the_Applications_Lifecycle/Monitor_and_Troubleshoot/Logging_database_and_architecture/Query_log_data).

You can also *define your own custom events* either using the [POST RequestEvents of the Monitoring API](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/PerformanceMonitoring_API#POST_RequestEvents) or the [LogMessage](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/System_Actions#LogMessage) built-in action to [log informations in your application flows](https://success.outsystems.com/Documentation/11/Developing_an_Application/Troubleshooting_Applications/Log_Information_in_Action_Flows).

## Step 2 - consume data and user-defined thresholds

Both the API data and the log data can them be consumed where you define custom logic for thresholds that will trigger alerts. You can build it using [OutSystems logic](https://success.outsystems.com/Documentation/11/Developing_an_Application/Implement_Application_Logic) or consume this data in any other third party application.

## Step 3 - trigger alerts and integration with 3rd party tools

Thresholds defined in your logic can trigger email notifications or call webservices to:

* create tickets in ITSM tools such as ServiceNow, Zendesk, Jira or Opsgenie
* send Slack messages
* integrate with any external service that exposes a webservice

OutSystems **Email** capabilities allow you to send emails from both [web](https://success.outsystems.com/Documentation/11/Developing_an_Application/Implement_Application_Logic/Send_an_Email_From_a_Web_Application), [reactive and mobile apps](https://success.outsystems.com/Documentation/11/Developing_an_Application/Implement_Application_Logic/Technical_Preview_-_Emails_in_Mobile_and_Reactive_Web_Apps/Sending_Emails).

You can even customize and extend the design of your emails using the [Emails API](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/Emails_API).

Most ITSM and messaging tools expose functionality in the form of webservices, such as the [ServiceNow REST API](https://docs.servicenow.com/bundle/paris-application-development/page/integrate/inbound-rest/concept/c_RESTAPI.html), [Slack API](https://api.slack.com/apis/connections), [Jira API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/) and [Opsgenie API](https://docs.opsgenie.com/v1.0/docs/alert-api) just to name a few.

With OutSystems you can integrate with anything, [consuming REST APIs](https://success.outsystems.com/Documentation/11/Extensibility_and_Integration/REST/Consume_REST_APIs) and [SOAP Web Services](https://success.outsystems.com/Documentation/11/Extensibility_and_Integration/SOAP/Consuming_SOAP_Web_Services) easily. Use these capabilities to create tickets or incidents to be handled by your IT services.

Check *pre-built integrations* for [Zendesk](https://www.outsystems.com/forge/component-overview/588/zendesk-connector) and [Jira](https://www.outsystems.com/blog/posts/jira-integration-app-feedback/)
