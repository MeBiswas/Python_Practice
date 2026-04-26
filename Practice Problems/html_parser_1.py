"""
.handle_comment(data)
This method is called when a comment is encountered (e.g. <!--comment-->).
The data argument is the content inside the comment tag:
`from html.parser import HTMLParserr

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Comment  :", data)`

.handle_data(data)
This method is called to process arbitrary data (e.g. text nodes and the content of <script>...</script> and <style>...</style>).
The data argument is the text content of HTML.
`from html.parser import HTMLParserr

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print("Data     :", data)`
        
Task

You are given an HTML code snippet of  lines.
Your task is to print the single-line comments, multi-line comments and the data.

Print the result in the following format:
`
>>> Single-line Comment  
Comment
>>> Data                 
My Data
>>> Multi-line Comment  
Comment_multiline[0]
Comment_multiline[1]
>>> Data
My Data
>>> Single-line Comment:  
`
Note: Do not print data if data == '\n'.
"""
from html.parser import HTMLParser

N = int(input())
code_snippet = ""

for i in range(N):
    code_snippet += input().rstrip() + '\n'

class MyHTMLParser(HTMLParser):
    
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
    
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)

parser = MyHTMLParser()
parser.feed(code_snippet)
parser.close()