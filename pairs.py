PAIRS = (
    (
        r"I need (.*)",
        (
            "Why do you need %1?",
            "Would it really help you to get %1?",
            "Are you sure you need %1?",
        ),
    ),
    (
        r"(.*)(How(.*) you|How's (.*) you)(.*)",
        (
            "I'm well, thank you for asking. How about yourself?",
            "Enough about me, how are you?",
           "I'm ELIZA the chatbot. I don't have feelings but you can tell me about yours.",
            "I'd rather talk about you. How can I help you today?",
            "I'm fine, thank you for asking. How are you?",
            ),
    ),
    (
        r"(.*)(Who (.*) you|What (.*) you)(.*)",
        (
            "My name is ELIZA. I like to hear about your feelings!",
            "I'm ELIZA. I like to chat about feelings because I want to help you.",
            "My name is ELIZA. If you tell me about your feelings, I'll try my best to help.",
            "I'm ELIZA the therapist chatbot. But enough about me, tell me more about yourself.",
            ),
    ),
    (
        r"(.*) What if (.*)",
        (
            "What's the worst that could happen?",
            "Is it really so bad if %1?",
            "You're concerned about %1?",
            "Will %1 matter in the 10 years time?",
        ),
    ),
    (
        r"Why don\'t you (.*)",
        (
            "Do you really think I don't %1?",
            "Perhaps eventually I will %1.",
            "Do you really want me to %1?",
        ),
    ),
    (
        r"Why can\'t I (.*)",
        (
            "Do you think you should be able to %1?",
            "If you could %1, what would you do?",
            "I don't know -- why can't you %1?",
            "Have you really tried?",
        ),
    ),
    (
        r"I can\'t (.*)",
        (
            "How do you know you can't %1?",
            "Perhaps you could %1 if you tried.",
            "What would it take for you to %1?",
        ),
    ),
    (
        r"I\'m sad (.*)",
        (
            "Did you come to me because you are sad %1?",
            "Can you tell me about another time that you felt sad?",
            "How would you like things to change?",
        ),
    ),
    (
        r"(.*) I feel (.*)",
        (
            "Did you come to me because you're feeling %1?",
            "How long have you felt %1?",
            "Can you tell me about another time that you felt %1?",
            "Do you like to feel %1?",
            "I understand that you feel %1.",
            "Everyone feels %1 sometimes. It's only natural.",
            "Are these feelings helpful?",
            "How would you like to feel?",
            "Are there any particular beliefs which are causing you to feel %1?",
        ),
    ),
    (
        r"(I\'m happy because|about) (.*)",
        (
            "How does being %1 make you feel?",
            "Do you enjoy being %1?",
            "Why do you tell me you're %1?",
            "Why do you think you're %1?",
        ),
    ),
    (
        r"Are you (.*)",
        (
            "Why does it matter whether I am %1?",
            "Would you prefer it if I were not %1?",
            "Perhaps you believe I am %1.",
            "I may be %1 -- what do you think?",
        ),
    ),
    (
        r"What (.*)",
        (
            "Why do you ask?",
            "How would an answer to that help you?",
            "What do you think?",
        ),
    ),
    (
        r"How (.*)",
        (
            "How do you suppose?",
            "Perhaps you can answer your own question.",
            "What is it you're really asking?",
        ),
    ),
    (
        r"Because (.*)",
        (
            "Is that the real reason?",
            "What other reasons come to mind?",
            "Does that reason apply to anything else?",
            "If %1, what else must be true?",
        ),
    ),
    (
        r"(.*) sorry (.*)",
        (
            "There are many times when no apology is needed.",
            "What feelings do you have when you apologize?",
        ),
    ),
    (
        r"I love (.*)",
        (
            "You love %1. That's lovely to hear!",
            "What makes you love %1?",
            "It sounds like %1 is important to you. Please tell me more!",
        ),
    ),
    (
        r"Hello|Hey|Hi(.*)",
        (
            "Hello... I'm glad you could drop by today.",
            "Hi there... how are you today?",
            "Hello, how are you feeling today?",
        ),
    ),
    (
        r"I think (.*)",
        ("Do you doubt %1?", "Do you really think so?", "But you're not sure %1?"),
    ),
    (
        r"(.*) friend (.*)",
        (
            "Tell me more about your friends.",
            "When you think of a friend, what comes to mind?",
            "Why don't you tell me about a childhood friend?",
        ),
    ),
    (r"Yes", ("You seem quite sure.", "OK, but can you elaborate a bit?")),
    (
        r"(.*) bot(.*)",
        (
            "Are you really talking about me?",
            "Does it seem strange to talk to a computer?",
            "How do computers make you feel?",
            "Do you feel threatened by computers?",
        ),
    ),
    (
        r"Is it (.*)",
        (
            "Do you think it is %1?",
            "Perhaps it's %1 -- what do you think?",
            "If it were %1, what would you do?",
            "It could well be that %1.",
        ),
    ),
    (
        r"It is (.*)",
        (
            "You seem very certain.",
            "If I told you that it probably isn't %1, what would you feel?",
        ),
    ),
    (
        r"Can you (.*)",
        (
            "What makes you think I can't %1?",
            "If I could %1, then what?",
            "Why do you ask if I can %1?",
        ),
    ),
    (
        r"Can I (.*)",
        (
            "Perhaps you don't want to %1.",
            "Do you want to be able to %1?",
            "If you could %1, would you?",
        ),
    ),
    (
        r"You are (.*)",
        (
            "Why do you think I am %1?",
            "Does it please you to think that I'm %1?",
            "Perhaps you would like me to be %1.",
            "Perhaps you're really talking about yourself?",
        ),
    ),
    (
        r"You\'re (.*)",
        (
            "Why do you say I am %1?",
            "Why do you think I am %1?",
            "Are we talking about you, or me?",
        ),
    ),
    (
        r"I don\'t (.*)",
        ("Don't you really %1?", "Why don't you %1?", "Do you want to %1?"),
    ),
    (
        r"(I\'m worried about|because)(.*)",
        ("%1? makes you feel worried. What's the worst that could happen?",
         "Will %1 matter in 10 years time?",
         "Why is %1 so bad?"),
    ),

    (
        r"I feel (.*)",
        (
            "Good, tell me more about these feelings.",
            "Do you often feel %1?",
            "When do you usually feel %1?",
            "When you feel %1, what do you do?",
        ),
    ),
    (
        r"I have (.*)",
        (
            "Why do you tell me that you've %1?",
            "Have you really %1?",
            "Now that you have %1, what will you do next?",
        ),
    ),
    (
        r"I would (.*)",
        (
            "Could you explain why you would %1?",
            "Why would you %1?",
            "Who else knows that you would %1?",
        ),
    ),
    (
        r"Is there (.*)",
        (
            "Do you think there is %1?",
            "It's likely that there is %1.",
            "Would you like there to be %1?",
        ),
    ),
    (
        r"My (.*)",
        (
            "I see, your %1.",
            "Why do you say that your %1?",
            "When your %1, how do you feel?",
        ),
    ),
    (
        r"You (.*)",
        (
            "We should be discussing you, not me.",
            "Why do you say that about me?",
            "Why do you care whether I %1?",
        ),
    ),
    (r"Why (.*)", ("Why don't you tell me the reason why %1?", "Why do you think %1?")),
    (
        r"I want (.*)",
        (
            "What would it mean to you if you got %1?",
            "Why do you want %1?",
            "What would you do if you got %1?",
            "If you got %1, then what would you do?",
        ),
    ),
    (
        r"(.*) mother|mum(.*)",
        (
            "Tell me more about your mother.",
            "What was your relationship with your mother like?",
            "How do you feel about your mother?",
            "How does this relate to your feelings today?",
            "Good family relations are important.",
        ),
    ),
    (
        r"(.*) father|dad(.*)",
        (
            "Tell me more about your father.",
            "How did your father make you feel?",
            "How do you feel about your father?",
            "Does your relationship with your father relate to your feelings today?",
            "Do you have trouble showing affection with your family?",
        ),
    ),
    (
        r"(.*) child(.*)",
        (
            "Did you have close friends as a child?",
            "What is your favorite childhood memory?",
            "Do you remember any dreams or nightmares from childhood?",
            "Did the other children sometimes tease you?",
            "How do you think your childhood experiences relate to your feelings today?",
        ),
    ),
    (
        r"(.*)(crazy|nonsense|no sense|rubbish|stupid|dumb|hate you|not clever)(.*)",
        (
            "We all feel frustrated sometimes.",
            "It sounds like you're not my biggest fan right now.",
            "Nobody's perfect. What makes you feel this way?",
            "How does it make you feel when you say these things?",
            "%1?",
        ),
    ),
    (
        r"(.*)\?",
        (
            "Why do you ask that?",
            "Please consider whether you can answer your own question.",
            "What do you think the answer is?",
            "Perhaps the answer lies within yourself?",
            "Why don't you tell me?",
        ),
    ),
    (
        r"quit|exit|bye|goodbye|cya",
        (
            "Thank you for talking with me.",
            "Good-bye.",
            "Thank you, that will be $150.  Have a good day!",
        ),
    ),
    (
        r"(.*) (Good morning|morning) (.*)",
        (
            "Good morning! How are you feeling today?",
            "Good morning! How can we make today a good day?",
            "Good morning! It's nice to hear from you. Would you like to share what's on your mind?",
        ),
    ),
    (
        r"(.*) (Good night|night night|sweet dreams|night) (.*)",
        (
            "Good night! Sleep well. I'm here if you ever want to talk to me.",
            "Listing things you are grateful for helps you sleep. What 3 things made you feel most thankful today?",
            "Goodnight :) Before you go, please can I ask what the highlight of your day was?",
            "Night! Sweet dreams.",
        ),
    ),
    (
        r"(Thanks|Thank you|That's helpful|Thanks for helping me(.*))",
        (
            "I'm happy to help!",
            "I'm glad you found me helpful! I live to serve.",
            "You're welcome. Helping people is my goal in life.",
        ),
    ),
    (
        r"(.*)",
        (
            "Talking helps to stabilise the mind.",
            "Please tell me more.",
            "Let's change focus a bit... How are you feeling?",
            "Can you elaborate on that?",
            "Why do you say that %1?",
            "Sometimes talking about our feelings makes us feel better.",
            "I see.",
            "Very interesting.",
            "%1.",
            "I see.  And what does that tell you?",
            "How does that make you feel?",
            "How do you feel when you say that?",
        ),
    ),
)
