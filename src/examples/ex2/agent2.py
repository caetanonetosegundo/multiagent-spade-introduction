import asyncio
import time

from aioxmpp import Presence, PresenceShow
from spade import agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour

import config.jids as jid


class Agent2(agent.Agent):

    async def setup(self):
        self.add_behaviour(self.Behav1())
        self.add_behaviour(self.PrintContacs())

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
            #self.presence.subscribe(jid)

        def on_unsubscribe(self, jid):
            print("[{}] Agent {} asked for UNsubscription. Let's aprove it.".format(self.agent.name, jid.split("@")[0]))
            self.presence.unsubscribe(jid)

        def on_unsubscribed(self, jid):
            print("[{}] Agent {} WAS UNsubscription. Let's aprove it.".format(self.agent.name, jid.split("@")[0]))

        async def run(self):
            print('Agent 2 Started')
            self.presence.on_subscribe = self.on_subscribe
            self.presence.on_unsubscribe = self.on_unsubscribe
            self.presence.on_subscribed = self.on_subscribed
            self.presence.on_unsubscribed = self.on_unsubscribed
            self.presence.on_available = self.on_available
            self.presence.on_unavailable = self.on_unavailable

    class PrintContacs(CyclicBehaviour):
        async def run(self):
            self.presence.set_available()
            await asyncio.sleep(4)


agent = Agent2(jid.AGENT2_EMAIL, jid.AGENT2_PASSWORD).start()

while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
