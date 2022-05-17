from multiprocessing.sharedctypes import SynchronizedString
import os

SubscriptionId = ''
ResourceGroup = ''
VirtualMachine = ''
Size = ''

# Run in terminal to list available Virtual Machine sizes:
# os.system(f'az vm list-vm-resize-options {ResourceGroup} --name {VirtualMachine} --output table')

os.system('az login')
os.system(f'az account set --subscription {SubscriptionId}')
os.system(f'az vm resize --resource-group {ResourceGroup} --name {VirtualMachine} --size {Size}')
