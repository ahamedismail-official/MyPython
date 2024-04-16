import random
secret_code=random.randint(1000,9999)
def secret(secret_code):
    if(len(str(secret_code))==len(set(a))):
        print((secret_code))
    else:
        secret()



print("NO OF GUESSES REQUIRED:")
n = int(input())

for i in range(n):
    bull = 0
    cow = 0
    print("Enter your guess:")
    guess = input()

    if secret_code == guess:
        print("YOU GUESSED RIGHT")
        break
    else:
        for j in range(len(guess)):
            if guess[j] == secret_code[j]:
                bull += 1
            elif guess[j] in secret_code:
                cow += 1
        print("RESPONSE:", bull, "bull", cow, "cow")
