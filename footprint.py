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


def slices(csvs, interval):
    pass


def count_stack(csvs):
    pass


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
    output = mar.processing.count_stack(slices) # count the free and mallocs by time

    basename = mar.utils.get_firstname(csvs[0])
    mar.graph.plot_save(output, basename, options)
    mar.utils.save_csv(output, basename, options)

if __name__ == '__main__':
    main()
