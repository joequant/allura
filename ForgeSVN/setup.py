#       Licensed to the Apache Software Foundation (ASF) under one
#       or more contributor license agreements.  See the NOTICE file
#       distributed with this work for additional information
#       regarding copyright ownership.  The ASF licenses this file
#       to you under the Apache License, Version 2.0 (the
#       "License"); you may not use this file except in compliance
#       with the License.  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#       Unless required by applicable law or agreed to in writing,
#       software distributed under the License is distributed on an
#       "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#       KIND, either express or implied.  See the License for the
#       specific language governing permissions and limitations
#       under the License.

from setuptools import setup, find_packages
import sys, os

from forgesvn.version import __version__

# "install_requires" can't be safely used with pysvn since pysvn is packaged
# strangely and is not always known to packaging tools (setup.py, pip) even
# when it is installed and can be imported and used
try:
    import pysvn
except ImportError:
    print '\npysvn must be installed for ForgeSVN to work\n'
    raise

setup(name='ForgeSVN',
      version=__version__,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'Allura'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [allura]
      SVN=forgesvn.svn_main:ForgeSVNApp
      """,
      )
