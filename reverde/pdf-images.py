
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reverde - LLM based, multimodal, conversion tool; transformation of the old to the new
@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""

"""Needs to run:

reverde.ps1 -c pdf-images -i testdata/ d:\\src\\almacenesfundacion

"""

from pathlib import Path
from typing import List
import fitz  # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_folder):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    
    # Iterate through each page
    for i in range(len(doc)):
        page = doc.load_page(i)  # number of page
        image_list = page.get_images(full=True)
        
        # Print how many images found on each page
        print(f"[+] Found {len(image_list)} images in page {i}")
        
        # Extract each image
        for image_index, img in enumerate(page.get_images(full=True)):
            # get the XREF of the image
            xref = img[0]
            
            # extract the image bytes
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            
            # get the image extension
            image_ext = base_image["ext"]
            
            # construct the image filename
            image_filename = f"image_Page_{i+1}_{image_index+1}.{image_ext}"
            image_filepath = os.path.join(output_folder, image_filename)
            
            # save the image
            with open(image_filepath, "wb") as image_file:
                image_file.write(image_bytes)
            
            print(f"[-] Saved image {image_index + 1} in page {i + 1}")

def __run__(input_files_path_spec: List[Path], output_files_path_spec: List[Path] | None = None, prompt: str | None = None):

    if len(output_files_path_spec) != 1:
        raise ValueError("You must specify exactly one output folder")

    for pdf in input_files_path_spec:
        if not pdf.is_file():
            raise ValueError(f"Input file {pdf} does not exist")
        extract_images_from_pdf(pdf, output_files_path_spec[0])


def __doc__(): # type: ignore
    print("This module extracts all images from the PDF file and saves them to the specified folder. The images are saved with the following naming convention: image_Page_{page_number}_{image_number}.{image_extension}")