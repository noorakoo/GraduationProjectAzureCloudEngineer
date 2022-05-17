import os


# Signing in and setting the subscription
SubscriptionId = 'e4305bfa-9413-4c0e-8527-8f5307a80a27'
Location = 'northeurope'
os.system('az login')
os.system(f'az account set --subscription {SubscriptionId}')

ResourceGroup = 'FortmuAppTeam'
Template = 'Template.json'
os.system(f'az portal dashboard import --resource-group {ResourceGroup} --name "DashboardFortmu" --input-path {Template}')