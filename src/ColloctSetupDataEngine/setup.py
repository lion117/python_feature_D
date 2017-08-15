# -*- coding: utf-8 -*-
# Created by leonardohe Data
# 2016/9/19


from distutils.core import setup
import py2exe
import sys



setup(console=["ProcessManager.py"],
      options={"py2exe": {
          "compressed": True,
          "optimize": 2,
          "bundle_files": 2}},
      dll_excludes=['msvcr71.dll', "IPHLPAPI.DLL", "NSI.dll",  "WINNSI.DLL",  "WTSAPI32.dll","OLEAUT32.dll ","USER32.dll","GDI32.dll"]
      )
