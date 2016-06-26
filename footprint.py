#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © Manoel Vilela
#
#    @project: Memory Analysis Report Footprint
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
#

import mar
import re
import pandas as pd
from tqdm import tqdm


def count_stack(dataframe, interval):
    global_stack = dict(free=[],
                        malloc=[],
                        total=[])
    local_stack = dict(free=0, malloc=0)
    values = tqdm(enumerate(dataframe.type),
                  total=len(dataframe.index))
    
    for i, allocation in values:
        if (i + 1) % interval == 0:
            last_edge = global_stack['total'][-1]
            global_stack['free'].append(local_stack['free'])
            global_stack['malloc'].append(local_stack['malloc'])
            global_stack['total'].append(last_edge + (local_stack, c))

    return pd.DataFrame(global_stack)
 

def main():
    mar.cli.minimal()  # load the minimal cli from mar
    options = mar.cli.parser.parse_args()  # get the options

    if options.ignore_first:
        options.ignore = re.compile('.*_1.csv')

    csvs = mar.utils.walk(options.csvs, options.ignore)  # load csvs
    groups = mar.processing.group(csvs)  # group each free malloc
    dfs = mar.processing.parse(groups, nil=True)   # parse csv to dataframe
    merged = (mar.processing.merge(m, f).sort_values('time')
              for m, f in dfs)  # merge free and mallocs ordering by time
    mean = mar.processing.mean(merged, by='time')  # mean of dataframes by time
    slices = mar.procesing.slices(mean, options.interval)  # get slices
    output = mar.processing.count_stack(slices) # count the free and mallocs

    basename = mar.utils.get_firstname(csvs[0]) # get the basename 
    mar.graph.plot_save(output, basename, options)  # plot and/or save image
    mar.utils.save_csv(output, basename, options)  # save csv

if __name__ == '__main__':
    main()
