# import PyPDF2
#
#
path=r'C:\Users\Drastis\Desktop\mic\Magic Item Compendium.pdf'
#
# file = open(path, 'rb')
# fileReader = PyPDF2.PdfFileReader(file,enco)
# print(fileReader.numPages)
# for i in range(fileReader.numPages):
#     page=fileReader.getPage(i)
#     page.getContents()
#     print(page.extractText())
#     input()


from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_string = StringIO()
with open(path, 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for i,page in enumerate(PDFPage.create_pages(doc)):
        interpreter.process_page(page)

# print(output_string.getvalue())


# print(output_string.getvalue()[8500:9500])




list_lines=output_string.getvalue().splitlines()




import re


















import datetime

# line_number=3
# sum=0
for i,line in enumerate(list_lines):
    print(line)
    try:
        if isinstance(datetime.datetime.strptime(line, '%m/%d/%y  %I:%M:%S %p'),datetime.datetime):
            print('-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X\n-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X\n')
            input()

    except:
        ''



    # if i%30 ==0:input()



x='12/21/06   5:16:33 AM'
date_time_obj = datetime.datetime.strptime(x, '%m/%d/%y  %I:%M:%S %p')


if isinstance(datetime.datetime.strptime(x, '%m/%d/%y  %I:%M:%S %p'),datetime.datetime):
    print('ok')

datetime.isdatetime()

isinstance(x,datetime.datetime.strftime(str(x), '%m/%d/%y  %I:%M:%S %p'))


x=[1,2,3,4]
for i in x:
    i+=1
