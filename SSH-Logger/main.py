##################################################
# SSH Authentication Analyzer
##################################################
# Author: Robin Visser
# Version: 1.0 (Beta)
# Email: robinvisser92@live.nl
# Copyright: 2021
##################################################

import time
import csv

# CSV DictReader
def readLog(fname):
    with open('system.log', 'r') as fp:
        lst = list(csv.DictReader(fp, delimiter=';'))
        # Get one item
        print(lst[0]["pid"])
    return lst

readLog('system.log')




