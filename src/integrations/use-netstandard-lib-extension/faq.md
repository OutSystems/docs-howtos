---
tags: 
---

# How to Use .NET Standard libraries in OutSystems extensions

## Requirements

* Microsoft Visual Studio 2017
* .NET Framework 4.7.2
* OutSystems Platform Server 11 - Release Apr.2019 or higher

## Use .NET Standard libraries in your extension

Windows improved .NET Standard support for .NET Framework applications in version 4.7.2. You can take advantage of this improvement and use .NET Standard libraries in your extensions.

Without respecting the instructions described on this page the extensions will be on an unsupported scenario (4.6.1 + .Net Standard) and can cause runtime issues.

Do the following:

1. Install .NET Framework 4.7.2 and Visual Studio 2017 in your development machine.

1. Change the Integration Studio options to start using Visual Studio 2017 and associated MSBuild to compile the extension.

    ![](images/integration-studio-config.png)

1. Change the extension's main project target framework from ".NET Framework 4.6.1" to ".NET Framework 4.7.2".

    ![](images/project-target.png)

1. Build your extension and reference the necessary libraries.

Before publishing validate that in extension does **not** include system builtin assemblies from .Net Standard.

![](images/extension-resources.png)

*Note*: sometimes it is normal to have a few system assemblies included (for example: "System.Runtime.CompilerServices.Unsafe.dll"), but having a large list indicates that it is incorrect. In particular having "netstandard.dll", "mscorlib.dll", "System.Runtime.InteropServices.RuntimeInformation.dll" or "System.Net.Http.dll" is clearly incorrect.


To cleanup the problematic assemblies:
1. Ensure that the target framework of all projects is correctly set to 4.7.2.
1. If necessary uninstall and reinstall any third party nuget packages.
1. Delete the contents of the \Bin folder  
1. In Integration Studio right click the \Bin folder in the Resources tab and choose "Exclude from extension"
1. In Integration Studio click on the "Update Source Code" button to regenerate the OutSystems assemblies inside the \Bin folder
1. Back in Visual studio build the solution again and validate that the assemblies were not added again

