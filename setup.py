from pathlib import Path

from setuptools import setup, find_namespace_packages

from sequence.__version__ import __version__

long_description = Path("README.md").read_text()

setup(
    name="sequentium",
    version=f"{__version__}",
    license="MIT",
    author="Vasco Schiavo",
    author_email="vasco.schiavo@protonmail.com",
    url="https://github.com/VascoSch92/sequentium",
    description="Sequentium is a user-friendly package that implements various well-known sequences, providing a "
    "seamless and intuitive experience for the user",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_namespace_packages(include=["sequence*"], exclude=["tests"]),
    entry_points={"console_scripts": ["sequence=sequence:main"]},
    # download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords=["math", "mathematics", "sequence", "fibonacci"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.9",
)
