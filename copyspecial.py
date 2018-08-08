#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse
import zipfile
from pprint import pprint

"""Copy Special exercise
"""

def get_special_paths(directory):
    special_list = []
    dirlist = os.listdir(directory)
    for files in dirlist:
        special = (str(re.findall(r"\w+__\w+__.\w+", files))[2:-2])
        if len(special) >= 1:
            pathway = os.path.abspath(special) 
            special_list.append(pathway)
    # print pathway
    return special_list

def copy_to(paths, dir):
    for path in paths:
        if os.path.exists(dir):
            shutil.copy(path,dir)
        else:
            os.makedirs(dir)
            shutil.copy(path,dir)

def zip_to(paths, zippath):
    string = ""
    with zipfile.ZipFile(zippath, 'w') as zip:
        for file in paths:
            string += " " +file
            zip.write(file)
        
    command = "zip -j " + zippath + string
    print "command im going to do: " 
    print command

def main(args = None):

    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='get all special files from whatever directory is specified after the --fromdir flag')
    args = parser.parse_args()
    print args
    special_files_list = get_special_paths('.')
    if args.fromdir:
         get_special_paths(args.fromdir)

    if args.todir:
        copy_to(special_files_list, args.todir)
        print "copy success"
        
    if args.tozip:
        zip_to(special_files_list, args.tozip)

   
if __name__ == "__main__":
    main(sys.argv[1:])
