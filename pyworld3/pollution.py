# -*- coding: utf-8 -*-

# © Copyright Charles Vanwynsberghe (2021)

# Pyworld3 is a computer program whose purpose is to run configurable
# simulations of the World3 model as described in the book "Dynamics
# of Growth in a Finite World".

# This software is governed by the CeCILL license under French law and
# abiding by the rules of distribution of free software. You can use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".

# As a counterpart to the access to the source code and rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty and the software's author, the holder of the
# economic rights, and the successive licensors have only limited
# liability.

# In this respect, the user's attention is drawn to the risks associated
# with loading, using, modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean that it is complicated to manipulate, and that also
# therefore means that it is reserved for developers and experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and, more generally, to use and operate it in the
# same conditions as regards security.

# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

import os
import json

from scipy.interpolate import interp1d
import numpy as np

from .specials import Dlinf3, clip, switch, Delay3
from .utils import requires


class Pollution:
    """
    Persistent Pollution sector. Can be run independantly from other sectors
    with exogenous inputs. The initial code is defined p.478.

    Examples
    --------
    Running the persistent pollution sector alone requires artificial
    (exogenous) inputs which should be provided by the other sectors. Start
    from the following example:

    >>> pol = Pollution()
    >>> pol.set_pollution_table_functions()
    >>> pol.init_pollution_variables()
    >>> pol.init_pollution_constants()
    >>> pol.set_pollution_delay_functions()
    >>> pol.init_exogenous_inputs()
    >>> pol.run_pollution()

    Parameters
    ----------
    year_min : float, optional
        start year of the simulation [year]. The default is 1900.
    year_max : float, optional
        end year of the simulation [year]. The default is 2100.
    dt : float, optional
        time step of the simulation [year]. The default is 1.
    pyear : float, optional
        implementation date of new policies [year]. The default is 1975.
    verbose : bool, optional
        print information for debugging. The default is False.

    Attributes
    ----------
    ppoli : float, optional
        persistent pollution initial [pollution units]. The default is 2.5e7.
    ppol70 : float, optional
        persistent pollution in 1970 [pollution units]. The default is 1.36e8.
    ahl70 : float, optional
        assimilation half-life in 1970 [years]. The default is 1.5.
    amti : float, optional
        agricultural materials toxicity index [pollution units/dollar].The
        default is 1.
    imti : float, optional
        industrial materials toxicity index [pollution units/resource unit].
        The default is 10.
    imef : float, optional
        industrial materials emission factor []. The default is 0.1.
    fipm : float, optional
        fraction of inputs as persistent materials []. The default is 0.001.
    frpm : float, optional
        fraction of resources as persistent materials []. The default is 0.02.
    ppgf1 : float, optional
        ppgf value before time=pyear []. The default is 1.
    ppgf2 : float, optional
        ppgf value after time=pyear []. The default is 1.
    ppgf21 : float, optional
        DESCRIPTION. The default is 1.
    pptd1 : float, optional
        pptd value before time=pyear [years]. The default is 20.
    pptd2 : float, optional
        pptd value after time=pyear [years]. The default is 20.
    ppol : numpy.ndarray
        persistent pollution [pollution units]. It is a state variable.
    ppolx : numpy.ndarray
        index of persistent pollution [].
    ppgao : numpy.ndarray
        persistent pollution generated by agricultural output
        [pollution units/year].
    ppgio : numpy.ndarray
        persistent pollution generated by industrial output
        [pollution units/year].
    ppgf : numpy.ndarray
        persistent pollution generation factor [].
    ppgr : numpy.ndarray
        persistent pollution generation rate [pollution units/year].
    ppapr : numpy.ndarray
        persistent pollution appearance rate [pollution units/year].
    ppasr : numpy.ndarray
        persistent pollution assimilation rate [pollution units/year].
    pptd : numpy.ndarray
        persistent pollution transmission delay [years].
    ahl : numpy.ndarray
        assimilation half-life [years].
    ahlm : numpy.ndarray
        assimilation half-life multiplier [].
    #neu hinzugefügt:
    arl : float [GHa]
        Arable Land. Default = 0.9
    ul : float  [GHa]
        Urban Land. Default = 8.2e-4
    ghup : float [GHa]
        GHa per Unit of Pollution. Default = 4e-9
    abl : numpy.ndarray [Gha]
        Absorbtion Land in Gha
    ef : numpy.ndarray
        Ecological Footprint
    """

    def __init__(self, year_min=1900, year_max=2100, dt=1, pyear=1975,
                 verbose=False):
        self.pyear = pyear
        self.dt = dt
        self.year_min = year_min
        self.year_max = year_max
        self.verbose = verbose
        self.length = self.year_max - self.year_min
        self.n = int(self.length / self.dt)
        self.time = np.arange(self.year_min, self.year_max, self.dt)
        print('Using local edit of pyworld3')

    def init_pollution_constants(self, ppoli=2.5e7, ppol70=1.36e8, ahl70=1.5,
                                 amti=1, imti=10, imef=0.1, fipm=0.001,
                                 frpm=0.02, ppgf1=1, ppgf2=1, ppgf21=1,
                                 pptd1=20, pptd2=20, arl = 0.9, ul = 8.2e-4, ghup= 4e-9):
        """
        Initialize the constant parameters of the pollution sector. Constants
        and their unit are documented above at the class level.

        """
        self.ppoli = ppoli
        self.ppol70 = ppol70
        self.ahl70 = ahl70
        self.amti = amti
        self.imti = imti
        self.imef = imef
        self.fipm = fipm
        self.frpm = frpm
        self.ppgf1 = ppgf1
        self.ppgf2 = ppgf2  # if sector is alone, modified as exogeneous
        self.ppgf21 = ppgf21
        self.pptd1 = pptd1
        self.pptd2 = pptd2
        
        #neu hinzugefügt
        self.arl = arl
        self.ul = ul
        self.ghup = ghup
        
        print('Using old version of pollution sector')
        
 
    def init_pollution_variables(self):
        """
        Initialize the state and rate variables of the pollution sector
        (memory allocation). Variables and their unit are documented above at
        the class level.

        """
        self.ppol = np.full((self.n,), np.nan)
        self.ppolx = np.full((self.n,), np.nan)
        self.ppgao = np.full((self.n,), np.nan)
        self.ppgio = np.full((self.n,), np.nan)
        self.ppgf = np.full((self.n,), np.nan)
        self.ppgr = np.full((self.n,), np.nan)
        self.ppapr = np.full((self.n,), np.nan)
        self.ppasr = np.full((self.n,), np.nan)
        self.pptd = np.full((self.n,), np.nan)
        self.ahlm = np.full((self.n,), np.nan)
        self.ahl = np.full((self.n,), np.nan)
        
        #neu hinzugefügt
        self.abl = np.full((self.n,), np.nan)
        self.ef = np.full((self.n,), np.nan)

    def set_pollution_delay_functions(self, method="euler"):
        """
        Set the linear smoothing and delay functions of the 1st or the 3rd
        order, for the pollution sector. One should call
        `self.set_pollution_delay_functions` after calling
        `self.init_pollution_constants`.

        Parameters
        ----------
        method : str, optional
            Numerical integration method: "euler" or "odeint". The default is
            "euler".

        """
        var_delay3 = ["PPGR"]
        for var_ in var_delay3:
            func_delay = Delay3(getattr(self, var_.lower()),
                                self.dt, self.time, method=method)
            setattr(self, "delay3_"+var_.lower(), func_delay)

    def set_pollution_table_functions(self, json_file=None):
        """
        Set the nonlinear functions of the pollution sector, based on a json
        file. By default, the `functions_table_world3.json` file from pyworld3
        is used.

        Parameters
        ----------
        json_file : file, optional
            json file containing all tables. The default is None.

        """
        if json_file is None:
            json_file = "./functions_table_world3.json"
            json_file = os.path.join(os.path.dirname(__file__), json_file)
        with open(json_file) as fjson:
            tables = json.load(fjson)

        func_names = ["AHLM"]

        for func_name in func_names:
            for table in tables:
                if table["y.name"] == func_name:
                    func = interp1d(table["x.values"], table["y.values"],
                                    bounds_error=False,
                                    fill_value=(table["y.values"][0],
                                                table["y.values"][-1]))
                    setattr(self, func_name.lower()+"_f", func)

    def init_exogenous_inputs(self):
        """
        Initialize all the necessary constants and variables to run the
        pollution sector alone. These exogenous parameters are outputs from
        the 4 other remaining sectors in a full simulation of World3.

        """
        # constants
        self.swat = 0
        self.tdd = 10
        self.pd = 5
        # variables
        self.pcrum = np.full((self.n,), np.nan)
        self.pop = np.full((self.n,), np.nan)
        self.aiph = np.full((self.n,), np.nan)
        self.al = np.full((self.n,), np.nan)
        self.pcti = np.full((self.n,), np.nan)
        self.pctir = np.full((self.n,), np.nan)
        self.pctcm = np.full((self.n,), np.nan)
        self.plmp = np.full((self.n,), np.nan)
        self.lmp = np.full((self.n,), np.nan)
        self.lmp1 = np.full((self.n,), np.nan)
        self.lmp2 = np.full((self.n,), np.nan)
        self.lfdr = np.full((self.n,), np.nan)
        self.lfdr1 = np.full((self.n,), np.nan)
        self.lfdr2 = np.full((self.n,), np.nan)
        self.ppgf22 = np.full((self.n,), np.nan)
        # tables
        func_names = ["PCRUM", "POP", "AIPH", "AL", "PCTCM", "LMP1", "LMP2",
                      "LFDR1", "LFDR2"]
        y_values = [[_ * 10**-2 for _ in [17, 30, 52, 78, 138, 280, 480, 660,
                                          700, 700, 700]],
                    [_ * 10**8 for _ in [16, 19, 22, 31, 42, 53, 67, 86, 109,
                                         139, 176]],
                    [6.6, 11, 20, 34, 57, 97, 168, 290, 495, 845, 1465],
                    [_ * 10**8 for _ in [9, 10, 11, 13, 16, 20, 24, 26, 27,
                                         27, 27]],
                    [0, -0.05],
                    [1, .99, .97, .95, .90, .85, .75, .65, .55, .40, .20],
                    [1, .99, .97, .95, .90, .85, .75, .65, .55, .40, .20],
                    [0, 0.1, 0.3, 0.5],
                    [0, 0.1, 0.3, 0.5]]
        x_to_2100 = np.linspace(1900, 2100, 11)
        x_0_to_100 = np.linspace(0, 100, 11)
        x_0_to_30 = np.linspace(0, 30, 4)
        x_values = [x_to_2100,
                    x_to_2100,
                    x_to_2100,
                    x_to_2100,
                    [0, 10],
                    x_0_to_100,
                    x_0_to_100,
                    x_0_to_30,
                    x_0_to_30]
        for func_name, x_vals, y_vals in zip(func_names, x_values, y_values):
            func = interp1d(x_vals, y_vals,
                            bounds_error=False,
                            fill_value=(y_vals[0],
                                        y_vals[-1]))
            setattr(self, func_name.lower()+"_f", func)
        # Delays
        var_dlinf3 = ["PCTI", "LMP"]
        for var_ in var_dlinf3:
            func_delay = Dlinf3(getattr(self, var_.lower()),
                                self.dt, self.time, method="euler")
            setattr(self, "dlinf3_"+var_.lower(), func_delay)

    def loopk_exogenous(self, k):
        """
        Run a sorted sequence to update one loop of the exogenous parameters.
        `@requires` decorator checks that all dependencies are computed
        previously.

        """
        j = k - 1
        kl = k
        jk = j

        self.pcti[k] = self.pcti[j] + self.dt * self.pctir[jk]

        self.pcrum[k] = self.pcrum_f(self.time[k])
        self.pop[k] = self.pop_f(self.time[k])
        self.aiph[k] = self.aiph_f(self.time[k])
        self.al[k] = self.al_f(self.time[k])

        self.ppgf22[k] = self.dlinf3_pcti(k, self.tdd)
        self.ppgf2 = switch(self.ppgf21, self.ppgf22[k], self.swat)

        self.plmp[k] = self.dlinf3_lmp(k, self.pd)
        self.pctcm[k] = self.pctcm_f(1 - self.plmp[k])

        self.pctir[kl] = clip(self.pcti[k] * self.pctcm[k], 0, self.time[k],
                              self.pyear)

        self.lmp1[k] = self.lmp1_f(self.ppolx[k])
        self.lmp2[k] = self.lmp2_f(self.ppolx[k])
        self.lmp[k] = clip(self.lmp2[k], self.lmp1[k], self.time[k],
                           self.pyear)
        self.lfdr1[k] = self.lfdr1_f(self.ppolx[k])
        self.lfdr2[k] = self.lfdr1_f(self.ppolx[k])
        self.lfdr[k] = clip(self.lfdr2[k], self.lfdr1[k], self.time[k],
                            self.pyear)

    def loop0_exogenous(self):
        """
        Run a sequence to initialize the exogenous parameters (loop with k=0).

        """
        self.pcti[0] = 1

        self.pcrum[0] = self.pcrum_f(self.time[0])
        self.pop[0] = self.pop_f(self.time[0])
        self.aiph[0] = self.aiph_f(self.time[0])
        self.al[0] = self.al_f(self.time[0])

        self.ppgf22[0] = self.dlinf3_pcti(0, self.tdd)
        self.ppgf2 = switch(self.ppgf21, self.ppgf22[0], self.swat)

        self.lmp1[0] = self.lmp1_f(self.ppolx[0])
        self.lmp2[0] = self.lmp2_f(self.ppolx[0])
        self.lmp[0] = clip(self.lmp2[0], self.lmp1[0], self.time[0],
                           self.pyear)

        self.plmp[0] = self.dlinf3_lmp(0, self.pd)
        self.pctcm[0] = self.pctcm_f(1 - self.plmp[0])

        self.pctir[0] = clip(self.pcti[0] * self.pctcm[0], 0, self.time[0],
                             self.pyear)

        self.lfdr1[0] = self.lfdr1_f(self.ppolx[0])
        self.lfdr2[0] = self.lfdr1_f(self.ppolx[0])
        self.lfdr[0] = clip(self.lfdr2[0], self.lfdr1[0], self.time[0],
                            self.pyear)

    def loop0_pollution(self, alone=False):
        """
        Run a sequence to initialize the pollution sector (loop with k=0).

        Parameters
        ----------
        alone : boolean, optional
            if True, run the sector alone with exogenous inputs. The default
            is False.

        """
        self.ppol[0] = self.ppoli
        self._update_ppolx(0)
        if alone:
            self.loop0_exogenous()  # EXOGENOUS HERE
        self._update_ppgio(0)
        self._update_ppgao(0)
        self._update_ppgf(0)
        self._update_ppgr(0, 0)
        self._update_pptd(0)
        self._update_ppapr(0, 0)
        self._update_ahlm(0)
        self._update_ahl(0)
        self._update_ppasr(0, 0)
        
        #neu hinzugefügt
        self._update_abl(0)
        self._update_ef(0)

    def loopk_pollution(self, j, k, jk, kl, alone=False):
        """
        Run a sequence to update one loop of the pollution sector.

        Parameters
        ----------
        alone : boolean, optional
            if True, run the sector alone with exogenous inputs. The default
            is False.

        """
        self._update_state_ppol(k, j, jk)
        self._update_ppolx(k)
        if alone:
            self.loopk_exogenous(k)
        self._update_ppgio(k)
        self._update_ppgao(k)
        self._update_ppgf(k)
        self._update_ppgr(k, kl)
        self._update_pptd(k)
        self._update_ppapr(k, kl)
        self._update_ahlm(k)
        self._update_ahl(k)
        self._update_ppasr(k, kl)
        
        #neu hinzugefügt
        self._update_abl(k)
        self._update_ef(k)


    def run_pollution(self):
        """
        Run a sequence of updates to simulate the pollution sector alone with
        exogenous inputs.

        """
        self.redo_loop = True
        while self.redo_loop:
            self.redo_loop = False
            self.loop0_pollution(alone=True)

        for k_ in range(1, self.n):
            self.redo_loop = True
            while self.redo_loop:
                self.redo_loop = False
                if self.verbose:
                    print("go loop", k_)
                self.loopk_pollution(k_-1, k_, k_-1, k_, alone=True)

    @requires(["ppol"])
    def _update_state_ppol(self, k, j, jk):
        """
        State variable, requires previous step only
        """
        self.ppol[k] = self.ppol[j] + self.dt * (self.ppapr[jk] -
                                                 self.ppasr[jk])

    @requires(["ppolx"], ["ppol"])
    def _update_ppolx(self, k):
        """
        From step k requires: PPOL
        """
        self.ppolx[k] = self.ppol[k] / self.ppol70

    @requires(["ppgio"], ["pcrum", "pop"])
    def _update_ppgio(self, k):
        """
        From step k requires: PCRUM POP
        """
        self.ppgio[k] = (self.pcrum[k] * self.pop[k] * self.frpm *
                         self.imef * self.imti)

    @requires(["ppgao"], ["aiph", "al"])
    def _update_ppgao(self, k):
        """
        From step k requires: AIPH AL
        """
        self.ppgao[k] = self.aiph[k] * self.al[k] * self.fipm * self.amti

    @requires(["ppgf"])
    def _update_ppgf(self, k):
        """
        From step k requires: PPGF22
        """

        self.ppgf[k] = clip(self.ppgf2, self.ppgf1, self.time[k],
                            self.pyear)

    @requires(["ppgr"], ["ppgio", "ppgao", "ppgf"])
    def _update_ppgr(self, k, kl):
        """
        From step k requires: PPGIO PPGAO PPGF
        """
        self.ppgr[kl] = (self.ppgio[k] + self.ppgao[k]) * self.ppgf[k]

    @requires(["pptd"])
    def _update_pptd(self, k):
        """
        From step k requires: nothing
        """
        self.pptd[k] = clip(self.pptd2, self.pptd1, self.time[k], self.pyear)

    @requires(["ppapr"], ["ppgr"], check_after_init=False)
    def _update_ppapr(self, k, kl):
        """
        From step k=0 requires: PPGR, else nothing
        """
        # !!! is originally ppgr[jk] rather than ppgr[k]
        self.ppapr[kl] = self.delay3_ppgr(k, self.pptd[k])
        
    @requires(["ahlm"], ["ppolx"])
    def _update_ahlm(self, k):
        """
        From step k requires: PPOLX
        """
        self.ahlm[k] = self.ahlm_f(self.ppolx[k])

    @requires(["ahl"], ["ahlm"])
    def _update_ahl(self, k):
        """
        From step k requires: AHLM
        """
        self.ahl[k] = self.ahlm[k] * self.ahl70

    @requires(["ppasr"], ["ahl", "ppol"])
    def _update_ppasr(self, k, kl):
        """
        From step k requires: AHL PPOL
        """
        self.ppasr[kl] = self.ppol[k] / (self.ahl[k] * 1.4)
    
    #neu hinzugefügt
    @requires(["ppgr"])
    def _update_abl(self,k):
        """
        From step k requires: ppgr
        """
        self.abl[k] = self.ppgr[k] * self.ghup
        
     #neu hinzugefügt
    @requires (["abl"])
    def _update_ef(self,k):
        """
        From step k requires: abl
        """
        self.ef[k] = (self.arl + self.ul + self.abl[k])/1.91

