import urllib2
def read_text():
    quotes = open(r"C:\Users\singh\Desktop\Pogramming foundations with python\Profanity Editor\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib2.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!!!!")
    elif "false" in output:
        print("okk!!!!")
    else:
        print("document needs to b scanned again!!!")

read_text()
