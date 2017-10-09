import os
import urllib.request
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

from lawsearcher.model.lawobject import *
from lawsearcher.search import BASE_TMP_PATH

PRECSEQ_REQUEST_URL = "http://law.go.kr/precScListWideR.do"
PDF_REQUEST_URL = "http://law.go.kr/precPdfPrint.do"


def get_judicial_precedents(law_list):
    files = list()
    not_crawled_list = list()

    for law in law_list:
        result = crawl_judicial_pdf(law.code)
        files.append(result)
        # try:
        #     result = crawl_judicial_pdf(code)
        #     files.append(result)
        #     pass
        # # TODO: deal exception with customized exception - ex) NotFoundedException
        # except Exception as e:
        #     print(e)

    return files, not_crawled_list


def get_crawling_result(law_list):
    files = list()
    not_crawled_list = list()

    for l in law_list:
        if isinstance(l, JudicialPrecedent):
            pass
        elif isinstance(l, Statute):
            pass

    return files, not_crawled_list


def crawl_judicial_pdf(code):
    precseq = __get_judicial_precseq(code)
    result = __get_judicial_pdf(precseq)

    file_name = "%s.pdf" % code

    result_file = open(os.path.join(BASE_TMP_PATH, file_name), "w+b")
    result_file.write(result)

    return result_file


def __get_judicial_precseq(code):
    print("__get_judicial_precseq is called with code: " + code)
    body = {"q": code, "section": "evtNm", "pg": 1, "outmax": 1}
    body = urllib.parse.urlencode(body).encode()

    precseq_request = urllib.request.Request(PRECSEQ_REQUEST_URL, data=body)
    response = urllib.request.urlopen(precseq_request)

    result = response.read().decode()

    soup = BeautifulSoup(result, "html.parser")

    mixed_precseq = soup.div.ul.li["id"]
    precseq = mixed_precseq[7:]
    return precseq


def __get_judicial_pdf(precseq):
    print("__get_judicial_pdf is called with precseq: " + precseq)
    body = {"precSeq": int(precseq), "conJo": "1,2,3,4,5,6,7,8"}
    body = urllib.parse.urlencode(body).encode()

    pdf_request = urllib.request.Request(PDF_REQUEST_URL, data=body)
    response = urllib.request.urlopen(pdf_request)

    return response.read()
