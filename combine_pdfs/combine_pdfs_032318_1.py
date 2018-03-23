# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 combine_pdfs_032318_1.py "../tests/testpdfs"

import PyPDF2, os, sys

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

directory_target = sys.argv[1]

# get all the pdf filenames

pdfFiles = []

for filename in os.listdir(directory_target):
	if filename.endswith('.pdf'):
		pdfFilePath = os.path.join(directory_target,filename)
		# pdfFiles.append(filename)
		pdfFiles.append(pdfFilePath)

pdfFiles.sort(key=str.lower) # list sorted into alpha order with keyword argument

logging.debug('pdf files list after sorting')
logging.debug(pdfFiles)

pdfWriter = PyPDF2.PdfFileWriter() # this is the new pdf temporary file, you will add pages to this

# loop through all the PDF files

for filename in pdfFiles:
	pdfFileObj = open(filename,'rb') # read in binary mode
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	# loop through all the pages (except the first) and add them
	for pageNum in range(1,pdfReader.numPages): # cycle through all pages except the first which is n = 0, hence start at n = 1
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)

# save the resulting PDF to a file

pdfOutput = open('combinedminutes.pdf','wb')
logging.debug('combinedminutes.pdf created and saved')
pdfWriter.write(pdfOutput)
pdfOutput.close()


