import os
import re

languages = {
    "nl": {"label": "De Symptoomval", "crisis": "De Crisis"},
    "fr": {"label": "Le Piège des Symptômes", "crisis": "La Crise"},
    "it": {"label": "La Trappola dei Sintomi", "crisis": "La Crisi"},
    "de": {"label": "Die Symptomfalle", "crisis": "Die Krise"},
    "es": {"label": "La Trampa de los Síntomas", "crisis": "La Crisis"},
    "pt": {"label": "A Armadilha dos Sintomas", "crisis": "A Crise"},
    "ar": {"label": "فخ الأعراض", "crisis": "الأزمة"},
    "zh": {"label": "症状陷阱", "crisis": "危机"},
    "en": {"label": "Symptom Trap", "crisis": "The Crisis"}
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
    label = languages[lang]["label"]
    crisis_label = languages[lang]["crisis"]
    link = f"symptom-trap-{lang}.html" if lang != "en" else "symptom-trap.html"
    
    with open(filename, 'r') as f:
        content = f.read()
    
    if f'href="{link}"' in content or f"href='{link}'" in content:
        # print(f"Skipping {filename}, already has link")
        continue

    # Find the "The Crisis" dropdown
    # It looks like:
    # <div class="nav-dropdown">
    #     <div class="nav-item">The Crisis</div>
    #     <div class="dropdown-content">
    #         ...
    #     </div>
    # </div>
    
    # We use a regex to find this block
    # Note: nav-item might have 'active' class
    pattern = re.compile(
        rf'(<div class="nav-item[^"]*">\s*{re.escape(crisis_label)}\s*</div>\s*<div class="dropdown-content">)',
        re.DOTALL
    )
    
    if pattern.search(content):
        # Insert after the dropdown-content opening tag
        # To maintain alphabetical or group order, maybe insert before Genocide Convention or after Social Mobility
        # But for simplicity, let's just insert it after the opening tag of dropdown-content
        new_link = f'\n                    <a href="{link}">{label}</a>'
        new_content = pattern.sub(r'\1' + new_link, content)
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        # Try a more broad search if the specific label match fails
        # Maybe search for any nav-dropdown and look for a known link inside it
        print(f"FAILED to find Crisis dropdown in {filename}")

