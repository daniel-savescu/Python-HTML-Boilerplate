import codecs
import webbrowser

fileObject = open('index.html', 'w')

html_boilerplate_template = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

  </body>
</html>
"""


fileObject.write(html_boilerplate_template)

fileObject.close()

file = codecs.open("index.html", 'r', "utf-8")

print(file.read())
webbrowser.open("index.html")
