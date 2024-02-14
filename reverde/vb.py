
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
from reverde.api import prompt_for_image, prompt_for_image

"""Needs to run:

reverde.ps1 -c vb -i D:\\src\\almancenesfundacion\\images\\Customer.png d:\\src\\almacenesfundacion

"""

def __run__(input_files_path_spec: List[Path], output_files_path_spec: List[Path] | None = None, prompt: str | None =None):
    
    prompt = """The image is from an VB6 form, showing one record.  Based on the displayed fields, generate a definition for a JDL (JHipter Data Language) definition for a JHipster entity. """
    #response = prompt_for_image(prompt, input_files_path_spec[0])
    response = prompt_for_image(prompt, input_files_path_spec[0])
    print(response)


def __doc__(): # type: ignore
    print("This module will use the OpenAI API to generate a Jphipster scaffold of an Entity based in image interpretation")