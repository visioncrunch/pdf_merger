"""
PDF Merger Script

This script merges multiple PDF files located in a specified folder into a single PDF file.

Dependencies:
    - PyPDF2 library

Usage:
    1. Ensure that the PyPDF2 library is installed. You can install it using pip:
        pip install PyPDF2

    2. Set the 'SOURCE_FOLDER' variable to the path of the folder containing the PDF files to be merged.

    3. Set the 'OUTPUT_FILE' variable to the desired path to save the merged PDF file.

    4. Run the script. The merged PDF file will be saved at the specified output path.

Notes:
    - It's recommended to sort the PDF files in ascending order in the file explorer before running the script to ensure the desired order of pages in the merged PDF.

Author:
    Anubhav (star this repo on GitHub - @visioncrunch)

Date:
    May 8, 2024

"""

import os
from PyPDF2 import PdfMerger

# Variables for source folder and output file path (Change these as needed)
SOURCE_FOLDER = "E:/course_pdfs/temporary/"
OUTPUT_FILE = "C:/Users/mukul/Downloads/output.pdf"

def merge_pdfs_in_folder(folder_path=SOURCE_FOLDER, output_path=OUTPUT_FILE):
    """
    Merge PDF files located in the specified folder into a single PDF file.

    Parameters:
        folder_path (str): Path to the folder containing PDF files. Defaults to 'SOURCE_FOLDER'.
        output_path (str): Path to save the merged PDF file. Defaults to 'OUTPUT_FILE'.

    Returns:
        None
    """
    merger = PdfMerger()

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            # Open each PDF file and append it to the merger
            with open(os.path.join(folder_path, filename), 'rb') as file:
                merger.append(file)

    # Write the merged PDF to the output file
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

# Call the function to merge PDFs
merge_pdfs_in_folder()
