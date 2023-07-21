"""Scanner module that run scanner command in daemon mode."""
import asyncio
import logging
import sys

import click

from ostorlab.cli import console as cli_console
from ostorlab.cli.rootcli import rootcli
from ostorlab.scanner import start

console = cli_console.Console()

logger = logging.getLogger(__name__)


@rootcli.command()
@click.option("--scanner-id", help="The scanner identifier.", required=True)
@click.option("--daemon/--no-daemon", help="Run in daemon mode", default=True)
@click.pass_context
def scanner(
    ctx: click.core.Context,
    daemon: bool,
    scanner_id: str,
) -> None:
    """Ostorlab scanner enables running custom instances of scanners.
    Scanners communicates with NATs to receive start scan messages.\n
    """
    if sys.platform != "linux":
        console.error("ostorlab scanner sub-command is only supported on Unix systems.")
        raise click.exceptions.Exit(2)

    # The import is done for Windows compatibility.
    import daemon as dm  # pylint: disable=import-outside-toplevel

    if daemon is True and ctx.obj.get("api_key") is not None:
        with dm.DaemonContext():
            start_nats_subscription_asynchronously(ctx.obj.get("api_key"), scanner_id)
    elif daemon is False and ctx.obj.get("api_key") is not None:
        start_nats_subscription_asynchronously(ctx.obj.get("api_key"), scanner_id)


def start_nats_subscription_asynchronously(api_key: str, scanner_id: str) -> None:
    """Run subscription to nats in eventloop.

    Args:
        api_key: The api key to login to the platform.
        scanner_id: The id of the scanner.
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        start.subscribe_to_nats(api_key=api_key, scanner_id=scanner_id)
    )
    try:
        logger.info("starting forever loop")
        loop.run_forever()
    finally:
        logger.info("closing loop")
        loop.close()
