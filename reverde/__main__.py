
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reverde - LLM based, multimodal, conversion tool; transformation of the old to the new
@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""
import argparse
import importlib
import os
from pathlib import Path
import sys
from typing import List
  
PLUGIN_PATH = "REVERDE_PLUGINS_PATH"
REVERDE_DESCRIPTION = "Reverde - LLM based, multimodal, conversion tool; transformation of the old to the new"
COPYRIGHT_MESSAGE = "Copyright © 2024 Iwan van der Kleijn. Released under the MIT License."
  
# Check if a module can be imported
def module_exists(module_name):
    spec = importlib.util.find_spec(module_name)
    return spec is not None

def convert_spec_to_path(str_list: List[str]) -> List[Path]:
    path_list = [Path(path_str) for path_str in str_list]
    return path_list

def load_module(module_name):
  if not module_exists(module_name):
      module_name = "reverde." + module_name
  return importlib.import_module(module_name)
  
def doc(conversion_type):
    # Load the module dynamically
    try:
      module = load_module(conversion_type)
      module.__doc__()
     
    except ModuleNotFoundError:
        print(f"Conversion type or processor '{conversion_type}' not found")
        sys.exit(1)
    

def run(args):
  # Dynamically load the module with the specified conversion type
    try:
        module = load_module(args.conversion_type[0])
        prompt = args.prompt[0] if args.prompt else None
        in_paths = convert_spec_to_path(args.input_files_path_spec)
        out_paths = convert_spec_to_path(args.output_files) if args.output_files else None  
        module.__run__(in_paths, out_paths, prompt)
        
    except ModuleNotFoundError:
        print(f"Conversion type or processor '{args.conversion_type}' not found")
        sys.exit(1)
            
def main():
    #Allow import of modules if PLUGIN_PATH (tpuically "REVERDE_PLUGINS_PATH") is set
    if PLUGIN_PATH in os.environ:
      sys.path.append(os.path.dirname(os.environ[PLUGIN_PATH]))
  
    # Create an argument parser
    parser = argparse.ArgumentParser(prog='reverde', 
                                     description=REVERDE_DESCRIPTION,
                                     epilog=COPYRIGHT_MESSAGE)

    # Add the command line arguments
    parser.add_argument('-p', '--prompt', nargs=1, help='Optional prompt to send to the AI (LLM)')
    parser.add_argument('-c', '--conversion_type', nargs=1, help='Conversion type (processor name)')
    parser.add_argument('-i', '--input_files_path_spec', nargs='*', help='Input files path specification')
    parser.add_argument('-o', '--output_files', nargs='*', help='Output files path specification')
    
    # Add the mutually exclusive help argument
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--doc', nargs=1, help='Show conversion_type documentation')
    
    # Parse the command line arguments
    args = parser.parse_args()
    
    if args.doc:
      doc(args.doc[0])
    elif not args.conversion_type:
      parser.error("conversion_type is required unless --doc is specified")
    elif not args.input_files_path_spec:
      parser.error("input_files_path_spec is required unless --doc is specified")
    else:
      run(args)
    
if __name__ == "__main__":
  main()
  
   