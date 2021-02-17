import subprocess
import argparse

from game_agents import agents

def main(agent_name: str):
    game_agent = agents.get(agent_name)

    if game_agent is None:
        print(f'{agent_name} is not a supported game agent.')
        exit(1)

    subprocess.Popen(['python3', './agent_framework/main.py'])
    print('subprocess started')

    # @@ start the agent.

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent_name', '--agent-name', help='str name of the agent to be ran', type=str)

    args = parser.parse_args()


