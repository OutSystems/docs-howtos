---
tags: version-10; deployment; DevOps; Jenkins; lifecycle; release
summary: 
---

# How to automate OutSystems Deployments with Jenkins

## Introduction

The following guide provides a step-by-step description of how to automate the execution of OutSystems deployment plans using an automation server such as [Jenkins](https://jenkins.io/) and the LifeTime Deployment API.

Please refer to the API [documentation](https://success.outsystems.com/Documentation/10/Reference/OutSystems_APIs/LifeTime_Deployment_API#v1) to familiarize yourself with the concepts of Environments, Applications and Deployment Plans mentioned extensively throughout this guide. In order to authenticate any request to the Deployment API, you’ll need to generate an Authentication Token (for a LifeTime Service Account), as explained [here](https://success.outsystems.com/Documentation/10/Reference/OutSystems_APIs/LifeTime_Deployment_API/REST_API_Authentication).

## Prerequisites

In order to complete the steps described in this guide, please confirm that you have the following prerequisites installed:

**Prerequisite** |  **Version used for this guide**  
---|---  
Copy Artifact Plugin  |  1.38.1  
Environment Injector Plugin  |  2.1.3  
Extended Choice Parameter Plugin  |  0.76  
Jenkins Automation Server  |  2.80  
Parameterized Trigger plugin  |  2.35.2  
PowerShell Plugin  |  1.3  
Windows PowerShell  |  4.0  
  
For installing Jenkins plugins, please refer to the Jenkins [documentation](https://jenkins.io/doc/book/managing/plugins/).

Although the automation process relies heavily on the usage of PowerShell scripts, actual PowerShell knowledge is not required to carry out the steps of this guide, as you’ll only be required to copy/paste from the provided template scripts.

## Step-by-step configuration guide

### Create a Folder in Jenkins (Optional)

Start by creating a new Jenkins **Folder** to store the Jenkins Projects that will be created in the following steps.

From the Jenkins Dashboard, go to **New Item**, select **Folder** and name it `OutSystems`.

![](<images/image-527.png?width=900>)

In the Folder **configuration** page, provide the following configuration values:

* **Name** : `OutSystems` 
* **DisplayName** : `OutSystems` 
* **Description** : `Contains projects for automating the deployment of OutSystems applications.` 

![](images/image-805.png?width=700)

#### Retrieve the list of Environments and Applications from LifeTime

Secondly, you’ll be creating a Jenkins **Project** to fetch the latest Environment and Application data from your LifeTime environment.

This information, including names and unique keys, will be used to specify the content of your automated deployment plans.

From the created OutSystems Folder, go to **New Item**, select **Freestyle project** and name it `FetchLifeTimeData`.

![](images/image-276.png?width=900)

In the **General** section, provide the following configuration values:

* **Name** : `FetchLifeTimeData` 
* **Description** : `Fetch the latest Environment and Application data in LifeTime for invoking the Deployment API.`

![](images/image-281.png?width=700)

In the **Build Trigger** section, check the **Build periodically** option and provide a scheduling configuration using cron syntax (e.g.: every day, around midnight):

![](images/image-439.png?width=700)

This will ensure that the information about OutSystems Environments and Applications is regularly retrieved by Jenkins and kept up-to-date.

In the **Build Environment** section, check the option **Inject environment variables to the build process** and copy/paste the following properties definition to the **Properties Content** field:

```  
    LifeTimeUrl=<URL of LifeTime environment>
    AuthorizationToken=<Authorization Token of LifeTime service account>
```    

![](images/image-113.png?width=700)

In the **Build** section, select **Add build step** and choose the **Windows Powershell** option. Next, copy/paste the contents of the following PowerShell script to the **Command** field:

```
    https://github.com/OutSystems/jenkins/blob/master/scripts/powershell/FetchLifeTimeData.ps1
```    

In the **Post-build Actions** section, select **Add post-build step** and choose the **Archive the artifacts** option, while providing the following configuration value:

* **Files to archive** : `*.mapping`

![](images/image-765.png?width=700)

This step is needed in order to make these artifacts retrievable from other Projects (as explained in the next section).

Click the **Save** option to persist changes to the Project.

Press **Build Now** to trigger a new build for this Project.

You can check the progress of the ongoing build through the **Console Output** option. This source provides additional troubleshooting information in case the build fails.

![](images/image-286.png?width=800)

For each **successful build** of this project, the following artifacts will be created in the project workspace:

**Artifact** |  **Description**  
---|---  
LT.Environments.mapping  |  Mapping file between Environment names and unique keys  
LT.Environments.properties  |  Properties file to use as source data for Build parameter  
LT.Applications.mapping  |  Mapping file between Application names and unique keys  
LT.Applications.properties  |  Properties file to use as source data for Build parameter  
  
![](images/image-530.png?width=400)

### Deploy latest Application tags to target LifeTime environment

Thirdly, you’ll be creating a Jenkins **Project** to deploy a list of LifeTime applications from a Source environment to a Target environment via the Deployment API.

When creating the deployment plan to execute, the **latest tags** of each application to deploy will be selected and **added** to the plan. This means that after a developer tags his code in the source environment (using the appropriate version number and tag description), Jenkins can automatically discover this application tag and deploy it to the target environment without further human intervention.

From the created **OutSystems** Folder, go to **New Item**, select **Freestyle project** and name it `DeployLatestTagsToTargetEnv`.

![](images/image-278.png?width=900)

In the **General** section, provide the following configuration values:

* **Name** : `DeployLatestTagsToTargetEnv` 
* **Description** : `Deploy to target environment the latest tags of configured Applications.` 

![](images/image-550.png?width=700)

In the **General** section, check the option **This project is parameterized** and configure the following build parameters:

<table markdown="1">
<thead>
<tr>
<th>Build Parameter</th>
<th>Configuration Values</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source Environment</td>
<td>Select **Add Parameter** and choose the **Extended Choice Parameter** option:<p>

* **Name** : `SourceEnvironment`
* **Description** : `Source environment when creating the deployment plan.` 

After selecting the **Basic Parameter Types** option:

* **Parameter Type** : Single Select 
* **Number of Visible Items** : `5` 

In the **Choose Source for Value** section :

* Select the **Property File** option and configure the path to the **LT.Environments.properties** file (available in FetchLifeTimeData project workspace) 
* **Property Key** : `Environments` 

![](images/image-357.png?width=600)</p>
</td>
</tr>
<tr> 
<td>Target Environment</td>
<td>
Select **Add Parameter** and choose the **Extended Choice Parameter** option:<p>

* **Name** : `TargetEnvironment` 
* **Description** : `Target environment when creating the deployment plan.` 

After selecting the **Basic Parameter Types** option:

* **Parameter Type** : Single Select 
* **Number of Visible Items** : `5` 

In the **Choose Source for Value** section :

* Select the **Property File** option and configure the path to the **LT.Environments.properties** file (available in FetchLifeTimeData project workspace) 
* **Property Key** : `Environments` 

![](images/image-355.png?width=600)</p>
</td>
</tr>
<tr>
<td>Applications To Deploy</td>
<td>
Select **Add Parameter** and choose the **Extended Choice Parameter** option:<p>

* **Name** : `ApplicationsToDeploy` 
* **Description** : `List of applications to include in the deployment plan.` 

After selecting the **Basic Parameter Types** option:

* **Parameter Type** : Check Boxes 
* **Number of Visible Items** : `15` 

In the **Choose Source for Value** section :

* Select the **Property File** option and configure the path to the **LT.Applications.properties** file (available in FetchLifeTimeData project workspace) 
* **Property Key** : `Applications` 

![](images/image-407.png?width=600)</p>
</td>
</tr>
</tbody>
</table>

In the **Build Environment** section, check the option **Inject environment variables to the build process** and copy/paste the following properties definition to the **Properties Content** field:

``` 
    LifeTimeUrl=<URL of LifeTime environment>
    AuthorizationToken=<Authorization Token of LifeTime service account>
    DeploymentTimeoutInSecs=300
    SleepPeriodInSecs=20
```    

![](images/image-69.png?width=700)

In the **Build** section, select **Add build step** and choose the **Copy artifacts from another project** option, while providing the following configuration values:

* **Project name** : `FetchLifeTimeData` 
* **Which build** : Latest successful build 
* **Artifacts to copy** : `*.mapping` 

![](images/image-400.png?width=700)

Still in the **Build** section, select **Add build step** and choose the **Windows Powershell** option. Next, copy/paste the contents of the following PowerShell script to the **Command** field:

```   
https://github.com/OutSystems/jenkins/blob/master/scripts/powershell/DeployLatestTagsToTargetEnv.ps1
```   

Click the **Save** option to persist changes to the Project.

From this point onwards, you can perform an automated OutSystems deployment in Jenkins, by triggering a new **Build with Parameters** of this Project and specifying the values for source and target Environments and selecting the Applications to deploy.

![](images/image-90.png?width=500)

You can check the progress of an ongoing build through the **Console Output** option. This source provides additional troubleshooting information in case the build fails.

![](images/image-781.png?width=800)

### Deploy periodically a set of Applications to a specific Environment

Additionally, you can opt to configure a separate Jenkins Project, that triggers the **DeployLatestTagsToTargetEnv** project with a specific build **parameterization** and **scheduling**, as described next.

From the created **OutSystems** Folder, go to **New Item** , select **Freestyle project** and name it `DeployIntranetApps` (for instance).

![](images/image-991.png?width=900)

In the **General** section, provide the following configuration values:

* **Name** : `DeployIntranetApps` 
* **Description** : `Deploy periodically the latest tags of Intranet apps (Directory, Cases and Timesheets) from DEV to QUA environments.` 

![](images/image-748.png?width=700)

In the **Build Trigger** section, check the **Build periodically** option and provide a scheduling configuration using cron syntax (e.g.: every weekday, at 23h):

![](images/image-453.png?width=700)

In the **Build** section, select **Add build step** and choose the **Trigger/call builds on other projects** option, while providing the following configuration values:

* **Project to build** : `DeployLatestTagsToTargetEnv` 
* Check the **Block until the triggered projects finish their builds** option 
* Select **Add Parameter** and choose **Predefined parameters** option 
* Provide the following properties definition in the **Parameters** field: 

```  
    SourceEnvironment=<Source Environment Name>
    TargetEnvironment=<Target Environment Name>
    ApplicationsToDeploy=<Names of Applications to deploy (csv)>
```    

![](images/image-574.png?width=1000)

Click the **Save** option to persist changes to the Project.

This approach can be replicated as many times as the number of desired build parameterizations.
