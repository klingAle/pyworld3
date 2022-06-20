import pyworld3.pollution as po
from pyworld3.utils import plot_world_variables


pol = po.Pollution()
pol.set_pollution_table_functions()
pol.init_pollution_variables()
pol.init_pollution_constants()
pol.set_pollution_delay_functions()
pol.init_exogenous_inputs()
pol.run_pollution()

plot_world_variables(pol.time, [pol.ppolx], ["PPOLX"], [[0, 32]], figsize=(7, 5), title="Solo Pollution")

plot_world_variables(pol.time, [pol.ppapr,pol.ppgr], ["ppapr","ppgr"], [[1e6, 4e9], [1e6, 4e9]], figsize=(7, 5), title="ppgr+ppapr")



print("ppapr:")
print(pol.ppapr)
print("pptd(constant):")
print(pol.pptd)
print("ppgr:")
print(pol.ppgr)

print('pyworld3_03 Update Version')
