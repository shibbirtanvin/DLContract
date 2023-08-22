# DLContract

This repository contains the reproducibility package, source code, benchmark, and results for the paper - **"Design by Contract for Deep Learning APIs"**, which appeared in ESEC/FSE’2023: The 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering at San Francisco, California.

### Authors
* Shibbir Ahmed, Iowa State University (shibbir@iastate.edu)
* Sayem Mohammad Imtiaz, Iowa State University (sayem@iastate.edu)
* Samantha Syeda Khairunnesa, Bradley University (skhairunnesa@fsmail.bradley.edu)
* Breno Dantas Cruz, Iowa State University (bdantasc@iastate.edu)
* Hridesh Rajan, Iowa State University (hridesh@iastate.edu)

**PDF** [DLContract Paper at_ESEC/FSE2023](https://github.com/shibbirtanvin/DLContract/blob/main/DLContractPaper_ESECFSE23.pdf)

**DOI:** This artifact is also published in Zenodo:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8271853.svg)](https://doi.org/10.5281/zenodo.8271853)


## Index
> 1. [Reproducibility Package](ReproducibilityPackage/)
  >> * [Installation and reproducibility instructions](INSTALL.md)
  >> * [DLContract annotated Keras environment](ReproducibilityPackage/@Keras)
  >> * [DLContract source code](ReproducibilityPackage/sourceFiles)
  >> * [Scripts to execute all the codes in the collected benchmarks](ReproducibilityPackage/scripts)
  >> * [Collected Benchmarks from publicly available URLs](ReproducibilityPackage/BenchmarksURLs.txt)
> 2. Example Programs
  >> * [Motivating example](ExamplePrograms/MotivatingExample)
  >> * [Some buggy and correct DL programs](ExamplePrograms/BuggyCorrectDLPrograms)
> 3. Experimental Results
  >> * [Experimental evaluation results comparing other techniques](Results/ExperimentalEvaluation)
  >> * [User study](Results/UserStudy)
  >  >> * [Instructions to participant for the user study](Results/UserStudy/InstructionsParticipantUserStudy.pdf)
  >  >> * [Survey results](Results/UserStudy/SurveyResults)
> 4. Appendix
  >> * [Appendix list of DL Contracts](Appendix/ListofContracts.pdf)

## Installation

To run DLContract, we need to install Python 3.x, Python 3.7 is recommended. The current version has been tested on Python 3.7. It is recommended to install Python virtual environment for the tool. Furthermore, we used bash shell scripts to automate running benchmark and Python scripts. Below are step-by-step instructions to setup the environment and run the tool.

### Environment Setup

Follow these steps to create a virtual environment and clone the DLContract repository.

1. Clone this repository and move to the directory using the terminal:

```
git clone https://github.com/shibbirtanvin/DLContract
cd DLContract/ReproducibilityPackage/@Keras
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

In the setup.sh, ```PYTHON_VERSION="3.7"``` for Python 3.7.x is by default
However, it can be changed for the other version ```PYTHON_VERSION="3.8" ``` for Python 3.8.x

If required, run the following command to update pip on Python: `python3 -m pip install --upgrade pip`. Alternatively, you can follow the [Python documentation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) to install virtual environment on your machine.

By default *motivExample.py* will be executed and *data normalization contract* will be shown as contract violation error.

4. To execute the motivating example buggy and correct programs execute the following commands in the terminal:

```
source venv/bin/activate
python motivExampleBug.py
python motivExampleCorrect.py
```

To run the tool with more sample example Buggy and Correct programs with example outputs, please refer to the [installation file](/INSTALL.md) for detailed instructions. The scripts to execute all DL programs from collected benchmarks are provided here in the [scripts to execute all the codes in the collected benchmarks](ReproducibilityPackage/scripts).

### Cite the paper as
```
@inproceedings{ahmed23dlcontract,
  author = {Shibbir Ahmed and Sayem Mohammad Imtiaz and Samantha Syeda Khairunnesa and Breno Dantas Cruz and Hridesh Rajan},
  title = {Design by Contract for Deep Learning APIs},
  booktitle = {ESEC/FSE'2023: The 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering},
  location = {San Francisco, California},
  month = {December 03-December 09},
  year = {2023},
  entrysubtype = {conference},
  abstract = {
    Deep Learning (DL) techniques are increasingly being incorporated in critical software systems today. DL software is buggy too. Recent work in SE has characterized these bugs, studied fix patterns, and proposed detection and localization strategies. In this work, we introduce a preventative measure. We propose design by contract for DL libraries, DL Contract for short, to document the properties of DL libraries and provide developers with a mechanism to identify bugs during development. While DL Contract builds on the traditional design by contract techniques, we need to address unique challenges. In particular, we need to document properties of the training process that are not visible at the functional interface of the DL libraries. To solve these problems, we have introduced mechanisms that allow developers to specify properties of the model architecture, data, and training process. We have designed and implemented DL Contract for Python-based DL libraries and used it to document the properties of Keras, a well-known DL library. We evaluate DL Contract in terms of effectiveness, runtime overhead, and usability. To evaluate the utility of DL Contract, we have developed 15 sample contracts specifically for training problems and structural bugs. We have adopted four well-vetted benchmarks from prior works on DL bug detection and repair. For the effectiveness, DL Contract correctly detects 259 bugs in 272 real-world buggy programs, from well-vetted benchmarks provided in prior work on DL bug detection and repair. We found that the DL Contract overhead is fairly minimal for the used benchmarks. Lastly, to evaluate the usability, we conducted a survey of twenty participants who have used DL Contract to find and fix bugs. The results reveal that DL Contract can be very helpful to DL application developers when debugging their code.
  }
}
```
