from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    sameline = []
    for line1 in a:
        for line2 in b:
            if line1 == line2:
                sameline.append(line1.rstrip())
    return list(set(sameline))


def sentences(a, b):
    """Return sentences in both a and b"""
    samesent = []
    for sent1 in sent_tokenize(a):
        for sent2 in sent_tokenize(b):
            if sent1 == sent2:
                samesent.append(sent1)
    return list(set(samesent))


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    chunka = []
    chunkb = []
    samesubstring = []
    ## n is the size of the chunk
    for i in a:
        for j in range(0, len(i), n):
            chunka.append(i[j:j+n])
    for k in b:
        for l in range(0, len(k), n):
            chunkb.append(k[l:l+n])
    for m in chunka:
        for o in chunkb:
            if m == o:
                samesubstring.append(m)

    return list(set(samesubstring))
