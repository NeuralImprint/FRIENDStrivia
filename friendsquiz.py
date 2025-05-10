import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Quotes dataset
quotes = [
    {"quote": "How you doin'?", "char": "Joey Tribbiani"},
    {"quote": "We were on a break!", "char": "Ross Geller"},
    {"quote": "Could I BE wearing any more clothes?", "char": "Joey Tribbiani"},
    {"quote": "Joey doesn't share food!", "char": "Joey Tribbiani"},
    {"quote": "Unagi.", "char": "Ross Geller"},
    {"quote": "Pivot!", "char": "Ross Geller"},
    {"quote": "I'm not great at the advice. Can I interest you in a sarcastic comment?", "char": "Chandler Bing"},
    {"quote": "I wish I could, but I don't want to.", "char": "Phoebe Buffay"},
    {"quote": "See? He's her lobster.", "char": "Phoebe Buffay"},
    {"quote": "No uterus, no opinion.", "char": "Rachel Green"},
    {"quote": "I KNOW!", "char": "Monica Geller"},
    {"quote": "Seven!", "char": "Monica Geller"},
    {"quote": "Oh. My. God.", "char": "Janice"},
    {"quote": "Smelly Cat, Smelly Cat, what are they feeding you?", "char": "Phoebe Buffay"},
    {"quote": "It's a moo point. It's like a cow's opinion; it doesn't matter. It's moo.", "char": "Joey Tribbiani"},
    {"quote": "Could I BE any more...?", "char": "Chandler Bing"},
    {"quote": "I'm fine!", "char": "Ross Geller"},
    {"quote": "Welcome to the real world. It sucks. You're gonna love it.", "char": "Monica Geller"},
    {"quote": "I got off the plane.", "char": "Rachel Green"},
    {"quote": "They don't know that we know they know we know.", "char": "Phoebe Buffay"},
    
    # Extended quotes
    {"quote": "If I had to, I'd pee on any one of you.", "char": "Joey Tribbiani"},
    {"quote": "Because she’s your lobster!", "char": "Phoebe Buffay"},
    {"quote": "I’m hopeless and awkward and desperate for love!", "char": "Chandler Bing"},
    {"quote": "Hi, I'm Chandler. I make jokes when I'm uncomfortable.", "char": "Chandler Bing"},
    {"quote": "That's not even a word!", "char": "Monica Geller"},
    {"quote": "It's like all my life everyone has always told me, 'You're a shoe!'", "char": "Rachel Green"},
    {"quote": "My eyes! MY EYES!", "char": "Phoebe Buffay"},
    {"quote": "I'm not so good with the advice. Can I interest you in a sarcastic comment?", "char": "Chandler Bing"},
    {"quote": "I grew up with Monica. If you didn't eat fast, you didn't eat.", "char": "Ross Geller"},
    {"quote": "It's not that common, it doesn't happen to every guy, and it is a big deal!", "char": "Rachel Green"},
    {"quote": "I'm gonna go get one of those job things.", "char": "Rachel Green"},
    {"quote": "I'm sorry, did my back hurt your knife?", "char": "Chandler Bing"},
    {"quote": "I’m curvy, and I like it!", "char": "Joey Tribbiani"},
    {"quote": "I say more dumb things before 9 a.m. than most people say all day.", "char": "Chandler Bing"},
    {"quote": "You were my midnight mystery kisser?", "char": "Rachel Green"},
    {"quote": "Your laundry is evil.", "char": "Phoebe Buffay"},
    {"quote": "I'm Chandler. I make jokes when I'm uncomfortable.", "char": "Chandler Bing"},
    {"quote": "Paper! Snow! A ghost!", "char": "Joey Tribbiani"},
    {"quote": "I'm gonna die alone.", "char": "Monica Geller"},
    {"quote": "Look at me! I'm Chandler! Could I BE wearing any more clothes?", "char": "Joey Tribbiani"}
]


all_chars = list(set(q["char"] for q in quotes))

# # Mapping for character images
# char_images = {
#     "Joey Tribbiani": "joey.jpg",
#     "Ross Geller": "ross.jpg",
#     "Chandler Bing": "chandler.jpg",
#     "Phoebe Buffay": "phoebe.jpg",
#     "Rachel Green": "rachel.jpg",
#     "Monica Geller": "monica.jpg",
#     "Janice": "janice.jpg",
# }


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FRIENDS Quiz")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Background
        bg_img = Image.open("friends.jpg").resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(bg_img)
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.q_no = 0
        self.score = 0
        self.qs = []
        self.cur_q = None
        self.timer_id = None
        self.time_left = 10

        self.q_label = tk.Label(root, text="", wraplength=700, font=("Helvetica", 18, "bold"), bg="#fff8f0")
        self.q_label.pack(pady=30)

        self.image_label = tk.Label(root, bg="#fff8f0")
        self.image_label.pack()

        self.btns = []
        for i in range(4):
            b = tk.Button(root, text="", font=("Arial", 14), width=40, height=2, bg="#f4c542", fg="black",
                          command=lambda i=i: self.check_ans(i))
            b.pack(pady=5)
            self.btns.append(b)

        self.timer_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="red", bg="#fff8f0")
        self.timer_label.pack(pady=15)

        self.status = tk.Label(root, text="", font=("Arial", 12), bg="#fff8f0")
        self.status.pack(pady=10)

        self.start_quiz()

    def start_quiz(self):
        self.qs = random.sample(quotes, 5)
        self.q_no = 0
        self.score = 0
        self.next_q()

    def next_q(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        if self.q_no >= 5:
            self.show_result()
            return

        self.cur_q = self.qs[self.q_no]
        quote = self.cur_q["quote"]
        ans = self.cur_q["char"]
        wrong = random.sample([c for c in all_chars if c != ans], 3)
        self.opts = wrong + [ans]
        random.shuffle(self.opts)

        self.q_label.config(text=f"Q{self.q_no + 1}: \"{quote}\"")
        for i, opt in enumerate(self.opts):
            self.btns[i].config(text=opt, state=tk.NORMAL, bg="#f4c542")

        # Load image
        #img_path = char_images.get(ans)
        # if img_path:
        #     img = Image.open(img_path).resize((200, 200))
        #     self.photo = ImageTk.PhotoImage(img)
        #     self.image_label.config(image=self.photo)
        # else:
        #     self.image_label.config(image="")

        self.status.config(text=f"Question {self.q_no + 1} of 5")

        self.time_left = 10
        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text=f"Time Left: {self.time_left}s")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.disable_buttons()
            pygame.mixer.music.load("wrong.wav")
            pygame.mixer.music.play()
            self.root.after(1500, self.next_q)

    def disable_buttons(self):
        for btn in self.btns:
            btn.config(state=tk.DISABLED, bg="#ccc")

    def check_ans(self, idx):
        selected = self.opts[idx]
        correct = self.cur_q["char"]
        if selected == correct:
            self.score += 1
            self.btns[idx].config(bg="green")
            pygame.mixer.music.load("correct.wav")
        else:
            self.btns[idx].config(bg="red")
            pygame.mixer.music.load("wrong.wav")
        pygame.mixer.music.play()
        self.disable_buttons()

        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        self.q_no += 1
        self.root.after(1500, self.next_q)

    def show_result(self):
        msg = f"You scored {self.score}/5!\n"
        if self.score == 5:
            msg += "You're a true FRIENDS fanatic!"
        elif self.score >= 3:
            msg += "Well done! You know your FRIENDS pretty well."
        else:
            msg += "Hmm... time for a few reruns!"

        play = messagebox.askyesno("Quiz Over", msg + "\n\nPlay again?")
        if play:
            self.start_quiz()
        else:
            self.root.destroy()


# Run the app
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
