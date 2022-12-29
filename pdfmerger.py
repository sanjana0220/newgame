from PyPDF2 import PdfMerger
pdfs=["1st sem.pdf","2nd sem.pdf","3rd sem.pdf"]
merger = PdfMerger()

for pdf in pdfs:
  merger.append(pdf)
merger.write("merged.pdf")
merger.close()