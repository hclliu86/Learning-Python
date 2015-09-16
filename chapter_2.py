# -*- coding: UTF-8 -*-
__author__ = 'liuhc'
import json
from collections import defaultdict
from collections import Counter
from pandas import DataFrame, Series
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

path = r'C:\Users\hcl_l_000.LIUHC\Documents\My libs\Data analysis with python\ch02\usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
def get_counts(seqence):
    counts = defaultdict(int)
    for x in seqence:
        counts[x] += 1
    return counts

def top_counts(count_dict, n= 10):
    value_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_pairs.sort()
    return value_pairs[-n:]

def top_counts2(count_dict, n=10):
    counts = Counter(count_dict)
    return counts.most_common(n)

frame = DataFrame(records)
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windws')
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
