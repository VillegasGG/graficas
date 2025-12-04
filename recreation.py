import json
from tree_generator import create_tree_from_sequence
from visualizer import TreeVisualizer

def load_experiment(experiment_file, id):
    with open(experiment_file, 'r') as f:
        data = json.load(f)
    experiment = data[id-1]

    return experiment

def load_positions(positions_file, id):
    with open(positions_file, 'r') as f:
        data = json.load(f)
    experiment = data[id-1]
    if id == experiment["id"]:
        print("Positions loaded successfully.")
        positions = experiment["nodes_positions"]

    return positions

experiment_file = "results/rollout_test_results_1_nodes.json"
positions_file = "experiments/experiments_moving_nodes.json"
id = 55

experiment = load_experiment(experiment_file, id)
positions = load_positions(positions_file, id)

# Create tree from sequence
sequence = experiment["sequence"]
tree = create_tree_from_sequence(sequence, add_positions=False, positions=positions)


# Visualize tree
visualizer = TreeVisualizer(tree)
visualizer.plot_3d_tree(tree, img_name="initial_tree")

