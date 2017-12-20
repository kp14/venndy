# -*- coding: utf-8 -*-
"""
Package: venn
Module: draw

This package provides functions for computing all sections of Venn diagrams.
Functionality for drawing the diagrams in SVG format is also provided. Input
can be sets or lists.

The length of the input, i.e., the number of individual sets/lists is arbitrary.
However, diagrmas can only be drawn up to length 5 - above that it gets too
confusing anyway.

Created on Mon Jun 15 15:34:04 2015

@author: kp14
"""
import sys
from jinja2 import Environment, PackageLoader

from . import compute


def draw(data, labels=None):
    '''Draws Venn diagrams for data sets/lists.

    At maximum, five sets/lists will be accepted. If not labels are provided,
    uppercase letters will be used.

    Args:
        data (list): List of sets/lists.
        labels (list): List of labels.

    Returns:
        SVG: Rendered Venn diagram.
    '''
    data_length = len(data)

    if data_length > 5:
        sys.exit('Too many sets/lists in data. Maximum is five.')

    lbls = _create_label_dict(labels, data_length)

    for key, val in compute.compute_sections(data, mode='length'):
        key_string = _numerical_iterable2string(key)
        lbls[key_string] = str(val)

    env = Environment(loader=PackageLoader('venndy', 'templates'))
    template = env.get_template('{}_set.svg'.format(str(data_length)))

    return template.render(lbls)



def _create_label_dict(labels, data_length):
    '''Create key-value pairs for filling in the SVG template on rendering.

    Args:
        labels (list): Lables for the datasets.
        data_length (int): Number of data sets.

    Returns:
        dict: with labels
    '''
    default = 'ABCDE'
    label_dict = {'A':None,
                  'B': None,
                  'C': None,
                  'D': None,
                  'E': None}

    if labels:
        if not len(labels) == data_length:
            sys.exit('Incorrect number of labels for data set.')
        else:
            for k, v in zip(default, labels):
                label_dict[k] = str(v)
    else:
        for lbl in default:
            label_dict[lbl] = lbl

    return label_dict


def _numerical_iterable2string(iterable):
    '''Translate sequences like (0,1,0,0,1) to OIOOI.

    Args:
        iterable: iterable with sequence consisting of 0's and 1's

    Returns:
        str
    '''
    return ''.join(['I' if x else 'O' for x in iterable])
