import os
import pathlib
from setuptools import setup, find_packages, Command

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]

with open("README.md", encoding="utf-8") as f:
    readme_content = f.read().strip()


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system("rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info")


setup(
    name="supermemo2",
    version="3.0.1",
    description="Implemented the SM-2 algorithm for spaced repetition learning.",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    url="https://github.com/alankan886/SuperMemo2",
    author="Alan Kan",
    author_email="",
    license="MIT",
    classifiers=classifiers,
    keywords="spaced-repetition SM-2 SuperMemo Python",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["attrs"],
    cmdclass={
        "clean": CleanCommand,
    },
)
