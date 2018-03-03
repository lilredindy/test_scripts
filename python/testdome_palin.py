class Palindrome:

    @staticmethod
    def is_palindrome(word):
        
        for index in range(len(word) //2):
            print (word[index].lower(), word[len(word)-1-index].lower())
            if (word[index].lower() != word[len(word)-1-index].lower()):
                return False
        return True
            
       
          
print(Palindrome.is_palindrome('Deleveled'))