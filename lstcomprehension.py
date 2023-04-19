# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:45:48 2023

@author: Kairu Cyrus
"""

"""
List comprehension is an elegant to create a new list by filtering or 
transforming an existing one
"""
#create a non-empty list
orig_list = [1,2,23,14]
#creating cubes of numbers in original list
new_list = [x**3 for x in orig_list]
print(new_list)  #returns [1, 8, 12167, 2744]

#flattening a list ; make a single list
org_list = [[2, 4, 7], [5, 11, 19], [12, 8, 17]]
flat_list = [item for sublist in org_list for item in sublist]
print(flat_list)

#given two lists, we can create a list of tuples
l_list = ['c', 'h', 'p']
k_list = [1, 2, 7]
tpl_list = [(a, b) for a in l_list for b in k_list]
print(tpl_list)
