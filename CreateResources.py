import os

# Signing in and setting the subscription
SubscriptionId = 'e4305bfa-9413-4c0e-8527-8f5307a80a27' 
Location = 'northeurope'
os.system('az login')
os.system(f'az account set --subscription {SubscriptionId}')

# Creating the environment / Resource Group and Template
ResourceGroup = 'FortmuAppTeam'
Location = 'northeurope'
TemplateName = 'FortmuTemplate'
os.system(f'az group create --name {ResourceGroup} --location {Location}')

# Deploying the Virtual Network
 
# Deploying the Virtual Machine 1
TemplateFile = 'TestEnvTemplates/DeployTestVM.json'
ParameterFile = '@TestEnvTemplates/TestVMParameters.json'
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

# Deploying the Virtual Machine 2

# Deploying the PostgreSQL Database
TemplateFile = 'TestEnvTemplates/DeployTestDB.json'
ParameterFile = '@TestEnvTemplates/TestDBParameters.json'
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

# Deploying the Private Link for Database

# Deploying the Web App & App Service Plan

# Deploying the Private Link for Web App

# Deploying the Monitoring Dashboard








# # Creating the production environment
# ResourceGroup = 'ProductionRG'
# TemplateName = 'ProductionTemplate'
# os.system(f'az group create --name {ResourceGroup} --location {Location}')

# # Deploying two production VMs
# TemplateFile = 'ProdEnvTemplates/DeployProdVM.json'
# ParameterFile = '@ProdEnvTemplates/ProdVM1Parameters.json'
# os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')
# ParameterFile = '@ProdEnvTemplates/ProdVM2Parameters.json'
# os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

# # Deploying the production database
# TemplateFile = 'ProdEnvTemplates/DeployProdDB.json'
# ParameterFile = '@ProdEnvTemplates/ProdDBParameters.json'
# os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')