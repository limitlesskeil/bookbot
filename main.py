def main():
    path="books/frankenstein.txt"
    all = get_book_text(path)
    count = get_count(all)
    letters = letter_count(all)
    list = create_list(letters)
    list.sort(reverse=True, key=sort_on)
    report = create_report(list)
    #print(all)
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document")
    print(" ")
    print(report)
    print("--- End report ---")
    #print(list)

def get_book_text(path):
    with open(path) as content:
        return content.read()

def get_count(all):
    words = all.split()
    return len(words)

def letter_count(all):
    alphabet = {}
    lower_case = all.lower()
    for letter in lower_case:
        if (letter not in alphabet):
            alphabet[letter] = 1
        else:
            alphabet[letter] +=1
    return alphabet

def create_list(letters):
    letters_list = []

    for letter, count in letters.items():
        if(letter.isalpha()):
            letter_dict = {"letter": letter, "count": count}
            letters_list.append(letter_dict)
        #print(letter)
    return letters_list

def sort_on(dict):
    return dict["count"]

def create_report(list):
    report_string = ""
    len_list = len(list)
    for i in range(0, len_list):
        temp_dict = list[i]
        print(temp_dict)
        temp_line = (f"The '{temp_dict["letter"]}' character was found {temp_dict["count"]} times\n")
        report_string += temp_line
    return report_string.rstrip()


main()