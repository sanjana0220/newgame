from PyPDF2 import PdfReader,PdfWriter
chapter1= list(range(5,9))
chapter2=[9,15]
chapter3=[16,24]
with open ("The Da Vinci COde.pdf","rb") as f:
  reader = PdfReader(f)
  c1writer =PdfWriter()
  c2writer=PdfWriter()
  c3writer=PdfWriter()
  for page in range(len(reader.pages)):
    if page in chapter1:
      c1writer.addPage(reader.getPage(page))
    elif page in chapter2:
      c2writer.addPage(reader.getPage(page))
    elif page in chapter3:
      c3writer.addPage(reader.getPage(page))  
  with open  ("chapter1.pdf","wb") as f2:
    c1writer.wirte(f2)
  with open  ("chapter2.pdf","wb") as f2:
    c2writer.wirte(f2)
  with open  ("chapter3.pdf","wb") as f2:
    c3writer.wirte(f2)  
          