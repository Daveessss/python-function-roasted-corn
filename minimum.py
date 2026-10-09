def length_of_string(word):
    return len(word)

print("The length of the word is: ", length_of_string("david"))


def character(word):
    if len(word) < 2:
        return ' '
    return word[:2] + word[-2:]

# no 3
def add at the end(word):
    if word[-3] == "ing":
       return word + "ly"
    elif len(word) >= 3:
        return word + "ing"
    elif len(word) < 3:
        return word
print (add_at_the_end("On"))

#   no 4

def longest_word(words):
    longest = " "
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest, len(longest)




def minimum_numbers(numbers):
    smallest = numbers[0]
    for the_number in numbers:
        if the_number < smallest:
            smallest = the_number
    return smallest

print("The minimum number is: " , minimum_numbers([2,5,8,9,4]))
                
def maximum_numbers(numbers):
    largest = numbers[0]
    for the_number in numbers:
        if the_number > largest:
            largest = the_number
    return largest

print("The maximum number is: " , maximum_numbers([2,5,8,9,4]))
    
    
def repeated(word, number):
    if type(number) == float:
        return word
      
    result = ""
    for index in range(number):
        result += word
    return result
print(repeated("david", 3))

def square(numbers):
    result = []
    for the_numbers in numbers:
        result.append(the_numbers * the_numbers)
    return result

def sum_of_square(numbers):
    total = 0
    for the_numbers in numbers:
        total += (the_numbers * the_numbers)
    return total
