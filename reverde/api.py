#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reverde - LLM based, multimodal, conversion tool; transformation of the old to the new
@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""
from openai import OpenAI, OpenAIError 
import load_dotenv #type: ignore
import os

try:
    #set the key from file "openai_key.txt" in the same directory as this file or set the environment variable OPENAI_API_KEY
    load_dotenv("openai_api_key.env")
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
except OpenAIError as e:
    print(e)
    exit(1) 

