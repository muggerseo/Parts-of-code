from PyPDF2 import PdfFileMerger
import os


merger = PdfFileMerger()
for item in os.listdir():
    if item.endswith('.pdf'):
        merger.append(item)
merger.write("Final_pdf.pdf")
merger = PdfFileMerger()
with open(originalFile, 'rb') as fin:
    merger.append(PdfFileReader(fin))
os.remove(originalFile)
merger.close
