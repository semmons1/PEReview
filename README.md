# PEReview
A Python project designed by Binary Analysis students, aimed specifically at analyzing suspicious .exe files. **Please** read the information below before you try running this package.  
## Preliminary requirements
This package requires the installation of the following modules:<br/>
**pefile**<br/>
**urlextract** NOTE: for urlextract  use `pip install urlextract` <br/>  
**idna**<br/>
**uritools**<br/>
**appdirs**<br/>
**requests**<br/>
These modules can/should be installed through the following examples:<br/>
If you prefer using Anaconda:<br/>
`conda install -c conda-forge <a_module_name>`<br/>
If you prefer using Python's package manager:<br/>
`pip install <a_module_name>`<br/>
Also, this package is designed to run with **Python 3.7**, so ensure that you are up-to-date with your Python version.
This package utilizes the API key of a poor student who uses the community addition of VirusTotal. This key is throttled to four requests a minute. You should/can replace the API key value in "riskAnalysis.py" with your own. After this assignment is submitted, I will be giving a proxy value for this key, as it is bad practice to have used the way I am using it.
## Running The Package
Start by opening a terminal or shell of your choice, and `cd` into the directory that you have placed this package in. Once in, type<br/> `python main.py`.<br/> Upon startup, you will be asked to choose the directory that holds a/some suspicious files. Once selected, the scripts will take care of everything, wait patiently for a new webpage to be generated.
### Examples
Coming soon lol

