from spade import agent
import config.jids as jid


# Agent without any behavior
class DummyAgent(agent.Agent):

    async def setup(self):
        print("Hello World! I'm agent {}".format(str(self.jid)))


dummy = DummyAgent(jid.AGENT1_EMAIL, jid.AGENT1_PASSWORD)
dummy.start()