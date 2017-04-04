import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import urllib.request


"""
S Helper

1) crawling case
2) manufacture text
3) text to pdf
"""

def get_precseq(case):
    request_url = "http://law.go.kr/precScListWideR.do"
    body = {"q": case, "section": "evtNm", "pg": 1, "outmax": 1}
    body = urllib.parse.urlencode(body).encode()

    precseq_request = urllib.request.Request(request_url, data=body)
    response = urllib.request.urlopen(precseq_request)

    result = response.read().decode()

    soup = BeautifulSoup(result, "html.parser")
    # print(soup.prettify())
    print(soup.div.ul.li["id"])

    mixed_precseq = soup.div.ul.li["id"]
    precseq = mixed_precseq[7:]
    return precseq

def get_pdf(precseq):
    request_url = "http://law.go.kr/precPdfPrint.do"
    body = {"precSeq": int(precseq), "conJo": "1,2,3,4,5,6,7,8"}
    body = urllib.parse.urlencode(body).encode()

    pdf_request = urllib.request.Request(request_url, data=body)
    response = urllib.request.urlopen(pdf_request)

    result = response.read()

    return result

FILE_NAME = "sample{0}.pdf"

if __name__ == "__main__":

    case_numbers = ["2015다18367", "2016도19027", "2014다230535"]
    count = 0
    for case in case_numbers:
        file_name = FILE_NAME.format(count)
        count += 1
        precseq = get_precseq(case)
        pdf_string = get_pdf(precseq)

        pdf_file = open(file_name, 'wb')
        pdf_file.write(pdf_string)

        pdf_file.close()
