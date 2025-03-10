import re
import sys

def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r'\b(um)\b', s, re.IGNORECASE) # re.IGNORECASE makes the search case-insensitive
    return len(matches)


if __name__ == "__main__":
    main()
