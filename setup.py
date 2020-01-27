import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AZMPNNtoolbox", # Replace with your own username
    version="0.0.1",
    author="M. Withnall, E. Lindelöf, O. Engkvist & H. Chen. Packed by JP Janet",
    description="Python packed version of original scripts at ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edvardlindelof/graph-neural-networks-for-drug-discovery",
    packages=setuptools.find_packages(),
    install_requires=["torch","scikit-learn"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
