# **CG initial configurations for MD calculations on DNA Hydrogels **
---

This utility is a small program that generates the initial 
configurations that will be utilised in MD (Molecular Dynamics) 
simulations. These initial configurations are designed in a 
CG (Coarse Grained) fashion as described in the publication 
[Structural and Linear Elastic Properties of DNA Hydrogels by Coarse-Grained Simulation](https://christopherjness.github.io/papers/acs.macromol.8b01948.pdf) by Xing et. al.
This program includes further additions to the model designed by 
Xing et. al., which are discussed in the publication 
[On the Role of Flexibility in Linker-Mediated DNA Hydrogels](https://arxiv.org/pdf/1909.05611.pdf) 
by Stoev et. al.
The generated files are designed so that they can be used 
in MD simulations with [LAMMPS](https://lammps.sandia.gov/).

## **Getting started**

### **Prerequisites**
The program is written in Python 3.6 
It is suggested that the user creates a virtual environment. 
Such packages for creating and using virtual environments are 
[mkvirtualenv](https://realpython.com/python-virtual-environments-a-primer/) 
and [pyenv](https://realpython.com/intro-to-pyenv/).
After initialising a virtual environment, the user 
has to install the package requirements with the command 
`pip install -r requirements.txt`.


## **Information on input and output**
The program provides a  variation of argumants that can be parsed. 
These are:
1. `-g` for generating a new configuration.
2. `-r` for plotting an existing configuration.


### **Example output**

## **Further Amendments**
There is a number of corrections/amendments that will be done 
in due time. These include:

## **Authors** 
If you have any suggestions/corrections, 
please contct [Iria Pantazi](iria.a.pantazi@gmail.com).


