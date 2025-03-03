"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    dct = hist.GetDict()
    mode = max(dct, key=dct.get)
    return mode


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    items = hist.Items()
    items_sorted = sorted(items, key=lambda x: x[1], reverse=True)
    return items_sorted


def WeightMeansDiff(firsts, others):
    """Compare mean weight of the first babies and others.

    firsts: DataFrane of first babies
    others: DataFrame of other babies

    returns: tuple with difference of means and Cohen's d
    """
    mean_diff = firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean()
    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    return mean_diff, d


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)

    mean_diff, d = WeightMeansDiff(firsts, others)
    print(f'Difference of means between fists and others: {mean_diff}')
    print(f'Cohen\'s d: {d}')

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
