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
        if special:
            pathway = os.path.abspath(special) 
            special_list.append(pathway)
    return special_list


def copy_to(paths, to_dir):
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for path in paths:
    filename = os.path.basename(path)
    shutil.copy(path, os.path.join(to_dir, filename))
 



def zip_to(paths, zippath):
  cmd = 'zip -j ' + zippath + ' ' + ' '.join(paths)
  print
  print "Command I'm going to do...\n " + cmd
  print
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='list all special files in  dir')

    arguments = sys.argv[1:]

    todir = ''
    if arguments[0] == '--todir':
        todir = arguments[1]
        del arguments[0:2]

    tozip = ''
    if arguments[0] == '--tozip':
        tozip = arguments[1]
        del arguments[0:2]

    if len(arguments) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    paths = []
    for dirname in arguments:
        paths.extend(get_special_paths(dirname))
    if todir:
        copy_to(paths, todir)
    elif tozip:
        zip_to(paths, tozip)
    else:
        print '\n'.join(paths)

   
if __name__ == "__main__":
    main()
