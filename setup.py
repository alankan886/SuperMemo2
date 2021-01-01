import os
import pathlib
from setuptools import setup, find_packages, Command

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
]

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')

setup(
    name='supermemo2',
    version='1.0.0',
    description='Implemented the SuperMemo-2/SM-2 algorithm for spaced repetition learning.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/alankan886/SuperMemo2',
    author='Alan Kan',
    author_email='',
    license='MIT',
    classifiers=classifiers,
    keywords='spaced-repetition SuperMemo-2 SM-2 SuperMemo Python',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['attrs'],
    cmdclass={
        'clean': CleanCommand,
    },
)
