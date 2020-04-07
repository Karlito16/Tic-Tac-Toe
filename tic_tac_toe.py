#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter


class Player:

    players = list()
    char = [('X', 'red'), ('O', 'blue')]

    def __init__(self, name):
        self.name = name
        Player.players.append(self)
        self.char = Player.char[len(Player.players) - 1]
        return

    def __str__(self):
        return self.name


class Game:

    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.on_turn = player_one
        self.board = [['', '', ''] for _ in range(3)]
        return

    def __str__(self):
        pass

    def check(self):
        def linearly(obj):
            for i in range(3):
                combo_r, combo_c = [], []
                for j in range(3):
                    combo_r.append(obj.board[i][j])
                    combo_c.append(obj.board[j][i])
                if combo_r == ['X'] * 3 or combo_r == ['O'] * 3 or combo_c == ['X'] * 3 or combo_c == ['O'] * 3:
                    return True
            return False

        def diagonally(obj):
            for i in range(0, 3, 2):
                combo = []
                for j in range(3):
                    combo.append(obj.board[j][abs(j - i)])
                first = combo[0]
                if first and combo == [first] * 3:
                    return True
            return False

        def fully():
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '':
                        return False
            return True

        if linearly(self) or diagonally(self) or fully():
            return True
        return False

    def next_turn(self):
        if self.on_turn == self.player_one:
            self.on_turn = self.player_two
        else:
            self.on_turn = self.player_one
        return

    def restart(self):
        self.__init__(self.player_one, self.player_two)


class MainFrame(tkinter.Frame):

    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.master.title('Tic Tac Toe')
        self.master.iconphoto(False, tkinter.PhotoImage(file='icon.ico'))
        self.master.resizable(width=False, height=False)
        super().__init__(self.master)
        self.field_var, self.fields = [], []
        self.grid()
        self.create_board()
        return

    def create_board(self):
        f = ('Arial', 50, 'bold')
        for i in range(9):
            self.field_var.append(tkinter.StringVar())
            widget = tkinter.Button(self, textvariable=self.field_var[i], width=3, height=1,
                                    command=lambda t=i: self.on_click(t), font=f)
            self.fields.append(widget)
            widget.grid(row=i // 3 + 1, column=i % 3 + 1)
        return

    def on_click(self, i):
        player = self.game.on_turn
        str_var = self.field_var[i]
        if str_var.get() not in ('X', 'O'):
            str_var.set(player.char[0])
            self.fields[i].config(fg=player.char[1])
            x, y = i // 3, i % 3
            self.game.board[x][y] = player.char[0]
            if self.game.check():
                for var in self.field_var:
                    var.set('')
                self.game.restart()
            else:
                self.game.next_turn()
        return


def main():
    player_one = Player('Player One')
    player_two = Player('Player Two')
    game = Game(player_one, player_two)
    MainFrame(tkinter.Tk(), game)
    tkinter.mainloop()
    return


if __name__ == '__main__':
    main()
