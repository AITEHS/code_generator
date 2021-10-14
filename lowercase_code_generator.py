###TODO add uppercase compatibility
import random

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"," "]

change_number_random = random.randint(1,len(alphabet)-1)###substract 1 to avoid full circle


while True:###Delete after finishing
    mode = input("Choose mode:")
    text = input("Input text:")
    change_number = int(input("input number of change:"))

    def split(word):
        return [char for char in text]###dividing input text into individual chatacters

    def check_compatability(list):
       return set(list).issubset(alphabet)#detecting if every char of divided list is in alphabet

    def coding(message,change_number = change_number_random):
        coded_message = ""
        for i in range(len(message)):
            index_num = (alphabet.index(message[i])+change_number)%len(alphabet)##(x+n) mod N
            coded_message+= alphabet[index_num] 
        return(coded_message)
    
    
    def decoding(message,change_number):
        decoded_message = ""
        for i in range(len(message)):
            index_num = (alphabet.index(message[i])-change_number)%len(alphabet)##(x-n) mod N
            decoded_message+= alphabet[index_num] 
        return(decoded_message)

    if check_compatability(split(text)) and mode == "encoding":
        print(coding(split(text),change_number))
    elif check_compatability(split(text)) and mode == "decoding":
        print(decoding(split(text),change_number))
    else:
        print("non-existent mode or mismatch of the text with the alphabet")
