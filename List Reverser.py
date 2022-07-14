# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 22:30:22 2022

@author: aenna
"""

def reverser(thelist):
    # ENG
    # reverser function reverses the list , if an index is a list the function also reverses the list at the index.
    # TUR
    # reverser fonksiyonu bir listeyi tersine çevirir , eğer herhangi bir indeks liste tipinde ise o indeksteki listeyi de tersine çevirir.
    thelist.reverse()
    for i in range(len(thelist)):
        if type(thelist[i]) == list:
            thelist[i].reverse()
    return thelist
            
test_list = [[1, 2], [3, 4], [5, 6, 7]]

print(reverser(test_list))