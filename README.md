## Language Translator

A desktop language translation application built with **PyQt5** and **Google Translate**.
---

## Features

- Translate text between dozens of languages using Google Translate
- Select source and target languages from dropdown menus
- Swap languages and text with a single **Reverse** button
- **Reset** button to clear all inputs instantly
- Lightweight desktop GUI — no browser needed

---

## Screenshot

(Translator.jpg)

---

## Project Structure

```
.
├── main.py          # Main application file (Home widget + entry point)
├── language.py      # Language list/dictionary (LANGUAGES, values)
└── README.md
```

---

## Running the App

```bash
python main.py
```

---

## How to Use

1. Select the **source language** from the first dropdown.
2. Select the **target language** from the second dropdown.
3. Type or paste text into the **top text box**.
4. Click **Translate Now!** — the translation appears in the bottom text box.
5. Click **Reverse** to swap both languages and both texts.
6. Click **Reset** to clear all text fields.

---
