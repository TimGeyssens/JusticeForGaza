import os
import re

translations = {
    'en': {'label': 'No Human is Illegal', 'arms': 'arms-trade.html', 'target': 'no-human-illegal.html'},
    'nl': {'label': 'Niemand is Illegaal', 'arms': 'arms-trade-nl.html', 'target': 'no-human-illegal-nl.html'},
    'fr': {'label': "Personne n'est Illégal", 'arms': 'arms-trade-fr.html', 'target': 'no-human-illegal-fr.html'},
    'it': {'label': 'Nessun Umano è Illegale', 'arms': 'arms-trade-it.html', 'target': 'no-human-illegal-it.html'},
    'de': {'label': 'Kein Mensch ist illegal', 'arms': 'arms-trade-de.html', 'target': 'no-human-illegal-de.html'},
    'es': {'label': 'Nadie es Ilegal', 'arms': 'arms-trade-es.html', 'target': 'no-human-illegal-es.html'},
    'pt': {'label': 'Ninguém é Ilegal', 'arms': 'arms-trade-pt.html', 'target': 'no-human-illegal-pt.html'},
    'ar': {'label': 'لا يوجد إنسان غير قانوني', 'arms': 'arms-trade-ar.html', 'target': 'no-human-illegal-ar.html'},
    'zh': {'label': '没有人是非法的', 'arms': 'arms-trade-zh.html', 'target': 'no-human-illegal-zh.html'}
}

def update_nav(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine language from file name
    lang = 'en'
    for l in translations.keys():
        if f'-{l}.html' in file_path:
            lang = l
            break
    
    # Special case for index files like ar.html, zh.html, etc.
    if lang == 'en':
        match = re.search(r'([a-z]{2})\.html$', file_path)
        if match and match.group(1) in translations:
            lang = match.group(1)

    trans = translations[lang]
    new_link = f'<a href="{trans["target"]}">{trans["label"]}</a>'
    
    # Find the arms trade link to insert before it
    pattern = re.escape(f'<a href="{trans["arms"]}">')
    if new_link in content:
        return # Already added
    
    # We need to be careful with the active class
    # The prompt says place it before 'Arms Trade'
    
    updated_content = content.replace(f'<a href="{trans["arms"]}">', f'{new_link}\n                    <a href="{trans["arms"]}">')
    
    if updated_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True
    return False

files = [f for f in os.listdir('.') if f.endswith('.html')]
updated_count = 0
for file in files:
    if update_nav(file):
        updated_count += 1

print(f"Updated {updated_count} files.")
