import random

abc123 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"," "]

x = random.randint(1,len(abc123)-1)


while True:
    text = input("Input text:")

    def split(word):
        return [char for char in text]

    def check_compatability(list):
       return set(list).issubset(abc123)

    def coding(message):
        coded_message = []
        for i in range(len(message)):
            index_num = abc123.index(message[i])+x
            print (index_num)
            if index_num< len(abc123)-1:
                coded_message.append(abc123[index_num])
            else:
                coded_message.append(abc123[index_num-len(abc123)-1])
            print(coded_message)

    if check_compatability(split(text)):
        coding(split(text))
    
    else:
        print("no")
