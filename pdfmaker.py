# This Program will convert '.jpg' images to pdf
import os
import PyPDF2 as pypdf
from PIL import Image

def pdf_conversion(loc):
    image1 = Image.open(fp=loc, mode='r')
    im1 = image1.convert('RGB')
    im1.save(fp='TeMpOrArYfi13.pdf', mode='r')

def main_func():
    files = os.listdir(path)
    for i in files:
        if i.endswith('.jpg')==False:
            continue
        temp = path + '\\' + i
        pdf_conversion(temp)
        pdf_read = pypdf.PdfFileReader('TeMpOrArYfi13.pdf')
        os.remove('TeMpOrArYfi13.pdf')
        p = pdf_read.getPage(0)
        pdf_write.addPage(p)

print("            *****************************************************           ")
print("-------******   Create A Folder And Copy Images To The Folder.  ******-------")
print("-------******    Only '.jpg' File Can Be Converted Into PDF.    ******-------")
print("            *****************************************************           ")
path=input("Enter Path: ")
final=input("Enter Final Product Name [Without extension]: ")+'.pdf'
pdf_write=pypdf.PdfFileWriter()

try:
    main_func()
except FileNotFoundError:
    print("Given path is not valid.")
    exit()

merge_pdf=open(final,'wb')
pdf_write.write(merge_pdf)
print("PDF Creation Successful.")