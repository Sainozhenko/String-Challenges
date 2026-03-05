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
</body>
</html>"""

page_title = "Full Page Challenge"
page_lang = "es"
html = html.replace("My Page", page_title)
html = html.replace('lang="en"', f'lang="{page_lang}"')

stylesheet = "app.min.css"
script_file = "main.bundle.js"

pos_css = html.find("styles.css")
html = html[:pos_css] + stylesheet + html[pos_css + len("styles.css"):]

pos_js = html.find("app.js")
html = html[:pos_js] + script_file + html[pos_js + len("app.js"):]

errors = []
if html.count("styles.css") != 0:
    errors.append("styles.css not replaced")
if html.count("app.js") != 0:
    errors.append("app.js not replaced")
if errors:
    for e in errors:
        print("Error:", e)
else:
    print("")

    h1 = "Welcome to the Full Page"
    h2 = "About the Project"
    h3 = "Technical Details"

body_content = f"    <h1>{h1}</h1>\n    <h2>{h2}</h2>\n    <h3>{h3}</h3>\n"

parts = html.split("<body>", 1)
html = parts[0] + "<body>\n" + body_content + parts[1]

paragraph_text = "This project was built entirely using Python string methods."
img_src = "hero.jpg"
img_alt = "A hero image for the page"

p_tag = f"    <p>{paragraph_text}</p>\n"
img_tag = f'    <img src="{img_src}" alt="{img_alt}">\n'

h1_pos = html.rfind("</h1>")
h2_pos = html.rfind("</h2>")
h3_pos = html.rfind("</h3>")

last_heading = max(h1_pos, h2_pos, h3_pos)
insert_pos = last_heading + len("</h3>")

html = html[:insert_pos] + p_tag + img_tag + html[insert_pos:]

title_start = html.find("<title>") + len("<title>")
title_end = html.find("</title>")
title_text = html[title_start:title_end]

second_p = f"    <p>This page is titled: {title_text}</p>\n"

body_close = html.find("</body>")
html = html[:body_close] + second_p + html[body_close:]

print("--- Validation Report ---")
print("✅ <title> is correct" if html.count(f"<title>{page_title}</title>") else "❌ <title> is correct")
print("✅ <h1> found" if html.count("<h1>") else "❌ <h1> found")
print("✅ <h2> found" if html.count("<h2>") else "❌ <h2> found")
print("✅ <h3> found" if html.count("<h3>") else "❌ <h3> found")
print("✅ <img> appears exactly once" if html.count("<img") == 1 else "❌ <img> appears exactly once")
print("✅ <p> appears exactly twice" if html.count("<p>") == 2 else f"❌ <p> appears exactly twice ({html.count('<p>')})")
print("✅ Starts with <!DOCTYPE html>" if html.startswith("<!DOCTYPE html>") else "❌ Starts with <!DOCTYPE html>")
print("✅ Ends with </html>" if html.strip().endswith("</html>") else "❌ Ends with </html>")
print("-------------------------")