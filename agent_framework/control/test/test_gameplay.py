from app.control.gameplay import GameplayAction, select_action

def test_next_action():
    next_action = select_action(GameplayAction.OP_1)

    assert next_action[0] == GameplayAction.OP_2