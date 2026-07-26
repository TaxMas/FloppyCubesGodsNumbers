# God Numbers for 1×3×3, 1×4×4, and 1×5×5 Rubik's Cubes

This repository contains Python programs used to compute the God Numbers of the 1×3×3, 1×4×4, and 1×5×5 Rubik's Cubes under different move metrics.

The program starts from the solved state of the puzzle and performs a breadth-first search (BFS) through the state space.

First, it generates every position that can be reached in one move from the solved state. Then, it generates all previously unseen positions that can be reached in two moves, followed by those at three moves, and so on.

At each depth, only new positions that have not been discovered before are added. This guarantees that every position is assigned its shortest possible distance from the solved state.

Eventually, the algorithm reaches a depth at which no new positions can be generated. At that point, every reachable state has already been explored, so the search stops. The last depth that produced new positions is the God Number for the chosen puzzle and move metric.

# Progress indicator

Since the 1×5×5 cube has a much larger state space than the other puzzles, its computation can take a considerable amount of time.

To make the execution easier to monitor, the program includes a simple progress indicator that reports the estimated completion percentage in 10% increments.

Please note that this percentage only reflects the progress of the main search. Once it reaches 100%, the program still requires some additional time to verify that no new states can be generated. Therefore, the computation is not necessarily finished as soon as the progress indicator reaches 100%.

# Notation
Click [here](https://www.speedsolving.com/wiki/index.php?title=Metric) to see the meaning of each metric.
## 1×3×3 Cube

- **F**: Turn the front layer 180°.
- **R**: Turn the right layer 180°.
- **B**: Turn the back layer 180°.
- **L**: Turn the left layer 180°.
- **M**: Turn the vertical middle layer 180°.
- **S**: Turn the horizontal middle layer 180°.

## 1×4×4 Cube

- **F**: Turn the front layer 180°.
- **Fw**: Turn the front two layers 180°.
- **f**: Turn the inner front layer 180°.
- **R**: Turn the right layer 180°.
- **Rw**: Turn the right two layers 180°.
- **r**: Turn the inner right layer 180°.
- **B**: Turn the back layer 180°.
- **b**: Turn the inner back layer 180°.
- **L**: Turn the left layer 180°.
- **l**: Turn the inner left layer 180°.
- **M**: Turn the two vertical middle layers 180°.
- **S**: Turn the two horizontal middle layers 180°.

## 1×5×5 Cube

- **F**: Turn the front layer 180°.
- **Fw**: Turn the front two layers 180°.
- **f**: Turn the inner front layer 180°.
- **R**: Turn the right layer 180°.
- **Rw**: Turn the right two layers 180°.
- **r**: Turn the inner right layer 180°.
- **B**: Turn the back layer 180°.
- **Bw**: Turn the back two layers 180°.
- **b**: Turn the inner back layer 180°.
- **L**: Turn the left layer 180°.
- **Lw**: Turn the left two layers 180°.
- **l**: Turn the inner left layer 180°.
- **M**: Turn the three vertical middle layers 180°.
- **m**: Turn the central vertical middle layer 180°.
- **S**: Turn the three horizontal middle layers 180°.
- **s**: Turn the central horizontal middle layer 180°.
- **rm**: Turn the central vertical middle layer and the inner right layer 180°.
- **lm**: Turn the central vertical middle layer and the inner left layer 180°.
- **fs**: Turn the central horizontal middle layer and the inner front layer 180°.
- **bs**: Turn the central horizontal middle layer and the inner back layer 180°.

# Results
<table>
  <tr>
    <th>Puzzle</th>
    <th>Scrambles</th>
    <th>Metric</th>
    <th>God's Number</th>
    <th>Examples</th>
  </tr>

  <tr>
    <td rowspan="2">1×3×3</td>
    <td rowspan="2">192</td>
    <td>HTM</td>
    <td><b>8</b></td>
    <td><code>U L B R L B L F</code></td>
  </tr>
  <tr>
    <td>STM</td>
    <td><b>6</b></td>
    <td><code>F R S L F M</code>, <code>F R F R F R</code></td>
  </tr>
  
  <tr>
    <td rowspan="2">1×4×4</td>
    <td rowspan="2">20,736</td>
    <td>OBTM</td>
    <td><b>11</b></td>
    <td><code>F B Fw R Fw Rw B L Rw B Fw</code></td>
  </tr>
  <tr>
    <td>BTM</td>
    <td><b>8</b></td>
    <td><code>F R S Rw b l Fw M</code></td>
  </tr>

  <tr>
    <td rowspan="2">1×5×5</td>
    <td rowspan="2">2,654,208</td>
    <td>OBTM</td>
    <td><b>14</b></td>
    <td><code>F B R Fw Bw Rw F B R Fw Rw Bw Rw Bw</code></td>
  </tr>
  <tr>
    <td>BTM</td>
    <td><b>10</b></td>
    <td><code>F L B L m Bw rm bs Rw s</code></td>
  </tr>
</table>


