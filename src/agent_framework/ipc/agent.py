#!/usr/bin/env python3.8
from agent_framework.ipc.base_ipc import IPC_Instance, BaseIPC

class AgentIPC():
    '''
    agent ipc data properties
    - last processed: datetime the last frame was processed
    - agent stats: dict of stats that will programatically be displayed on the overlay
    - last action: controllerEventType
    '''

    def __init__(self, ipc_type: IPC_Instance = BaseIPC):
        self.ipc_instance = ipc_type(name='agent_ipc')

    def transmit_frame(self, action: str, agent_stats: dict ):
        pass

    def read(self):
        pass