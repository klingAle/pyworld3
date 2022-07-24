# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from pyworld3 import World3
from pyworld3.utils import plot_world_variables

params = {'lines.linewidth': '3'}
plt.rcParams.update(params)

world3 = World3(pyear = 1975, pyear_res_tech= 4000, dt = 0.5)
world3.init_world3_constants()
world3.init_world3_variables()
world3.set_world3_table_functions()
world3.set_world3_delay_functions()
world3.run_world3(fast=False)

plot_world_variables(world3.time,
                     [world3.nrfr, world3.iopc, world3.fpc, world3.pop,
                      world3.ppolx],
                     ["NRFR", "IOPC", "FPC", "POP", "PPOLX"],
                     [[0, 1], [0, 1e3], [0, 1e3], [0, 16e9], [0, 32]],
                     img_background="./img/fig7-7.png",
                     figsize=(7, 5),
                     title="World3 standard run")

print("ic:")
print(world3.ic[1])

print("fcaor:")
print(world3.fcaor[1])

print("cuf:")
print(world3.cuf[1])

print("icor:")
print(world3.icor[1])

print("io:")
print(world3.io[1])

print("icir:")
print(world3.icir[1])

print("icdr:")
print(world3.icdr[1])

print("fioai:")
print(world3.fioai[1])

print("ifpc:")
print(world3.ifpc[1])

print("fpc:")
print(world3.fpc[1])

print("fioaa:")
print(world3.fioaa[1])

print("fioas:")
print(world3.fioas[1])

print("fioac:")
print(world3.fioac[1])

print("pop:")
print(world3.pop[1])

print("f:")
print(world3.f[1])

print("iopc:")
print(world3.iopc[1])

print("ppolx:")
print(world3.ppolx[1])

print("pp:")
print(world3.pp[1])

"""
läuft zwar durch berechnet allerdings nichts nan
ich muss durch jeden sektor gehen und die angeforderten variablen ändern. Check, alles richtig, trotzdem wird nicht berechnet
manche variablen werden nicht berechnet im ersten durchlauf, alle variablen checken und herraussuchen welche nicht berechnet werden, danach lösung für jede variable finden
"""

"""
plot_world_variables(world3.time,
                     [world3.fcaor, world3.io, world3.tai, world3.aiph,
                      world3.fioaa],
                     ["FCAOR", "IO", "TAI", "AI", "FIOAA"],
                     [[0, 1], [0, 4e12], [0, 4e12], [0, 2e2], [0, 0.201]],
                     img_background="./img/fig7-8.png",
                     figsize=(7, 5),
                     title="World3 standard run - Capital sector")

plot_world_variables(world3.time,
                     [world3.ly, world3.al, world3.fpc, world3.lmf,
                      world3.pop],
                     ["LY", "AL", "FPC", "LMF", "POP"],
                     [[0, 4e3], [0, 4e9], [0, 8e2], [0, 1.6], [0, 16e9]],
                     img_background="./img/fig7-9.png",
                     figsize=(7, 5),
                     title="World3 standard run - Agriculture sector")

plot_world_variables(world3.time,
                     [world3.hef, world3.hwi],
                     ["HEF", "HWI"],
                     [[0, 2], [0,1]],
                     figsize=(7, 5), title="Ecological Footprint + Human Welfare Index")
"""
"""
plot_world_variables(world3.time,
                     [world3.fcaor1, world3.fcaor2, world3.fcaor],
                     ["fcaor1", "fcaor2", "fcaor"],
                     [[-1, 1], [-1.5, 1], [-1.7,1]],
                     figsize=(7, 5), title="fcaor1+fcaor2")
"""

