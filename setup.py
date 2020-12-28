from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='supermemo2',
    version='1.0.0',
    description='Implements the SuperMemo-2/SM-2 algorithm for spaced repetition learning.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alankan886/SuperMemo2',
    author='Alan Kan',
    author_email='',
    license='MIT',
    classifiers=classifiers,
    keywords='spaced-repetition SuperMemo-2 SM-2 SuperMemo',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['']
)
