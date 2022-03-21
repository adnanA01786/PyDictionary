import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyDictionary", # Replace with your own username
    version="3.0.0",
    author="Adnan Afzal",
    author_email="adnan01786@gmail.com",
    description="A real dictionary module for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geekpradd/PyDictionary",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'bs4',
        'click',
        'requests'
    ]
)
