from agent_framework.agent import Agent_Instance, ProcessedFrameContext

from game_agents.halo_5_guardians.menu_prediction.model import Model
from game_agents.halo_5_guardians.gameplay.simple_1 import select_action

class Agent(Agent_Instance):
    def __init__(self):
        self.menu_prediction_model = Model(file_path="../bin/menu-prediction.joblib") 
        self.menu_prediction_model.load()
        self.last_action = None

    def process_frame(self, frame):
        frame_prediction:str = self.menu_prediction_model.predict(frame)
        
        if frame_prediction == 'gameplay':
            self.last_action = select_action(self.last_action[0])    
        else: 
            self.last_action = None

        return ProcessedFrameContext(game_control_action=self.last_action, display_properties={
            'frame_prediction': frame_prediction,
        })
