from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
figlet.getFonts()


if len(sys.argv) == 1:
    is_random = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    is_random = False
else:
    print("Invalid Usage")
    sys.exit(1)

if is_random == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())


text = input("Input:")
print("Output:", figlet.renderText(text))
