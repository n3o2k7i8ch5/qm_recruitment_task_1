import itertools

OCEAN_FIELD = 0
ICELAND_FIELD = 1

list_2d = list[list[int]]


def dfs(row_idx: int, col_idx: int, map: list_2d):
    # An implementation of the depth-first search algorithm that recursively fills all
    # neighbouring and visited `ICELAND_FIELD`s with `OCEAN_FIELD`s in order to prevent
    # counting them twice when searching for consecutive islands.
    if not (0 <= row_idx < len(map) and 0 <= col_idx < len(map[0])):
        return

    if map[row_idx][col_idx] != ICELAND_FIELD:
        return

    map[row_idx][col_idx] = OCEAN_FIELD  # Mark as visited

    dfs(row_idx - 1, col_idx, map)
    dfs(row_idx + 1, col_idx, map)
    dfs(row_idx, col_idx - 1, map)
    dfs(row_idx, col_idx + 1, map)


def count_islands(n_rows: int, n_columns: int, map: list_2d) -> int:
    """
    Algorithm for finding the number of islands
    Solution complexity: O(n_rows * n_columns)
    :param n_rows: Number of rows.
    :param n_columns: Number of columns.
    :param map: A two-dimensional list of integers representing the islands-oceans-map.
    :return: Number of islands found.
    """
    if type(map) is not list and type(map[0]) is not list:
        raise ValueError(f"Please provide a valid map of type {list_2d}.")

    if n_rows != len(map):
        raise ValueError("`n_rows` must match `len(map)`.")

    if n_columns != len(map[0]):
        raise ValueError("`n_columns` must match `len(map[0])`.")

    count = 0
    for row_idx, col_idx in itertools.product(range(n_rows), range(n_columns)):
        if map[row_idx][col_idx] == ICELAND_FIELD:
            count += 1
            dfs(row_idx, col_idx, map)

    return count
