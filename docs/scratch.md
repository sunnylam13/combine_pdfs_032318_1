# Scratch Notes and Log

## Friday, March 23, 2018 2:55 PM

Program actions...

* find all pdf files in the current working directory (cwd)

* sort the filenames so the PDFs are added in order

* write each page, excluding the first page, of each PDF to the output file

what the code should do...

* call `os.listdir()` to find all files in cwd and remove non-pdf files

* call python `sort()` to alpha order the filenames

* create `PdfFileWriter` object for output PDF

* loop over each pdf file, create a `PdfFileReader` object for it

* loop over each page (except first) in each pdf file

* add pages to output pdf

* write output pdf to a file `combinedminutes.pdf`

