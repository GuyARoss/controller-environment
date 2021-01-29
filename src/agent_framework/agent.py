from abc import ABC, abstractmethod
from typing import NoReturn

from agent_framework.ipc.agent import AgentIPC

class Agent_Instance(ABC):
    @abstractmethod
    def __init__(self, ipc_instance: AgentIPC):
        pass

    @abstractmethod
    def process_frame(self, frame):
        pass

    @abstractmethod
    def write_ipc(self):
        pass

def invoke_agent(instance: Agent_Instance):
    # @ read frame,
    # @ ipc <- out <- process frame
    pass