import pyworld3.resource as re
from pyworld3.utils import plot_world_variables


rsc = re.Resource(szenario = 2)
rsc.set_resource_table_functions()
rsc.init_resource_variables()
rsc.init_resource_constants()
rsc.set_resource_delay_functions()
rsc.init_exogenous_inputs()
rsc.run_resource()

plot_world_variables(rsc.time,
                     [rsc.nrfr, rsc.iopc, rsc.pop],
                     ["NRFR", "IOPC", "POP"],
                     [[0, 1], [0, 1e3], [0, 16e9]],
                     figsize=(7, 5), title="Solo Resources")

plot_world_variables(rsc.time,
                     [rsc.nruf, rsc.rt],
                     ["NRUF", "RT"],
                     [[0, 1.5], [0, 1.5]],
                     figsize=(7, 5), title="NRUF+RT")

print(rsc.nruf)
print(rsc.rt)
print('pyworld3_03 Update Version')