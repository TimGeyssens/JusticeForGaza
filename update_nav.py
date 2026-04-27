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
    if "-" not in filename and filename.endswith(".html"):
        # Special case for files like history.html which are English
        return "en"
    return "en"

files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in files:
    # Skip the symptom-trap files we just generated as they should be correct already
    # but let's check symptom-trap.html itself which existed before
    
    lang = get_lang(filename)
    label = languages[lang]
    link = f"symptom-trap-{lang}.html" if lang != "en" else "symptom-trap.html"
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Check if link already exists
    if f'href="{link}"' in content or f"href='{link}'" in content:
        print(f"Skipping {filename}, link already exists.")
        continue

    # Pattern to find the The Crisis dropdown content
    # We want to insert it after Social Mobility
    
    # Search for Social Mobility link to insert after it
    # We need to find the localized version of Social Mobility link
    
    social_mobility_links = {
        "en": "social-mobility.html",
        "nl": "social-mobility-nl.html",
        "fr": "social-mobility-fr.html",
        "it": "social-mobility-it.html",
        "de": "social-mobility-de.html",
        "es": "social-mobility-es.html",
        "pt": "social-mobility-pt.html",
        "ar": "social-mobility-ar.html",
        "zh": "social-mobility-zh.html"
    }
    
    sm_link = social_mobility_links[lang]
    
    # Try to find the link tag for social mobility
    pattern = re.compile(f'(<a href="{sm_link}">.*?</a>)')
    if not pattern.search(content):
        # Try with single quotes
        pattern = re.compile(f"(<a href='{sm_link}'>.*?</a>)")
    
    if pattern.search(content):
        new_link = f'\n                    <a href="{link}">{label}</a>'
        new_content = pattern.sub(r'\1' + new_link, content)
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Could not find social mobility link in {filename}")

