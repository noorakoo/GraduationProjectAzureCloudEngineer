import os

ToDeploy = input("""
\n
Which environment would you like to deploy?
    1. Testing 
    2. Production
    3. Both options
Enter the number of the desired deployment: """)



while ToDeploy not in ["1", "2", "3"]:
    ToDeploy = input("""
\n
Please enter a valid input value!
Which environment would you like to deploy?
    1. Testing 
    2. Production
    3. Both options
Enter the number of the desired deployment: """)



if ToDeploy == "1" or ToDeploy == "3": 
    # Signing in and setting the subscription
    SubscriptionId = '07c29cd9-f0b0-42f7-be1c-01d2cfc5ee2c' 
    Location = 'northeurope'
    os.system('az login')
    os.system(f'az account set --subscription {SubscriptionId}')

    # Creating the environment / Resource Group and Template
    ResourceGroup = 'FortmuTest'
    Location = 'northeurope'
    TemplateName = 'FortmuTempTest'
    os.system(f'az group create --name {ResourceGroup} --location {Location}')

    # Deploying the Virtual Network
    TemplateFile = 'TestEnvTemplates/TestVirtualNetworkTemplate.json'
    ParameterFile = '@TestEnvTemplates/TestVirtualNetworkParameters.json'
    os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

    # Deploying the Virtual Machine 1
    TemplateFile = 'TestEnvTemplates/TestVirtualMachineTemplate.json'
    ParameterFile = '@TestEnvTemplates/TestVirtualMachineParameters.json'
    os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

    # Deploying the PostgreSQL Database
    TemplateFile = 'TestEnvTemplates/TestDatabaseTemplate.json'
    ParameterFile = '@TestEnvTemplates/TestDatabaseParameters.json'
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

    # Deploying the Dashboard
    TemplateFile = 'TestEnvTemplates/TestDashboard.json'
    DashboardName = 'TestDashboard'
    os.system('az config set extension.use_dynamic_install=yes_without_prompt')
    os.system(f'az portal dashboard import --resource-group {ResourceGroup} --name {DashboardName} --input-path {TemplateFile}')

    # Deploying the Budget
    TemplateFile = 'TestEnvTemplates/TestBudget.json'
    os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile}')



if ToDeploy == "2" or ToDeploy == "3":
 # Signing in and setting the subscription
    SubscriptionId = '07c29cd9-f0b0-42f7-be1c-01d2cfc5ee2c' 
    Location = 'northeurope'
    os.system('az login')
    os.system(f'az account set --subscription {SubscriptionId}')

    # Creating the environment / Resource Group and Template
    ResourceGroup = 'FortmuAppTeam'
    Location = 'northeurope'
    TemplateName = 'FortmuTemp'
    os.system(f'az group create --name {ResourceGroup} --location {Location}')

    # Deploying the Virtual Network
    TemplateFile = 'ProdEnvTemplates/ProdVirtualNetworkTemplate.json'
    ParameterFile = '@ProdEnvTemplates/ProdVirtualNetworkParameters.json'
    os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

    # Deploying the Virtual Machine 1
    TemplateFile = 'ProdEnvTemplates/ProdVirtualMachineTemplate.json'
    ParameterFile = '@ProdEnvTemplates/ProdVirtualMachineParameters.json'
    os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

    # Deploying the Virtual Machine 2
    TemplateFile = ''
    ParameterFile = '@'
    os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

    # Deploying the PostgreSQL Database
    TemplateFile = 'ProdEnvTemplates/ProdDatabaseTemplate.json'
    ParameterFile = '@ProdEnvTemplates/ProdDatabaseParameters.json'
    os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

    # Deploying the Private Link for Database
    TemplateFile = 'ProdEnvTemplates/ProdDBPrivateLinkTemplate.json'
    ParameterFile = '@ProdEnvTemplates/ProdDBPrivateLinkParameters.json'
    os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

    # Deploying the Web App & App Service Plan
    TemplateFile = 'ProdEnvTemplates/ProdAppTemplate.json'
    ParameterFile = '@ProdEnvTemplates/ProdAppParameters.json'
    os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

    # Deploying the Private Link for Web App
    TemplateFile = 'ProdEnvTemplates/ProdAppPrivateLinkTemplate.json'
    ParameterFile = '@ProdEnvTemplates/ProdAppPrivateLinkParameters.json'
    os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile} --parameters {ParameterFile}')

    # Deploying the Dashboard
    TemplateFile = 'ProdEnvTemplates/ProdDashboard.json'
    DashboardName = 'ProdDashboard'
    os.system('az config set extension.use_dynamic_install=yes_without_prompt')
    os.system(f'az portal dashboard import --resource-group {ResourceGroup} --name {DashboardName} --input-path {TemplateFile}')

    # Deploying the Budget
    TemplateFile = 'ProdEnvTemplates/ProdBudget.json'
    os.system(f'az deployment group create --name {TemplateName} --resource-group {ResourceGroup} --template-file {TemplateFile}')