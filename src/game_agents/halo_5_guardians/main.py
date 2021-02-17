#!/usr/bin/env python3.8
import argparse
from typing import NoReturn

from agent_framework.ipc.agent import AgentIPC

def main(should_train: bool) -> NoReturn:

    # @@todo: read the current frame, make prediction, do controller action.


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', '--train', help="set true if the training process should be ran", type=bool, default=False)
    parser.add_argument('--noloop', '--noloop', help="set true if the main process loop should not be ran", type=bool, default=False)

    args = parser.parse_args()

    main(
        should_train=args.train,
        no_loop=args.noloop,
    )