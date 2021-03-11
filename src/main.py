#!/usr/bin/env python3.8
import subprocess
import argparse
import cv2

from typing import Callable, NoReturn
from functools import partial

from game_agents import agents
from agent_framework.agent import invoke_agent
from agent_framework.ipc.agent import AgentIPC

def main(game_agent: Callable[[any], NoReturn]):
    subprocess.Popen(['python3', './agent_framework/main.py'], stdout=subprocess.PIPE)
    # os.killpg(os.getpgid(pro.pid), signal.SIGTERM)

    while True:
        try:
            game_frame = cv2.imread('../bin/current_frame.jpg')
            game_agent(game_frame)
        except:
            pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent_name', '--agent_name', help='str name of the agent to be ran', type=str)

    args = parser.parse_args()
    if args.agent_name is None:
        print('error: agent name not specified')
        exit(1)

    game_agent = agents.get(args.agent_name)

    if game_agent is None:
        print(f'{agent_name} is not a supported game agent.')
        exit(1)

    agent = partial(
        invoke_agent, 
        instance=game_agent,
        ipc=AgentIPC(),
        # @@todo: read pin data from config-> load controller
        controller=None
    )

    main(agent)


