import streamlit as st
from PIL import Image
import random
import time

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

def run_quiz():
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "q_no" not in st.session_state:
        st.session_state.q_no = 0
    if "qs" not in st.session_state:
        st.session_state.qs = random.sample(quotes, 5)
    if "time_left" not in st.session_state:
        st.session_state.time_left = 10
    if "opts" not in st.session_state:
        st.session_state.opts = []
    if "current_question" not in st.session_state:
        st.session_state.current_question = st.session_state.qs[st.session_state.q_no]

    st.title("FRIENDS Quiz")
    
    # Show background image
    bg_image = Image.open("friends.jpg")
    st.image(bg_image, use_column_width=True)

    st.markdown(f"### Q{st.session_state.q_no + 1}: \"{st.session_state.current_question['quote']}\"")

    correct_char = st.session_state.current_question["char"]
    wrong_chars = random.sample([c for c in all_chars if c != correct_char], 3)
    options = wrong_chars + [correct_char]
    random.shuffle(options)
    st.session_state.opts = options

    # Buttons for options
    def check_answer(selected):
        if selected == correct_char:
            st.session_state.score += 1
            st.success("Correct!")
        else:
            st.error(f"Wrong! Correct answer was: {correct_char}")
        st.session_state.q_no += 1
        if st.session_state.q_no < 5:
            st.session_state.current_question = st.session_state.qs[st.session_state.q_no]
            st.experimental_rerun()
        else:
            st.experimental_rerun()

    for opt in options:
        if st.button(opt):
            check_answer(opt)
            break

    # Show score and progress
    st.write(f"Question {st.session_state.q_no + 1} of 5")
    st.write(f"Score: {st.session_state.score}")

    # Show result if quiz is over
    if st.session_state.q_no >= 5:
        st.markdown(f"## Quiz Over!")
        st.markdown(f"Your final score: {st.session_state.score}/5")
        if st.session_state.score == 5:
            st.success("You're a true FRIENDS fanatic!")
        elif st.session_state.score >= 3:
            st.info("Well done! You know your FRIENDS pretty well.")
        else:
            st.warning("Hmm... time for a few reruns!")

        if st.button("Play Again"):
            st.session_state.score = 0
            st.session_state.q_no = 0
            st.session_state.qs = random.sample(quotes, 5)
            st.session_state.current_question = st.session_state.qs[0]
            st.experimental_rerun()

if __name__ == "__main__":
    run_quiz()
