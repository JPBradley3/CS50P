### Same code using a tupple set up in main

def main():
    information = get_info()

    ## The tupple returns an indexed series of values and this archaetecture can keep getting mroe sophisticated.
    print(f"{information[0]}, {information[1]}")

def get_info():
          a = input("name: ")
          b = input("house: ")

          ## Putting a container on this line makes the tupple get searched as [] = list () = Variables {} = dictionary
          return a, b

if __name__ == "__main__":
       main()
