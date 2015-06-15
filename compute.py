# -*- coding: utf-8 -*-
"""
Package: venn
Module: compute

This package provides functions for computing all sections of Venn diagrams.
Functionality for drawing the diagrams in SVG format is also provided. Input
can be sets or lists.

The length of the input, i.e., the number of individual sets/lists is arbitrary.
However, diagrmas can only be drawn up to length 5 - above that it gets too
confusing anyway.

Created on Mon Jun 15 15:34:04 2015

@author: kp14
"""
import itertools
from decimal import Decimal


def compute_sections(data, mode='set'):
    '''Compute data sections of Venn diagrams.

    Data is supposed to be a list of sets or at least a list of lists.
    Works for arbitrary length of data. By default, returns sections as sets.
    However, thia can be changed using the 'mode' parameter so that numbers,
    i.e., the length of the sets, or fractions, i.e., the normalized lengths
    are returned.

    Parameters:
    data: list of sets or list of lists, arbitraty length
    mode: 'set', 'length' or 'normalized'; default: 'set'
    
    Returns:
    combination(as set), section (as set)
    '''
    data_sets = _ensure_set(data)
    no_of_sets = len(data_sets)
    all_datapoints = Decimal(len(set.union(*data_sets)))

    combinations = itertools.product(range(2), repeat=no_of_sets)

    for combi in combinations:
        to_intersect = _sets_to_be_intersected(data_sets, combi)
        to_union = _sets_to_be_unioned(data_sets, combi)

        if to_intersect:
            if len(to_intersect) == 1 and len(to_union) == 1:
                section = to_intersect[0] - to_union[0]

            elif len(to_intersect) == 1 and len(to_union) > 1:
                 section = to_intersect[0] - set.union(*to_union)

            elif len(to_intersect) > 1 and len(to_union) == 1:
                section = set.intersection(*to_intersect) - to_union[0]

            elif len(to_intersect) > 1 and len(to_union) > 1:
                 section = set.intersection(*to_intersect) - set.union(*to_union)

            elif len(to_intersect) > 1 and not to_union:
                section = set.intersection(*to_intersect)

            if mode == 'length':
                section = len(section)

            if mode == 'normalized':
                section = len(section) / all_datapoints

            yield combi, section


def _sets_to_be_intersected(data, selectors):
    to_intersect = []
    for item in itertools.compress(data, selectors):
        to_intersect.append(item)
    return to_intersect


def _sets_to_be_unioned(data, selectors):
    to_union = []
    for item in compress_negative(data, selectors):
        to_union.append(item)
    return to_union
    
    
def _ensure_set(data):
    return [set(x) for x in data]


def compress_negative(data, selectors):
    '''Complements itertools.compress by returning only False-mapping values.

    # compress('ABCDEF', [1,0,1,0,1,1]) --> B D'''
    return (d for d, s in zip(data, selectors) if not s)