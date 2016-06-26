## Abstract

This project is about a special standalone of MAR whose try get a footprint of each program memory debug. The implementation is based on the core of [`mar`](https://gitlab.com/ryukinix/mar) as the lib to handle all the information.

## Getting Start

```
sudo apt-get install python3-pip
pip3 install setuptools
pip3 install -r requirements.txt
```

## Command Line Interface
```
[lerax@starfox λ mar-footprint (master)]$ python footprint.py --help
usage: footprint.py [-h] [-t TARGET] [-l LONG] [-i INTERVAL] csvs [csvs ...]

Read malloc-free pairs CSVs from debugmalloc program,do a sequence of stats
processing to processing data.On the final of processing, get a summarization
and put on new CSV.Beyond that, the user can choice by CLI to save or show
graphs. v0.5.2 Developed by Manoel Vilela on Federal University of Pará as
Student Researcher at 2016

positional arguments:
  csvs                  The list of pair malloc_0x.csv free_0x separated by
                        spaces or a dir

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        The path (can be a folder name or path) to save the
                        output
  -l LONG, --long-range LONG
                        The long range range like [x, y] (closed-range) or (a,
                        b) (open-range) to labelize the allocation time. Use
                        +inf or -inf to handle infinite intervals like (-inf,
                        +inf) will get all allocations
  -i INTERVAL, --interval INTERVAL
                        The interval number to count longs on streaking rows
```

# Author