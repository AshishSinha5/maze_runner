# SARSA (on poilicy TD control) learning algorithm
Simple implementation of SARSA learning algorithm in python  to solve a maze [[1]](#1)

#### Status : Active

## Dataset 
Data is fed into the algorithm as text file containing specifications about the maze e.g. - 
<pre><code>
sssssssssssssss
000000000000000
000000000000000
000000000000000
000000000000000
0000xxxxxxx0000
000000000000000
000000000000000
000000000000000
xxxxx00000xxxxx
000000000000000
000000000000000
000000000000000
0000xxxxxxx0000
000000000000000
000000000000000
fffffffffffffff
</code></pre>
Where
- **x** - barrier
- **s** - start
- **f** - final

## Getting Started
- Clone the repository to your local machine
<pre><code>
git clone https://github.com/AshishSinha5/maze_runner/
</pre></code>
- run main.py with apropiate args e.g. - 
<pre><code>
python main.py -f "data/maze2.txt" -a 0.4 -g 0.9 -e 0.1
</pre></code>

## Inferences
The **state space** are the coordinates of the maze with (-1,-1) being the state when the agent goes out of bounds and **action space** are the two components of velocity with a constrint that it can have a absolute value of greater than 5.

The algorithm was tested for three mazes, and the outputs and plots are shown below. We can see that the algorithm(agent) starts to find the currect path after few iteration and also the proportion of successes keep on increasing with the number of episodes as the agent finds the optimal action value function.

Maze 1             |          Maze 2 |                   Maze 3
:-------------------------:|:-------------------------:|:-------------------------:|
![maze 1 gif](https://github.com/AshishSinha5/maze_runner/blob/master/outputs/maze1.gif)  |  ![maze 2 gif](https://github.com/AshishSinha5/maze_runner/blob/master/outputs/maze2.gif)|  ![maze 3 gif](https://github.com/AshishSinha5/maze_runner/blob/master/outputs/maze3.gif)
![maze 1 succ](https://github.com/AshishSinha5/maze_runner/blob/master/plots/maze1_prop_succ.png) | ![maze 2 succ](https://github.com/AshishSinha5/maze_runner/blob/master/plots/maze2_prop_succ.png) | ![maze 3 succ](https://github.com/AshishSinha5/maze_runner/blob/master/plots/maze3_prop_succ.png)
![maze 1 rewards](https://github.com/AshishSinha5/maze_runner/blob/master/plots/maze1_rewards.png) | ![maze 2 rewards](https://github.com/AshishSinha5/maze_runner/blob/master/plots/maze2_rewards.png) |![maze 3 rewards](https://github.com/AshishSinha5/maze_runner/blob/master/plots/maze3_rewards.png) 

## References
<a id = "1">[1]</a>Reinforcement Learning: An Introduction, R. Sutton, and A. Barto., The MIT Press, Second edition, (2018)

## Appendix
### SARSA (on policy TD control) to estimate action-value function
```
Algoithm Parameters : step size &#945;
```
