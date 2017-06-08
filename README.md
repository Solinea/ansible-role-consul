# ansible-role-consul

https://travis-ci.org/Solinea/ansible-role-consul.svg?branch=master

## Purpose:
A simple role to install consul

## Testing 
This role is instrumented with the [`Molecule`](https://molecule.readthedocs.io/en/stable-1.25/) test harness. To run it, install `Molecule` with pip
 ```commandline
$ pip install ansible
$ pip install docker
$ pip install molecule
```
then execute the tests like this
```commandline
$ molecule test 
```
