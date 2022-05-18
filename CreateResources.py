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
TemplateFile = 'TestEnvTemplates/TestVirtualNetworkTemplate.json'
ParameterFile = '@TestEnvTemplates/TestVirtualNetworkParameters.json'
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

# Deploying the Virtual Machine 1
TemplateFile = 'TestEnvTemplates/TestVirtualMachineTemplate.json'
ParameterFile = '@TestEnvTemplates/TestVirtualMachineParameters.json'
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

# #Deploying the Virtual Machine 2
# TemplateFile = ''
# ParameterFile = '@'
# os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

# Deploying the PostgreSQL Database
TemplateFile = 'TestEnvTemplates/TestDatabaseTemplate.json'
ParameterFile = '@TestEnvTemplates/TestDatabaseParameter.json'
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

# Deploying the Private Link for Database
TemplateFile = 'TestEnvTemplates/TestDBPrivateLinkTemplate.json'
ParameterFile = '@TestEnvTemplates/TestDBPrivateLinkParameters.json'
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

# Deploying the Web App & App Service Plan
TemplateFile = 'TestEnvTemplates/TestAppTemplate.json'
ParameterFile = '@TestEnvTemplates/TestAppParameters.json'
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

# Deploying the Private Link for Web App
TemplateFile = 'TestEnvTemplates/TestAppPrivateLinkTemplate.json'
ParameterFile = '@TestEnvTemplates/TestAppPrivateLinkParameters.json'
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

# # Deploying the Dashboard
# TemplateFile = 'TestEnvTemplates/TestDashboardTemplate.json'
# ParameterFile = '@TestEnvTemplates/TestDashboardParameter.json'
# os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')