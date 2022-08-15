# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from xlwt import Workbook
from pyworld3 import World3
from pyworld3.utils import plot_world_variables

import time
startTime = time.time()


def dcfsn_f(i):
    dcfsn = [3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0]
    return dcfsn[i]

params = {'lines.linewidth': '3'}
plt.rcParams.update(params)

wb = Workbook()
pop = wb.add_sheet("Population")
d = wb.add_sheet("Death per Year")
b = wb.add_sheet("Birth per Year")
fpc = wb.add_sheet("Food per Capita")
ef = wb.add_sheet("Ecological Footprint")
hwi = wb.add_sheet("Human Welfare Index")

world3 = World3(dt = 1)


for i in range(0,9):
    print("Simulation")
    print(i+1)

    world3.init_world3_constants(dcfsn = dcfsn_f(i))
    world3.init_world3_variables()
    world3.set_world3_table_functions()
    world3.set_world3_delay_functions()
    world3.run_world3(fast=False)
    """
    plot_world_variables(world3.time,
                     [world3.nrfr, world3.io, world3.f, world3.pop,
                      world3.ppolx],
                     ["NRFR", "IO", "F", "POP", "PPOLX"],
                     [[0, 1.975], [0, 4e12], [0, 6e12], [0, 12e9], [0, 40]],
                     img_background="./img/fig 4-1-1.png",
                     figsize=(7, 5),
                     title="World3 Referenze Run, 2004 Szenario 1. Simulation")
    """
    for y in range(0,200):
        pop.write(y+1, i+1, world3.pop[y])
        d.write(y+1, i+1, world3.d[y])
        b.write(y+1, i+1, world3.b[y])
        fpc.write(y+1, i+1, world3.fpc[y])
        ef.write(y+1, i+1, world3.ef[y])
        hwi.write(y+1, i+1, world3.hwi[y])

wb.save('sim-values.xls')

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
