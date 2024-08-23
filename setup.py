from setuptools import setup

with open("README.md") as f:
    readme = f.read()

setup(
    version="0.0.1",
    name="salesforce-marketing-cloud-python-sdk",
    description="Salesforce Marketing Cloud Fuel SDK for Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="ExactTarget",
    py_modules=["ET_Client"],
    packages=["FuelSDK"],
    license="MIT",
    install_requires=[
        "pyjwt",
        "requests>=2.18.4",
        "suds-community>=1.1.1",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
    ],
)
