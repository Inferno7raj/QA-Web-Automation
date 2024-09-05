import base64
import os
import pdfplumber
import logging
import pdb


## BASE_DIR holds project's root dir path . Ex. 'C:\\Users\\www.abcom.in\\Desktop\\Demo_project
BASE_DIR = os.getcwd()

## TEST_DATA_DIR parameter holds dir path for json
TEST_DATA_DIR = os.path.join(BASE_DIR, 'data')

## LOG_DIR parameter holds dir path for logs
LOG_DIR = os.path.join(BASE_DIR, 'logs')

## DOWNLOAD_DIR parameter holds dir path for downloads
DOWNLOAD_DIR = os.path.join(BASE_DIR, 'downloads')

## EXCEL_DATA_FILES parameter holds dir path for excel_data_files
EXCEL_DATA_FILES = os.path.join(BASE_DIR, 'excel_data_files')

site_url = "https://opensource-demo.orangehrmlive.com"

username = "QWRtaW4="  # Admin
password = "YWRtaW4xMjM="   # admin123


def decode(input_string):

    decoded_bytes = base64.b64decode(input_string)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string









