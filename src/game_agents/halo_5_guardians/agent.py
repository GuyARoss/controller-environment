from agent_framework.agent import Agent_Instance
from game_agents.halo_5_guardians.menu_prediction.model import Model
from game_agents.halo_5_guardians.gameplay.simple_1 import select_action

class Agent(Agent_Instance):
    def __init__(self, ipc_instance: AgentIPC):
        self.ipc_instance = ipc_instance

        self.menu_prediction_model = Model(file_path="../bin/menu-prediction.joblib") 
        self.menu_prediction_model.load()
        self.last_action = None

    def process_frame(self, frame):
        frame_prediction = self.menu_prediction_model.predict(frame)
        
        
