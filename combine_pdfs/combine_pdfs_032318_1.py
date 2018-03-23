# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 combine_pdfs_032318_1.py

import PyPDF2, os

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

# get all the pdf filenames

pdfFiles = []

for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)

pdfFiles.sort(key/str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# TODO:  loop through all the PDF files

# TODO:  loop through all the pages (except the first) and add them

# TODO:  save the resulting PDF to a file

