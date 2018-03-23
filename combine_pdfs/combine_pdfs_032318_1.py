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

pdfFiles.sort(key/str.lower) # list sorted into alpha order with keyword argument

pdfWriter = PyPDF2.PdfFileWriter()

# loop through all the PDF files

for filename in pdfFiles:
	pdfFileObj = open(filename,'rb') # read in binary mode
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# TODO:  loop through all the pages (except the first) and add them

# TODO:  save the resulting PDF to a file

