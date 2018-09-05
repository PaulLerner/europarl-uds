# -*- coding: utf-8 -*-
# Extracts monolingual corpus from sentence-split XML

import glob
import sys
from lxml import etree
import xml.etree.ElementTree as ET
import codecs
import argparse
import os
from os.path import isfile, join


def create_arg_parser():
    """"Creates and returns the ArgumentParser object."""
    parser = argparse.ArgumentParser(description='Extract sentence-split raw text from EPIC.')
    parser.add_argument('inputDirectory',
                    help='Path to the input directory.')
    parser.add_argument('outputDirectory',
                    help='Path to the output directory.')
    return parser

def extract_text(source_path, target_path):
    """Extracts sentences from sorted files in source path
    and writes to one file."""
    outfile = join(target_path, 'comparable')
    with codecs.open(outfile, 'w', 'utf-8') as w:
        for ifile in sorted(glob.glob(source_path+"*.xml")):
            print "Extracting from "+ifile
            with codecs.open(ifile, 'r', 'utf-8') as f:
                tree = etree.parse(f)
                root = tree.getroot()
                for sent in root.iter('s'):
                    #for sentence-aligned: 's', if paragraphs change to 'p'
                    sent = sent.text.strip()
                    w.write(sent+'\n')


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    args = arg_parser.parse_args(sys.argv[1:])
    source_path=args.inputDirectory
    target_path=args.outputDirectory
    extract_text(source_path,target_path)