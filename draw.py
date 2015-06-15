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
from jinja2 import Environment, FileSystemLoader

import compute


def draw(data, labels=None):
    '''Draws Venn diagrams for data sets/lists.

    At maximum, five sets/lists will be accepted. If not labels are provided,
    uppercase letters will be used.

    Parameters:
    data: list of sets/lists
    labels: list of strings

    Returns:
    Rendered Venn diagram in SVG format.
    '''
    data_length = len(data)

    if data_length > 5:
        sys.exit('Too many sets/lists in data. Maximum is five.')

    lbls = _create_label_dict(labels, data_length)

    for key, val in compute.compute_sections('blah', mode='length'):
        lbls[key] = str(val)

    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template('{}_set.svg'.format(str(data_length)))

    print(lbls)

    return template.render(lbls)



def _create_label_dict(labels, data_length):
    default = 'ABCDE'
    label_dict = {'A':None,
                  'B': None,
                  'C': None,
                  'D': None,
                  'E': None}

    if labels:
        if not len(labels) == data_length:
            sys.exit('Incorrect number of labels for data set:'
                     '{0} vs. {1}'.format(str(len(labels), str(data_length))))
        else:
            for k, v in zip(default, labels):
                label_dict[k] = str(v)
    else:
        for lbl in default:
            label_dict[lbl] = lbl

    return label_dict
    
    
def _numerical_iterable2string(iterable):
    return ''.join([str(x) for x in iterable])


if __name__ == '__main__':
    a = list(range(0, 10))
    b = list(range(1, 11))
    c = list(range(2, 12))
    d = list(range(3, 13))
    e = list(range(4, 14))
    
    with open('test.svg', 'w') as f:
        f.write(draw([a,b,c,d,e], labels='klmno'))