# Analyze_text function
def analyze_text(text):
    # Print stats header
    print("--Stats--")
    
    # Print character count
    print("\tChar Count:\t", len(text))
    
    # Get the number of words and print
    words = text.split()
    print("\tWord Count:\t", len(words))
    
    # Print the calculated average word length
    print("\tAverage Word Length:\t", len(text) / len(words))
    
    # Print transformations header
    print("--Transformations--")
    
    # Print lower case
    print("\tLower Case:\t", text.lower())
    
    # Print upper case
    print("\tUpper Case:\t", text.upper())
    
    # Print title case
    print("\tTitle Case:\t", text.title())
    
    # Print Reversed
    print("\tReversed:\t", reverse(user_input))
    
    # Print Word Reversed
    print("\tWords Reversed:\t", reverse(words, " "))
    
    # Print Mock Case
    print("\tMock Case:\t", mock(user_input))

# Reverse function
def reverse(text, seperator = ""):
    # Set result string to an empty string
    result = ""

    for i in range(1, len(text) + 1):
        result += text[-i] + seperator
        
    return result
    
# Mock function
def mock(text):
    # Set result string to an empty string
    result = ""
    
    for i in range(0, len(text)):
        remainder = i % 2
        
        if remainder == 0:
            result += text[i].lower()
        else:
            result += text[i].upper()
            
    return result

# Set keep_going to true
keep_going = True

# While keep_going is true, get user input and analyze
while keep_going:
    user_input = input("Enter a sentence:\n>")
    
    # If user input is empty, they want to quit
    if user_input == "":
        keep_going = False
        
    # Otherwise, do the analysis
    else:
        analyze_text(user_input)
    