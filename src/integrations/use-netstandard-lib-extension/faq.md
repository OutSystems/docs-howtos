---
summary: Learn how to use .NET Standard libraries in OutSystems 11 (O11) extensions by upgrading to .NET Framework 4.7.2 and adjusting Visual Studio settings.
tags: .net framework, visual studio, extension development, .net standard, integration studio
guid: 62335c22-2480-4119-8bcf-597538f63ee1
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/gKoXqtZTY2IJjyMWschrRB/Integrations?node-id=1242:336
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - backend developers
outsystems-tools:
  - integration studio
  - platform server
coverage-type:
  - apply
---

# How to use .NET Standard libraries in OutSystems extensions

## Requirements

* Microsoft Visual Studio 2017
* .NET Framework 4.7.2
* OutSystems Platform Server 11 - Release Apr.2019 or higher

## Use .NET Standard libraries in your extension

Windows improved .NET Standard support for .NET Framework applications in version 4.7.2. You can take advantage of this improvement and use .NET Standard libraries in your extensions.

<div class="warning" markdown="1">

If you don't follow the instructions on this page, your extensions will be in an **unsupported scenario** (using .NET 4.6.1 along with .NET Standard) that causes runtime issues.

</div>

Do the following:

1. Install .NET Framework 4.7.2 and Visual Studio 2017 in your development machine.

1. Change the Integration Studio options to start using Visual Studio 2017 and associated MSBuild to compile the extension.

    ![Screenshot of the Integration Studio configuration dialog showing paths for .NET Software Development Kit and .NET Integrated Development Environment.](images/integration-studio-config.png "Integration Studio Configuration Dialog")

1. Change the extension's main project target framework from ".NET Framework 4.6.1" to ".NET Framework 4.7.2".

    ![Visual Studio project properties window highlighting the target framework set to .NET Framework 4.7.2.](images/project-target.png "Project Properties Target Framework")

1. Build your extension and reference the necessary libraries.

Before publishing the extension in Integration Studio, make sure that your extension **doesn't include** system built-in assemblies from .NET Standard:

![Comparison of incorrect and correct extension resources in OutSystems, highlighting the exclusion of system assemblies like 'netstandard.dll'.](images/extension-resources.png "Extension Resources Comparison")

<div class="info" markdown="1">

**Note:** Sometimes you need to include a few system assemblies in your extension, for example `System.Runtime.CompilerServices.Unsafe.dll`. This won't cause any issues.

However, including a large list of system assemblies in an extension is a sign that you're including libraries that shouldn't be present in your extension.

For example, including the following system assemblies in extensions causes runtime issues:

* `netstandard.dll`
* `mscorlib.dll`
* `System.Runtime.InteropServices.RuntimeInformation.dll`
* `System.Net.Http.dll`

</div>

To remove the problematic assemblies do the following:

1. In Visual Studio, ensure that the target framework of all projects is `4.7.2`.

1. If necessary, uninstall and install again any third-party NuGet packages.

1. Delete the content of the `\Bin` folder.

1. In Integration Studio, right-click the `\Bin` folder in the **Resources** tab and choose **Exclude from extension**.

1. Click **Update Source Code** in the toolbar to regenerate the OutSystems assemblies inside the `\Bin` folder.

1. Back in Visual Studio, build the solution again and validate that the assemblies weren't added again.

1. In Service Studio, open the modules that consume the extension, refresh the references and publish.
