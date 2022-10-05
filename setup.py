from setuptools import setup, find_packages


setup(
    name="backropy",
    version="0.1.0",
    description="...",
    author="Will Roper",
    author_email="w.roper@sussex.ac.uk",
    url="https://github.com/WillJRoper/backronym_generator",
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        "console_scripts": ["backronym=backropy.main:main"]
    },
)
