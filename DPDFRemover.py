# Dupilcated PDF Remover
# -*- coding:utf-8 -*-
# !/usr/bin/python
import os
import hashlib
import imagehash
from PIL import Image
from PyPDF2 import PdfFileReader

def get_image_hash(image_path):
    """Generate a perceptual hash for an image file."""
    with Image.open(image_path) as img:
        img_hash = imagehash.average_hash(img)
    return img_hash

def get_pdf_hash(pdf_path):
    """Generate a hash for a PDF file based on its content."""
    hasher = hashlib.md5()
    try:
        with open(pdf_path, 'rb') as f:
            pdf = PdfFileReader(f)
            for page_num in range(pdf.numPages):
                page = pdf.getPage(page_num)
                hasher.update(page.extract_text().encode('utf-8', errors='ignore'))
    except Exception as e:
        print(f"Error processing PDF {pdf_path}: {e}")
        return None
    return hasher.hexdigest()

def find_duplicate_files(folder_path):
    """Find and remove duplicate images and PDFs in a folder, including subdirectories."""
    file_hashes = {}
    duplicates = []

    # Traverse through all files in the folder and subdirectories
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Process image files
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    img_hash = get_image_hash(file_path)

                    if img_hash in file_hashes:
                        duplicates.append(file_path)
                    else:
                        file_hashes[img_hash] = file_path

                # Process PDF files
                elif file.lower().endswith('.pdf'):
                    pdf_hash = get_pdf_hash(file_path)

                    if pdf_hash and pdf_hash in file_hashes:
                        duplicates.append(file_path)
                    else:
                        file_hashes[pdf_hash] = file_path
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    return duplicates

def delete_files(file_list):
    """Delete files from the given list."""
    for file in file_list:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")

if __name__ == "__main__":
    print("검증되지 않았으니 사용을 금함")
    exit(0)

    folder_path = input("Enter the folder path to clean duplicate images and PDFs: ")

    if os.path.exists(folder_path):
        duplicates = find_duplicate_files(folder_path)

        if duplicates:
            print(f"Found {len(duplicates)} duplicate files.")
            delete_files(duplicates)
        else:
            print("No duplicate files found.")
    else:
        print("Invalid folder path!")