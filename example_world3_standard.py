# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from pyworld3 import World3
from pyworld3.utils import plot_world_variables
from datetime import datetime

params = {'lines.linewidth': '3'}
plt.rcParams.update(params)

world3 = World3(pyear = 1975, pyear_res_tech= 4000, dt = 0.5)
world3.init_world3_constants()
world3.init_world3_variables()
world3.set_world3_table_functions()
world3.set_world3_delay_functions()
world3.run_world3(fast=False)

"""
plot_world_variables(world3.time,
                     [world3.nrfr, world3.iopc, world3.fpc, world3.pop,
                      world3.ppolx],
                     ["NRFR", "IOPC", "FPC", "POP", "PPOLX"],
                     [[0, 1.975], [20, 6e2], [0, 1e3], [0, 11e9], [-0.2, 26]],
                     img_background="./img/fig 4-11-1.png",
                     figsize=(7, 5),
                     title="World3 standard run, 2004")

plot_world_variables(world3.time,
                     [world3.nrfr, world3.iopc, world3.fpc, world3.pop,
                      world3.ppolx],
                     ["NRFR", "IOPC", "FPC", "POP", "PPOLX"],
                     [[0, 1], [0, 1e3], [0, 1e3], [0, 16e9], [0, 32]],
                     img_background="./img/fig7-7.png",
                     figsize=(7, 5),
                     title="World3 standard run, wrong background")
"""

plot_world_variables(world3.time,
                     [world3.nrfr, world3.io, world3.f, world3.pop,
                      world3.ppolx],
                     ["NRFR", "IO", "F", "POP", "PPOLX"],
                     [[0, 1.975], [0, 4e12], [0, 6e12], [0, 11e9], [-0.2, 26]],
                     img_background="./img/fig 4-11-1.png",
                     figsize=(7, 5),
                     title="World3 standard run, 2004")
"""
plot_world_variables(world3.time,
                     [world3.fcaor, world3.io, world3.tai, world3.aiph,
                      world3.fioaa],
                     ["FCAOR", "IO", "TAI", "AI", "FIOAA"],
                     [[0, 1], [0, 4e12], [0, 4e12], [0, 2e2], [0, 0.201]],
                     img_background="./img/fig7-8.png",
                     figsize=(7, 5),
                     title="World3 standard run - Capital sector")
"""
plot_world_variables(world3.time,
                     [world3.le, world3.fpc, world3.sopc],
                     ["LE", "FPC", "SOPC"],
                     [[2, 75], [0,1020],[0,1050]],
                     img_background="./img/fig 4-11-2.png",
                     figsize=(7, 5),
                     title="World3 standard run - Material standard of living, 2004")

"""
plot_world_variables(world3.time,
                     [world3.ly, world3.al, world3.fpc, world3.lmf,
                      world3.pop],
                     ["LY", "AL", "FPC", "LMF", "POP"],
                     [[0, 4e3], [0, 4e9], [0, 8e2], [0, 1.6], [0, 16e9]],
                     img_background="./img/fig7-9.png",
                     figsize=(7, 5),
                     title="World3 standard run - Agriculture sector")
"""
plot_world_variables(world3.time,
                     [world3.hef, world3.hwi],
                     ["HEF", "HWI"],
                     [[0.1, 2.4], [0,0.9]],
                     img_background="./img/fig 4-11-3.png",
                     figsize=(7, 5), title="Ecological Footprint + Human Welfare Index, 2004")



