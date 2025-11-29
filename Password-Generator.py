# Important Note! : This code is created for only experimantal purposes only, use it on your own risk #
# Önemli Not! : Bu kod sadece deneysel amaçlarla oluşturulmuştur, kullanımı kendi sorumluluğunuzdadır #
import random # <-- Calls 'random' library for generating random patterns
import string # <-- Calls 'string' library to select the characters to be used in the password.


# Welcome Page # <-- Contains the welcome page and starts it.
def welcome():
    print(),print()
    print("Welcome To Random Password Generator!")
    print()
    wel_answer = input("To continue, type (Y/N?): ")
    if wel_answer not in ("y", "Y", "n", "N"):
        print("Please enter a valid value"),print(""),welcome()
    if wel_answer in ("n", "N"):
        quit(0)
    print("")
welcome() # <-Starts the definition

# End Welcome Page #


# Language Choose # <-- This section make user to choose a language. (English/Turkish)
def ask_lang():
    global lang
    lang = str("E") # The program comes with english language.
    print("Please choose a language to continue (English/Turkish)")
    lang_answer = input("(E/T?):")
    if lang_answer not in ("e", "E", "t", "T"):
        print("Please enter a valid value!"),print(""),ask_lang() # Gives an error message when user types an unintended input. 
    if lang_answer in ("e", "E"):
        lang = str("E")
    if lang_answer in ("t", "T"):
        lang = str("T")
ask_lang() # <-Starts the definition

# End Language Choose #


# Language Text Parts # <-- This section contains texts for both languages.
##>English Language
def lang_eng():
    global text_ask_q, error_value_q, error_amount_q, text_pass_start, text_ask_l, text_ask_d, text_ask_p, error_value, error_char_n, text_pass, text_pass_end, text_gen_again
    text_pass_start = ("Adjust The Password Rules!") 
    text_ask_q = ("Set the password length (10-128): ")
    error_value_q = ("ValueError!: Please enter an integer!")
    error_amount_q = ("ValueError!: Please enter an integer between 10 and 128!")
    text_ask_l = ("Password contain letters (Y/N?):")
    error_value = ("Please enter a valid value")
    text_ask_d = ("Password contain digits (Y/N?):")
    text_ask_p = ("Password contain punctuations (Y/N?):")
    error_char_n = ("LogicalError!: Please choose at least one character type to generate password")
    text_pass = ("The Password = ")
    text_pass_end = ("The Password Has Been Generated")
    text_gen_again = ("Create new password? (Y): ") 
    
##>Turkish Language
def lang_tr():
    global text_ask_q, error_value_q, error_amount_q, text_pass_start, text_ask_l, text_ask_d, text_ask_p, error_value, error_char_n, text_pass, text_pass_end, text_gen_again
    text_pass_start = ("Şifre Kurallarını Ayarla!") 
    text_ask_q = ("Şifre Uzunluğunu belirle (10-128): ")
    error_value_q = ("DeğerHatası!: Lütfen bir tam sayı girin!")
    error_amount_q = ("DeğerHatası!: Lütfen 10 ila 128 arasında tam sayı girin!")
    text_ask_l = ("Şifre Harf İçersin (E/H?):")
    error_value = ("Lütfen Geçerli Bir Değer Girin!")
    text_ask_d = ("Şifre Sayı İçersin (E/H?):")
    text_ask_p = ("Şifre Özel Karakterler İçersin (E/H?):")
    error_char_n = ("MantıkHatası!: Lütfen en azından bir karakter tipi seçin!")
    text_pass = ("Şifre = ")
    text_pass_end = ("Şifre Oluşturma İşlemi Tamamlandı")
    text_gen_again = ("Yeni şifre oluştur (E): ") 
##>Select Language
if lang == ("E"): lang_eng()
elif lang == ("T"): lang_tr()
else: print("unkown error in language text parts")

# End Language Text Parts #


# Password Rules # <-- Asks user to under what specified conditions the password will be created like password longess etc.

def rules_pass_start():
    print("")
    print(text_pass_start)
    print("")
rules_pass_start() # <-Starts the definition

def quantity_pass(): # <-Asks user to determine the password lenght
    global pass_longness
    ask_quantity = int("10")
    try:
        ask_quantity = int(input(text_ask_q)) # Asks how many characters the password should contain.
    except ValueError: print(error_value_q),print(""),quantity_pass() # Gives an error message if user input other than integer.
    if ask_quantity < 10 or ask_quantity > 128: # Looks if the user input between 10-128, (note: you can change the min/max length of the password with changing these numbers)
        print(error_amount_q),print(""),quantity_pass()
    pass_longness = (ask_quantity) # <- 'ask_quantity' variable only use in this definition/section of the code, outside of this, ‘pass_longness’ is used.
quantity_pass() # <-Starts the definition

def rules_pass_letter(): # Asks the user whether they want to use letters in the password and receives the answer along with through selected language.
    global use_letter
    use_letter = str("Y") # Starts the def with, using letters open
    use_letter = input(text_ask_l) # Asks, use letters in the password or not.
    if lang == "E":
        if use_letter not in ("y","Y","n","N"): # <- receives the answer in the selected language
            print(error_value),print(""),rules_pass_letter() # <- Gives an error message when user types an unintended input. And Starts the definition again.
        elif use_letter in ("y","Y"):
            use_letter = str("Y")
        else: 
            use_letter = str("N")
    elif lang == "T":
        if use_letter not in ("e","E","h","H"): # <- receives the answer in the selected language (E = yes, H = no)
            print(error_value),print(""),rules_pass_letter() # <- Gives an error message when user types an unintended input. And Starts the definition again.
        elif use_letter in ("e","E"):
            use_letter = str("Y")
        else: 
            use_letter = str("N")
    else: print("unkown error in rules_pass_letter definition")
rules_pass_letter() # <-Starts the definition

def rules_pass_digit():# Asks the user whether they want to use digits in the password and receives the answer along with through selected language.
    global use_digit
    use_digit = str("Y") # Starts the def with, using digits open
    use_digit= input(text_ask_d) # Asks, use letters in the password or not.
    if lang == "E":
        if use_digit not in ("y","Y","n","N"): # <- receives the answer in the selected language
            print(error_value),print(""),rules_pass_digit() # <- Gives an error message when user types an unintended input. And Starts the definition again.
        elif use_digit in ("y","Y"):
            use_digit = str("Y")
        else: 
            use_digit = str("N")
    elif lang == "T":
        if use_digit not in ("e","E","h","H"): # <- receives the answer in the selected language (E = yes, H = no)
            print(error_value),print(""),rules_pass_digit() # <- Gives an error message when user types an unintended input. And Starts the definition again.
        elif use_digit in ("e","E"):
            use_digit = str("Y")
        else: 
            use_digit = str("N")
    else: print("unkown error in rules_pass_digit definition")
rules_pass_digit() # <-Starts the definition

def rules_pass_punct(): # Asks the user whether they want to use punctuations in the password and receives the answer along with through selected language.
    global use_punct
    use_punct = str("Y") # Starts the def with, using punct open
    use_punct = input(text_ask_p)
    if lang == "E":
        if use_punct not in ("y","Y","n","N"): # <- receives the answer in the selected language
            print(error_value),print(""),rules_pass_punct() # <- Gives an error message when user types an unintended input. And Starts the definition again.
        elif use_punct in ("y","Y"):
            use_punct = str("Y")
        else: 
            use_punct = str("N")
    elif lang == "T":
        if use_punct not in ("e","E","h","H"): # <- receives the answer in the selected language (E = yes, H = no)
            print(error_value),print(""),rules_pass_punct() # <- Gives an error message when user types an unintended input. And Starts the definition again.
        elif use_punct in ("e","E"):
            use_punct = str("Y")
        else: 
            use_punct = str("N")
    else: print("unkown error in rules_pass_digit definition")
rules_pass_punct() # <-Starts the definition

if use_letter == use_digit and use_digit == use_punct and use_punct == "N":
    print(""),print(error_char_n),print("")
    rules_pass_start()
    rules_pass_letter()
    rules_pass_digit()
    rules_pass_punct()

# End Password Rules #


# Lists For Charachers # <-- Creates the lists of the characters that is going to be used in password
list_ascii = list(string.ascii_letters)
list_digit = list(string.digits)
list_punct = list(string.punctuation)
# End Lists For Characters #


# Percentages # <-- Creates a lists and variables to ensure characters are evenly distributed when creating the password
list_per33 = ["1","2","3"]
list_per50 = ["1","2"]

per_33 = str("1")
per_50 = str("1")
# End Percentages #


# Random Password Generator # <-- Creates a password with the rules that user selected.

rules_use = (use_letter + use_digit + use_punct)
the_char = str()
chars = str()
def password_generator():
    global the_char, chars, gen_password
    the_char = str()
    chars = str()
    gen_password = str()
    match rules_use: # <- Looks every possible combination for password characters
        case "YNN":
            for i in range (0, pass_longness, 1):
                the_char = random.choice(list_ascii)
                chars = (chars + the_char)

        case "NYN":
            for i in range (0, pass_longness, 1):
                the_char = random.choice(list_digit)
                chars = (chars + the_char)

        case "NNY":
            for i in range (0, pass_longness, 1):
                the_char = random.choice(list_punct)
                chars = (chars + the_char)

        case "YYY":
            for i in range (0, pass_longness, 1):
                per_33 = str(random.choice(list_per33))
                match per_33:
                    case "1":
                        the_char = random.choice(list_ascii)
                        chars = (chars + the_char)
                    case "2":
                        the_char = random.choice(list_digit)
                        chars = (chars + the_char)
                    case "3":
                        the_char = random.choice(list_punct)
                        chars = (chars + the_char)

        case "YYN":
            for i in range (0, pass_longness, 1):
                per_50 = str(random.choice(list_per50))
                match per_50:
                    case "1":
                        the_char = random.choice(list_ascii)
                        chars = (chars + the_char)
                    case "2":
                        the_char = random.choice(list_digit)
                        chars = (chars + the_char)

        case "YNY":
            for i in range (0, pass_longness, 1):
                per_50 = str(random.choice(list_per50))
                match per_50:
                    case "1":
                        the_char = random.choice(list_ascii)
                        chars = (chars + the_char)
                    case "2":
                        the_char = random.choice(list_punct)
                        chars = (chars + the_char)

        case "NYY":
            for i in range (0, pass_longness, 1):
                per_50 = str(random.choice(list_per50))
                match per_50:
                    case "1":
                        the_char = random.choice(list_digit)
                        chars = (chars + the_char)
                    case "2":
                        the_char = random.choice(list_punct)
                        chars = (chars + the_char)
    gen_password = (chars) # <- Password that is generated
password_generator() # <-Starts the definition

if gen_password == (""):
    print("unkown error accured when password generating")
# End Random Password Generator #


# End Page #
print(),print(text_pass_end) # End page title

def gen_pass_end(): # Provides the user with the password and gives them the option to create a new password.
    global gen_again
    gen_again = ("N")
    print(),print()
    print(text_pass + gen_password)
    print()
    gen_again = str(input(text_gen_again))
    if gen_again in ("y","Y","e","E"): # Checks if the user wants a new password or not.
        password_generator() # Creates a new password with the same rules.
        gen_pass_end() # Gives the new password and asks to create new one again.
gen_pass_end() # <-Starts the definition

# End Page #
# Important Note! : This code is created for only experimantal purposes only, use it on your own risk #
# Önemli Not! : Bu kod sadece deneysel amaçlarla oluşturulmuştur, kullanımı kendi sorumluluğunuzdadır #