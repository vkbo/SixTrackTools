# -*- coding: utf-8 -*
"""Python Toolbox for SixTrack, HDF5 Submodule

  SixTrack Tools - HDF5 Tools
 =============================
  Python Toolbox for SixTrack, HDF5 Submodule
  By: Veronica Berglyd Olsen
      CERN (BE-ABP-HSS)
      Geneva, Switzerland

"""

import logging

# Submodules
from .concatenator import Concatenator
from .wrapper      import H5Wrapper

__all__ = ["Concatenator","H5Wrapper"]

# Logging
logger   = logging.getLogger(__name__)
logLevel = logging.DEBUG

if logLevel == logging.DEBUG:
    logging.basicConfig(
        format  = "[%(asctime)s] %(name)s:%(lineno)d %(levelname)s: %(message)s",
        level   = logging.DEBUG,
        datefmt = "%Y-%m-%d %H:%M:%S",
    )
else:
    logging.basicConfig(
        format  = "%(levelname)s: %(message)s",
        level   = logLevel,
        datefmt = "%H:%M:%S",
    )