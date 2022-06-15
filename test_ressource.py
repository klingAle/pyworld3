'''
This skript is written for testing the ressource sector while updating it to the 2004 Version of World3
'''


import pyworld3.resource as r


res = r.Resource()
res.set_resource_table_functions()
res.init_resource_constants()
res.init_resource_variables()
res.set_resource_delay_functions()
res.init_exogenous_inputs()
res.run_resource()

print('pyworld3_03 Update Version')