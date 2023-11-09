# Pr1-FSI
First practice for Fundamentals of Intelligent Systems.
Authored by Juan Carlos Domínguez Dopazo and Asmae Ez Zaim Driouch, from group 43.
University of Las Palmas de Gran Canaria

## Goals
- Explore the implementation of the Branch and Bound algorithm and its significant enhancements.
- Understanding how the initial approach evolved into a more efficient solution that takes underestimation into account.

## Implementations
### First implementation: Shortest path.
Branch and Bound method without underestimation, choosing the shortest path in each case without considering the total cost of the other paths.

### Second implementation: Shortest path with underestimation.
Implementation of the shortest path with underestimation, choosing the shortest path in each case while considering the Euclidean distance from the node to the goal node.

## Extra features
- Count of generated and visited nodes
- Total cost
- Timestamps
- Implementation of all test routes

## Output and tests

| Problem    | Generated | Visited | Total cost | Path                                          |
|------------|-----------|-----------|-------------|-----------------------------------------------|
| A to B     | 21        | 16        | 450         | Breadth-First Path: [B, F, S, A]             |
|            | 18        | 10        | 733         | Depth-First Path: [B, P, C, D, M, L, T, A]   |
|            | 31        | 24        | 418         | Branch and Bound Path: [B, P, R, S, A]      |
|            | 16        | 6         | 418         | Branch and Bound with subestimation Path: [B, P, R, S, A] |
| O to E     | 45        | 43        | 730         | Breadth-First Path: [E, H, U, B, F, S, O]    |
|            | 41        | 31        | 698         | Depth-First Path: [E, H, U, B, P, R, S, O]   |
|            | 43        | 40        | 698         | Branch and Bound Path: [E, H, U, B, P, R, S, O] |
|            | 32        | 15        | 698         | Branch and Bound with subestimation Path: [E, H, U, B, P, R, S, O] |
| G to Z     | 41        | 34        | 615         | Breadth-First Path: [Z, A, S, F, B, G]       |
|            | 32        | 21        | 1284        | Depth-First Path: [Z, A, T, L, M, D, C, P, R, S, F, B, G] |
|            | 41        | 35        | 583         | Branch and Bound Path: [Z, A, S, R, P, B, G] |
|            | 26        | 12        | 583         | Branch and Bound with subestimation Path: [Z, A, S, R, P, B, G] |
| N to D     | 32        | 26        | 765         | Breadth-First Path: [D, C, P, B, U, V, I, N] |
|            | 31        | 19        | 1151        | Depth-First Path: [D, C, P, R, S, F, B, U, V, I, N] |
|            | 32        | 26        | 765         | Branch and Bound Path: [D, C, P, B, U, V, I, N] |
|            | 23        | 12        | 765         | Branch and Bound with subestimation Path: [D, C, P, B, U, V, I, N] |
| M to F     | 31        | 23        | 520         | Breadth-First Path: [F, S, R, C, D, M]       |
|            | 29        | 18        | 928         | Depth-First Path: [F, B, P, R, S, A, T, L, M] |
|            | 36        | 27        | 520         | Branch and Bound Path: [F, S, R, C, D, M]    |
|            | 25        | 16        | 520         | Branch and Bound with subestimation Path: [F, S, R, C, D, M] |
