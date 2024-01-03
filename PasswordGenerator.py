import random
import string

if __name__ == "__main__":
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    
    try:

        askLength = int(input("Enter Password Length \n"))
        askLengthUpper = int(input("Enter Password Length of UpperChar \n"))
        askLengthLower = int(input("Enter Password Length of LowerChar \n"))
        askLengthDigit = int(input("Enter Password Length of Digits\n"))
        askLengthSpecial = int(input("Enter Password Length of SpecialChar \n"))

        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        # random.shuffle(s)
        ran1 = random.sample(s1,askLengthUpper)
        ran2 = random.sample(s2,askLengthLower)
        ran3 = random.sample(s3,askLengthDigit)
        ran4 = random.sample(s4,askLengthSpecial)

        d = ran1 + ran2 + ran3 + ran4
        print("Your Generated Password : ")
        print("".join(d[0:askLength]))

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    # print("".join(s[0:askLength]))