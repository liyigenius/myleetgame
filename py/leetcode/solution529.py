from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """

        :param board:
        :param click:
        :return:
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        checkN = self.checkNumber(board, click[1], click[0])
        if checkN != 0:
            board[click[0]][click[1]] = str(checkN)
            return board

        ll = []
        ll.append((click[0], click[1]))
        w, h = len(board[0]), len(board)
        used = set()
        while len(ll) > 0:
            y, x = ll.pop(0)
            if (y,x) in used:
                continue
            used.add((y,x))
            res = self.checkNumber(board, x, y)
            if res != 0:
                board[y][x] = str(res)
                continue
            else:
                board[y][x] = 'B'
                if y - 1 >= 0:
                    if x - 1 >= 0:
                        if board[y - 1][x - 1] == 'E':
                            ll.append((y - 1, x - 1))
                    if board[y - 1][x] == 'E':
                        ll.append((y - 1, x))
                    if x + 1 <= w - 1:
                        if board[y - 1][x + 1] == 'E':
                            ll.append((y - 1, x + 1))
                if x - 1 >= 0:
                    if board[y][x - 1] == 'E':
                        ll.append((y, x - 1))
                if x + 1 <= w - 1:
                    if board[y][x + 1] == 'E':
                        ll.append((y, x + 1))
                if y + 1 <= h - 1:
                    if x - 1 >= 0:
                        if board[y + 1][x - 1] == 'E':
                            ll.append((y + 1, x - 1))
                    if board[y + 1][x] == 'E':
                        ll.append((y + 1, x))
                    if x + 1 <= w - 1:
                        if board[y + 1][x + 1] == 'E':
                            ll.append((y + 1, x + 1))

        return board

    def checkNumber(self, board, x, y):
        w = len(board[0])
        h = len(board)
        cnt = 0
        if y - 1 >= 0:
            if board[y - 1][x] == 'M':
                cnt += 1
            if x - 1 >= 0:
                if board[y - 1][x - 1] == 'M':
                    cnt += 1
            if x + 1 <= w - 1:
                if board[y - 1][x + 1] == 'M':
                    cnt += 1
        if x - 1 >= 0:
            if board[y][x - 1] == 'M':
                cnt += 1
        if x + 1 <= w - 1:
            if board[y][x + 1] == 'M':
                cnt += 1
        if y + 1 <= h - 1:
            if x - 1 >= 0:
                if board[y + 1][x - 1] == 'M':
                    cnt += 1
            if x + 1 <= w - 1:
                if board[y + 1][x + 1] == 'M':
                    cnt += 1
            if board[y + 1][x] == 'M':
                cnt += 1
        return cnt
