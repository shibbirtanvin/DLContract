# Badges

We apply for the three badges *Artifacts Evaluated - Functional*, *Artifacts Evaluated - Reusable*, and *Artifacts Available*. Here are the reasons why we believe that the artifact deserves the badges.


### Functional and Reusable
The artifact contains both the data and software components that is executable. We also automated the process of running the tool using command line interface. Specifically, our artifact contains the following to be fully functional.

1. All necessary environment and contract annotated Keras library needed to run the tool using sample buggy and correct DL programs from the collected benchmark.
2. We collected benchmark models and datasets from four prior works DeepLocalize, UMLAUT, AUTOTRAINER, NeuraLint which are listed below in the artifact.
    a. DeepLocalize : https://github.com/Wardat-ISU/DeepLocalize
    b. UMLAUT: https://github.com/BerkeleyHCI/umlaut
    c. AUTOTRAINER: https://github.com/shiningrain/AUTOTRAINER
    d. NeuraLint: https://github.com/neuralint/neuralint
3. We shared executable Python source codes and a simplified script to execute the tool. We also shared the scripts to execute all the DL programs from collected benchmarks.

We also provided detailed instructions for installation, environment setup, and running the tool with buggy and correct DL programs. Furthermore, we shared the following necessary components of the artifact to make it reusable:

* Instructions to create virtual Python environment and run the tool in that environment.
* We provided general instructions to run the tool on any operating system.
* Automatically install necessary packages from the requirements file.
* Provide shell script file to automate the process of installation, transferring DL Contract annotated Keras library files to required library directories  
* The experimental results including user study are shared in the repository as the artifact, which are used in the paper.


### Available
The artifact is publicly shared in the GitHub repository: `https://github.com/shibbirtanvin/DLContract`.
Furthermore, the latest release is published in Zenodo and a DOI is obtained:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.TODO.svg)](https://doi.org/10.5281/zenodo.TODO)
