trm.cline
=========

``trm.cline`` handles parameter input for Python scripts, interpreting
those entered on the command line, and internally prompting for those
not given according to names defined within the scripts. It uses disk
files to save the parameter values so that they can be recalled as
defaults on next invocation, potentially saving much typing. It also
allows multiple scripts to share parameters.

Installation
------------

``trm.cline`` uses standard Python throughout (but does require Python
3.6+). Install with::

 pip install trm.cline

to get via PyPI, or::

 pip install .

if you have cloned from github. If you don't have root access, replace
``pip install`` with ``pip install --user`` in the above commands to
get a local install.

* Free software: BSD license

