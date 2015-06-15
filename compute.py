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


def compute_sections(data, mode='sets'):

    for idx, combi in enumerate(itertools.product([0,1], repeat=5)):
        yield ''.join([str(x) for x in combi]), set(range(idx, idx + 5))
