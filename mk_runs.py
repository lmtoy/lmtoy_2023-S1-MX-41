#! /usr/bin/env python
#
#   script generator for project="2021-S1-US-3"
#
#   lmtinfo.py grep US-3 Science Map | awk '{print $2}' | sort


import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy)
    from lmtoy import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)
    
project="2023-S1-MX-41"

on = {}

on["IRAS13349+2438"] =  [ 106061, 106062, 106063, 106065, 106066, 106067,
                          106128, 106129, 106130, 106132, 106133, 106134,
                          106136, 106137, 106138,]                         # feb 18



on["PG1211+143"] =  [ 105809, 105810, 105811, 105813, 105814, 105815,
                      105817, 105818, 105819, 105823, 105824, 105825,
                      105827, 105828, 105829, 105831, 105832, 105833,     # feb 15
                      105955, 105956, 105957, 105959, 105960, 105961,]    # feb 17

pars1 = {}
pars1["IRAS13349+2438"] = ""
pars1["PG1211+143"] = ""

pars2 = {}
pars2["IRAS13349+2438"] = ""
pars2["PG1211+143"] = ""

if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2)

