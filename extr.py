#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import pandas as pd
import sys
import patoolib
import re
import pdb
from os import listdir
from os.path import isfile, join, isdir
import shutil
import stat
import glob

main_path = os.path.join(currentFolder,'STC_Kuwait_POD')
log_path = os.path.join(currentFolder,'STC_Kuwait_POD_Logs')

def clear_dir(input_path):
    if os.path.exists(input_path):
        for files in os.listdir(input_path):
            path = os.path.join(input_path, files)
            os.chmod(path, stat.S_IWRITE)
            try:
                shutil.rmtree(path)
    
            except OSError:
                os.remove(path)
        os.chmod(input_path, stat.S_IWRITE)
        shutil.rmtree(input_path)

#Creat logs path and move logs.xlsx
os.mkdir(log_path)
shutil.move(src_log_path, log_path)
   
#Creat main path and move invoices
os.mkdir(main_path)
shutil.move(src_path, main_path)


# extarct files rar or zip
def extracting_files(zippedFile, toFolder):
    try:
        print("Extracting file =====> " + str(zippedFile) + " dir ======> " + toFolder)

        patoolib.extract_archive(zippedFile, outdir=toFolder)
        os.remove(zippedFile)
    except Exception as e:
        print("Could not process " + zippedFile + " now retrying")
        print(sys.exc_info()[1])

        pass
    for root, dirs, files in os.walk(toFolder):
        for filename in files:
            if re.search(r'\.zip$', filename) or re.search(r'\.bz2$', filename) or \
                    re.search(r'\.tar$', filename) or re.search(r'\.gz$', filename) or \
                    re.search(r'\.arc$', filename) or re.search(r'\.arj$', filename) or \
                    re.search(r'\.z$', filename) or re.search(r'\.rar$', filename):
                fileSpec = os.path.join(root, filename)
                extracting_files(fileSpec, root)


extracting_files(main_path, main_path)


# Get file path
def get_file_path(input_path, file_keyword):
    list_of_file = []
    for root, dirs, files in os.walk(input_path):
        try:
            for filename in files:
                if filename.startswith(file_keyword):
#                if re.search(file_keyword, filename):
                    file_found = os.path.join(root, filename)
                    list_of_file.append(file_found)
                    return list_of_file
        except:
            list_of_file = []
            return list_of_file



# get sub-folder path
list_subfolders_paths = [f.path for f in os.scandir(main_path) if f.is_dir()]
sub_folder = list_subfolders_paths[0]

onlyfiles = [f for f in listdir(sub_folder) if isfile(join(sub_folder, f))]

# check file exists function
def file_exists(files_list,start_part):
    # val = any(string.startswith(name_part) in string for string in files_list)
    val = any(string.startswith(start_part) for string in files_list)
    return val

# Get file path
def get_file_path(input_path,file_keyword):
    list_of_file = []
    for root,dirs,files in os.walk(input_path):
        try:
            for filename in files:
                if filename.startswith(file_keyword):
                    file_found = os.path.join(root,filename)
                    list_of_file.append(file_found)
        except:
            list_of_file = list_of_file
        return list_of_file

# check each file one by one
summary_flag1 = file_exists(onlyfiles,'Summary')
summary_flag2 = file_exists(onlyfiles,'summary')
flag01 = file_exists(onlyfiles,'01')
flag02 = file_exists(onlyfiles,'02')
flag03 = file_exists(onlyfiles,'03')
flag04 = file_exists(onlyfiles,'04')
flag05 = file_exists(onlyfiles,'05')
flag06 = file_exists(onlyfiles,'06')
flag07 = file_exists(onlyfiles,'07')

# check folder folder_structure
if (summary_flag1 or summary_flag2) and flag01 and flag02 and flag03 and flag04 and flag05 and flag06 and flag07:
    folder_structure = "valid"
else:
    folder_structure = "invalid"

message = ""
if folder_structure == "invalid":
    if not (summary_flag1 or summary_flag2):
        message = "Missing Invoice Summary excel file"
    if not flag01:
        if not message:
            message = "Missing Coverage Sites pdf file"
        else:
            message = message + "; Missing Coverage Sites pdf file"
    if not flag02:
        if not message:
            message = "Missing Contract Attachment pdf file"
        else:
            message = message + "; Missing Contract Attachment pdf file"
    if not flag03:
        if not message:
            message = "Missing Quotation pdf file"
        else:
            message = message + "; Missing Quotation pdf file"

    if not flag04:
        if not message:
            message = "Missing Acceptance pdf file"
        else:
            message = message + "; Missing Acceptance pdf file"

    if not flag05:
        if not message:
            message = "Missing Penalty analysis pdf file"
        else:
            message = message + "; Missing Penalty analysis pdf file"

    if not flag06:
        if not message:
            message = "Missing Invoice pdf file"
        else:
            message = message + "; Missing Invoice pdf file"

    if not flag07:
        if not message:
            message = "Missing Full view report excel file"
        else:
            message = message + "; Missing Full view report excel file"
else:
    message = "All files available"

# Get attachment files path
if folder_structure == "valid":
    paths_01 = get_file_path(sub_folder,"01")
    paths_02 = get_file_path(sub_folder,"02")
    paths_03 = get_file_path(sub_folder,"03")
    paths_04 = get_file_path(sub_folder,"04")
    paths_05 = get_file_path(sub_folder,"05")
    paths_06 = get_file_path(sub_folder,"06")
    path_06 = paths_06[0]
    paths_07 = get_file_path(sub_folder,"07")
    
    invoice_paths = paths_04 + paths_05 + paths_06 + paths_07
    other_paths = paths_05 + paths_06 + paths_07

    list_summary_upper = get_file_path(sub_folder,"Summ")
    list_summary_lower = get_file_path(sub_folder,"summ")
    if not list_summary_upper:
        summary_files_list = list_summary_lower
    elif not list_summary_lower:
        summary_files_list = list_summary_upper
    summary_file = summary_files_list[0]
    
# check file exists function

pathLogs = glob.glob(log_path+ "/*.xlsx")[0]


