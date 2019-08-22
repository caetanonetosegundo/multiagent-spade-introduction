import asyncio

from spade import agent
from spade.behaviour import CyclicBehaviour

import config.jids as jid


class CyclicAgent(agent.Agent):

    async def setup(self):

        print("Hello World! I'm agent {}".format(str(self.jid)))

        self.add_behaviour(
            self.CyclicBehav()
        )

    class CyclicBehav(CyclicBehaviour):
        async def run(self):
            print("Hi! I'm a cyclic behavior")
            await asyncio.sleep(1)

        async def on_end(self):
            await self.agent.stop()

        async def on_start(self):
            print("Cyclic Behavior Started")


agent = CyclicAgent(jid.AGENT1_EMAIL, jid.AGENT1_PASSWORD)
agent.start()
agent.web.start(hostname="127.0.0.1", port="10000")