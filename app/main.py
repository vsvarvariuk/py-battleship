class Deck:
    def __init__(self, row: int = 10,
                 column: int = 10) -> None:
        self.row = row
        self.column = column

    def create_field(self) -> list:
        matrix = [[u"\u007E" for _ in range(self.column)]
                  for _ in range(self.row)]
        return matrix


class Ship:
    def __init__(self, ships: list) -> None:
        self.ship = ships
        self.matrix = Deck().create_field()

    def get_deck(self) -> list:
        for i in range(len(self.ship)):
            cordinats_1 = self.ship[i][0]
            cordinats_2 = self.ship[i][1]
            row_1, column_1 = cordinats_1
            row_2, column_2 = cordinats_2
            if row_1 == row_2:
                for j in range(column_1, column_2 + 1):
                    self.matrix[row_1][j] = u"\u25A1"
            if column_1 == column_2:
                for j in range(row_1, row_2 + 1):
                    self.matrix[j][column_1] = u"\u25A1"
        return self.matrix


class Battleship:
    def __init__(self, ships: list) -> None:
        self.ship = ships
        self.matrix = Ship(ships).get_deck()

    def fire(self, kord: tuple) -> str:
        x, y = kord
        if self.matrix[x][y] == u"\u25A1":
            self.matrix[x][y] = "*"
            for i in self.ship:
                a, b = i
                if (self.matrix[a[0]][a[1]] == "*"
                        and self.matrix[b[0]][b[1]] == "*"):
                    return "Sunk!"
            return "Hit!"
        elif self.matrix[x][y] != u"\u25A1":
            return "Miss!"
