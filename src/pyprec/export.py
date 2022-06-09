"""This module"""
import logging
from pathlib import Path

from .pyexporter import load_fill_and_export
from .utils.utils import boldface
from pyprec import PACKAGE

logger = logging.getLogger(PACKAGE)


def create_folder_tree(source_folder: Path):
    """Creates the source directory tree.

    Directory tree is:

    .. code-block:: text
        root
        |-- source_folder # ``src/<pkgname>``
        |       |-- scripts
        |       |-- utils


    Parameters
    ----------
    source_folder: Path
        The folder to create the package source files to.

    Raises
    -------
    FileExistsError
        If the source directory already exists.
    """
    source_folder.parent.mkdir(parents=True)
    source_folder.mkdir()
    source_folder.joinpath("scripts").mkdir()
    source_folder.joinpath("utils").mkdir()


def create_package_light(setup: dict):
    """Light wrapper function to copy template in package destination folder.

    Parameters
    ----------
    setup: dict
        The key-value pairs to be inserted in the template fields.
    """
    prefix_folder = setup["prefix_folder"]
    source_folder = prefix_folder / f"src/{setup['pkgname']}"
    create_folder_tree(source_folder)

    # __init__ files
    source_folder.joinpath("scripts/__init__.py").touch()
    source_folder.joinpath("utils/__init__.py").touch()
    load_fill_and_export("initfile.inc", setup, source_folder / "__init__.py")

    # setup files
    load_fill_and_export("pyproject.inc", setup, prefix_folder / "pyproject.toml")
    load_fill_and_export("setup.inc", setup, prefix_folder / "setup.cfg")

    # configlog file
    utils_folder = source_folder / "utils"
    load_fill_and_export("configlog.inc", setup, utils_folder / "configlog.py")

    # entry point file
    script_folder = source_folder / "scripts"
    load_fill_and_export(
        "main_script.inc", setup, script_folder / f"{setup['pkgname']}.py"
    )

    msg = boldface(
        f"{setup['pkgname']} package successfully created at {prefix_folder}"
    )
    logger.info(msg)
