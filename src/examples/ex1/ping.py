import asyncio

from spade.message import Message
from spade import agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
import config.jids as jid


class PingAgent(agent.Agent):
    class PingBehav(CyclicBehaviour):
        async def run(self):
            print("OneShot Ping started")
            await asyncio.sleep(1)
            msg = await self.receive()  # wait for a message for 10 seconds

            if msg:
                print('Received a message')
                msg = Message(to=jid.AGENT2_EMAIL)
                msg.body = "ping"
                await self.send(msg)

    async def setup(self):
        b = self.PingBehav()
        self.add_behaviour(b)


agent_ping = PingAgent(jid.AGENT1_EMAIL, jid.AGENT1_PASSWORD).start()