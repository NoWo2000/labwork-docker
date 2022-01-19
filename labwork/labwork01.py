import collections

def handle_strcat(assignment):
    return " ".join(assignment["parts"])

def handle_histogram(assignment):
    return collections.Counter(assignment["text"])

def handle_caesar_cipher(assignment):
    action = assignment["action"]
    
    if action == "encrypt":
        letter_shift = assignment["letter_shift"] 
        text = assignment["plaintext"]  
        
    if action == "decrypt":
        letter_shift = -assignment["letter_shift"] 
        text = assignment["ciphertext"]
    
    result_string = ""
    for i in range(len(text)):
        character = text[i]
        
        if character.isupper():
            result_string += chr((ord(character) + letter_shift-65) % 26 + 65)
            
        elif character.islower():
            result_string += chr((ord(character) + letter_shift - 97) % 26 + 97)
        
        else:
            result_string += character
            
    return result_string
    