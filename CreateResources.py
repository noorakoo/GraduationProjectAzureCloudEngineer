import os

SubscriptionId = '07c29cd9-f0b0-42f7-be1c-01d2cfc5ee2c'
Location = 'northeurope'
MyResourceGroup = 'testRG2'
TemplateName = 'blanktemplate'
TemplateFileName = 'azuredeploy.json'
ParameterFile = '@vm_parameters.json'

os.system('az login')
os.system(f'az account set --subscription {SubscriptionId}')
os.system(f'az group create --name {MyResourceGroup} --location {Location}')
os.system(f'az group create --name {MyResourceGroup} --location {Location}')
os.system(f'templateFile=".\{TemplateFileName}"')
os.system(f'az deployment group create --name {TemplateName} --resource-group {MyResourceGroup} --template-file {TemplateFileName} --parameters {ParameterFile}')