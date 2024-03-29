"""Tests for scan run command."""

import pathlib

from pytest_mock import plugin
import httpx
import pytest
from click.testing import CliRunner

from ostorlab.cli import rootcli
from ostorlab import exceptions
from ostorlab.cli.scan.run import run


def testOstorlabScanRunCLI_whenNoOptionsProvided_showsAvailableOptionsAndCommands(
    mocker,
):
    """Test ostorlab scan command with no options and no sub command.
    Should show list of available commands and exit with exit_code = 0."""

    runner = CliRunner()
    mocker.patch("ostorlab.runtimes.local.LocalRuntime.__init__", return_value=None)
    result = runner.invoke(rootcli.rootcli, ["scan", "run"])
    assert "Usage: rootcli scan run [OPTIONS] COMMAND [ARGS]..." in result.output
    assert "Commands:" in result.output
    assert "Options:" in result.output
    assert result.exit_code == 2


def testRunScanCLI_WhenAgentsAreInvalid_ShowError(mocker):
    """Test ostorlab scan command with all options and no sub command.
    Should show list of available commands (assets) and exit with error exit_code = 2.
    """

    mocker.patch(
        "ostorlab.runtimes.local.runtime.LocalRuntime.can_run", return_value=False
    )
    runner = CliRunner()
    mocker.patch("ostorlab.runtimes.local.LocalRuntime.__init__", return_value=None)
    result = runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "--runtime=local",
            "run",
            "--agent=agent1",
            "--title=scan1",
            "android-apk",
        ],
    )

    assert isinstance(result.exception, BaseException)


@pytest.mark.docker
def testRunScanCLI_WhenNoConnection_ShowError(mocker):
    """Test ostorlab scan command with all options and no sub command.
    Should show list of available commands (assets) and exit with error exit_code = 2.
    """

    mocker.patch(
        "ostorlab.runtimes.cloud.runtime.CloudRuntime.can_run", return_value=True
    )
    mocker.patch("ostorlab.runtimes.local.LocalRuntime.__init__", return_value=None)
    mocker.patch(
        "ostorlab.runtimes.local.LocalRuntime.install",
        side_effect=httpx.ConnectError("No internet connection"),
    )
    api_ubjson_requests = mocker.patch(
        "ostorlab.apis.runners.authenticated_runner.AuthenticatedAPIRunner.execute_ubjson_request"
    )

    api_requests = mocker.patch(
        "ostorlab.apis.runners.authenticated_runner.AuthenticatedAPIRunner.execute"
    )
    agent_details_reponse = {
        "data": {
            "agent": {
                "name": "whatweb",
                "gitLocation": "https://github.com/Ostorlab/agent_whatweb",
                "yamlFileLocation": "ostorlab.yaml",
                "dockerLocation": "ostorlab.store/agents/agent_5448_whatweb",
                "access": "PUBLIC",
                "listable": True,
                "key": "agent/ostorlab/whatweb",
                "versions": {"versions": [{"version": "0.1.12"}]},
            }
        }
    }

    agent_group_response = {"data": {"publishAgentGroup": {"agentGroup": {"id": "1"}}}}
    asset_response = {"data": {"createAsset": {"asset": {"id": 1}}}}
    scan_response = {"data": {"createAgentScan": {"scan": {"id": 1}}}}
    api_responses = [
        agent_details_reponse,
        asset_response,
        scan_response,
    ]
    api_ubjson_responses = [
        agent_group_response,
    ]

    api_requests.side_effect = api_responses
    api_ubjson_requests.side_effect = api_ubjson_responses
    runner = CliRunner()
    result = runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "--runtime=local",
            "run",
            "--install",
            "--agent=agent/ostorlab/nmap",
            "--title=scan1",
            "ip",
            "127.0.0.1",
        ],
    )
    assert (
        "Error: Could not install the agents: No internet connection\n" in result.output
    )
    assert result.exit_code == 1


def testRunScanCLI__whenValidAgentsAreProvidedWithNoAsset_ShowSpecifySubCommandError(
    mocker,
):
    """Test oxo scan run command with all valid options and no sub command.
    Should show list of available commands (assets) and exit with error exit_code = 2.
    """

    mocker.patch(
        "ostorlab.runtimes.local.runtime.LocalRuntime.can_run", return_value=True
    )
    runner = CliRunner()
    mocker.patch("ostorlab.runtimes.local.LocalRuntime.__init__", return_value=None)
    result = runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "--runtime=local",
            "run",
            "--agent=agent1 --agent=agent2",
            "--title=scan1",
        ],
    )

    assert "Error: Missing command." in result.output
    assert result.exit_code == 2


def testScanRunCloudRuntime_whenValidArgsAreProvided_CreatesAgGrAssetAndScan(mocker):
    """Unittest oxo scan run in cloud runtime with all valid options and arguments.
    Should send api requests for creating Agent group, asset & scan.
    And displays Scan created successfully.
    """

    mocker.patch(
        "ostorlab.runtimes.cloud.runtime.CloudRuntime.can_run", return_value=True
    )

    api_ubjson_requests = mocker.patch(
        "ostorlab.apis.runners.authenticated_runner.AuthenticatedAPIRunner.execute_ubjson_request"
    )

    api_requests = mocker.patch(
        "ostorlab.apis.runners.authenticated_runner.AuthenticatedAPIRunner.execute"
    )
    agent_details_reponse = {
        "data": {
            "agent": {
                "name": "nmap",
                "gitLocation": "https://github.com/Ostorlab/agent_whatweb",
                "yamlFileLocation": "ostorlab.yaml",
                "dockerLocation": "ostorlab.store/agents/agent_5448_nmap",
                "access": "PUBLIC",
                "listable": True,
                "key": "agent/ostorlab/nmap",
                "versions": {"versions": [{"version": "0.1.12"}]},
            }
        }
    }

    agent_group_response = {"data": {"publishAgentGroup": {"agentGroup": {"id": "1"}}}}
    asset_response = {"data": {"createAsset": {"asset": {"id": 1}}}}
    scan_response = {"data": {"createAgentScan": {"scan": {"id": 1}}}}
    api_responses = [
        agent_details_reponse,
        asset_response,
        scan_response,
    ]
    api_ubjson_responses = [
        agent_group_response,
    ]

    api_requests.side_effect = api_responses
    api_ubjson_requests.side_effect = api_ubjson_responses

    runner = CliRunner()
    result = runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "--runtime=cloud",
            "run",
            "--agent=agent/ostorlab/nmap",
            "--title=scan1",
            "ip",
            "127.0.0.1",
        ],
    )

    assert result.exception is None
    api_requests.assert_called()
    assert "Scan created successfully" in result.output


def testScanRunCloudRuntime_whenValidMultipleLinksGiven_CreatesAgGrAssetAndScan(mocker):
    """Unittest oxo scan run in cloud runtime with multiple links.
    Should send api requests for creating Agent group, asset & scan.
    And displays Scan created successfully.
    """

    mocker.patch(
        "ostorlab.runtimes.cloud.runtime.CloudRuntime.can_run", return_value=True
    )

    api_ubjson_requests = mocker.patch(
        "ostorlab.apis.runners.authenticated_runner.AuthenticatedAPIRunner.execute_ubjson_request"
    )

    api_requests = mocker.patch(
        "ostorlab.apis.runners.authenticated_runner.AuthenticatedAPIRunner.execute"
    )
    agent_details_reponse = {
        "data": {
            "agent": {
                "name": "whatweb",
                "gitLocation": "https://github.com/Ostorlab/agent_whatweb",
                "yamlFileLocation": "ostorlab.yaml",
                "dockerLocation": "ostorlab.store/agents/agent_5448_whatweb",
                "access": "PUBLIC",
                "listable": True,
                "key": "agent/ostorlab/whatweb",
                "versions": {"versions": [{"version": "0.1.12"}]},
            }
        }
    }

    agent_group_response = {"data": {"publishAgentGroup": {"agentGroup": {"id": "1"}}}}
    asset_response = {"data": {"createAsset": {"asset": {"id": 1}}}}
    scan_response = {"data": {"createAgentScan": {"scan": {"id": 1}}}}
    api_responses = [
        agent_details_reponse,
        asset_response,
        scan_response,
    ]
    api_ubjson_responses = [
        agent_group_response,
    ]

    api_requests.side_effect = api_responses
    api_ubjson_requests.side_effect = api_ubjson_responses
    runner = CliRunner()

    result = runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "--runtime=cloud",
            "run",
            "--agent=agent1 --agent=agent2",
            "link",
            "--url",
            "https://ostorlab.co",
            "--method",
            "GET",
            "--url",
            "https://ostorlab.ma",
            "--method",
            "GET",
        ],
    )

    assert result.exception is None
    api_requests.assert_called()
    assert "Scan created successfully" in result.output


def testScanRun_whenNoAssetFlagWithInjectAssetSubCommand_raisesErrors(mocker):
    """Unittest to ensure scan run command fails when both --no-asset flag and
    inject asset sub-commands are provided."""
    mocker.patch(
        "ostorlab.runtimes.local.runtime.LocalRuntime.can_run", return_value=False
    )
    mocker.patch("ostorlab.runtimes.local.LocalRuntime.__init__", return_value=None)
    runner = CliRunner()

    result = runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "run",
            "--no-asset",
            "--agent=agent1",
            "--title=scan1",
            "ip",
            "8.8.8.8",
        ],
    )

    assert "Sub-command ip specified with --no-asset flag." in result.output


def testScanRunCloudRuntime_whenRuntimeRaisesException_showsErrorMessage(mocker):
    """Test error message shown when runtime fails and exits gracefully."""

    mocker.patch(
        "ostorlab.runtimes.local.runtime.LocalRuntime.can_run",
        side_effect=exceptions.OstorlabError("Error message"),
    )

    runner = CliRunner()
    result = runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "run",
            "--agent=agent/ostorlab/nmap",
            "ip",
            "127.0.0.1",
        ],
    )

    assert isinstance(result.exception, SystemExit) is True
    assert "Error message" in result.output


def testScanRunLocalRuntime_whenIInvalidYamlAgentGroupDefinition_showsErrorMessage(
    mocker: plugin.MockerFixture,
) -> None:
    """Ensure the Agent group definition YAML is handled gracefully when a parsing error is encountered."""
    invalid_agent_group = (
        pathlib.Path(__file__).parent / "invalid_agent_group_definition.yaml"
    )
    runner = CliRunner()

    result = runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "--runtime=cloud",
            "run",
            "-g",
            invalid_agent_group,
            "--title=invalid_scan",
            "ip",
            "127.0.0.1",
        ],
    )

    assert isinstance(result.exception, SystemExit)
    assert result.exit_code == 2
    assert "Agent group definition YAML parse error" in result.output


def testOstorlabScanRunCLI_whenWrongArgsFormatProvided_showsErrorMessage() -> None:
    """Test ostorlab scan command with wrong args format. Should show error message."""

    runner = CliRunner()
    result = runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "run",
            "--agent=agent/ostorlab/nmap",
            "--arg=test,test",
            "ip",
            "127.0.0.1",
        ],
    )

    assert (
        "Invalid argument test,test. The expected format is name:value."
        in result.output
    )


@pytest.mark.parametrize(
    "invalid_agent_key", ["/nmap", "@agent/ostorlab/nmap/", "agent/ostorlab/nmap/"]
)
def testOstorlabScanRunCLI_whenInvalidArgKey_showsErrorMessage(
    invalid_agent_key: str,
) -> None:
    """Test ostorlab scan command with wrong agent key. Should show error message."""

    runner = CliRunner()
    result = runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "run",
            f"--agent={invalid_agent_key}",
            "--arg=test,test",
            "ip",
            "127.0.0.1",
        ],
    )

    assert f"Invalid agent key: {invalid_agent_key}" in result.output


def testPrepareAgentsToFollow_whenNoFollow_shouldReturnEmptyList() -> None:
    """Test prepare_agents_to_follow function when no follow option is provided.
    Should return empty list.
    """
    result = run.prepare_agents_to_follow([], [], True)

    assert result == set()


def testPrepareAgentsToFollow_whenFollow_shouldReturnSpecifiedAgents() -> None:
    """Test prepare_agents_to_follow function when follow option is provided.
    Should return specified agents.
    """
    result = run.prepare_agents_to_follow(
        ["agent/ostorlab/nmap", "agent/ostorlab/asteroid"],
        ["agent/ostorlab/nmap"],
        False,
    )

    assert len(result) == 1
    assert "agent/ostorlab/nmap" in result


def testPrepareAgentsToFollow_whenDefault_shouldReturnAllAgents() -> None:
    """Test prepare_agents_to_follow function when follow option is provided.
    Should return specified agents.
    """
    result = run.prepare_agents_to_follow(
        ["agent/ostorlab/nmap", "agent/ostorlab/asteroid"], [], False
    )

    assert len(result) == 2
    assert "agent/ostorlab/nmap" in result
    assert "agent/ostorlab/asteroid" in result


def testOstorlabScanRunCLI_whenDefault_shouldLogAllAgents(
    mocker: plugin.MockerFixture,
) -> None:
    """Test ostorlab scan command when no follow option is provided,
    should log all agents.
    """
    runner = CliRunner()
    spy_follow = mocker.spy(run, "prepare_agents_to_follow")

    runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "run",
            "--agent=agent/ostorlab/nmap",
            "--agent=agent/ostorlab/asteroid",
            "ip",
            "8.8.8.8",
        ],
    )

    assert spy_follow.called is True
    assert spy_follow.call_count == 1
    assert len(spy_follow.spy_return) == 2
    assert "agent/ostorlab/nmap" in spy_follow.spy_return
    assert "agent/ostorlab/asteroid" in spy_follow.spy_return
    assert "agent/ostorlab_inject_asset" not in spy_follow.spy_return


def testOstorlabScanRunCLI_whenNoFollow_shouldNotLogAnyAgent(
    mocker: plugin.MockerFixture,
) -> None:
    """Test ostorlab scan command when follow option is provided,
    should not log any agent.
    """
    runner = CliRunner()
    spy_follow = mocker.spy(run, "prepare_agents_to_follow")

    runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "run",
            "--no-follow",
            "--agent=agent/ostorlab/nmap",
            "--agent=agent/ostorlab/asteroid",
            "ip",
            "8.8.8.8",
        ],
    )

    assert spy_follow.called is True
    assert spy_follow.call_count == 1
    assert len(spy_follow.spy_return) == 0


def testOstorlabScanRunCLI_whenFollow_shouldFollowSpecifiedAgents(
    mocker: plugin.MockerFixture,
) -> None:
    """Test ostorlab scan command when follow option is provided,
    should log specified agents.
    """
    runner = CliRunner()
    spy_follow = mocker.spy(run, "prepare_agents_to_follow")

    runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "run",
            "--follow=agent/ostorlab/nmap",
            "--agent=agent/ostorlab/nmap",
            "--agent=agent/ostorlab/asteroid",
            "ip",
            "8.8.8.8",
        ],
    )

    assert spy_follow.called is True
    assert spy_follow.call_count == 1
    assert len(spy_follow.spy_return) == 1
    assert "agent/ostorlab/nmap" in spy_follow.spy_return
    assert "agent/ostorlab/asteroid" not in spy_follow.spy_return
    assert "agent/ostorlab_inject_asset" not in spy_follow.spy_return
