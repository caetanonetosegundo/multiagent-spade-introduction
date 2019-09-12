import asyncio
import time

from spade import agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour

import config.jids as jid


class Agent1(agent.Agent):

    async def setup(self):
        self.add_behaviour(self.Behav1())
        #self.add_behaviour(self.PrintContacs())

    class Behav1(OneShotBehaviour):

        def on_available(self, jid, stanza):
            print("[{}] Agent {} is available.".format(self.agent.name, jid.split("@")[0]))

        def on_unavailable(self, jid, stanza):
            print("[{}] Agent {} is UNavailable.".format(self.agent.name, jid.split("@")[0]))

        def on_subscribed(self, jid):
            print("[{}] Agent {} has accepted the subscription.".format(self.agent.name, jid.split("@")[0]))
            print("[{}] Contacts List: {}".format(self.agent.name, self.agent.presence.get_contacts()))

        def on_subscribe(self, jid):
            print("[{}] Agent {} asked for subscription. Let's aprove it.".format(self.agent.name, jid.split("@")[0]))
            self.presence.approve(jid)

        async def run(self):
            print('Agent 1 Started')
            self.presence.on_subscribe = self.on_subscribe
            self.presence.on_subscribed = self.on_subscribed
            self.presence.on_available = self.on_available
            self.presence.on_unavailable = self.on_unavailable
            #self.presence.subscribe(jid.AGENT2_EMAIL)

    class PrintContacs(CyclicBehaviour):
        async def run(self):
            print(self.presence.get_contacts())
            await asyncio.sleep(4)


agent = Agent1(jid.AGENT1_EMAIL, jid.AGENT1_PASSWORD).start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break

