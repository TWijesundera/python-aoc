import itertools
import re
import math
from typing import List, Dict, Tuple


class Instructions:
    def __init__(self, directions: str) -> None:
        self.direction_gen = itertools.cycle(list(directions.strip("\n")))


class Networks:
    def __init__(self, networks: List[str], instructions: "Instructions"):
        self.instructions = instructions
        self.networks = self._populate_network(networks)

    def _populate_network(self, networks) -> Dict[str, Tuple[str, str]]:
        node_network = {}
        for network in networks:
            node, next_nodes = network.rstrip("\n").split("=")
            node_network[node.strip()] = tuple(
                filter(None, re.split(r"\W", next_nodes.strip()))
            )
        return node_network

    def calculate_steps(self, start_node: str):
        next_nodes = self.networks[start_node]
        steps = 0

        for direction in self.instructions.direction_gen:
            steps += 1
            if direction == "L":
                next_nodes = self.networks[start_node := next_nodes[0]]
            else:
                next_nodes = self.networks[start_node := next_nodes[1]]

            if start_node.endswith("Z"):
                break
        return steps


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as fp:
        input = fp.readlines()
    directions = Instructions(input[0])

    networks = Networks(input[2:], directions)
    print(f"Part 1 Solution: {networks.calculate_steps("AAA")}")
    a_ending = [
        network for network in networks.networks.keys() if network.endswith("A")
    ]
    lcms = [networks.calculate_steps(node) for node in a_ending]
    print(f"Part 2 Solution {math.lcm(*lcms)}")
