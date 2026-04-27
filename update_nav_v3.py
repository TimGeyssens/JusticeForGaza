import os
import re

languages = {
    "nl": "De Symptoomval",
    "fr": "Le Piège des Symptômes",
    "it": "La Trappola dei Sintomi",
    "de": "Die Symptomfalle",
    "es": "La Trampa de los Síntomas",
    "pt": "A Armadilha dos Sintomas",
    "ar": "فخ الأعراض",
    "zh": "症状陷阱",
    "en": "Symptom Trap"
}

def get_lang(filename):
    if filename == "index.html":
        return "en"
    for lang in languages.keys():
        if filename.endswith(f"-{lang}.html"):
            return lang
    return "en"

files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in files:
    lang = get_lang(filename)
    label = languages[lang]
    link = f"symptom-trap-{lang}.html" if lang != "en" else "symptom-trap.html"
    
    with open(filename, 'r') as f:
        content = f.read()
    
    if f'href="{link}"' in content or f"href='{link}'" in content:
        continue

    # Find the dropdown-content that contains history-link
    history_link = "history.html" if lang == "en" else f"history-{lang}.html"
    
    # Regex to find the dropdown-content div that contains the history link
    # We want to insert it right after <div class="dropdown-content">
    pattern = re.compile(r'(<div class="dropdown-content">)(?=[^<]*<a href="' + re.escape(history_link) + r'")', re.DOTALL)
    
    if not pattern.search(content):
        # Try with single quotes
        pattern = re.compile(r"(<div class=\"dropdown-content\">)(?=[^<]*<a href='" + re.escape(history_link) + r"')", re.DOTALL)

    if pattern.search(content):
        new_link = f'\n                    <a href="{link}">{label}</a>'
        new_content = pattern.sub(r'\1' + new_link, content)
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        # Fallback for main language files where maybe history link is different?
        # In nl.html it is history-nl.html.
        print(f"FAILED to find Crisis dropdown in {filename} using history link {history_link}")

