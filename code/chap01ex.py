"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

from collections import defaultdict
import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    #CleanFemPreg(df)
    return df

def MakeRespMap(df):
    """Make a map from caseid to list of preg indices.

    df: DataFrame

    returns: dict that maps from caseid to list of indices into preg df
    """
    d = defaultdict(list)
    for index, caseid in df.caseid.iteritems():
        d[caseid] = index
    return d

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)
    df = nsfg.ReadFemPreg()
    #print(df.pregnum)
    preg_map = nsfg.MakePregMap(df)
    dfr = ReadFemResp()
    resp_map = MakeRespMap(dfr)
    #print(preg_map)
    for caseid in sorted(preg_map):
        preg_count = len(preg_map[caseid])
        
        index = resp_map[caseid]
        numpregs = dfr.numpregs[index]
        if preg_count != numpregs:
            print(caseid, preg_count,numpregs)

if __name__ == '__main__':
    main(*sys.argv)
