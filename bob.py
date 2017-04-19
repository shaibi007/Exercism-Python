import re

def hey(txt):
    text = txt.rstrip()
    if text.isupper():
        return "Whoa, chill out!"
    elif text[-1:] == "?":
        return "Sure."
    elif not text:
        return "Fine. Be that way!"
    else:
        return "Whatever."
def main():
    print(hey("You are, what, like 15?"))
    print(hey("WHAT THE HELL WERE YOU THINKING?"))
    print(hey("\t\t\t\t\t\t\t\t\t\t"))
    print(hey("This is a statement ending with whitespace?      "))

if __name__ == '__main__':
    main()
