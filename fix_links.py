import os
import re

translations = {
    'en': {'target': 'no-human-illegal.html', 'terms': ['No Human is Illegal', 'Migration', 'Borders']},
    'nl': {'target': 'no-human-illegal-nl.html', 'terms': ['Niemand is Illegaal', 'Migratie', 'Grenzen']},
    'fr': {'target': 'no-human-illegal-fr.html', 'terms': ["Personne n'est Illégal", 'Migration', 'Frontières']},
    'it': {'target': 'no-human-illegal-it.html', 'terms': ['Nessun Umano è Illegale', 'Migrazione', 'Confini']},
    'de': {'target': 'no-human-illegal-de.html', 'terms': ['Kein Mensch ist illegal', 'Migration', 'Grenzen']},
    'es': {'target': 'no-human-illegal-es.html', 'terms': ['Nadie es Ilegal', 'Migración', 'Fronteras']},
    'pt': {'target': 'no-human-illegal-pt.html', 'terms': ['Ninguém é Ilegal', 'Migração', 'Fronteiras']},
    'ar': {'target': 'no-human-illegal-ar.html', 'terms': ['لا يوجد إنسان غير قانوني', 'الهجرة', 'الحدود']},
    'zh': {'target': 'no-human-illegal-zh.html', 'terms': ['没有人是非法的', '移民', '边界']}
}

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lang = 'en'
    for l in translations.keys():
        if f'-{l}.html' in file_path:
            lang = l
            break
    if lang == 'en':
        match = re.search(r'([a-z]{2})\.html$', file_path)
        if match and match.group(1) in translations:
            lang = match.group(1)

    trans = translations[lang]
    target = trans['target']

    # 1. Fix duplicate nav
    # Find all occurrences of links to no-human-illegal.html in the nav
    nav_pattern = r'<a href="no-human-illegal[^"]*">[^<]+</a>'
    
    # We want to keep only the one that is correct.
    # Actually, a simpler way to fix the duplicate added by update_nav.py:
    # It added it right before arms-trade.
    arms_file = f'arms-trade{"-" + lang if lang != "en" else ""}.html'
    
    # Match the specific duplicate added: 
    # <a href="no-human-illegal...html">...</a>\n                    <a href="arms-trade...html">
    duplicate_pattern = re.escape(f'<a href="{target}">{translations[lang]["terms"][0]}</a>') + r'\n\s+<a href="no-human-illegal'
    # Wait, that's not quite right.
    
    # Let's just find the nav block and remove duplicates of the same target
    nav_match = re.search(r'<div class="dropdown-content">.*?</div>', content, re.DOTALL)
    if nav_match:
        nav_content = nav_match.group(0)
        # Find all links in this nav_content
        links = re.findall(r'<a [^>]+>.*?</a>', nav_content)
        seen_targets = set()
        new_links = []
        changed_nav = False
        for link in links:
            t_match = re.search(r'href="([^"]+)"', link)
            if t_match:
                t = t_match.group(1)
                if t == target:
                    if t in seen_targets:
                        changed_nav = True
                        continue # Skip duplicate
                    seen_targets.add(t)
            new_links.append(link)
        
        if changed_nav:
            # Reconstruct nav_content
            # This is tricky because of whitespace.
            # Let's try a simpler replacement: if we have two links to the same target, remove the one without class="active" if the other has it, or just remove the first one.
            pass # We'll do a better one below

    # Improved duplicate removal:
    # If we find <a href="target">label</a> followed by <a href="target" class="active">label</a> or vice versa
    pattern1 = re.escape(f'<a href="{target}">{translations[lang]["terms"][0]}</a>') + r'\s+<a href="' + re.escape(target) + r'" class="active">'
    content = re.sub(pattern1, f'<a href="{target}" class="active">', content)
    
    pattern2 = re.escape(f'<a href="{target}" class="active">{translations[lang]["terms"][0]}</a>') + r'\s+<a href="' + re.escape(target) + r'">'
    content = re.sub(pattern2, f'<a href="{target}" class="active">', content)

    # 2. Internal linking
    # We only want to link terms in the <main> section to avoid breaking nav/headers
    main_match = re.search(r'<main>.*?</main>', content, re.DOTALL)
    if main_match:
        main_content = main_match.group(0)
        original_main = main_content
        for term in trans['terms']:
            # Use regex to find term but NOT if it's already inside an <a> tag or is a tag itself
            # Negative lookahead/lookbehind is hard in Python for tags.
            # Simpler: replace term with link if it's not preceded by href=" or >
            
            # We also don't want to link the term if it's in a header (h1, h2, h3)
            # Actually, the user said "where appropriate".
            
            # regex for term not already in <a>
            # We'll use a placeholder for existing links to protect them
            existing_links = re.findall(r'<a [^>]+>.*?</a>', main_content)
            for i, link in enumerate(existing_links):
                main_content = main_content.replace(link, f'__LINK_{i}__')
            
            # Now replace the term
            # Word boundary check
            # For non-latin characters (ar, zh), \b might not work as expected.
            if lang in ['ar', 'zh']:
                # For ar/zh, just replace it if it's not in a link placeholder
                main_content = main_content.replace(term, f'<a href="{target}">{term}</a>')
            else:
                pattern = r'\b' + re.escape(term) + r'\b'
                main_content = re.sub(pattern, f'<a href="{target}">{term}</a>', main_content)
            
            # Restore links
            for i, link in enumerate(existing_links):
                main_content = main_content.replace(f'__LINK_{i}__', link)
                
        # Avoid double linking if target is already linked
        # If we have <a href="target"><a href="target">term</a></a>, fix it.
        # But our placeholder should have prevented that.
        
        content = content.replace(original_main, main_content)

    return content

files = [f for f in os.listdir('.') if f.endswith('.html')]
for file in files:
    new_content = fix_file(file)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Fixed duplicates and added internal links.")
