for item in range(1,101):
    what_we_say = ''
    
    if item % 3 == 0:
        what_we_say = "Fizz"
    
    if item % 5 == 0:
        if what_we_say:
            what_we_say += ' '
        what_we_say += "Buzz"
    
    if len(what_we_say) == 0:
        what_we_say = str(item)
    
    printend = '\n' if item == 100 else ', '
    
    print(what_we_say, end=printend)