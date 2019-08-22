import asyncio
import datetime

from spade import agent
from spade.behaviour import PeriodicBehaviour

import config.jids as jid


class PeriodicAgent(agent.Agent):

    async def setup(self):

        print("Hello World! I'm agent {}".format(str(self.jid)))

        self.add_behaviour(
            self.PeriodicBehav(period=2, start_at= datetime.datetime.now())
        )

    class PeriodicBehav(PeriodicBehaviour):
        async def run(self):
            print("Hi! I'm a periodic behavior")

        async def on_end(self):
            await self.agent.stop()

        async def on_start(self):
            print("Periodic Behavior Started")


agent = PeriodicAgent(jid.AGENT1_EMAIL, jid.AGENT1_PASSWORD)
agent.start()
agent.web.start(hostname="127.0.0.1", port="10000")