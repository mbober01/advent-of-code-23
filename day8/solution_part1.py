from typing import Optional, List, Dict

from aoc_utils.data_utils import get_data


class Journey:
    def __init__(self, input_data):
        self.input = get_data(input_data)
        self.instructions = []
        self.steps = 0
        self.nodes: Dict[str, Node] = {}
        self.current_node: Optional[Node] = None

    def __repr__(self):
        return f"Journey: {self.instructions}"

    @staticmethod
    def read_node(node_def):
        for remove in [" ", "(", ")", ",", "="]:
            if remove in [",", "="]:
                node_def = node_def.replace(remove, " ")
            else:
                node_def = node_def.replace(remove, "")

        node_def = node_def.split(" ")
        name, left_name, right_name = node_def
        return Node(name, left_name, right_name)

    def read_instructions(self):
        lines_to_remove = []
        for line in self.input:
            if line != "":
                self.instructions.extend([direction for direction in line])
                lines_to_remove.append(line)
            else:
                lines_to_remove.append(line)
                for li in lines_to_remove:
                    self.input.remove(li)
                break

    def read_all_nodes(self):
        for node_def in self.input:
            node = self.read_node(node_def)
            self.nodes[node.name] = node

    def go_on_journey(self):
        self.current_node = self.nodes["AAA"]
        while self.current_node.name != "ZZZ":
            direction = self.instructions[self.steps % len(self.instructions)]
            new_node_name = self.current_node.move(direction)
            self.current_node = self.nodes[new_node_name]
            self.steps += 1


class Node:
    def __init__(self, name, left_name, right_name):
        self.name = name
        self.left_name = left_name
        self.right_name = right_name

    def __repr__(self):
        return f"Node: {self.name} = {self.left_name} {self.right_name}"

    def move(self, direction):
        if direction == "L":
            return self.left_name
        elif direction == "R":
            return self.right_name


def main():
    journey = Journey("input.txt")
    journey.read_instructions()
    journey.read_all_nodes()
    journey.go_on_journey()
    print(journey.steps)


if __name__ == "__main__":
    main()
