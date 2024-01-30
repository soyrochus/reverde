#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reverde - LLM based, multimodal, conversion tool; transformation of the old to the new
@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""
import base64
import mimetypes
from pathlib import Path
from openai import OpenAI, OpenAIError 

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from load_dotenv import load_dotenv #type: ignore
import os

#set the key from file "openai_key.txt" in the same directory as this file or set the environment variable OPENAI_API_KEY
load_dotenv("openai_api_key.env")


def encode_image_data_url(image_path):
    mime_type, _ = mimetypes.guess_type(image_path)
    if mime_type is None:
        raise ValueError("Could not determine the MIME type of the image")

    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    return f"data:{mime_type};base64,{encoded_string}"


def prompt_for_image(prompt:str, image_path: Path, max_tokens = 3000) -> str:
    """
    Prompt for image using OpenAI API
    See: https://github.com/langchain-ai/langchain/blob/master/cookbook/openai_v1_cookbook.ipynb
    """
    data_url = encode_image_data_url(image_path)
    
    chat = ChatOpenAI(model="gpt-4-vision-preview", max_tokens=max_tokens)
    response = chat.invoke(
    [
        HumanMessage(
            content=[
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": data_url,
                        "detail": "auto",
                            },
                        },
                    ]
                )
            ]
        )
    return response.content #type: ignore

