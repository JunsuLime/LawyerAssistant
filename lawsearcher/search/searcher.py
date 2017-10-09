from lawsearcher.model.lawobject import ADMINISTRATIVE_RULE, AUTONOMOUS_RULE, STATUTE, JUDICIAL_PRECEDENT, PRESCRIPT

import lawsearcher.search.inputreader as reader
import lawsearcher.search.crawler as crawler
import lawsearcher.search.pdfeditor as editor


def search(option, *, file=None, string=None):

    requests = None

    # build objected requests
    if file is not None:
        if option is STATUTE:
            requests = reader.read_statute_file(file)
        elif option is JUDICIAL_PRECEDENT:
            requests = reader.read_judicial_precedent_file(file)
    if string is not None:
        if option is STATUTE:
            requests = reader.read_statute_string(string)
        elif option is JUDICIAL_PRECEDENT:
            requests = reader.read_judicial_precedent_string(string)

    if requests is None:
        # TODO: 2017.10.08 raise customized exception
        raise Exception

    # crawling is done
    files, not_crawled_list = crawler.get_judicial_precedents(requests)

    response_file = editor.merge_pdf_list(files)

    return response_file, not_crawled_list


"""
file or request string
==
LawRequest object
==
pdf files and not crawled item list
==
result file path, exception list
"""


