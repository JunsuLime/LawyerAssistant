from lawsearcher.model.lawobject import JudicialPrecedent

def read_statute_file(file):
    pass


def read_statute_string(request_string):
    pass


def read_judicial_precedent_file(file):
    raw_requests = file.read().decode()

    requests = list()
    for raw_request in raw_requests.split('\r\n'):
        j = JudicialPrecedent(raw_request)
        requests.append(j)

    return requests

def read_judicial_precedent_string(request_string):
    pass
