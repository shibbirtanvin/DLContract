------------------------------------
The reproducibility package contains:
------------------------------------
1) DlContract source code (sourceFiles.zip)
3) @Keras environment (@Keras.zip) with Buggy code and correct code demonstrated as motivation example with Instructions.txt
3) URL of the Benchmarks 
4) Scripts to execute all the codes in the respective benchmarks (scripts.zip)

----------------------------------
Instructions for reproducibility: (Instructions.txt)
----------------------------------
Requirements: Need to install Python 3.x, 3.7 is recommended.

1. open terminal at the downloaded folder
2. give execution permission using the following command: 
	chmod +x setup.sh
3. run shell script using the following command: 
	./setup.sh
4. By default motivExample.py will be executed and data normalization contract will be shown as contract violation error.

5. In the setup.sh, 
	PYTHON_VERSION="3.7" for Python 3.7.x is by default
   Can be changed for the other version
	PYTHON_VERSION="3.8" for Python 3.8.x
6. To execute buggy and correct python files, execute in the terminal following commands:
         source venv/bin/activate
	 python motivExampleBug.py 
         python motivExampleCorrect.py 
 

----
Please ensure all the following commands (in setup.sh) executed in MacOS (intel) or Linux terminal.
setup.sh
---
#!/bin/sh

PYTHON_VERSION="3.7"

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cp -f Augkeras/training.py venv/lib/python$PYTHON_VERSION/site-packages/tensorflow/python/keras/engine/
cp -f Augkeras/core.py venv/lib/python$PYTHON_VERSION/site-packages/tensorflow/python/keras/layers/
cp -f DLContract/* venv/lib/python$PYTHON_VERSION/site-packages/contracts
source venv/bin/activate
python motivExample.py

--
requirements.txt
--
Required Packages:
keras -version 2.4.3
tensorflow - version 2.2.0
PyContracts -version 1.8.12
decorator - version 4.0.10
numpy -version 1.19.2
pandas -version 1.1.5
pip -version 19.0.3
pyparsing -version 2.2.2
Scikit-learn -version 0.21.2
Scipy -version 1.6.0

--- 
