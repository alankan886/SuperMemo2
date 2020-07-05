from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
]

setup(
  name='supermemo2',
  version='0.0.2',
  description='Implements the SuperMemo-2/SM-2 algorithm for spaced repetition learning.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
  url='https://github.com/alankan2004/SuperMemo2',  
  author='Alan Kan',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='spaced-repetition SuperMemo-2 SM-2 SuperMemo',
  packages=find_packages(exclude=['tests', 'test_*']),
  exclude_package_data={"": ['tests']},
  install_requires=[''] 
)
