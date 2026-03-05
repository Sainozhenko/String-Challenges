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

stylesheet= "main.min.css"
script_file="bundle.js"

pos = html.find("styles.css")
html = html[:pos] + stylesheet + html[pos + len("styles.css"):]

pos1 = html.index("app.js")
html = html[:pos1] + script_file + html[pos1 + len("app.js"):]

print(html)