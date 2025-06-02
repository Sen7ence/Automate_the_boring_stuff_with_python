import PyPDF2

pdfFileObj = open(r"hy\13\meetingminutes.pdf", "rb")
pdfReader = PyPDF2.PdfReader(pdfFileObj)
print(len(pdfReader.pages))  # 打印PDF文件的页数
