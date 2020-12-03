#!/usr/bin/env python

import argparse
import sys
import csv


fields = [
    'office',
    'district',
    'candidate',
    'party',
    'reporting_level',
    'jurisdiction',
    'votes',
]


def parse_raw_csv(infile, outfile, district):
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fields)

    candidates = reader.fieldnames

    writer.writeheader()
    for row in reader:
        for candidate in candidates[1:]:
            writer.writerow({
                'office': "State House",
                'district': district,
                'candidate': candidate,
                'party': "",
                'reporting_level': "County",
                'jurisdiction': row['County'],
                'votes': row[candidate],
            })


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("infile", nargs='?', type=argparse.FileType('r'),
                            default=sys.stdin, help="input filename")
    arg_parser.add_argument("outfile", nargs='?', type=argparse.FileType('w'),
                            default=sys.stdout, help="output filename")

    args = arg_parser.parse_args()

    parse_raw_csv(args.infile, args.outfile, 4)
