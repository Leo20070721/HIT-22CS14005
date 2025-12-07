import random
import tkinter as tk
from tkinter import scrolledtext, font


class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.active = True
    def choose(self):
        choices = ['石头','剪刀','布']
        return random.choice(choices)

class Game:
    def __init__(self,num_players=5,text_area=None):
        self.num_players = [Player(i+1)for i in range(num_players)]
        self.round = 1
        self.text_area = text_area#scrolledtext.ScrolledText()

    def log(self, message):
        if self.text_area:
            self.text_area.insert(tk.END, message + "\n")
            self.text_area.see(tk.END)
        else:
            print(message)

    def get_active_players(self):
        return [p for p in self.num_players if p.active]

    def run(self):
        active_players = self.get_active_players()
        if len(active_players) == 1:
            self.log(f"游戏结束！最终获胜的玩家是{active_players[0].id}")
            return False
        self.log(f"----第{self.round}轮----")
        self.log(f"当前参赛玩家：{[p.id for p in active_players]}")
        choices = {p: p.choose() for p in active_players}
        for p,c in choices.items():
            self.log(f"玩家{p.id}选择了：{c}")
        winners = self.determine_winners(choices)
        eliminated = []
        for p in active_players:
            if p not in winners:
                eliminated.append(p)
        for p in eliminated:
            p.active = False
        if eliminated:
            self.log(f"本轮淘汰玩家：{[p.id for p in eliminated]}")
            self.log(f"本轮获胜玩家：{[p.id for p in winners]}")
        else:
            self.log("本轮未决出胜负，开始新的一轮")

        active_players = self.get_active_players()
        if len(active_players) == 1:
            self.log(f"游戏结束！最终获胜的玩家是{active_players[0].id}")
            return False

        self.round += 1
        return True

    def determine_winners(self, choices):
        unique_choices = list(set(choices.values()))
        if len(unique_choices) == 1:
            return list(choices.keys())

        if len(unique_choices) == 2:
            c1, c2 = unique_choices[0], unique_choices[1]

            win_pairs = [("石头", "剪刀"), ("剪刀", "布"), ("布", "石头")]
            if (c1, c2) in win_pairs:
                winner = c1
            elif (c2, c1) in win_pairs:
                winner = c2
            else:
                return list(choices.keys())
            return [p for p, c in choices.items() if c == winner]

        eliminated = '剪刀' if '石头' in choices else \
            '布' if '剪刀' in choices else '石头'
        return [p for p, c in choices.items() if c != eliminated]

class GUI:
    def __init__(self,root):
        self.root = root
        self.root.title("石头剪刀布游戏")
        self.root.geometry("640x520")
        self.root.resizable(True,True)
        self.custom_font=font.Font(family="SimHei",size=10)
        self.text_area = scrolledtext.ScrolledText(root,wrap=tk.WORD,font=self.custom_font,
        bg="#f0f0f0",padx=10,pady=10)
        self.text_area.pack(padx=10,pady=15,fill=tk.X)
        self.text_area.config(state=tk.NORMAL)

        self.button_frame=tk.Frame(root)
        self.button_frame.pack(side=tk.LEFT,fill=tk.X)

        self.start_btn = tk.Button(self.button_frame,text="开始游戏",command=self.start_game,
                                   font=self.custom_font,bg="#4CAF50",fg="white",height=2)
        self.start_btn.pack(side=tk.LEFT,padx=5,fill=tk.X,expand=True)

        self.next_btn = tk.Button(self.button_frame, text="下一轮", command=self.next_round,
                                   font=self.custom_font, bg="#2196F3", fg="white", height=2,state=tk.DISABLED)
        self.next_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.reset_btn = tk.Button(self.button_frame, text="重置游戏", command=self.reset_game,
                                   font=self.custom_font, bg="#4CAF50", fg="white", height=2)
        self.reset_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.name_btn = tk.Button(self.button_frame, text="刘宇轩",
                                   font=self.custom_font, bg="#"+str(hex(random.randint(0,255))[2:])+str(hex(random.randint(0,255))[2:])+str(hex(random.randint(0,255))[2:]), fg="white", height=2)
        self.name_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.game = None

    def start_game(self):
        self.text_area.delete("1.0",tk.END)
        self.text_area.insert(tk.END,"--------石头剪刀布游戏开始--------\n")
        self.game = Game(5,self.text_area)
        self.start_btn.config(state=tk.DISABLED)
        self.next_btn.config(state=tk.NORMAL)
    def next_round(self):
        if self.game:
            continue_game=self.game.run()
            if not continue_game:
                self.next_btn.config(state=tk.DISABLED)
                self.start_btn.config(state=tk.NORMAL)
    def reset_game(self):
        self.text_area.delete("1.0",tk.END)
        self.game = None
        self.start_btn.config(state=tk.NORMAL)
        self.next_btn.config(state=tk.DISABLED)



if __name__ == "__main__":
    root=tk.Tk()
    app=GUI(root)
    root.mainloop()