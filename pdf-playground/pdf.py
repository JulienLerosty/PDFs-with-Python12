from re import template
import PyPDF2
import sys

inputs = sys.argv[1:]


#CombinePDFs
def pdf_combiner(pdf_list):
  merger = PyPDF2.PdfMerger()
  for pdf in pdf_list:
    print(pdf)
    merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(inputs)

with open('dummy.pdf', 'rb') as file:
  print(file)
  reader = PyPDF2.PdfReader(file)
  page = reader.pages[0]
  print(len(reader.pages))
  page.rotate(90)
  writer = PyPDF2.PdfWriter()
  writer.add_page(page)

with open('tilt.pdf', 'wb') as new_file:
  writer.write(new_file)

#Watermark super.pdf
template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
  page = template.pages[i]
  page.merge_page(watermark.pages[0])
  output.add_page(page)

  with open('watermarked.pdf', 'wb') as file:
    output.write(file)
