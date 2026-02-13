from setuptools import setup, find_packages

setup(
    name = "euroncal",
    version  = "0.1.0",
    author  ="Prince Francis",
    author_email=  "prince.francis64@gmail.com",
    description= "A simple calculator package",
    long_description = open("README.md","r",encoding = "utf-8").read(),
    long_description_content_type="text,markdown",
    packages = find_packages(),
    python_requires = ">=3.6",
    entry_points = {
        "console_scripts":[
            "euroncal = euron_cal_package.calculator:main"
        ],
    },
classifiers= [
    "Programming Language :: Python :; 3",
    "License :: OSI Approved :: MIT License",
    "Operation System :: OS Independent"
]
)