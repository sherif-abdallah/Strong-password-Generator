from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: MacOS :: Windows :: Linux',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pyrand',
  version='0.0.1',
  description='Strong Password by Chosing The characters of password',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='http://sherif.rf.gd/',  
  author='Sherif Abdullah',
  author_email='sherifabdalla2005@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='random', 
  packages=find_packages(),
  install_requires=[''] 
)
