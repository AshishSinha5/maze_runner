import numpy as np
import matplotlib.pyplot as plt
import argparse
from play import play


def get_maze(maze_file):
    maze = []
    with open(maze_file, 'r') as f:
        for line in f:
            maze.append(line)
    maze = np.array([list(line)[:-1] for line in maze])
    return maze


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_path", help='FIle path to maze', default='data/maze1.txt', type=str)
    parser.add_argument("-e", "--epsilon", help="Epsilon value", default=0.1, type=float)
    parser.add_argument("-a", "--alpha", help='Alpha value fro TD-SARSA algorithm', default='0.5', type=float)
    parser.add_argument("-g", "--gamma", help="Gamma value for TD-SARSA algorithm", default=0.9, type=float)
    parser.add_argument("-n", "--num_trials", help="Number of trials/episodes", default=50000, type=int)
    args = parser.parse_args()
    maze_file =args.file_path
    eps = args.epsilon
    alpha = args.alpha
    gamma = args.gamma
    n_trials = args.num_trials

    maze = get_maze(maze_file)
    print(maze.shape)
    print(maze)

    agent = play(maze, alpha=alpha, gamma=gamma, eps=eps, n_trials=n_trials)
    camera, rewards, prop_succ = agent.td_sarsa()

    animation = camera.animate()
    animation.save('outputs/{}.gif'.format(maze_file[5:-4]))
    plt.close()

    plt.title("Rewards v/s Episodes")
    plt.plot(np.arange(len(rewards)), rewards)
    plt.xlabel('Episodes')
    plt.ylabel('Rewards')
    plt.savefig('plots/{}_rewards.png'.format(maze_file[5:-4]))
    plt.close()

    plt.title("Proportion of success v/s Number of trials")
    plt.plot(np.arange(len(prop_succ)), prop_succ)
    plt.xlabel('Episodes')
    plt.ylabel('Proportion of Success')
    plt.savefig('plots/{}_prop_succ.png'.format(maze_file[5:-4]))
    plt.close()