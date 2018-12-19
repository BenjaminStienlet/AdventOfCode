
class Node:

    def __init__(self, child_nodes, metadata):
        self.child_nodes = child_nodes
        self.metadata = metadata

    def parse_tree(input_list):
        nr_nodes = input_list[0]
        nr_metadata = input_list[1]
        nodes = []
        adapted_input = input_list[2:]
        for i in range(nr_nodes):
            node, adapted_input = Node.parse_tree(adapted_input)
            nodes.append(node)

        metadata = adapted_input[0:nr_metadata]
        adapted_input = adapted_input[nr_metadata:]
        return (
         Node(nodes, metadata), adapted_input)

    def sum_metadata(self):
        result = sum(self.metadata)
        for node in self.child_nodes:
            result += node.sum_metadata()

        return result


data_file = open('day8/input.txt')
data_in = list(map(int, data_file.readline().split(' ')))
root_node, input_remainder = Node.parse_tree(data_in)
print('Result: %d' % root_node.sum_metadata())
