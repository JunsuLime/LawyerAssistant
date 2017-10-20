import os

from PyPDF2 import PdfFileReader, PdfFileWriter
from lawsearcher.search import BASE_TMP_PATH


def merge_pdf_list(pdf_files):
    if pdf_files is None:
        return None

    if len(pdf_files) == 1:
        return pdf_files[0]

    base_pdf_writer = PdfFileWriter()
    for file in pdf_files:
        __append_pdf(base_pdf_writer, PdfFileReader(file))

    file_name = "%s_외_%d개.pdf" % (os.path.join(BASE_TMP_PATH, pdf_files[0].name[:-4]), len(pdf_files) - 1)

    file = open(file_name, "wb")
    base_pdf_writer.write(file)

    return file


def __append_pdf(base_pdf, merged_pdf):
    [base_pdf.addPage(merged_pdf.getPage(page_num)) for page_num in range(merged_pdf.numPages)]
