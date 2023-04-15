from random import randrange
password = []
while len(password) != 4:
    p = randrange(1, 10)
    if p not in password:
        password.append(p)
pw = password[0] * 1000 + password[1] * 100 + password[2] * 10 + password[3]
guess = eval(input("Please enter your guess:"))
g1 = int(guess / 1000)
g2 = int((guess - g1 * 1000) / 100)
g3 = int((guess - g1 * 1000 - g2 * 100) / 10)
g4 = int(guess - g1 * 1000 - g2 * 100 - g3 * 10)
while guess != pw:
    if guess < 1000 or guess > 9999:
        print("Please enter number between 1000 to 9999.")
    elif g1 == g2 or g1 == g3 or g1 == g4 or g2 == g3 or g3 ==g4:
        print("You can't enter repeated number.")
    else:
        count1, count2 = 0, 0
        if g1 == password[0]:
            count1 += 1
        if g2 == password[1]:
            count1 += 1
        if g3 == password[2]:
            count1 += 1
        if g4 == password[3]:
            count1 += 1
        if g1 != password[0] and g1 in password:
            count2 += 1
        if g2 != password[1] and g2 in password:
            count2 += 1
        if g3 != password[2] and g3 in password:
            count2 += 1
        if g4 != password[3] and g4 in password:
            count2 += 1
        print(f"{count1}A{count2}B")
        if guess != pw:
            guess = eval(input("Please enter your guess:"))
            g1 = int(guess / 1000)
            g2 = int((guess - g1 * 1000) / 100)
            g3 = int((guess - g1 * 1000 - g2 * 100) / 10)
            g4 = int(guess - g1 * 1000 - g2 * 100 - g3 * 10)
print("You got it!")