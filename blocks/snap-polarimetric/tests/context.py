"""
This module is used in test_snap_polarimetry script.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../libs')))

from snap_polarimetry import SNAPPolarimetry  # pylint: disable=unused-import,wrong-import-position
from helper import LOG_FORMAT, get_logger, load_params, ensure_data_directories_exist  # pylint: disable=unused-import,wrong-import-position,line-too-long
