class PositionControllerV1:
    def __init__(self, initial_horizontal, initial_depth):
        self.horizontal_position = initial_horizontal
        self.depth = initial_depth

    @property
    def composite_position(self):
        return self.horizontal_position * self.depth

    def execute_command(self, command):
        print(f"Executing command: {command}")
        direction, magnitude = command.lower().split(" ")
        magnitude = int(magnitude)
        if direction == "forward":
            self.horizontal_position += magnitude
        elif direction == "down":
            self.depth += magnitude
        elif direction == "up":
            self.depth -= magnitude


class PositionControllerV2:
    def __init__(self, initial_horizontal, initial_depth, initial_aim):
        self.horizontal_position = initial_horizontal
        self.depth = initial_depth
        self.aim = initial_aim

    @property
    def composite_position(self):
        return self.horizontal_position * self.depth

    def execute_command(self, command):
        print(f"Executing command: {command}")
        direction, magnitude = command.lower().split(" ")
        magnitude = int(magnitude)
        if direction == "forward":
            self.horizontal_position += magnitude
            self.depth += self.aim * magnitude
        elif direction == "down":
            self.aim += magnitude
        elif direction == "up":
            self.aim -= magnitude


def import_commands(path):
    with open(path, "r") as input_file:
        lines = [line.strip("\n") for line in input_file.readlines()]
    return lines


if __name__ == "__main__":
    commands = import_commands("input.txt")
    while 1:
        version = input("V1/V2? ")
        if version == "1":
            pc = PositionControllerV1(0, 0)
            break
        if version == "2":
            pc = PositionControllerV2(0, 0, 0)
            break

    list(map(pc.execute_command, commands))
    print(f"\nFinal depth: {pc.depth}")
    print(f"Final horizontal: {pc.horizontal_position}")
    print(f"Composite position: {pc.composite_position}\n")
