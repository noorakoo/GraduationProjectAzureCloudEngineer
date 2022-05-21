[![Build Status](https://dev.azure.com/AcademyAzure2022/Fortmu%20Ltd%20-%20Group%203/_apis/build/status/FortmuDemo?branchName=master)](https://dev.azure.com/AcademyAzure2022/Fortmu%20Ltd%20-%20Group%203/_build/latest?definitionId=142&branchName=master)

# Introduction 
Landing Zone for Fortmu Ltd Application Development & Production Team in the Microsoft Azure Cloud platform.

With this Landing Zone you will have a cloud based environment up and running in just a couple of clicks to build your Web Apps. Customize the platform to suit your needs through parameter files.
```
Run azure-pipelines.yml to deploy your Landing Zone through Pipeline (.yml will run CreateResourcesPipeline.py)

Run CreateResources.py to deploy your Landing Zone through code editor

Run Rename.py to rename any strings in the parameter and template files (e.g. naming, location, subscription ID)

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
Get started with your Landing Zone by running this Bash command on your terminal to install Python. 
The libraries we will be using (json and os) come preinstalled:
	
Install Python
```bash
sudo apt install python3.10
```

# Build your Landing Zone
> Deploy Landing Zone through code editor:
1.	Clone the repository to your code editor
2.	Run 'Getting started' installment in the terminal
3.	Press Run or run in Bash terminal:
```bash
python CreateResources.py
```
4.	Select your environment and sign in to your Azure account as prompted by the terminal

> Deploy Landing Zone through DevOps Pipeline:
1.	Press 'Set up build' from repository
2.	Sign in to your Azure account when prompted by the Pipeline
3.	Watch your environment deploy through the Pipeline

> Open your Web App through the Private Link, and you are ready to code and deploy your Apps!

![Alt text](/README.md_photo/WebApp.PNG "Web App")

&copy; Noora Kataja & Jonas Richter
