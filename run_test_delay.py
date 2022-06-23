# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 15:42:06 2022

@author: Tim Schell
"""

import pyworld3.test_delay3 as td
from pyworld3.utils import plot_world_variables


rsc = td.test_delay3()
rsc.init_resource_variables()
rsc.init_resource_constants()
rsc.set_resource_delay_functions()
rsc.run_delay_test()


plot_world_variables(rsc.time,
                     [rsc.array, rsc.array_geglättet],
                     ["Array", "Array Geglättet"],
                     [[0, 200], [0, 200]],
                     figsize=(7, 5), title="Test Delay3")




print("Array:")
print(rsc.array)
print("Array geglättet:")
print(rsc.array_geglättet)
print('pyworld3_03 Update Version')