import asyncio

from spade import agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

import config.jids as jid


class CyclicSendMessageAgent(agent.Agent):

    async def setup(self):

        print("Hello World! I'm agent {}".format(str(self.jid)))

        self.add_behaviour(
            self.CyclicBehav()
        )

    class CyclicBehav(CyclicBehaviour):
        async def run(self):
            print("Hi body")
            msg = Message(to=jid.AGENT2_EMAIL)
            msg.body = "Hi body"

            await self.send(msg)
            await asyncio.sleep(5)

        async def on_end(self):
            await self.agent.stop()

        async def on_start(self):
            print("Cyclic Behavior Send Message Started")


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


agentSender = CyclicSendMessageAgent(jid.AGENT1_EMAIL, jid.AGENT1_PASSWORD).start()
