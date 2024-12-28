import os

# Specify the directory containing the text files
folder_path = "E:\\ANALOG DEVICES\Annotations\\13_12_2024_10_10_lays"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        # Open the file and read its content
        with open(file_path, 'r') as file:
            content = file.readlines()
        
        # Modify the first and second lines if they contain '15'
        #change the number 15 to 4
        if len(content) > 0 and '4' in content[0]:
            #change the number 16 to the number you want
            content[0] = content[0].replace('16', '0', 1)  # Replace first occurrence of '15' in line 1
        
        # if len(content) > 1 and '15' in content[1]:
        #     content[1] = content[1].replace('0', '16', 1)  # Replace first occurrence of '15' in line 2
        
        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(content)

print("All files have been updated.")
