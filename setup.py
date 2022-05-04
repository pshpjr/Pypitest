import setuptools

setuptools.setup(

include_package_data = True,

name='MyFirstPypi-pshpjr', # 패키지 명

version='0.1',

description='Test Package',

author='pshpjr',

author_email='pshpjr@naver.com',

classifiers = ["Programming Language :: Python ::3", "Operation System :: OS.Indepentent",],

url='https://github.com/pshpjr/Pypitest',

license='MIT',

py_modules=['output'], 

install_requires=["pytest"], 

packages=['firstModul'] 

)
