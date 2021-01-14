import time
import random
from typing import List, NoReturn, Callable
from enum import IntEnum

from driver import Controller

class GameplayAction(IntEnum):
    OP_1 = 0
    OP_2 = 1
    OP_3 = 2

def ActionOP_1(controller: Controller) -> NoReturn:
    '''
    Operation 1: left stick forward 2s
    '''
    controller.right_thumbstick.center()
    controller.left_thumbstick.linear_min()
    time.sleep(3)


def ActionOP_2(controller: Controller) -> NoReturn:
    '''
    Operation 2: return left stick to center position 1s
    '''
    controller.right_thumbstick.center()
    controller.left_thumbstick.center()
    time.sleep(1)

def ActionOP_3(controller: Controller) -> NoReturn:
    '''
    Operation 3: right stick move either right or left for 1s
    '''
    rnd = random.randrange(0, 100, 2)
    controller.right_thumbstick.linear_max() if rnd >= 50 else controller.right_thumbstick.linear_min()
    time.sleep(1)

def Action_Pre(controller: Controller) -> NoReturn:
    controller.left_thumbstick.center()
    controller.right_thumbstick.center()

    ActionOP_1(controller)

def select_action(last_action: GameplayAction) -> (GameplayAction, Callable[[Controller], NoReturn]):
    actions = {
        GameplayAction.OP_1: ActionOP_1,
        GameplayAction.OP_2: ActionOP_2,
        GameplayAction.OP_3: ActionOP_3
    }

    if last_action is None:
        return (GameplayAction.OP_1, Action_Pre)

    iter_action = int(last_action) + 1
    new_action = GameplayAction.OP_1 if iter_action > 2 else GameplayAction(iter_action)
    
    return (new_action, actions[new_action])
    
def call_select_option(last_action: GameplayAction, controller: any) -> GameplayAction:
    selected, handler = select_action(last_action)
    if handler != None: 
        handler(controller)

    return selected