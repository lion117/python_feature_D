# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:20:37 2014

@author: rd64
"""

import os
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.ui'):
            os.system('pyuic4 -o %s.py -x %s' \
                      % (file.rsplit('.', 1)[0], file))
        elif file.endswith('.qrc'):
         os.system('pyrcc4 -o %s_rc.py %s' \
                      % (file.rsplit('.', 1)[0], file))