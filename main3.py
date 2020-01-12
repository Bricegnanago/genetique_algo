#!/usr/bin/python
# -*- coding: latin-1 -*-
from urllib3.connectionpool import xrange


def permutliste(seq, er=False, k=0):
    """retourne la liste de toutes les permutations de la liste seq (récursif)
       si er=True: élimination des répétitions quand seq en a (ex: [1,2,2]
    """
    n = len(seq)
    if k == n - 1:
        return []
    p = []
    z = seq[:]
    for c in xrange(0, n - k):
        if er == False or (z not in p):
            p.append(z[:])
            p.extend(permutliste(z, er, k + 1)[1:])
        z.append(z.pop(k))
    return p


permutliste([1, 2, 3])
