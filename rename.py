import os

# Path to the folder containing your images
input_folder_path = "E:\\Machine Learning\\Final_annotation\\somna_oranghe"

# Path to the output folder
output_folder_path = "E:\\Machine Learning\\Final_annotation\\output_images"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Loop through all files in the folder
for filename in os.listdir(input_folder_path):
    # Extract the file extension
    file_extension = os.path.splitext(filename)[1].lower()
    
    for i in range(41, 49):
        for j in range(1, 61):
            # Check if the file is a .jpg
            if file_extension == ".jpg":
                # Generate new file name
                new_name = f"saved_image_{i}_{j}{file_extension}"
                
                # Full paths
                old_file = os.path.join(input_folder_path, filename)
                new_file = os.path.join(output_folder_path, new_name)
                
                # Move and rename the file to the output folder
                os.rename(old_file, new_file)
                print(f"Moved and renamed: {filename} -> {new_name}")
            else:
                print(f"Skipped: {filename} (not a .jpg file)")
