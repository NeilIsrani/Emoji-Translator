'''
Homework 6
Neil Israni
Program 1: Emojini
This program implements a text transformation solution that
substitutes words to and from english and their appropriate
text-based emojis based on instructions in another directives
text file.
'''

def load_dictionary(emoji_file_name: str):
    '''
    This function loads a dictionary for all the languages in the
    emoji_file_name file, in the form of keys being the language
    names and their lower case words or emojis being the values.
    Returns: dictionary for all languages in the form of keys being
    the language names and their lower case words or emojis being
    the values.
    Parameters: emoji_file_name text file which contains language
    names as first row and their words or emojis in their respective
    columns.
    '''
    dictionary = {}
    with open(emoji_file_name, 'r') as infile:
        sentence = infile.read().splitlines()
        for i in range(len(sentence)):
            if i == 0:
                languages_list = sentence[0].lower().split()
                languages_list.pop(0)
                for name in languages_list:
                    name_copy = name.lower()
                    dictionary[name_copy] = []
            elif i > 0:
                languages_list = list(dictionary.keys())
                values = sentence[i].split()
                for j in range(len(values)):
                    if languages_list[j] == "english":
                        real_value = values[j].lower()
                        dictionary[languages_list[j]].append(real_value)
                    else:
                        dictionary[languages_list[j]].append(values[j]) 
    return dictionary

def batch_translate(emoji_file_name: str, directives_file_name: str):
    '''
    This function first loads our dictionary through load_dictionary function
    and then reads the directives file and extracts useful information of
    which language to translate from, language to translate to, file to
    translate and what the translated file should be named. Then, it uses
    this information to create our new translated file with unchanged
    line indentations.
    Returns: txt file of translated document.
    Parameters: emoji_file_name txt file which contains language
    names as first row and their words or emojis in their respective
    columns, and directives_file_name txt which has instructions
    of language to translate from, language to translate to, file to
    translate and what the translated file should be named.
    '''
    try:
        dictionary = load_dictionary(emoji_file_name)
        with open(directives_file_name, 'r') as infile:
            instructions = infile.read().splitlines()
            for instruction in instructions:
                translations = []
                words = instruction.split(' ')
                language_from = words[0].lower()
                language_to = words[1].lower()
                conversion_file = words[2]
                new_file = words[3]
                print(f"Converting {conversion_file} to {new_file}")
                with open(conversion_file, 'r') as infile:
                    lines_to_convert = infile.readlines()
                    for line in lines_to_convert:
                        translated_line = []
                        words_to_convert = line.split()
                        for word in words_to_convert:
                            if word not in dictionary[language_from]:
                                translated_line.append(word)
                            else:
                                value_w = dictionary[language_from].index(word)
                                trs_word = dictionary[language_to][value_w]
                                translated_line.append(trs_word)
                        translations.append(' '.join(translated_line))
                output = '\n'.join(translations)
                with open(new_file, 'w') as outfile: 
                    outfile.write(output)
    except FileNotFoundError as err: 
        print(err)
              
def main():
    emoji = "emojis.txt"
    directives = "emoji_directives.txt"
    translator = batch_translate(emoji, directives)

if __name__ == "__main__":
    main()
