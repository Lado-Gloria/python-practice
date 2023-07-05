# Write a Python function to calculate
#  the factorial of a given number.
def factorial(n):
    result=1
    for i in range(2, n+1):
        result *= i
    return result
print(factorial(10))    

# Write a Python program to check whether 
# a given string is a palindrome or not.
def ispalidrome(str):
    rev =''.join(reversed(str))
    if(str==rev):
      return True   
    else:
        return False
    
print(ispalidrome("malayalam"))
print(ispalidrome("gloria"))

# Write a Python program to find the sum 
# of all numbers in a list.



def summ(num):

    sum= 0

    for i in num:
     sum+= i

    return sum

print(summ([2,5,8,3,6]))

list=[1,2,3,4]

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_of_list([1,2,4,6]))

# Write a Python function to count
#  the number of vowels in a given string.
def countnnmber(num):
    count =0
    vo =('a','e','i','o','u')
    for x in num:
     if x in vo:
        count+=1
    return count
print(countnnmber("gloria"))  

# Write a Python program to find 
# the second largest number in a list.
def secondlargst(num):
    largest =float()
    secound=float()
    for nu in num:
     if nu >largest: 
      largest = nu
     elif nu >secound and nu !=largest:
        secound=nu
    return secound
print(secondlargst([1,5,8,5,10,34,23,]))
def larger(numbers):
   large = float()
   small =float()
   for number in numbers:
      if number > large:
         large =number
      elif number >small and number != large:
       small =number
   return small  
print(larger([2,6,9,8,4,7,6])) 

# Write a Python program to generate a 
# Fibonacci sequence of a given length.
def fibonacci(length):
    sequence = [0, 1]
    while len(sequence) < length:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence
print(fibonacci(10))

# Write a Python function to remove
#  duplicate elements from a given list.
def removedup(lst):

  return (set(lst))
lists = [2,3,2,6,3,2,5]

   
print(removedup(lists))    

# Write a Python program to read a text
#  file and count the frequency of each word.
# from collections import Counter
# def count_words(filename):
#     with open(filename, 'r') as file:
#         words = file.read().split()
#         word_count = Counter(words)
#         return word_count
# filename = input("Hello Hello my wold good morning")
# word_count = count_words(filename)
# print(word_count)

def count_word(str):
    counts =dict()
    words =str.split()
    for word in words:
       if word in counts:
          counts[word]+=1
       else: counts[word]=1
    return counts
print(count_word("hello hello my beautiful world"))
      

def dat(wrd):
   counting=dict()
   data =wrd.split()
   for x in data:
      if x in counting:
         counting[x]+=1
      else:counting[x]=1
      return counting
print(dat("hello hello gloria,hello gloria my beautiful gloria")) 

# Write a Python function to check 
# whether a given number is prime or not.
num =13

def isprime(num):
   num<=1
   print("num is not a prime")
for n in range(2,num):
     if num%n==0:
      print( "num is not a prime ")
      break
     else:
        print("num is prime")
    #  print(isprime(13))




class Feedback:
    def __init__(self,customer,message):
        self.customer = customer
        self.message = message

    def display(self):
         return f"Hello {self.message}"
        
    def get_customer(self):
       return self.customer

    def get_message(self):
      return self.message


class Book:
   def __init__(self, tittle,author,publicationYear):
      self.tittle=tittle
      self.author=author
      self.publicationYear=publicationYear
   
   def reading(self) :
      return f"iam reading {self.tittle} by {self.author} produce in {self.publicationYear}" 
class Novel(Book):
      def __init__(self, tittle,author,publicationYear,genre):
         super().__int__(tittle,author,publicationYear)
         self.genre=genre
      def readig(self):
            return f"iam reading {self.tittle} by {self.author} produce in {self.publicationYear} with a unque {self.genre}"
         
class Textbook(Book):
       def __init__(self, tittle, author, publicationYear,subject):
          super().__init__(tittle, author, publicationYear) 
          self.subject=subject
       def readg(self):
            return f"iam reading {self.tittle} by {self.author} produce in {self.publicationYear} with a unque {self.subject}" 


class Magagine(Book):
   def __init__(self, tittle, author, publicationYear,issuenumber):
      super().__init__(tittle, author, publicationYear)
      self.issuenumber=issuenumber
   def readng(self):
            return f"iam reading {self.tittle} by {self.author} produce in {self.publicationYear} with a unque {self.issuenumber}" 


books =Book("Pride of predices","Charles","2023")
print(books.reading())
lat =Novel("beautiful queen","Lado","2021","lovely")
print(lat.readig())
obj2 =Textbook("Born a crime","Noah travor","1984","story")
print(obj2.readg())
obj3 =Magagine("Child in the forest","Gloria","2000","20")
print(obj3.readng())
      
   

