
# For ciao installed using ciao-install:
#
#     python setup.py build -e "/usr/bin/env python" install --prefix "$ASCDS_INSTALL/contrib" 
#
# For ciao installed using conda
#
#     python setup.py install


import os
import sys

assert "ASCDS_INSTALL" in os.environ, "Please setup for CIAO before installing"

from distutils.core import setup

setup( name='rank_roi',
       version='0.0.9',
       description='Assign overlap area to roi output files',
       author='Glotfelty',
       author_email='glotfeltyk@si.edu',
       url='https://github.com/kglotfelty/rank_roi/',
       scripts=["rank_roi", ],
       data_files=[('param',['rank_roi.par']),
                    ('share/doc/xml',['rank_roi.xml'])
                    ]       
    )

from subprocess import check_output
print("Update ahelp database ...")
check_output("ahelp -r".split())
