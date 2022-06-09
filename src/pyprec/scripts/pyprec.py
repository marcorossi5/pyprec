import argparse
from pathlib import Path
from ..ui import ui, load_setup_from_runcard
from ..export import create_package_light


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--runcard", type=Path, help="The settings runcard file.")
    args = parser.parse_args()

    setup = load_setup_from_runcard(args.runcard) if args.runcard is not None else ui()

    create_package_light(setup)
