import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from config import jids as jid


class WaitingAgent(Agent):
    class LongBehav(OneShotBehaviour):
        async def run(self):
            print("Long Behaviour has started")
            await asyncio.sleep(10)
            print("Long Behaviour has finished")

    class WaitingBehav(OneShotBehaviour):
        async def run(self):
            print("Waiting Behaviour behav")
            await self.agent.behav.join()
            print("Behav already finished")


    async def setup(self):
        print("Agent starting . . .")
        self.behav = self.LongBehav()
        self.add_behaviour(self.behav)
        self.behav2 = self.WaitingBehav()
        self.add_behaviour(self.behav2)


if __name__ == "__main__":
    agent = WaitingAgent(jid.AGENT1_EMAIL, jid.AGENT1_PASSWORD)
    agent.start()
