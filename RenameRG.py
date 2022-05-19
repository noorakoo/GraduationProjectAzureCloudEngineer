import json
import os

#RGName = ""
#NewRGName = ""

for directory in ['./ProdEnvTemplates', './TestEnvTemplates']:
    # Iterating over files in the directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        if ".json" in filename:
            # Updating lines¨
            with open(directory + "/" + filename, 'r') as fr:
                pre_ = fr.read()
                lines = pre_.split('\n')
                updated_lines = []

                for line in lines:
                    if RGName in line:
                        line = line.replace(RGName, NewRGName)
                    elif RGName.lower() in line.lower():
                        line = line.replace(RGName.lower(), NewRGName.lower())
                
                    updated_lines.append(line)
                    
            # Writing to new json
            with open(directory + "/Updated"+filename, "w") as outfile:
                for line in updated_lines:
                    outfile.write(line + "\n")