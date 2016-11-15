#!/usr/bin/env python

import first
import nsfg
import thinkplot
import thinkstats2

def PmfMean(pmf):
	mean = 0.0
	for x,p in pmf.d.items():
		mean = mean + p * x
	return mean

def PmfVar(pmf):
	var = 0.0
	mean = PmfMean(pmf)
	for x,p in pmf.d.items():
		diff2 = (x - mean) ** 2
		var = var + p * diff2
	return var


def PairwiseDiff(live):
	preg_map = nsfg.MakePregMap(live) 
	diffs = []
	for caseid, children in preg_map.items():
		if len(children) >= 2:
			preg_lengths = live.loc[children].prglngth.values
			first = preg_lengths[0]
			rest = preg_lengths[1:]
			diffs.extend( [ first - r for r in rest ] )
	return diffs


def main():
	live,firsts,others = first.MakeFrames()	
	diffs = PairwiseDiff(live)
	mean = thinkstats2.Mean(diffs)
	print('Mean: ',mean)
	pmf = thinkstats2.Pmf(diffs)
	thinkplot.Hist(pmf)
	thinkplot.Show(xlabel='Diff in wks',ylabel='PMF')

if __name__ == '__main__':
	main()
