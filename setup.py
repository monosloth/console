import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monosloth-console",
    version="0.0.1",
    license='MIT',
    author="monosloth",
    author_email="admin@monosloth.com",
    description="A command line utility for monosloth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/monosloth/console",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pyyaml'
    ],
)
