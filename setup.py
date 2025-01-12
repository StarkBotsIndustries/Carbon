# Carbon - Create beautiful carbon code images using python or terminal
# Copyright (C) 2022 Stark Bots <https://github.com/StarkBotsIndustries>
#
# This file is part of Carbon.
#
# Carbon is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Carbon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Carbon. If not, see <https://www.gnu.org/licenses/>.


import re
from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = "\n".join([x for x in f.read().split("\n") if not x.startswith('>')])

with open("requirements.txt", encoding="utf-8") as r:
    install_requires = [i.strip() for i in r if not i.startswith('#')]

with open("carbon/_constants.py", "r", encoding="utf-8") as f:
    text = f.read()
    pat = r"['\"]([^'\"]+)['\"]"
    version = re.search("__version__ = "+pat, text).group(1)
    description = re.search("__description__ = "+pat, text).group(1)


setup(
    name='carbon-api',
    packages=["carbon"],
    version=version,
    license='LGPLv3+',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='StarkProgrammer',
    author_email='starkbotsindustries@gmail.com',
    url='https://github.com/StarkBotsIndustries/Carbon',
    keywords=['carbon', 'carbon-now', 'cli', 'python'],
    install_requires=install_requires,
    zip_safe=False,
    python_requires=">=3.9",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Natural Language :: English',
        'Topic :: Communications :: Chat',
        'Topic :: Education :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    project_urls={
        "Support": "https://t.me/StarkBotsChat",
        "Community": "https://t.me/StarkBots",
    },
    entry_points={
        'console_scripts': [
            'carbon-app = carbon._cli:main',
        ],
    },
)
