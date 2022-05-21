from multiprocessing.sharedctypes import SynchronizedString
import os

SubscriptionId = ''
ResourceGroup = ''
VirtualMachine = ''
Size = ''

os.system('az login')
os.system(f'az account set --subscription {SubscriptionId}')
os.system(f'az vm list-vm-resize-options --resource-group {ResourceGroup} --name {VirtualMachine} --output table')

Size = input("Please enter the VM-size to update to.")
os.system(f'az vm resize --resource-group {ResourceGroup} --name {VirtualMachine} --size {Size}')
