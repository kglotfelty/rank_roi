
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

from setuptools import setup
from setuptools.command.install import install


class InstallAhelpWrapper(install):
    'A simple wrapper to run ahelp -r after install to update ahelp index'

    @staticmethod
    def update_ahelp_database():
        print("Update ahelp database ...")
        from subprocess import check_output
        sout = check_output(["ahelp","-r"])
        for line in sout.decode().split("\n"):
            for summary in ["Processed", "Succeeded", "Failed", "Purged"]:
                if line.startswith(summary):
                    print("    "+line)

    
    def run(self):
        install.run(self)
        self.update_ahelp_database()


setup( name='rank_roi',
       version='0.0.9',
       description='Assign overlap area to roi output files',
       author='Glotfelty',
       author_email='glotfeltyk@si.edu',
       url='https://github.com/kglotfelty/rank_roi/',
       scripts=["rank_roi", ],
       data_files=[('param',['rank_roi.par']),
                    ('share/doc/xml',['rank_roi.xml'])
                    ],
       cmdclass={'install': InstallAhelpWrapper},
    )

