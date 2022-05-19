[![Build Status](https://dev.azure.com/AcademyAzure2022/Fortmu%20Ltd%20-%20Group%203/_apis/build/status/FortmuDemo?branchName=master)](https://dev.azure.com/AcademyAzure2022/Fortmu%20Ltd%20-%20Group%203/_build/latest?definitionId=142&branchName=master)

# Introduction 
Landing Zone for Fortmu Ltd Application Development & Production Team.

With this Landing Zone you will have a cloud based environment up and running in just a couple of clicks to build your Web Apps. Customize the platform to suit your needs through parameter files.
```
Run azure-pipelines.yml to deploy your Landing Zone through Pipeline

Run CreateResources.py to deploy your Landing Zone through code editor

Run ResizeVM.py to resize a deployed Virtual Machine 
```


## What the Landing zone includes:
**Testing environment:**
| Virtual Network | Windows Virtual Machine | PostgreSQL Database  | Web App & App Service Plan |
| ------------- | ------------- | ------------- | ------------- |
| Bastion connection  | 1 instance  | General Purpose 2 vCores  | Premium P2v2 |
|  | Open to port HTTPS 443 | Version 11  | Windows .NET Core 3.1 (LTS) |
|  | OS Disk Type: StandardSSD_LRS | Private Link connection   | Private Link connection |
|  | Size: Standard_DS1_v2  |  |  |
|  | Patch Mode: Automatic by OS |  |  |
|  | Monitoring & Diagnostics |  |  |

**Production environment:**
| Virtual Network | Windows Virtual Machine | PostgreSQL Database  | Web App & App Service Plan |
| ------------- | ------------- | ------------- | ------------- |
| Bastion connection  | 2 instances  | General Purpose 4 vCores  | Premium P2v2 |
|  | Open to port HTTPS 443 | Version 11  | Windows .NET Core 3.1 (LTS) |
|  | OS Disk Type: Premium_LRS | Private Link connection   | Private Link connection |
|  | Size: Standard_DS1_v2  |  |  |
|  | Patch Mode: Automatic by OS |  |  |
|  | Monitoring & Diagnostics |  |  |

**Both environments include:**
| Dashboard |  |
| --- | --- |
| Monitoring | Virtual Machine CPU and memory usage, Database CPU and reclaimable space, log-ins |
| Budget | Start and End dates, Customizable thresholds, E-mail alert |

# Getting Started
Get started with your Landing Zone by running these Bash commands:
	
Install Python
```
command
```
Install json
```
command
```
Install os module
```
command
```

# Build your Landing Zone
Deploy Landing Zone through code editor:
1.	Clone the repository to your code editor
2.	Run 'Getting started' installments from the terminal
3.	Select your environment and change the variable values accordingly
4.	Press Run or run from terminal:
```
python CreateResources.py
```

Deploy Landing Zone through pipeline:
1.	Press 'Set up build' from respository
2.	Sign in to your Azure account when prompted by the Pipeline
3.	Watch your environment deploy through the Pipeline

Photo here of the empty web app "hello developers..."

