import argparse

from game_agents. import agents
'''
@@@
- init framework/ start on child process
- take in agent from flag
- init agent
- run agent
- profit
'''
def main(agent_name: str):
    if agent_name not in agents:
        # @ err 
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent_name', '--agent-name', help='str name of the agent to be ran', type=str)

    args = parser.parse_args()


