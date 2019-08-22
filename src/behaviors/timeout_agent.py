import asyncio
import datetime

from spade import agent
from spade.behaviour import TimeoutBehaviour

import config.jids as jid


class TimeOutAgent(agent.Agent):

    async def setup(self):

        print("Hello World! I'm agent {}".format(str(self.jid)))
        start_at = datetime.datetime.now() + datetime.timedelta(seconds=5)

        self.add_behaviour(
            self.TimeOutBehav(start_at=start_at)
        )

    class TimeOutBehav(TimeoutBehaviour):
        async def run(self):
            print("Hi! I'm a TimeOut behavior")

        async def on_end(self):
            await self.agent.stop()

        async def on_start(self):
            print("TimeOut Behavior Started")


agent = TimeOutAgent(jid.AGENT1_EMAIL, jid.AGENT1_PASSWORD)
agent.start()