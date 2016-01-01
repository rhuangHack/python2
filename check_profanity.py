import urllib

def read_text():
    quotes = open("/home/renda/Documents/Python/python2/Readme.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    profanity_check(content)

def profanity_check(text):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This Document has no curse words!")
    else:
        print("Could not scan the document properly.")

read_text()
