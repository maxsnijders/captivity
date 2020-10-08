import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="captivity",
    version="0.1",
    description="Cages in Pandas",
    long_description=long_description,
    author="Max Snijders",
    author_email="max@msnijders.com",
    copyright="Max Snijders",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        "methodtools==0.1.2",
        "pyyaml==5.3.1"
    ]
)
