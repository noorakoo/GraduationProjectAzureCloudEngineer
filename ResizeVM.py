from multiprocessing.sharedctypes import SynchronizedString
import os

SubscriptionId = '07c29cd9-f0b0-42f7-be1c-01d2cfc5ee2c'
ResourceGroup = 'FortmuAppTeamTest'
VirtualMachine = 'FortmuTestVM'
Size = ''

os.system('az login')
os.system(f'az account set --subscription {SubscriptionId}')
os.system(f'az vm list-vm-resize-options --resource-group {ResourceGroup} --name {VirtualMachine} --output table')

Size = input("Please enter the VM-size to update to.")
os.system(f'az vm resize --resource-group {ResourceGroup} --name {VirtualMachine} --size {Size}')