#!/usr/bin/env python3.8
from agent_framework.ipc.base_ipc import IPC_Instance

class AgentIPC:
    '''
    agent ipc data properties
    - last processed: datetime the last frame was processed
    - agent stats: dict of stats that will programatically be displayed on the overlay
    - last action: controllerEventType
    '''

    def __init__(self, ipc_type: IPC_Instance):
        self.ipc_instance = ipc_type(name='agent_ipc')

    def update_properties(self, agent_stats: dict, action: str):
        pass

    def read(self):
        pass