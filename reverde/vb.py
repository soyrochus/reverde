
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reverde - LLM based, multimodal, conversion tool; transformation of the old to the new
@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""
import os
from pathlib import Path
from typing import List
import os
from reverde.api import prompt_for_image

"""Needs to run:

reverde.ps1 -c vb -i D:\\src\\almancenesfundacion\\images\\Customer.png d:\\src\\almacenesfundacion

"""
# def __run__(input_files_path_spec: List[Path], output_files_path_spec: List[Path] = None, prompt: str=None):
#     print(f"Generating Jhipster scaffold based on D:\\src\\almancenesfundacion\\images\\Customer.png to d:\\src\\almacenesfundacion")
    
    
#     print("Sending prompt...")
#     # Wait for 4 seconds
#     time.sleep(4)

#     # Change directory
#     os.chdir("D:/src/almancenesfundacion")

#     # Write the customer.jdl file
#     jdl_content = """
# entity Customer {
#   address String required,
#   city String required,
#   companyName String required,
#   contactName String required,
#   contactTitle String required,
#   country String required,
#   customerID String required,
#   fax String,
#   phone String required,
#   postalCode String required,
#   region String
# }

# dto Customer with mapstruct
# service Customer with serviceClass
# paginate Customer with pagination
# """
#     with open("customer.jdl", "w", encoding="utf-8") as file:
#         file.write(jdl_content)

#     # Extend PATH environment variable
#     os.environ["PATH"] = "D:\\apps\\jdk-21.0.1\\bin;D:\\apps\\node-v20.10.0-win-x64;" + os.environ["PATH"]

#     # Execute the command
#     process = subprocess.Popen("jhipster --force import-jdl customer.jdl", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = process.communicate()

#     # Print output and error (if any)
#     print(stdout.decode())
#     if stderr:
#         print("Error:", stderr.decode())

def __run__(input_files_path_spec: List[Path], output_files_path_spec: List[Path] | None = None, prompt: str | None =None):
    
    prompt = """The image is from an VB6 form, showing one record.  Based on the displayed fields, generate a definition for a JDL (JHipter Data Language) definition for a JHipster entity. """
    response = prompt_for_image(prompt, input_files_path_spec[0])
    print(response)


def __doc__(): # type: ignore
    print("This module will use the OpenAI API to generate a Jphipster scaffold of an Entity based in image interpretation")