import json
from tree_generator import create_tree_from_sequence
from visualizer import TreeVisualizer

def load_experiment(experiment_file, id):
    with open(experiment_file, 'r') as f:
        data = json.load(f)
    experiment = data[id-1]

    return experiment

def load_data(positions_file, id):
    with open(positions_file, 'r') as f:
        data = json.load(f)
    experiment = data[id-1]
    if id == experiment["id"]:
        return experiment
    else:
        raise ValueError("ID mismatch in experiment data")
    
def load_results(file, kind, id):
    with open(file, 'r') as f:
        data = json.load(f)
    results = data[kind]
    results = results[id-1]
    if id == results["experiment"]:
        return results
    else:
        raise ValueError("ID mismatch in results data")

def get_leaf_nodes(tree):
    leaf_nodes = []
    for node in tree.nodes:
        if len(tree.get_children(node)) == 0:
            leaf_nodes.append(node)
    return leaf_nodes

def calculate_protected_nodes(tree, ff_route):
    protected_nodes = set()
    for node in ff_route:
        path = tree.get_subtree_nodes(node)
        protected_nodes.update(path)
    return protected_nodes


experiment_file = "results/rollout_parallel_test_results_1_nodes.json"
positions_file = "experiments/experiments_moving_nodes.json"
id = 56

experiment = load_experiment(experiment_file, id)
experiment_data = load_data(positions_file, id)
positions = experiment_data["nodes_positions"]
root = experiment_data["root"]
ff_initial_position = experiment_data["initial_firefighter_position"]

# Create tree from sequence
sequence = experiment["sequence"]
tree = create_tree_from_sequence(sequence, add_positions=False, positions=positions)
tree, _ = tree.convert_to_directed(root)
ff_route = experiment["solution"]

# Visualize tree
visualizer = TreeVisualizer(tree)



results_file = "experiments/results_moving_nodes.json"
greedy_result = load_results(results_file, "greedy", id)
ilp_result = load_results(results_file, "ilp", id)

print("Greedy result:", greedy_result)
print("ILP result:", ilp_result)

greedy_route = greedy_result["solution"][1:]
ilp_route = ilp_result["solution"][1:]

protected_nodes_rollout = calculate_protected_nodes(tree, ff_route) - set(ff_route)
protected_nodes_greedy = calculate_protected_nodes(tree, greedy_route) - set(greedy_route)
protected_nodes_ilp = calculate_protected_nodes(tree, ilp_route) - set(ilp_route)

visualizer.final_ff_route(root, tree, ff_initial_position, ff_route, protected_nodes_rollout, "Rollout")
visualizer.final_ff_route(root, tree, ff_initial_position, greedy_route, protected_nodes_greedy, "Greedy")
visualizer.final_ff_route(root, tree, ff_initial_position, ilp_route, protected_nodes_ilp,"ILP")