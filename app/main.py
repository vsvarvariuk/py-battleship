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
                print(b[1] - a[1])
                if a[0] == b[0] and b[1] - a[1] == 1:
                    return "Hit"
                if self.matrix[a[0]][a[1]] == "*" and self.matrix[b[0]][b[1]] == "*":
                    return "Sunk!"
            return "Hit!"
        elif self.matrix[x][y] != u"\u25A1":
            return "Miss!"

# battle_ship = Battleship(
#         ships=[
#             ((2, 0), (2, 3)),
#             ((4, 5), (4, 6)),
#             ((3, 8), (3, 9)),
#             ((6, 0), (8, 0)),
#             ((6, 4), (6, 6)),
#             ((6, 8), (6, 9)),
#             ((9, 9), (9, 9)),
#             ((9, 5), (9, 5)),
#             ((9, 3), (9, 3)),
#             ((9, 7), (9, 7)),
#         ]
#     )
#
#
# print(battle_ship.fire((0, 4))) #== "Miss!"
# print(battle_ship.fire((1, 7))) # == "Miss!"
# print(battle_ship.fire((2, 0))) # == "Hit!"
# print(battle_ship.fire((2, 1))) #== "Hit!"
# print(battle_ship.fire((2, 2))) #== "Hit!"
# print(battle_ship.fire((2, 3)))  #== "Sunk!"
# print(battle_ship.fire((4, 3)))  #== "Miss!"
# print(battle_ship.fire((4, 5))) #== "Hit!"