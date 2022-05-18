import os

# Signing in and setting the subscription
SubscriptionId = 'e4305bfa-9413-4c0e-8527-8f5307a80a27' 
Location = 'northeurope'
ResourceGroup = 'FortmuAppTeam'
VnetName = 'TestVnet'


os.system('az login')
os.system(f'az account set --subscription {SubscriptionId}')
os.system(f'az network vnet create --name {VnetName} --resource-group {ResourceGroup} --subnet-name default')