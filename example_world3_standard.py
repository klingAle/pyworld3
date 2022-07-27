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

plot_world_variables(world3.time,
                     [world3.nrfr, world3.iopc, world3.fpc, world3.pop,
                      world3.ppolx],
                     ["NRFR", "IOPC", "FPC", "POP", "PPOLX"],
                     [[0, 1], [0, 1e3], [0, 1e3], [0, 16e9], [0, 32]],
                     img_background="./img/fig7-7.png",
                     figsize=(7, 5),
                     title="World3 standard run")

datei = open('variablenwerte.txt','w')
datei.write("Time:\n")
print(datetime.now())
datei.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
datei.write("\napfay:\n")
datei.write(str(world3.apfay))
datei.write("\nymap1:\n")
datei.write(str(world3.ymap1))
datei.write("\nymap2:\n")
datei.write(str(world3.ymap2))
datei.write("\nfio70:\n")
datei.write(str(world3.fio70))
datei.write("\npii:\n")
datei.write(str(world3.pii))
datei.write("\npcrum:\n")
datei.write(str(world3.pcrum))
datei.write("\nppgi:\n")
datei.write(str(world3.ppgi))
datei.write("\naiph:\n")
datei.write(str(world3.aiph))
datei.write("\nppga:\n")
datei.write(str(world3.ppga))
datei.write("\nppgr:\n")
datei.write(str(world3.ppgr))
datei.write("\nppar:\n")
datei.write(str(world3.ppar))
datei.write("\nppasr:\n")
datei.write(str(world3.ppasr))
datei.write("\npp:\n")
datei.write(str(world3.pp))
datei.write("\nppasr:\n")
datei.write(str(world3.ppasr))
datei.write("\nahl:\n")
datei.write(str(world3.ahl))
datei.write("\nahlm:\n")
datei.write(str(world3.ahlm))
datei.write("\nppolx:\n")
datei.write(str(world3.ppolx))
datei.write("\npptc:\n")
datei.write(str(world3.pptc))
datei.write("\npptcm:\n")
datei.write(str(world3.pptcm))
datei.write("\npptcr:\n")
datei.write(str(world3.pptcr))
datei.write("\nppt:\n")
datei.write(str(world3.ppt))
datei.write("\nppgf2:\n")
datei.write(str(world3.ppgf2))
datei.write("\nppgf:\n")
datei.write(str(world3.ppgf))
datei.write("\npptmi:\n")
datei.write(str(world3.pptmi))
datei.write("\nabl:\n")
datei.write(str(world3.abl))
datei.write("\nhef:\n")
datei.write(str(world3.hef))
 #viele table functions funktionieren nicht
datei.write("\npop:\n")
datei.write(str(world3.pop))
datei.write("\np1:\n")
datei.write(str(world3.p1))
datei.write("\np2:\n")
datei.write(str(world3.p2))
datei.write("\np3:\n")
datei.write(str(world3.p3))
datei.write("\np4:\n")
datei.write(str(world3.p4))
datei.write("\nd1:\n")
datei.write(str(world3.d1))
datei.write("\nd2:\n")
datei.write(str(world3.d2))
datei.write("\nd3:\n")
datei.write(str(world3.d3))
datei.write("\nd4:\n")
datei.write(str(world3.d4))
datei.write("\nmat1:\n")
datei.write(str(world3.mat1))
datei.write("\nmat2:\n")
datei.write(str(world3.mat2))
datei.write("\nmat3:\n")
datei.write(str(world3.mat3))
datei.write("\nd:\n")
datei.write(str(world3.d))
datei.write("\ncdr:\n")
datei.write(str(world3.cdr))
datei.write("\nfpu:\n")
datei.write(str(world3.fpu))
datei.write("\nle:\n")
datei.write(str(world3.le))
datei.write("\nlmc:\n")
datei.write(str(world3.lmc))
datei.write("\nlmf:\n")
datei.write(str(world3.lmf))
datei.write("\nlmhs:\n")
datei.write(str(world3.lmhs))
datei.write("\nlmhs1:\n")
datei.write(str(world3.lmhs1))
datei.write("\nlmhs2:\n")
datei.write(str(world3.lmhs2))
datei.write("\nlmp:\n")
datei.write(str(world3.lmp))
datei.write("\nm1:\n")
datei.write(str(world3.m1))
datei.write("\nm2:\n")
datei.write(str(world3.m2))
datei.write("\nm3:\n")
datei.write(str(world3.m3))
datei.write("\nm4:\n")
datei.write(str(world3.m4))
datei.write("\nehspc:\n")
datei.write(str(world3.ehspc))
datei.write("\nhsapc:\n")
datei.write(str(world3.hsapc))
datei.write("\nb:\n")
datei.write(str(world3.b))
datei.write("\ncbr:\n")
datei.write(str(world3.cbr))
datei.write("\ncmi:\n")
datei.write(str(world3.cmi))
datei.write("\ncmple:\n")
datei.write(str(world3.cmple))
datei.write("\ntf:\n")
datei.write(str(world3.tf))
datei.write("\ndtf:\n")
datei.write(str(world3.dtf))
datei.write("\ndcfs:\n")
datei.write(str(world3.dcfs))
datei.write("\nfce:\n")
datei.write(str(world3.fce))
datei.write("\nfie:\n")
datei.write(str(world3.fie))
datei.write("\nfm:\n")
datei.write(str(world3.fm))
datei.write("\nfrsn:\n")
datei.write(str(world3.frsn))
datei.write("\nmtf:\n")
datei.write(str(world3.mtf))
datei.write("\nnfc:\n")
datei.write(str(world3.nfc))
datei.write("\nple:\n")
datei.write(str(world3.ple))
datei.write("\nsfsn:\n")
datei.write(str(world3.sfsn))
datei.write("\naiopc:\n")
datei.write(str(world3.aiopc))
datei.write("\ndiopc:\n")
datei.write(str(world3.diopc))
datei.write("\nfcfpc:\n")
datei.write(str(world3.fcfpc))
datei.write("\nfcapc:\n")
datei.write(str(world3.fcapc))
datei.write("\nfsafc:\n")
datei.write(str(world3.fsafc))
datei.write("\nlei:\n")
datei.write(str(world3.lei))
datei.write("\ngdpc:\n")
datei.write(str(world3.gdpc))
datei.write("\ngdpi:\n")
datei.write(str(world3.gdpi))
datei.write("\nei:\n")
datei.write(str(world3.ei))
datei.write("\nhwi:\n")
datei.write(str(world3.hwi))


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

