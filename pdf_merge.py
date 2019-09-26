import os
import PyPDF2

space = os.listdir()
pdfspace=[]
fileDst = '集合.pdf'
for item in space:
    if((item[-4:] == '.pdf') and (item != fileDst)):
        pdfspace.append(item)
        
print(pdfspace)

def get_num(item):
    num = int(item[0:2])
    return num

def pdf_append(pdf_name):
    
    pdfFile = open(pdf_name,'rb')
    pdfFileReader = PyPDF2.PdfFileReader(pdfFile)
    
    pageStart = 0
    pageEnd = pdfFileReader.getNumPages()

    for pageNum in range(pageStart,pageEnd):
        pagObj = pdfFileReader.getPage(pageNum)
        pdfWriter1.addPage(pagObj)

    
    if pdfOutputFile.mode!=1:
        pdfWriter1.write(pdfOutputFile)
        
    pdfFile.close()

pdf_dic = {}
for item in pdfspace:
    pdf_dic[get_num(item)]=item
# print(pdf_dic)   

pdfOutputFile = open(fileDst,'wb')
pdfWriter1 = PyPDF2.PdfFileWriter()

for num in range(1,len(pdfspace)+1):
    file = pdf_dic[num]
    print(file)
    pdf_append(file)

pdfOutputFile.close()