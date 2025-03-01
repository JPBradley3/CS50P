
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
