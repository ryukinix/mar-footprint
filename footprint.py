#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © Manoel Vilela
#
#    @project: Memory Analysis Report Footprint
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
#

from tqdm import tqdm
import pandas as pd
import mar


__version__ = '0.1'
__date__ = '2016'
__author__ = 'Manoel Vilela'
__email__ = 'manoel_vilela@engineer.com'
__url__ = 'https://gitlab.com/ryukinix/mar-footprint'


def count_stack(dataframe, interval):
    global_stack = dict(free=[],
                        malloc=[],
                        total=[])
    local_stack = dict(free=0, malloc=0)
    operations = tqdm(enumerate(dataframe.type),
                      total=len(dataframe.index))

    for i, operation in operations:
        if (i + 1) % interval == 0:
            if global_stack['total']:
                last_edge = global_stack['total'][-1]
            else:
                last_edge = 0 
            global_stack['free'].append(local_stack['free'])
            global_stack['malloc'].append(local_stack['malloc'])
            diff = local_stack['malloc'] - local_stack['free']
            global_stack['total'].append(last_edge + diff)
            local_stack['free'], local_stack['malloc'] = 0, 0

        if operation == 'free':
            local_stack['free'] += 1
        elif operation == 'malloc':
            local_stack['malloc'] += 1

    return pd.DataFrame(global_stack)


def main():
    mar.cli.minimal()  # load the minimal cli from mar
    mar.cli.graph()
    options = mar.cli.parser.parse_args()  # get the options
    csvs = mar.utils.walk(options.csvs)  # load csvs
    groups = mar.processing.group(csvs)  # group each free malloc
    dfs = mar.processing.parse(groups, nil=True)   # parse csv to dataframe
    merged = (mar.processing.merge(m, f).sort_values('time')
              for m, f in dfs)  # merge free and mallocs ordering by time
    mean = mar.processing.mean(merged, total=len(groups), by='time')
    output = count_stack(mean, options.interval) # count the free and mallocs
    basename = mar.utils.get_firstname(csvs[0])  # get the basename 
    mar.graph.plot_save(output, basename, options)  # plot and/or save image
    mar.utils.save_csv(output, basename, options)  # save csv

if __name__ == '__main__':
    main()
