# Emoticon to Emoji Converter\\ \large Python Application


## Introduction

This is a simple Python script that converts text emoticons (`":)"` and `":("`) into their corresponding Unicode emojis (`🙂` and `🙁`). The script reads a user-inputted sentence, performs the conversion, and displays the result.

## Requirements

- Python 3.x

## Installation

No installation is necessary. Just ensure Python 3 is available on your system.

## Usage

1. Save the script to a file, e.g., `emoticon_to_emoji.py`.

2. Open your terminal or command prompt.

3. Run the script using the command:

```

python emoticon_to_emoji.py

```

4. Enter a sentence containing emoticons like `":)"` and/or `":("` when prompted.

5. The output will display your sentence with the appropriate emojis.

## Example

**Input:**

```

Please input a sentence with emoticons: Hello there! :)

```

**Output:**

```

Hello there! 🙂

```

## Source Code

```python
def main():

## Get User Input Labeled as "sentence"
sentence = input("Please input a sentence with emoticons: ")
sentence = convert(sentence)
print(sentence)

## Define a function called convert that takes the constant variable "sentence" from above and explicitly converts the needed characters and no others.
def convert(sentence):

## Find the emoji and repreint them with the actual emoji
sentence = sentence.replace(":)", "🙂")
sentence = sentence.replace(":(", "🙁")
return sentence

main()
```

## Customization

Currently, only `":)"` and `":("` are converted. To add more emoticons, simply extend the `convert` function.
