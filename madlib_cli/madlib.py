import re



def read_template(path):
    try:
        file = open(path)
    except FileNotFoundError:
        print('File path is invalid')
        raise FileNotFoundError
    else:
        content = file.read()
        file.close()
        return content
        

def parse_template(content):
    # print(type(content))
    parts = re.findall('{(.+?)}',content)
    
    # print(parts)
    for part in parts:
        # print(part)
        content = re.sub(part, "", content)
    # print(content)
    parts = tuple(parts)
    # print(parts)
    
    return  content, parts

def user_input(parts):
    user_inputs = []
    for part in parts:
      item  = input(f'Please type in {part}: ')
      user_inputs.append(item)
    return user_inputs
    
   

def merge(content,user_inputs):

    for item in user_inputs:
        result = content.format(*user_inputs)
        
        # print(result)
    return result


if __name__ == '__main__':
    print('''
    ****Mad Libs is a phrasal template word game. It consists of one player prompting others for a list of
    ****words to substitute for blanks in a story before reading aloud
    ****So please type in what is needed like adjective, noun, etc when asked and see the outcome unfold\n''')

    read = read_template('assets/madlib.txt')
    parse, words = parse_template(read)
    inputs  = user_input(words)
    finished = merge (parse,inputs)
    
    print(finished)
            



            
# parse_template(read_template("assets/dark_and_stormy_night_template.txt"))

# merge("It was a {} and {} {}.", ['Red','blue','Zaid'])

        
            


       

