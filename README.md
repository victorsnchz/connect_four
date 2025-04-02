# connect_four
play connect-four against your friend (or yourself)

Started as a small project, turned out to be way more interesting than expected.

Algos:
- (local) matrix DFS to check if player wins after a move
- (global) matrix DFS to check if input grid contains a winning sequence
- binary search to find first slot free in a column

Data struct:
- lists, tuples and sets but surprisingly no dicts
- dataclasses and frozen dataclasses

A comprehensive test-bench.
