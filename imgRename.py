#    Copyright (C) 2025 Tjaart de Kock

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses.

import os

def rename_images(directory, base_name):
    # List all files in the directory
    files = sorted(os.listdir(directory))
    
    # Counter to append to the base name
    counter = 1
    
    # Loop through each file in the directory
    for file in files:
        # Get the file extension
        file_ext = os.path.splitext(file)[1]
        
        # Only process files that are images (you can add more extensions here)
        if file_ext.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']:
            # Create the new filename
            new_name = f"{base_name}-{counter:02d}{file_ext}"
            
            # Build the full paths
            old_file_path = os.path.join(directory, file)
            new_file_path = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            
            print(f"Renamed: {file} -> {new_name}")
            
            # Increment the counter
            counter += 1

if __name__ == "__main__":
    # Get the directory and base name from the user
    directory = input("Enter the path to the directory containing the images: ")
    base_name = input("Enter the base name for the images (e.g., img): ")
    
    # Rename the images
    rename_images(directory, base_name)
