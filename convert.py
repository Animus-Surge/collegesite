#!/usr/bin/env python3
# A script to turn a markdown file into an HTML page. CSS is located in main.css, the title should be whatever the first header is.
# Each page is made using the contents of template.html, the field {{content}} is replaced with the contents of the markdown file
# rendered as HTML. The field {{title}} is replaced with the title of the page.

import markdown
import sys


# Check if the user has provided a file to convert
if len(sys.argv) < 2:
    print("Usage: ./md2html.py <markdown file>")
    exit()

print("Converting " + sys.argv[1] + " to HTML")

# Read the markdown file
with open(sys.argv[1], "r") as f:
    md = f.read()

# Convert the markdown to HTML
html = markdown.markdown(md)

# Read the template file
with open("template.html", "r") as f:
    template = f.read()

# Replace the fields in the template with the HTML and title
template = template.replace("{{content}}", html)
template = template.replace("{{title}}", md.split("\n")[0][2:])

# Write the HTML to a file
with open(sys.argv[1].replace(".md", ".html"), "w") as f:
    f.write(template)

print("Done!")
