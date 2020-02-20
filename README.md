# **CG initial configurations of DNA Hydrogels for MD**
---

This is a set of programs with codes for the generation of CG
(Coarse Grained) initial configurations of building blocks that 
are used MD (Molecular Dynamics) simulations of DNA hydrogels.

## **Introduction**
Even if DNA is widely known as the molecule that encodes all biological information in living organisms, 
it is also a building block that can be used in DNA Nanotechnology. 
DNA has been used as a structural material for nanoscale devices, and can be 
used for biomedical applications, and therapeutics.
A group of promissing materials for controlled drug delivery are polymeric 
networks made entirely of DNA building blocks, called DNA hydrogels.
A key objective in DNA-based material science is understanding and precisely 
controlling the mechanical properties of DNA hydrogels. For this purpose, 
microrheology is employed by the group of  
[Prof Erika Eiser](https://www.pnas.org/content/pnas/115/32/8137.full.pdf). 


The initial configurations that will be utilised in MD 
simulations. These initial configurations are designed in a 
CG fashion as described in the publication 
[Structural and Linear Elastic Properties of DNA Hydrogels by Coarse-Grained Simulation](https://christopherjness.github.io/papers/acs.macromol.8b01948.pdf) by Xing et. al.
This program includes further additions to the model designed by 
Xing et. al., which are discussed in the publication 
[On the Role of Flexibility in Linker-Mediated DNA Hydrogels](https://arxiv.org/pdf/1909.05611.pdf) 
by Stoev et. al.
The generated files are designed so that they can be used 
in MD simulations with [LAMMPS](https://lammps.sandia.gov/).

## **Getting started**
The directories are arranged:

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
The program provides a  variation of arguments that can be parsed. 
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


