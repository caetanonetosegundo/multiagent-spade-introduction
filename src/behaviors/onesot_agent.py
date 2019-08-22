import asyncio
import datetime

from spade import agent
from spade.behaviour import OneShotBehaviour

import config.jids as jid


class OneShotAgent(agent.Agent):

    async def setup(self):

        print("Hello World! I'm agent {}".format(str(self.jid)))
        start_at = datetime.datetime.now() + datetime.timedelta(seconds=5)

        self.add_behaviour(
            self.OneShotBehav()
        )

    class OneShotBehav(OneShotBehaviour):
        async def run(self):
            print("Hi! I'm a OneShot behavior")

        async def on_end(self):
            await self.agent.stop()

        async def on_start(self):
            print("OneShot Behavior Started")


agent = OneShotAgent(jid.AGENT1_EMAIL, jid.AGENT1_PASSWORD)
agent.start()