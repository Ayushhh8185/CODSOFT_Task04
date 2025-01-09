import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f8ff")  

        self.choices = ["Rock", "Paper", "Scissors"]

        
        self.title_label = tk.Label(
            root, text="Rock Paper Scissors", font=("Helvetica", 24, "bold"), bg="#f0f8ff", fg="#4682b4"
        )
        self.title_label.pack(pady=20)

        
        self.score_frame = tk.Frame(root, bg="#f0f8ff")
        self.score_frame.pack(pady=10)

        self.player_score_label = tk.Label(
            self.score_frame, text="Player: 0", font=("Helvetica", 14), bg="#f0f8ff", fg="#4682b4"
        )
        self.player_score_label.grid(row=0, column=0, padx=20)

        self.computer_score_label = tk.Label(
            self.score_frame, text="Computer: 0", font=("Helvetica", 14), bg="#f0f8ff", fg="#4682b4"
        )
        self.computer_score_label.grid(row=0, column=1, padx=20)

       
        self.button_frame = tk.Frame(root, bg="#f0f8ff")
        self.button_frame.pack(pady=20)

        self.rock_button = tk.Button(
            self.button_frame, text="Rock", font=("Helvetica", 14, "bold"), bg="#4682b4", fg="#ffffff",
            width=10, command=lambda: self.play("Rock")
        )
        self.rock_button.grid(row=0, column=0, padx=10)
        self.rock_button.bind("<Enter>", lambda e: self.on_hover(self.rock_button))
        self.rock_button.bind("<Leave>", lambda e: self.on_leave(self.rock_button))

        self.paper_button = tk.Button(
            self.button_frame, text="Paper", font=("Helvetica", 14, "bold"), bg="#4682b4", fg="#ffffff",
            width=10, command=lambda: self.play("Paper")
        )
        self.paper_button.grid(row=0, column=1, padx=10)
        self.paper_button.bind("<Enter>", lambda e: self.on_hover(self.paper_button))
        self.paper_button.bind("<Leave>", lambda e: self.on_leave(self.paper_button))

        self.scissors_button = tk.Button(
            self.button_frame, text="Scissors", font=("Helvetica", 14, "bold"), bg="#4682b4", fg="#ffffff",
            width=10, command=lambda: self.play("Scissors")
        )
        self.scissors_button.grid(row=0, column=2, padx=10)
        self.scissors_button.bind("<Enter>", lambda e: self.on_hover(self.scissors_button))
        self.scissors_button.bind("<Leave>", lambda e: self.on_leave(self.scissors_button))

       
        self.result_label = tk.Label(
            root, text="Make your choice!", font=("Helvetica", 16, "italic"), bg="#f0f8ff", fg="#4682b4"
        )
        self.result_label.pack(pady=20)

       
        self.player_score = 0
        self.computer_score = 0

    def play(self, player_choice):
        computer_choice = random.choice(self.choices)

        if player_choice == computer_choice:
            result_text = f"It's a tie! Both chose {player_choice}."
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            self.player_score += 1
            result_text = f"You win! {player_choice} beats {computer_choice}."
        else:
            self.computer_score += 1
            result_text = f"You lose! {computer_choice} beats {player_choice}."

        self.update_scores()
        self.result_label.config(text=result_text)

    def update_scores(self):
        self.player_score_label.config(text=f"Player: {self.player_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")

    def on_hover(self, button):
        button.configure(bg="#87ceeb")  

    def on_leave(self, button):
        button.configure(bg="#4682b4")  

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
