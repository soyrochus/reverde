
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reverde - LLM based, multimodal, conversion tool; transformation of the old to the new
@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""

"""
Con Peñazo, los desarrolladores pueden dibujar el esquema de sus interfaces utilizando caracteres ASCII, 
donde cada símbolo y espacio en blanco se traduce directamente en componentes Angular funcionales y estilizados.
Este enfoque no solo hace que la definición de interfaces sea más accesible y menos tediosa (evitando el "peñazo" tradicional)
 sino que también fomenta una rápida prototipación y colaboración entre diseñadores y desarrolladores.

 """

from pathlib import Path
from typing import List
from reverde.api import send_prompt


form = """"

form: 

name: string | required | label: "Name" | placeholder: "Enter your name" | minlength: 3 | maxlength: 20
email: string | required | label: "Email" | placeholder: "Enter your email" | email
password: string | required | label: "Password" | placeholder: "Enter your password" | minlength: 6 | maxlength: 20
button: submit | label: "Submit"

"""

def generate_angular_form(source:str)-> str:

    context = f"""
I need to generate an Angular form from a string that contains the form definition. The form definition is a string that contains the form fields and their properties.
Each field is separated by a pipe character. The properties of each field are separated by a pipe character as well. The properties are key-value pairs separated by a colon. The key is the name of the property and the value is the value of the property. The properties are separated by a pipe character as well.
The form definition string is as follows:

{source}

Generate the Angular form from the form definition string. Focos on the generation of the defintiion of the component view. 
"""
    response = send_prompt(context)
    print(response)


def __run__(input_files_path_spec: List[Path], output_files_path_spec: List[Path] | None = None, prompt: str | None =None):
    
    response = generate_angular_form(form)
    print(response)


def __doc__(): # type: ignore
    print("This module will use the informal Peñazo form definition to generate an Angular form.")