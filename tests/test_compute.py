# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:14:09 2015

@author: kp14
"""
from venn import compute

def test_ensure_set_with_lists():
    test_list = [list(range(10)),
                 list(range(5)),
                 list(range(12)),
                 list(range(20)),
                 ]
    set_list = compute._ensure_set(test_list)
    assert len(set_list) == 4
    for item in set_list:
        assert isinstance(item, set)


def test_ensure_set_with_sets():
    test_list = [set(list(range(10))),
                 set(list(range(5))),
                 set(list(range(12))),
                 set(list(range(20))),
                 ]
    set_list = compute._ensure_set(test_list)
    assert len(set_list) == 4
    for item in set_list:
        assert isinstance(item, set)


def test_compress_negative():
    data = 'ABCDEF'
    selectors = [1, 0, 1, 0, 1, 0]
    compressed = []
    for item in compute.compress_negative(data, selectors):
        compressed.append(item)
    assert compressed == ['B', 'D', 'F']