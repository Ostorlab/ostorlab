"""Sample agent that implements the start method and sends a message."""
import datetime

from ostorlab.agent import agent, definitions as agent_definitions
from ostorlab.runtimes import definitions as runtime_definitions


class StartTestAgent(agent.Agent):
    """Agent implementation."""
    def start(self) -> None:
        """Sends ping message.

        Returns:
            None
        """
        self.emit('v3.healthcheck.ping', {'body': f'from test agent at {datetime.datetime.now()}'})


definition = agent_definitions.AgentDefinition(
    name='start_test_agent',
    out_selectors=['v3.healthcheck.ping'])
settings = runtime_definitions.AgentSettings(
    key='agent/ostorlab/start_test_agent',
    bus_url='amqp://guest:guest@localhost:5672/',
    bus_exchange_topic='ostorlab_test',
    healthcheck_port=5301)

start_agent = StartTestAgent(definition, settings)
start_agent.run()
