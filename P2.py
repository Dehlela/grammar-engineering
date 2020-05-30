import nltk
from nltk import FeatureChartParser

fcfg = nltk.data.load('P2.fcfg')
parser = FeatureChartParser(fcfg)


def parse_text(text):
    examples = text.splitlines()
    count = 0
    for sent in examples:
        count = count + 1
        print("[", count, "]", sent)
        parses = parser.parse(sent.split())
        i = 1
        for tree in parses:
            print(i, "\n", tree)
            print("\n")
            i = i + 1


def parse_file(name):
    f = open(name, 'r')
    text = f.read()
    f.close()
    parse_text(text)


print("================ Positive examples ================")
parse_file('P2.pos')
print("================ Negative examples ================")
parse_file('P2.neg')
