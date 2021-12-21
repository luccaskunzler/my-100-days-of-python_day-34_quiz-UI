from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quiz:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.points = 0
        self.score = Label(fg='white', bg=THEME_COLOR)
        self.score.config(text=f"Score: {self.points}")
        self.score.grid(row=0, column=1)
        self.response = None

        self.canvas = Canvas(
            width=300,
            height=250,
            bg='white',
            highlightthickness=0)
        self.text_canvas = self.canvas.create_text(
            150,
            125,
            text="Question",
            font=('Arial', 20, "italic"),
            fill="black",
            width = 280)
        self.canvas.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=20,
            pady=20)

        true_image = PhotoImage(file="./images/true.png")
        self.yes = Button(image=true_image, highlightthickness=0, command=self.click_true, borderwidth=0)
        self.yes.grid(row=2, column=0, padx=20, pady=20)

        false_image = PhotoImage(file="./images/false.png")
        self.no = Button(image=false_image, highlightthickness=0, command=self.click_false, borderwidth=0)
        self.no.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()
        self.window.mainloop()

    def click_false(self):
        is_right = self.quiz.check_answer("False")
        self.update_score(is_right)

    def click_true(self):
        is_right = self.quiz.check_answer("True")
        self.update_score(is_right)

    def update_score(self, result):
        if result:
            self.points += 1
            self.score.config(text=f"Score: {self.points}")
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_canvas, text=q_text)
        else:
            q_text = "You have reached the end of the game"
            self.canvas.itemconfig(self.text_canvas, text=q_text)
            self.no.config(state="disabled")
            self.yes.config(state="disabled")