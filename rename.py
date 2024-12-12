import os

# Path to the folder containing your images
folder_path = "D:\image_rec\multi_green_processed\multi_green_processed"

# Counter for the new filenames
count = 1

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Extract the file extension
    file_extension = os.path.splitext(filename)[1].lower()
    for i in range(1,10):
        for j in range(1,76):
        # Check if the file is a .jpeg
            if file_extension == ".jpg":
                # Generate new file name
                new_name = f"saved_image_{i}_{j}{file_extension}"
                
                # Full paths
                old_file = os.path.join(folder_path, filename)
                new_file = os.path.join(folder_path, new_name)
                
                # Rename the file
                os.rename(old_file, new_file)
                print(f"Renamed: {filename} -> {new_name}")
                
                # Increment the counter
                count += 1
            else:
                print(f"Skipped: {filename} (not a .jpeg file)")
