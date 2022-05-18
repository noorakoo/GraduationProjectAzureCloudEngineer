import os


# Signing in and setting the subscription
SubscriptionId = '07c29cd9-f0b0-42f7-be1c-01d2cfc5ee2c'
Location = 'northeurope'
os.system('az login')
os.system(f'az account set --subscription {SubscriptionId}')

ResourceGroup = 'FortmuAppTeam'
Template = 'TestDashboardTemplate.json'
os.system(f'az portal dashboard import --resource-group {ResourceGroup} --name "DashboardFortmu" --input-path {Template}')
