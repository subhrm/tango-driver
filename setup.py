from setuptools import setup, find_packages

'''
    To build run the command : python setup.py bdist_wheel 
'''

name, version = "", ""
# Get the name and version from tango_driver/__version__.py without importing the package
exec(compile(open('tango_driver/__version__.py').read(),
             'tango_driver/__version__.py', 'exec'))

print("%s - Building version %s" % (name, version))

setup(
    # Name of the project   (REQUIRED)
    name=name,
    version=version,


    # Long description (OPTIONAL)
    long_description='',

    # Project home page (OPTIONAL)
    url='http://infygit.ad.infosys.com/charminar/charminar-explorer-service',

    # Classifiers (OPTIONAL)
    # Valid list of classifiers - https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: MIT',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    # Keywords  (OPTIONAL)
    keywords='Exploer Makethon',

    # Project specific packages     (REQUIRED)
    # Specific packages can be manually added or use find_packages()
    packages=find_packages(),

    # List additional groups of dependencies    (OPTIONAL)
    extras_require={},

    python_requires='>=3.5',

    data_files=[],

    # Entry points for the project
    entry_points={
        'console_scripts': [
            'charminar-explorer-service = tango_driver:main'
        ],
    },
)
