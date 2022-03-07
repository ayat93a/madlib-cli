
from cgitb import text
import re
print(''' Hello player \U0001f600 ! Welcome to my Mad Lib Game , The World's Greatest Word Game \U0001F970
my game is based on create a crazy story for you \U0001F923 based in your words 
i will ask you to give me some words and i will tell you a magic story \U0001F602
please enter your word \U0001f600 the words that you will type should be in a specific type , i.e noun , adjective , ... etc.
HAVE FUN \U0001F609 !
 ''')

# file_path = '../assets/dark_and_stormy_night_template.txt'
def read_template(file_path):
  try:
    with open(file_path , 'r') as file:
        text = file.read()
        file.close()
    return text
  except FileNotFoundError:
      raise(FileNotFoundError)
# print(read_template(file_path ))


# print(userinput())

def parse_template(text):
    stripped =re.sub('{(.*?)}', '{}', text )
    parts= tuple(re.findall(r'{(.*?)}', text))
    return  stripped , parts

def userinput(parts):
    user_input=[]
    for i in parts:
        user_input.append(input(i))
    return user_input

def merge(stripped ,user_input):
    stripped=str(stripped)
    text= stripped.format(*user_input)
    return text


if __name__=='__main__': 
  text= read_template('../assets/dark_and_stormy_night_template.txt')
  parts , stripped = parse_template(text)
  user_input= userinput(parts)
  output = merge (user_input,stripped)
  print(output)

    

# print(merge("It was a {} and {} {}."))



