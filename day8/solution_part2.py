from typing import List

from solution_part1 import Journey, Node
from math import lcm


class Journey2(Journey):
    def __init__(self, input_data):
        super().__init__(input_data)
        self.starting_nodes: List[Node] = []

    def read_all_nodes(self):
        for node_def in self.input:
            node = self.read_node(node_def)
            self.nodes[node.name] = node
            if node.name[-1] == "A":
                self.starting_nodes.append(node)

    def go_on_journey(self):
        needed_steps = []
        for node in self.starting_nodes:
            current_node = node
            while current_node.name[-1] != "Z":
                direction = self.instructions[self.steps % len(self.instructions)]
                new_node_name = current_node.move(direction)
                current_node = self.nodes[new_node_name]
                self.steps += 1

            needed_steps.append(self.steps)
            self.steps = 0

        return needed_steps


def main():
    journey = Journey2("input.txt")
    journey.read_instructions()
    journey.read_all_nodes()
    needed_steps = journey.go_on_journey()
    print(lcm(*needed_steps))


if __name__ == "__main__":
    main()
