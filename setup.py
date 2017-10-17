from setuptools import setup
import os

def read(f):
    return open(os.path.abspath(f)).read().strip()

datadir = os.path.join('query_understanding','dataset')

datafiles = [(d, [os.path.join(d, f) for f in files])
             for d, folders, files in os.walk(datadir)]
print(datafiles)
setup(
    name='query_understanding',
    packages=['query_understanding'],
    version='1.0.3',
    description='Universal encoding detector',
    author='Kunal Gupta and Moghira Rahman',
    author_email='kunal1340@iiitd.ac.in',
    py_modules=['query_understanding.annotate', 'query_understanding.color', 'query_understanding.gender',
                'query_understanding.price', 'query_understanding.shop', 'query_understanding.size',
                'query_understanding.spell_checker', 'query_understanding.term'],
    data_files=datafiles,
    install_requires=['jellyfish', 'fuzzywuzzy', 'nltk'],
    url='https://github.com/DataEngg/Query-Understanding',
)
