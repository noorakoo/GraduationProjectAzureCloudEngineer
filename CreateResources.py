import os

SubscriptionId = '07c29cd9-f0b0-42f7-be1c-01d2cfc5ee2c'
Location = 'northeurope'
ResourceGroup = 'testRG3'
TemplateName = 'blanktemplate'
TemplateFile = 'templates/azuredeploy.json'
ParameterFile = '@templates/vm_parameters.json'

os.system('az login')
os.system(f'az account set --subscription {SubscriptionId}')
os.system(f'az group create --name {ResourceGroup} --location {Location}')
os.system(f'az group create --name {ResourceGroup} --location {Location}')
os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')
