import re
import ast
import setuptools

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('books/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(
        _version_re.search(f.read().decode('utf-8')).group(1)))

#with open('./requirements.txt', 'r') as f:
#    required = f.read().splitlines()

setuptools.setup(
    name='books-pyhton-wrappers',
    version=version,
    description='books-pyhton-wrappers',
    url='',
    author='Harshal Choudhari',
    author_email='harshal.c@amazatic.com',
    license='MIT',
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=[
        'httplib2==0.17.3',
        'urllib3==1.25.8',
    ]
)
