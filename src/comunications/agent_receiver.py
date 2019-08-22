import asyncio

from spade import agent
from spade.behaviour import CyclicBehaviour
import config.jids as jid


class ReceiverAgent(agent.Agent):
    class RecvBehav(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=10)  # wait for a message for 10 seconds
            if msg:
                print(msg.body)
            else:
                print("Did not received any message after 10 seconds")
                self.kill()

        async def on_end(self):
            await self.agent.stop()

    async def setup(self):
        b = self.RecvBehav()
        self.add_behaviour(b)

agentReceiver = ReceiverAgent(jid.AGENT2_EMAIL, jid.AGENT2_PASSWORD).start()