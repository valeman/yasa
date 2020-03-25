"""Test I/O."""
import logging
import unittest
from yasa.io import (set_log_level, is_tensorpac_installed,
                     is_pyriemann_installed)

logger = logging.getLogger('yasa')
levels = ['debug', 'info', 'warning', 'error', 'critical']


class TestIO(unittest.TestCase):
    """Test IO functions."""

    def test_log_level(self):
        """Test setting the log level."""
        for l in levels:
            set_log_level(l)
        set_log_level(False)
        set_log_level(True)
        set_log_level(None)

    def test_logger(self):
        """Test logger levels."""
        logger.debug("debug")
        logger.info("info")
        logger.warning("warning")
        logger.critical("critical")

    def test_dependence(self):
        """Test dependancies."""
        is_tensorpac_installed()
        is_pyriemann_installed()
