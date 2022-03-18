#!/usr/bin/env Python
# -*- coding: utf-8 -*-


def solution(bishops):
    if not bishops:
        return 64

    answer = 0
    width = 8
    d = [[0 for x in range(width)] for y in range(width)]

    position = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
    for node in bishops:
        b_x = ord(node[0]) - ord('A')
        b_y = int(node[1]) - 1

        d[b_y][b_x] = 2

        for i in range(width):
            for j in range(4):
                temp_x = b_x + (position[j][1] * i)
                temp_y = b_y + (position[j][0] * i)

                if -1 < temp_x < width and -1 < temp_y < width and d[temp_y][temp_x] == 0:
                    d[temp_y][temp_x] = 1

    for i in d:
        for j in i:
            if j == 0:
                answer += 1

    return answer


def test_solution():
    assert solution(["D5"]) == 50
    assert solution(["D5", "E8", "G2"]) == 42
    assert solution(["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"]) == 12


# print(solution(["D5"]))
print(solution(["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"]))
# print(solution([]))
