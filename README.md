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
Testing Environment:
| Virtual Network | Windows Virtual Machine | PostgreSQL Database  | Web App & App Service Plan | Monitoring Dashboard | Budget |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Bastion connection  | 1 instance  | General Purpose 2 vCores  | Premium P2v2 | Virtual Machine CPU | Start and End dates |
|  | Open to port HTTPS 443 | Version 11  | Windows .NET Core 3.1 (LTS) | Virtual Machine memory usage | Customizable thresholds |
|  | OS Disk Type: StandardSSD_LRS | Private Link connection   | Private Link connection | Database CPU | E-mail alert |
|  | Size: Standard_DS1_v2  |  |  | Database reclaimable space |  |
|  | Patch Mode: Automatic by OS |  |  | Log-ins |  |
|  | Monitoring & Diagnostics |  |  |  |  |

Production Environment:
| Virtual Network | Windows Virtual Machine | PostgreSQL Database  | Web App & App Service Plan | Monitoring Dashboard | Budget |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Bastion connection  | 2 instances  | General Purpose 4 vCores  | Premium P2v2 | Virtual Machine CPU | Start and End dates |
|  | Open to port HTTPS 443 | Version 11  | Windows .NET Core 3.1 (LTS) | Virtual Machine memory usage | Customizable thresholds |
|  | OS Disk Type: Premium_LRS | Private Link connection   | Private Link connection | Database CPU | E-mail alert |
|  | Size: Standard_DS1_v2  |  |  | Database reclaimable space |  |
|  | Patch Mode: Automatic by OS |  |  | Log-ins |  |
|  | Monitoring & Diagnostics |  |  |  |  |

# Getting Started
Get started with your Landing Zone by running these Bash commands on your code editor:
	
Install Python
```bash
sudo apt install python3.10
```

# Build your Landing Zone
Deploy Landing Zone through code editor:
1.	Clone the repository to your code editor
2.	Run 'Getting started' installments from the terminal
3.	Press Run or run from terminal:
```bash
python CreateResources.py
```
4.	Select your environment as prompted by the terminal

Deploy Landing Zone through pipeline:
1.	Press 'Set up build' from respository
2.	Sign in to your Azure account when prompted by the Pipeline
3.	Watch your environment deploy through the Pipeline

Photo here of the empty web app "hello developers..."

