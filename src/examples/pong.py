import asyncio

from spade.message import Message
from spade import agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
import config.jids as jid


class PongAgent(agent.Agent):
    class PongBehav(CyclicBehaviour):
        async def run(self):
            print("OneShot Pong started")
            await asyncio.sleep(1)
            msg = await self.receive()  # wait for a message for 10 seconds

            if msg:
                print('Received a message')
                msg = Message(to=jid.AGENT1_EMAIL)
                msg.body = "pong"
                await self.send(msg)

    async def setup(self):
        b = self.PongBehav()
        self.add_behaviour(b)

agent_pong = PongAgent(jid.AGENT2_EMAIL, jid.AGENT2_PASSWORD).start()
