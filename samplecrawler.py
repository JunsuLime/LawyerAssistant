from bs4 import BeautifulSoup
import urllib.request
import urllib.parse


"""
S Helper

1) crawling case
2) manufacture text
3) text to pdf
"""

sample_url = "http://law.go.kr/precSc.do?menuId=3&query=2016도18941"
# sample_url = "http://law.go.kr/precSc.do?menuId=3&query=2016%EB%8F%8418941"


def find_case(case_number):
    """

    :param case_number:
    :return:
    """
    print(sample_url)
    print(urllib.parse.quote("2016도18941"))

    # using urllib, find case related html file
    fp = urllib.request.urlopen(sample_url)
    print(fp.read())
    # get case from html file
    beautifulsoup_obj = BeautifulSoup(fp.read(), "html.parser")
    # use this beautifulsoup_obj, find wanted text
    text = beautifulsoup_obj.get_text
    return text


def prettify_text(text):
    """

    :param text:
    :return:
    """
    pass

import json
import urllib.request
from bs4 import BeautifulSoup

class Scraper(object):
    def __init__(self):
        pass

    def scrape(self):
        law_cases = self.scrape_case()
        for law_case in law_cases:
            print(law_case)

    def scrape_case(self, scrap_case):
        query = {}
        details = urllib.parse.urlencode(query)
        details = details.encode()
        request_url = "http://law.go.kr"
        req = urllib.request.Request(request_url, details)
        # req.add_header(None, None) # key, value

        response = urllib.request.urlopen(req).read().decode()

        print(response)

from urllib import request, parse

if __name__ == "__main__":
    request_url = "http://law.go.kr/precScListWideR.do"
    case_number = "2015다18367"
    body = {"q": case_number, "section": "evtNm", "pg": 1, "outmax": 1}
    body = parse.urlencode(body).encode()

    pre_request = urllib.request.Request(request_url, data=body)
    response = urllib.request.urlopen(pre_request)

    result = response.read().decode()

    soup = BeautifulSoup(result, "html.parser")
    # print(soup.prettify())
    print(soup.div.ul.li["id"])

    mixed_precseq = soup.div.ul.li["id"]
    precseq = mixed_precseq[7:]
    print(precseq)

    request_url = "http://law.go.kr/precInfoR.do"
    body = {"vSct": "2015다18367", "precSeq": int(precseq)}
    body = parse.urlencode(body).encode()

    final_request = urllib.request.Request(request_url, data=body)
    response = urllib.request.urlopen(final_request)

    result = response.read().decode()
    soup = BeautifulSoup(result, "html.parser")
    print(soup.prettify())


