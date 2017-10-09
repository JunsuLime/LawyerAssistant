import os
from lawsearcher import app

# test case
from lawsearcher.model.lawobject import *
from lawsearcher.search.searcher import search

SAMPLE_JUDICIAL_PRECEDENTS_FILE_NAME = "sample_judicial_precedents.txt"

if __name__ == "__main__":
    # app.run()

    # judicial precedent test case

    base_path = os.path.join("./tmp")
    access_path = os.path.join(base_path, SAMPLE_JUDICIAL_PRECEDENTS_FILE_NAME)

    with open(access_path, "rb") as f:
        result1, result2 = search(JUDICIAL_PRECEDENT, file=f)
        print(result1, result2)
