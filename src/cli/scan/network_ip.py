import logging

from cli.rootcli import scan

logger = logging.getLogger(__name__)


@scan.command()
def ip():
    """Command on cli1"""
