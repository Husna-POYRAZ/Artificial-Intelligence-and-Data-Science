# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 07:21:47 2021

@author: DELL
"""

dictionary1 = {"key1": 100, "key2": {"key5": 4}, "key3": [10, 2.4, "husna", "poyraz"]}
print(dictionary1.keys())          # dict_keys(['key1', 'key2', 'key3'])
print(dictionary1.values())        # dict_values([100, {'key5': 4}, [10, 2.4, 'husna', 'poyraz']])
print(dictionary1["key1"])         # 100
print(dictionary1["key2"]["key5"]) # 4
print(dictionary1["key3"][2])      # husna