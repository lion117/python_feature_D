# -*- coding: utf-8 -*-
# Created by leonardohe Data
# 2016/9/19


from distutils.core import setup
import py2exe



setup(console=["ProcessManager.py"],
      options={"py2exe": {
          "compressed": True,
          "optimize": 2,
          "bundle_files": 2,
      }
      })
