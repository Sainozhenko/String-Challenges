# 🧩 Python String Manipulation Challenges — HTML Builder

5 Python challenges to build and modify a minimal HTML page using string methods
and concatenation only. No parsers, no libraries — pure string primitives.

## Rules
- Only string methods (`.replace, .find, .rfind, .split, .index, .count, etc.`) are allowed
- String concatenation with + and += is allowed
- f-strings may be used to build values before insertion
- Converting the string to a list to index elements is NOT allowed
- No imports or external libraries of any kind

## Challenges

| # | Challenge | Branch | Status |
|---|-----------|--------|--------|
| 1 | Update Page Metadata | `challenge/01-metadata` | ✅ Done |
| 2 | Update Stylesheet and Script Sources | `challenge/02-assets` | ✅ Done |
| 3 | Inject Heading Tags | `challenge/03-headings` | ✅ Done |
| 4 | Add Paragraph and Image Tags | `challenge/04-content` | ✅ Done |
| 5 | Full Page Builder | `challenge/05-full-page` | ✅ Done |


## Outputs

### Challenge 1 — Update Page Metadata

**Concepts:** `.replace()`, f-strings, string concatenation

**Solution file:** `challenge_01_metadata.py`

**HTML output file:** `html_outputs/challenge_01_output.html`

**Terminal output:**

![Challenge 1 Terminal](screenshots/task_1.png)

**Browser preview:** Open `html_outputs/challenge_01_output.html` in a browser to verify
the updated `lang` attribute and `<title>` tag render correctly.



### Challenge 2 — Update Stylesheet and Script Sources

**Concepts:** `.find()`, `.index()`, string slicing with computed positions, concatenation

**Solution file:** `challenge_02_stylesheets_and_scripts.py`

**HTML output file:** `html_outputs/challenge_02_output.html`

**Terminal output:**

![Challenge 2 Terminal](screenshots/task_2.png)

**Browser preview:** Open `html_outputs/challenge_02_output.html` in a browser to verify
the updated `src` and `href`



### Challenge 3 — Inject Heading Tags

**Concepts:** `.find()`, `.split()` on a specific separator, string concatenation, multi-line string building

**Solution file:** `challenge_03_headings.py`

**HTML output file:** `html_outputs/challenge_03_output.html`

**Terminal output:**

![Challenge 3 Terminal](screenshots/task_3.png)

**Browser preview:** Open `html_outputs/challenge_03_output.html` in a browser to verify
the updated `html`.



### Challenge 4 — Add Paragraph and Image Tags

**Concepts:**  `.find()`, `.rfind()`, multi-step string reconstruction, f-strings, `\n`and indentation management

**Solution file:** `challenge_04_content.py`

**HTML output file:** `html_outputs/challenge_04_output.html`

**Terminal output:**

![Challenge 4 Terminal](screenshots/task_4.png)

**Browser preview:** Open `html_outputs/challenge_04_output.html` in a browser to verify
the updated `html`



### Challenge 5 — Full Page Builder

**Concepts:**  All previous methods combined, multi-step transformation pipeline, string validation

**Solution file:** `challenge_05_full_page.py`

**HTML output file:** `html_outputs/challenge_05_output.html`

**Terminal output:**

![Challenge 5 Terminal](screenshots/task_5.png)

**Browser preview:** Open `html_outputs/challenge_05_output.html` in a browser to verify
the updated `html`