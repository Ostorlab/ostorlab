"""Unit tests for OpenTelemetryMixin module."""
import json
import sys
import tempfile
import pytest

from ostorlab.agent import agent
from ostorlab.agent import definitions as agent_definitions
from ostorlab.runtimes import definitions as runtime_definitions
from ostorlab.agent import message as agent_message
from ostorlab.agent.message import serializer


class TestAgent(agent.Agent):
    """Helper class to test OpenTelemetry mixin implementation."""

    def process(self, message: agent_message.Message) -> None:
        pass


@pytest.mark.skipif(sys.platform == 'win32', reason='does not run on windows')
def testOpenTelemetryMixin_whenEmitMessage_shouldTraceMessage(agent_mock):
    """Unit test for the OpenTelemetry Mixin, ensure the correct exporter has been used and trace span has been sent."""
    del agent_mock
    with tempfile.NamedTemporaryFile(suffix='.json') as tmp_file_obj:
        agent_definition = agent_definitions.AgentDefinition(
            name='some_name',
            out_selectors=['v3.report.vulnerability'])
        agent_settings = runtime_definitions.AgentSettings(
            key='some_key',
            tracing_collector_url=f'file://{tmp_file_obj.name}')
        test_agent = TestAgent(
            agent_definition=agent_definition,
            agent_settings=agent_settings)

        test_agent.emit('v3.report.vulnerability', {
            'title': 'some_title',
            'technical_detail': 'some_details',
            'risk_rating': 'MEDIUM'
        })
        test_agent.force_flush_file_exporter()

        with open(tmp_file_obj.name, 'r', encoding='utf-8') as trace_file:
            trace_content = trace_file.read()
            trace_object = json.loads(trace_content)

            assert trace_object['name'] == 'emit_message'
            assert trace_object['attributes']['agent.name'] == 'some_name'
            assert trace_object['attributes']['message.selector'] == 'v3.report.vulnerability'


@pytest.mark.skipif(sys.platform == 'win32', reason='does not run on windows')
def testOpenTelemetryMixin_whenProcessMessage_shouldTraceMessage(agent_mock):
    """Unit test for the OpenTelemtry Mixin, ensure the correct exporter has been used and trace span has been sent."""
    del agent_mock
    with tempfile.NamedTemporaryFile(suffix='.json') as tmp_file_obj:
        agent_definition = agent_definitions.AgentDefinition(
            name='some_name',
            in_selectors=['v3.report.vulnerability'])
        agent_settings = runtime_definitions.AgentSettings(
            key='some_key',
            tracing_collector_url=f'file://{tmp_file_obj.name}')
        test_agent = TestAgent(
            agent_definition=agent_definition,
            agent_settings=agent_settings)
        data = {
            'title': 'some_title',
            'technical_detail': 'some_details',
            'risk_rating': 'MEDIUM'
        }
        raw = serializer.serialize('v3.report.vulnerability', data).SerializeToString()

        test_agent.process_message(selector='v3.report.vulnerability', message=raw)
        test_agent.force_flush_file_exporter()

        with open(tmp_file_obj.name, 'r', encoding='utf-8') as trace_file:
            trace_content = trace_file.read()
            trace_object = json.loads(trace_content)

            assert trace_object['name'] == 'process_message'
            assert trace_object['attributes']['agent.name'] == 'some_name'
            assert trace_object['attributes']['message.selector'] == 'v3.report.vulnerability'