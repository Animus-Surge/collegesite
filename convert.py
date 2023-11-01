#!/usr/bin/env python3
# A script to turn a markdown file into an HTML page. CSS is located in main.css, the title should be whatever the first header is.
# Each page is made using the contents of template.html, the field {{content}} is replaced with the contents of the markdown file
# rendered as HTML. The field {{title}} is replaced with the title of the page. css is included in the template, same with javascript.
# The script must search through the /public directory for markdown files, and then create a new HTML file for each markdown file in the
# same directory.

import os
import markdown

# Get the current working directory
cwd = os.getcwd()

# Get the path to the public directory
public = os.path.join(cwd, "public")

# Get the path to the template file
template = os.path.join(cwd, "template.html")

# Now search public for all markdown files
for root, dirs, files in os.walk(public):
    for file in files:
        # If the file is a markdown file
        if file.endswith(".md"):
            # Get the path to the markdown file
            md = os.path.join(root, file)

            # Get the path to the new HTML file
            html = md.replace(".md", ".html")

            # Open the markdown file
            with open(md, "r") as f:
                # Read the contents of the markdown file
                contents = f.read()

                # Convert the markdown to HTML
                html_contents = markdown.markdown(contents)

                # Open the template file
                with open(template, "r") as t:
                    # Read the contents of the template file
                    template_contents = t.read()

                    # Replace the {{content}} field with the HTML contents
                    template_contents = template_contents.replace("{{content}}", html_contents)

                    # Replace the {{title}} field with the title of the page
                    template_contents = template_contents.replace("{{title}}", html_contents.split("<h1>")[1].split("</h1>")[0])

                    # Open the new HTML file
                    with open(html, "w") as h:
                        # Write the contents of the template file to the new HTML file
                        h.write(template_contents)