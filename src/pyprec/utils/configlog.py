import os
import logging

# set package name
PACKAGE = __name__.split(".")[0]

# Log levels
LOG_DICT = {
    "0": logging.ERROR,
    "1": logging.WARNING,
    "2": logging.INFO,
    "3": logging.DEBUG,
}

# Read the pyprec log level environment variables
_log_level_idx = os.environ.get("PYPREC_LOG_LEVEL")

# Logging
_bad_log_warning = None
if _log_level_idx not in LOG_DICT:
    _bad_log_warning = _log_level_idx
    _log_level_idx = None

if _log_level_idx is None:
    # If no log level is provided, set some defaults
    _log_level = LOG_DICT["2"]
else:
    _log_level = LOG_DICT[_log_level_idx]

# Configure pyprec logging
logger = logging.getLogger(PACKAGE)
logger.setLevel(_log_level)

# Create and format the log handler
_console_handler = logging.StreamHandler()
_console_handler.setLevel(_log_level)
# _console_format = logging.Formatter("[%(levelname)s] (%(name)s) %(message)s")
_console_format = logging.Formatter("%(message)s")
_console_handler.setFormatter(_console_format)
logger.addHandler(_console_handler)
