"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def read_fem_resp(dct_file='2002FemResp.dct',
                  dat_file='2002FemResp.dat.gz'):
    """Reads the female respondents data.

    :param str dct_file: stata dictionary file name
    :param str dat_file: dat file name
    :returns: female respondents data
    :rtype: pandas.DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    data = dct.ReadFixedWidth(dat_file, compression='gzip')
    return data


def validate_pregnums(resp_data):
    """Checks if pregnum in respondents file equals number of pregnancies from pregnancies file.

    :param pandas.DataFrame resp_data: female respondents data
    :return: True if numbers of pregnancies match, otherwise False
    :rtype: bool
    """
    preg_data = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg_data)
    resp_pregnum = resp_data[['caseid', 'pregnum']].copy()
    resp_pregnum['pregs_list_len'] = resp_pregnum.caseid.map(lambda x: len(preg_map[x]))
    errors = resp_pregnum[resp_pregnum['pregnum'] != resp_pregnum['pregs_list_len']]
    print(errors)
    if errors.shape[0] > 0:
        return False
    else:
        return True


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp_data = read_fem_resp()
    resp_pregnums = resp_data.pregnum.value_counts().sort_index()

    assert(len(resp_data) == 7643)
    assert(resp_pregnums[0] == 2610)
    assert(validate_pregnums(resp_data))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
