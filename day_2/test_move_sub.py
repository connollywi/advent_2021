from . import move_sub


commands = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
]


def test_move_sub_v1():
    position_controller = move_sub.PositionControllerV1(0, 0)
    for command in commands:
        position_controller.execute_command(command)
    assert position_controller.composite_position == 150


def test_move_sub_v2():
    position_controller = move_sub.PositionControllerV2(0, 0, 0)
    for command in commands:
        position_controller.execute_command(command)
    assert position_controller.composite_position == 900
    assert position_controller.horizontal_position == 15
    assert position_controller.depth == 60
