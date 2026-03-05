html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
    <h1>Welcome to My Page</h1>
    <h2>About This Project</h2>
    <h3>Technical Details</h3>
</body>
</html>"""

paragraph_text="This project was built entirely using Python string methods."
img_src="hero.jpg"
img_alt="A hero image for the page"

p_tag = f"    <p>{paragraph_text}</p>\n"
img_tag = f'    <img src="{img_src}" alt="{img_alt}">\n'

h1_pos = html.rfind("</h1>")
h2_pos = html.rfind("</h2>")
h3_pos = html.rfind("</h3>")

last_heading = max(h1_pos, h2_pos, h3_pos)

if last_heading == -1:
    insert_pos = html.find("<body>") + len("<body>")
else:
    insert_pos = last_heading + len("</h3>")

html = html[:insert_pos] + "\n" + p_tag + img_tag + html[insert_pos:]

print(html)