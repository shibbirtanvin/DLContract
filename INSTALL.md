# Installation and Usage

To run DLContract, we need to install Python 3.x, Python 3.7 is recommended. The current version has been tested on Python 3.7. It is recommended to install Python virtual environment for the tool. Furthermore, we used bash shell scripts to automate running benchmark and Python scripts. Below are step-by-step instructions to setup environment and run the tool.

### Environment Setup

Follow these steps to create a virtual environment and clone the DLContract repository.

1. Clone this repository and move to the directory using the terminal:

```
git clone https://github.com/shibbirtanvin/DLContract
cd ReproducibilityPackage/@Keras
```

2. Give execution permission using the following command:

```
chmod +x setup.sh
```

3. Run shell script using the following command to create a virtual environment:

```
./setup.sh
```

Please ensure all the following commands (in setup.sh) executed in MacOS (intel) or Linux terminal.
No need to add any new commands in setup.sh:

```
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
```

If required, run the following command to update pip on Python: `python3 -m pip install --upgrade pip`. Alternatively, you can follow the [Python documentation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) to install virtual environment on your machine.

In the setup.sh, ```PYTHON_VERSION="3.7"``` for Python 3.7.x is by default
However, it can be changed for the other version ```PYTHON_VERSION="3.8" ``` for Python 3.8.x

By default *motivExample.py* will be executed and *data normalization contract* will be shown as contract violation error.

4. To execute the motivating example buggy and correct programs execute following commands in the terminal:

```
source venv/bin/activate
python motivExampleBug.py
python motivExampleCorrect.py
```

### Run the DLContract tool on Buggy and Correct programs

#### Example Buggy DL programs
Navigate to the ExamplePrograms directory `cd ExamplePrograms/` with command line. To execute some sample buggy and correct python files from the collected benchmarks, execute following commands in the terminal

```
source venv/bin/activate
```
**Example1:**
```
python BuggyProgram1.py
```
The output from DL Contract annotated Keras library will demonstrate following the contract violation message:

```
contracts.interface.ContractException: Data should be normalized before training, should not be within range 0.0 and 255.0 ; So, after loading train and test data should be divided by value 255.0
```
**Example2:**
```
python BuggyProgram2.py
```
DL Contract shows below output indicating following bug:

```
contracts.interface.ContractException: For multiclass classification activation_func should be softmax
```
**Example3:**
```
python BuggyProgram3.py
```
The output from the DL Contract annotated Keras library with following contract violation will be shown as below:

```
contracts.interface.ContractException: loss_function should be categorical crossentropy
```

#### Example Correct DL programs

```
python CorrectProgram.py
```

There will be no contract violation and the DL program will yield better accuracy. The output will be shown as below:

```
val_loss: 0.0373 - val_accuracy: 0.9905
```
