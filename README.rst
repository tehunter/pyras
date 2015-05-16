.. image:: https://pypip.in/version/PyRAS/badge.svg
   :target: https://pypi.python.org/pypi/PyRAS/
   :alt: Latest PyPI version

.. image:: https://pypip.in/download/PyRAS/badge.svg
   :target: https://pypi.python.org/pypi/PyRAS/
   :alt: Number of PyPI downloads

.. image:: https://pypip.in/py_versions/PyRAS/badge.svg
   :target: https://pypi.python.org/pypi/PyRAS/
   :alt: Supported python version
   
.. image:: https://pypip.in/license/PyRAS/badge.svg

   
PyRAS - Python for River AnalysiS
=================================

DISCLAIMER
----------
This module is under development and is considered a beta-release (not suitable for production use yet). 
The API will most likelly change during this development process with the help of any feedback received from
potential beta testers.


Description
-----------

A Python suite for working with river models. 

Goals
-----
Offer an abstraction layer for the definition of river models and tools to operate on this models
or when possible calling the model engine (controller). So far the library offers:

* **HEC-RAS**: Wrapper for the COM interface of the HEC-RAS controller. (windows only)

For the upcoming developments this library will define a pythonic interface to different objects
found in the HEC-RAS river model (sections, structures, nodes etc).


Requirements
------------

This package depends on pywin32 for accessing the HECRASController interface.

Additionally, you need to have a working version of HEC-RAS installed. 
Current support includes version 4.1.0 and 5.0.0.


Installation
------------

**The easy way:**

1. Install the anaconda distribution (comes with PyWin32 preinstalled)

2. On the command line type:

.. code-block:: python

	pip install pyras --upgrade

**The hard way:**

1. Install python

2. Download pywin32 installer from the `project webpage`_  and install.

3. On the command line type:

.. code-block:: python

	pip install pyras --upgrade
	
License
-------

MIT License. Copyright 2015 - Gonzalo Peña-Castellanos


Status
------
This is a project under development and is currently in beta testing.

Although the project should be compatible with python versions 2.6, 2.7, 3.1,
3.2, 3.3 and 3.4, the project will only provide testing for 2.7, 3.3 and 3.4

.. _project webpage: http://sourceforge.net/projects/pywin32/files/
