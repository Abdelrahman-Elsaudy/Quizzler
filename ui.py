from tkinter import *
from quiz_brain import quiz

THEME_COLOR = "#375362"
RIGHT_COLOR = "#029220"
WRONG_COLOR = "#ff0000"


class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text="score:0", bg=THEME_COLOR, fg="white", font=["arial", 10])
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="a question",
                                                     fill=THEME_COLOR,
                                                     width=280,
                                                     font=["arial", 20, "italic"])
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="./images/true.png")
        self.right = Button(image=true_image, highlightthickness=0, command=self.right_click)
        self.right.grid(column=0, row=2)

        false_image = PhotoImage(file="./images/false.png")
        self.wrong = Button(image=false_image, highlightthickness=0, command=self.wrong_click)
        self.wrong.grid(column=1, row=2)

        self.user_answer = None
        self.display()
        self.window.mainloop()

    def display(self):
        self.right.config(state="active")
        self.wrong.config(state="active")
        if quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"Q.{quiz.number+1}: {quiz.text}")
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the game.")
            self.canvas.config(bg="white")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def right_click(self):
        self.user_answer = "true"
        self.right.config(state="disabled")      # Buttons are disabled till the next question
                                                 # to prevent several clicks for the same question.
        self.wrong.config(state="disabled")
        self.give_feedback()

    def wrong_click(self):
        self.user_answer = "false"
        self.right.config(state="disabled")
        self.wrong.config(state="disabled")
        self.give_feedback()

    def give_feedback(self):
        if quiz.check_answer(self.user_answer) is True:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"score: {quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, quiz.next_question)
        self.window.after(1000, self.display)
