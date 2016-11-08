"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import math
import sys
from operator import itemgetter

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    most_freq_pair = [0,0]
    max_freq = 0
    for p in hist.Items():
        if p[1] > most_freq_pair[1]:
            most_freq_pair = p
            print('mfp:',most_freq_pair)
    return most_freq_pair[0]


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    return sorted(hist.Items(), key = lambda p: -p[1])

def cohen_d(firsts,others):
    n1 = len(firsts)
    n2 = len(others)
    pooled_var = (n1 * firsts.var() + n2 * others.var()) / (n1 + n2)
    S = math.sqrt(pooled_var)
    d = (firsts.mean() - others.mean()) / S

    return d



def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert(mode == 39)

    # test AllModes
    modes = AllModes(hist)
    print(modes)
    assert(modes[0][1] == 4693)

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)
    print("Cohen's d:", cohen_d(firsts.totalwgt_lb,others.totalwgt_lb))


if __name__ == '__main__':
    main(*sys.argv)
