from abc import ABC, abstractmethod
from typing import NoReturn

from agent_framework.ipc.agent import AgentIPC
from agent_framework.control.controller import Controller

class ProcessedFrameContext():
    def __init__(self, game_control_action, display_properties = None):
        self.game_control_action = game_control_action
        self.display_properties = display_properties


class Agent_Instance(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def process_frame(self, frame):
        pass


def invoke_agent(
    instance: Agent_Instance,
    ipc: AgentIPC,
    controller: Controller,
    frame,
):
    agent_out = instance.process_frame(frame)
    action_name, action_fn = agent_out.game_control_action

    ipc.transmit_frame(
        action=action_name,
        agent_stats=agent_out.display_properties,
    )

    action_fn(controller)
    