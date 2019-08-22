import asyncio
import time

from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State

from config import jids as jid

STATE_ONE = "ONE"
STATE_TWO = "TWO"
STATE_THREE = "THREE"


class FSMBehaviour(FSMBehaviour):
    async def on_start(self):
        print(f"FSM starting at initial state {self.current_state}")


class StateOne(State):
    async def run(self):
        print("I'm at state one (initial state)")
        await asyncio.sleep(5)
        self.set_next_state(STATE_TWO)


class StateTwo(State):
    async def run(self):
        print("I'm at state two")
        await asyncio.sleep(5)
        self.set_next_state(STATE_THREE)


class StateThree(State):
    async def run(self):
        await asyncio.sleep(5)
        print("I'm at state three")
        self.set_next_state(STATE_ONE)


class FSMAgent(Agent):
    async def setup(self):
        fsm = FSMBehaviour()
        fsm.add_state(name=STATE_ONE, state=StateOne(), initial=True)
        fsm.add_state(name=STATE_TWO, state=StateTwo())
        fsm.add_state(name=STATE_THREE, state=StateThree())
        fsm.add_transition(source=STATE_ONE, dest=STATE_TWO)
        fsm.add_transition(source=STATE_TWO, dest=STATE_THREE)
        fsm.add_transition(source=STATE_THREE, dest=STATE_ONE)
        self.add_behaviour(fsm)


fsmagent = FSMAgent(jid=jid.AGENT1_EMAIL, password=jid.AGENT1_PASSWORD)
fsmagent.start()
fsmagent.web.start(hostname="127.0.0.1", port="10000")