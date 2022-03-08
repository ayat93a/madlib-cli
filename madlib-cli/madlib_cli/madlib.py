
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

def userinput(stripped ):
    user_input=[]
    # parts=list(parts)
    for i in stripped :
        user_input.append(input(i))
        # print(i)
    return user_input


def merge(parts ,user_input):
    parts=str(parts)
    text= parts.format(*user_input)
    return text


if __name__=='__main__': 
  text= read_template('madlib.txt')
  parts , stripped = parse_template(text)
  user_input= userinput(stripped )
  output = merge (parts,user_input)
  print(output)
  my_file = open("this_is_file.txt","w+")
  my_file.write(output)

    

# print(merge("It was a {} and {} {}."))



