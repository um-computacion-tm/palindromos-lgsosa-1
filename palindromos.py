def is_palindrome(word):

    cleaned_word = ''.join(char for char in word if char.isalnum())     # isalnum es para verificar si es alfanumerico (no olvidar).

    return cleaned_word.lower() == cleaned_word[::-1].lower()

def obtener_cantidad_de_palabras_palindrome(word_list): 

#recordar que sinstance es para verificar si un objeto es de una clase dada-> formato isinstance(objeto,clase)

    if isinstance(word_list, str):     # Si es cadena, divido en palabras individuales
        words = word_list.split()
    elif isinstance(word_list, list):     # Si es una lista, directamentamente la uso
        words = word_list
    else:
        raise ValueError

    palindrome_words = [] 
    
    for word in words:
        if is_palindrome(word):
            palindrome_words.append(word)
    
    return len(palindrome_words)