import os
import random
import threading
import time

data = ""

def update_data():
    global data
    while True:
        combined = ""

        for filename in os.listdir("."):
            if filename != "main.py" and filename.endswith(".txt"):
                try:
                    with open(filename, "r", encoding="utf-8") as f:
                        combined += f.read()
                except:
                    pass
                
                data = combined
                time.sleep(2)
            
threading.Thread(target=update_data, daemon=True).start()

def generate_response(message):
    global data

    dataarray = data.split("\n")
    msgarray = message.split()

    startlist = []
    finalmessage = ""

    for i in range(len(dataarray) - 1):
        current_line = dataarray[i].strip()
        next_line = dataarray[i + 1].strip()

        if not current_line or not next_line:
         continue

        eachdata = current_line.split()
        next_words = next_line.split()

        if not eachdata or not next_words or not msgarray:
            continue

        if eachdata[-1].lower() == msgarray[-1].lower():
            startlist.append(next_words[0])

            if len(eachdata) > 1 and len(msgarray) > 1:
                if eachdata[-2].lower() == msgarray[-2].lower():
                    for _ in range(3):
                        startlist.append(next_words[0])

    if startlist:
        currentword = random.choice(startlist)
        finalmessage = currentword

        for _ in range(random.randint(0, 14)):
            nextword = []

            for line in dataarray:
                words = line.split()
                for j in range(len(words) - 1):
                    if currentword.lower() == words[j].lower():
                        nextword.append(words[j + 1])

            if nextword:
                currentword = random.choice(nextword)
                finalmessage += " " + currentword
            else:
                break

    return finalmessage

print("Betabot is now online.")
print("write something racist and ill speak to you i guess... ")

while True:
    user_input = input("> ")

    with open("chatlog.txt", "a", encoding="utf-8") as f:
        f.write(user_input.replace("\n", " ") + "\n")

    reply = generate_response(user_input)

    if reply:
        print("bot: ", reply)
    else:
        print("bot:...")
