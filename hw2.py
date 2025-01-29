#!/usr/bin/env python

import re

from typing import Iterable, List


def read_cd(path: str) -> Iterable[List[str]]:
    """Opens a CELEX `.cd` file like it's a CSV."""
    with open(path, "r") as source:
        for line in source:
            yield line.rstrip().split("\\")


def main() -> None:
    target_words = set()  # Just in case there are duplicates.
    efw = read_cd("data/efw.cd")
    emw = read_cd("data/emw.cd")
    epw = read_cd("data/epw.cd")
    for frow, mrow, prow in zip(efw, emw, epw):
        word = frow[1]
        freq = int(frow[3])
        if freq >= 1790:
            continue
        morph = mrow[4]
        if morph != "S":
            continue
        pron = prow[6]
        if not re.match(r"['\"]?sk", pron):
            continue
        target_words.add(word)
    for word in sorted(target_words):
        print(word)


if __name__ == "__main__":
    main()
