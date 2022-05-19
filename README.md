[![Build Status](https://dev.azure.com/AcademyAzure2022/Fortmu%20Ltd%20-%20Group%203/_apis/build/status/FortmuDemo?branchName=master)](https://dev.azure.com/AcademyAzure2022/Fortmu%20Ltd%20-%20Group%203/_build/latest?definitionId=142&branchName=master)

# Introduction 
Landing Zone for Fortmu Ltd Application Development & Production Team.

With this Landing Zone you will have a cloud based environment up and running in just a couple of clicks to build your Web Apps. Customize the platform to suit your needs through parameter files when needed.
```bash
Run azure-pipelines.yml to deploy your Landing Zone through Pipeline
Run CreateResources.py to deploy your Landing Zone through editor
Run ResizeVM.py to resize a deployed Virtual Machine 
```

What the Landing zone includes:
## Testing environment:
1.	Virtual Network:
    + Bastion connection
2.	1 instance Windows Virtual Machine
    + Open to port HTTPS 443
    + OS Disk Type: StandardSSD_LRS
    + Size: Standard_DS1_v2
    + Patch Mode: Automatic by OS
    + Monitoring & Diagnostics
3.	PostgreSQL Database
    + General Purpose 2 vCores
    + Version 11
    + Private Link connection 
4.	Web App & App Service Plan
    + Premium P2v2
    + Windows .NET Core 3.1 (LTS)
    + Private Link connection
5. Monitoring Dashboard
    + CPU and Memory usage by percentage to Virtual Machine
    + xxxx to Database
6. Budget with thresholds

## Production environment:
1.	Virtual Network:
    + Bastion connection
2.	2 instances Windows Virtual Machine
    + Open to port HTTPS 443
    + OS Disk Type: Premium_LRS
    + Size: Standard_DS1_v2
    + Patch Mode: Automatic by OS
    + Monitoring & Diagnostics
3.	PostgreSQL Database
    + General Purpose 4 vCores
    + Version 11
    + Private Link connection 
4.	Web App & App Service Plan
    + Premium P2v2
    + Windows .NET Core 3.1 (LTS)
    + Private Link connection
5. Monitoring Dashboard
    + Virtual Machine CPU and Memory usage by percentage
    + Database
6. Budget with thresholds

# Getting Started
How to get started with your platform for building Apps:
	
Install Python
```bash
command
```
Install Flask
```bash
command
```
Install os module
```bash
command
```

# Build your Landing Zone
Deploy Landing Zone through editor:
1.	Clone the repository to your text editor
2.	Run installments from the terminal
3.	Select your environment and change the variable values accordingly
4.	Press Run 

Deploy Landing Zone through pipeline:
1.	Press 'Set up build' from respository
2.	Sign in to your Azure account when prompted by the Pipeline
3.	Watch your environment deploy through the Pipeline

Photo here of the empty web app "hello developers..."
