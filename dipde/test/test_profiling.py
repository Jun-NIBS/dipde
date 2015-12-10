import numpy as np
from dipde.profiling import profile_simulation, extract_value
from dipde.examples.singlepop import get_simulation
import re



def test_profile_singlepop():
    
    dv = .0001
    update_method = 'approx'
    approx_order = None
    tol = 1e-14
    
    run_dict = {'dt':.0001, 't0':0, 'tf':.2}
    simulation = get_simulation(dv=dv, update_method=update_method, approx_order=approx_order, tol=tol)
    total_time_list = []
    profile_result = profile_simulation(simulation.to_dict(), run_dict)
    run_time = extract_value(profile_result, 'cumtime', 'simulation.py', 'run')

    
    
if __name__ == "__main__":                      # pragma: no cover
    test_profile_singlepop()                    # pragma: no cover