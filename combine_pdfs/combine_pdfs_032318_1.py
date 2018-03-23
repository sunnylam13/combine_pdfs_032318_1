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

pdfWriter = PyPDF2.PdfFileWriter() # this is the new pdf temporary file, you will add pages to this

# loop through all the PDF files

for filename in pdfFiles:
	pdfFileObj = open(filename,'rb') # read in binary mode
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	# loop through all the pages (except the first) and add them
	for pageNum in range(1,pdfReader.numPages): # cycle through all pages except the first which is n = 0, hence start at n = 1
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)

# TODO:  save the resulting PDF to a file

