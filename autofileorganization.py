import os
import shutil

# Step 1: Choose the folder to organize
folder_path = "C:/filesforcoding"  # 🔁 Change this to your target folder

# Step 2: Define file type categories
file_types = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Audio': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar'],
    'Scripts': ['.py', '.js', '.cpp', '.java'],
    'Others': []
}

# Step 3: Create subfolders and move files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if os.path.isfile(file_path):
        moved = False
        ext = os.path.splitext(filename)[1].lower()
        
        for folder_name, extensions in file_types.items():
            if ext in extensions:
                dest_folder = os.path.join(folder_path, folder_name)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                moved = True
                break
        
        if not moved:
            others_folder = os.path.join(folder_path, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))

print("✅ Files have been organized by type!")