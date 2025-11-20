# Dupilcated Image Remover
# -*- coding:utf-8 -*-
# !/usr/bin/python
import os
from PIL import Image
import numpy as np
from skimage.metrics import structural_similarity as ssim
import shutil

def load_image_as_array(image_path):
    """Load an image and convert it to a grayscale array."""
    try:
        with Image.open(image_path) as img:
            img = img.convert('L')  # Convert to grayscale for simpler comparison
            img = img.resize((100, 100))  # Resize to standard size for faster processing
            return np.array(img)
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

def calculate_similarity(img1, img2):
    """Calculate the similarity between two images using SSIM."""
    return ssim(img1, img2)

def find_duplicates(folder_path, similarity_threshold=0.9, move_to_folder=None):
    """Find and handle duplicate images in a specified folder and its subdirectories based on visual similarity."""
    if not os.path.isdir(folder_path):
        print("Specified folder does not exist.")
        return

    # Store processed images for comparison
    processed_images = []
    duplicates = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Only consider image files
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff')):
                img_array = load_image_as_array(file_path)
                
                if img_array is not None:
                    is_duplicate = False
                    for original_img_path, original_img_array in processed_images:
                        similarity = calculate_similarity(original_img_array, img_array)
                        if similarity >= similarity_threshold:
                            print(f"Duplicate found: {file_path} -> {original_img_path} (Similarity: {similarity:.2f})")
                            duplicates.append(file_path)
                            if move_to_folder:
                                # Create subdirectory structure in the move folder
                                rel_path = os.path.relpath(root, folder_path)
                                target_folder = os.path.join(move_to_folder, rel_path)
                                os.makedirs(target_folder, exist_ok=True)
                                shutil.move(file_path, os.path.join(target_folder, file))
                            else:
                                os.remove(file_path)

                            is_duplicate = True
                            break

                    # Only add non-duplicate images to the list
                    if not is_duplicate:
                        processed_images.append((file_path, img_array))

    print("\nDuplicates Removed.")
    if move_to_folder:
        print(f"Moved duplicates to: {move_to_folder}")
    else:
        print("Deleted duplicates.")
        
if __name__ == "__main__":
    # Folder where images are located
    folder_path = input("Enter the path of the folder to clean (including subdirectories): ")
    # action = input("Type 'move' to move duplicates to a separate folder or 'delete' to remove them: ")
    action = "move"
    
    if action == 'move':
        move_to_folder = input("Enter the folder path to move duplicates to: ")
        if not os.path.exists(move_to_folder):
            os.makedirs(move_to_folder)
        find_duplicates(folder_path, move_to_folder=move_to_folder)
    else:
        find_duplicates(folder_path)
