# PyPReC: Python Package Repository Creator

This package automates the process of repository creation for Python packages.

## Installation

The package can be installed with Python's pip package manager.

```bash
pip install pyprec
```

Or manually:

```bash
git clone https://github.com/marcorossi5/pyprec.git
cd pyprec
pip install .
```

The last command installs the `pyprec` program into the environment python path.

## Running the code

Package help message:

```bash
$ bash --help
usage: pyprec [-h] [-r RUNCARD]

optional arguments:
  -h, --help            show this help message and exit
  -r RUNCARD, --runcard RUNCARD
                        The settings runcard file.
```

If a runcard is specified, settings are loaded from it. Please, find a default
runcard [here](./cards/default_runcard.yaml).

If no runcard is given by the user, the interactive mode is triggered: answer
the prompted questions to proceed.

:warning: **Note:**  
Both modes require that the `prefix_folder` does not contain any `src` folder
inside. This is needed to ensure a clean workspace and avoid unintentional file
deletion.
