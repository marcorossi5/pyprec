import argparse
import logging
from pathlib import Path
from ..ui import ui, load_setup_from_runcard
from ..export import create_package_light
from pyprec import PACKAGE

logger = logging.getLogger(PACKAGE)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--runcard", type=Path, help="The settings runcard file.")
    log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    parser.add_argument(
        "-l", default=None, help="set logging level", choices=log_levels, dest="logging"
    )
    args = parser.parse_args()

    if args.logging:
        logger.setLevel(args.logging)
        logger.handlers[0].setLevel(args.logging)
        logger.warning(f"Log level set to {args.logging}")

    setup = load_setup_from_runcard(args.runcard) if args.runcard is not None else ui()

    create_package_light(setup)
