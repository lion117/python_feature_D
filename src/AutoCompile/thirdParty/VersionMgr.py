# -*- coding: utf-8 -*-
import os, sys
import time
import  re

# source taken from
# http://stackoverflow.com/questions/4003725/modifying-rc-file-with-python-regexp-involved



def set_rc_version(rcfile, target_version):
    with open(rcfile, "r+") as f:
        rc_content = f.read()

        # first part
        #FILEVERSION 6,0,20,163         
        #PRODUCTVERSION 6,0,20,163
        #...

        # second part
        #VALUE "FileVersion", "6, 0, 20, 163"
        #VALUE "ProductVersion", "6, 0, 20, 163"

        # first part
        regex_1 = re.compile(r"\b(FILEVERSION|FileVersion|PRODUCTVERSION|ProductVersion) \d+,\d+,\d+,\d+\b", re.MULTILINE)

        # second part
        regex_2 = re.compile(r"\b(VALUE\s*\"FileVersion\",\s*\"|VALUE\s*\"ProductVersion\",\s*\").*?(\")", re.MULTILINE)
        
        version = r"\1 " + target_version
        #modified_str = re.sub(regex, version, rc_content)

        pass_1 = re.sub(regex_1, version, rc_content)
        version = re.sub(",", ", ", version) #replacing "x,y,v,z" with "x, y, v, z"
        pass_2 = re.sub(regex_2, r"\g<1>" + target_version + r"\2", pass_1)

        # overwrite
        f.seek(0)
        f.write(pass_2)
        f.truncate()


#SetRcVersion(r"C:/repo/projectA/resources/win/projectA.rc", "3,4,5,6")