# ansible-role-consul

[![Build Status](https://travis-ci.org/Solinea/ansible-role-consul.svg?branch=master)](https://travis-ci.org/Solinea/ansible-role-consul)

## Purpose:
A simple role to install [Hashicorp's consul](https://www.consul.io/)

## Testing 
This role is instrumented with the [`Molecule`](https://molecule.readthedocs.io/en/stable-1.25/) test harness. To run it, install `Molecule` with pip
 ```commandline
$ pip install ansible
$ pip install docker
$ pip install molecule==1.25
$ pip install testinfra==1.6.4
```
then execute the tests like this
```commandline
$ molecule test 
```
