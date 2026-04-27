import os
import re

mappings = {
    'en': {'label': 'Philosophy', 'link': 'philosophy.html', 'group': 'The Human Lens'},
    'nl': {'label': 'Filosofie', 'link': 'philosophy-nl.html', 'group': 'De Menselijke Lens'},
    'fr': {'label': 'Philosophie', 'link': 'philosophy-fr.html', 'group': 'La Lentille Humaine'},
    'it': {'label': 'Filosofia', 'link': 'philosophy-it.html', 'group': 'La Lente Umana'},
    'de': {'label': 'Philosophie', 'link': 'philosophy-de.html', 'group': 'Die Menschliche Linse'},
    'es': {'label': 'Filosofía', 'link': 'philosophy-es.html', 'group': 'La Lente Humana'},
    'pt': {'label': 'Filosofia', 'link': 'philosophy-pt.html', 'group': 'A Lente Humana'},
    'ar': {'label': 'الفلسفة', 'link': 'philosophy-ar.html', 'group': 'المنظور الإنساني'},
    'zh': {'label': '哲学', 'link': 'philosophy-zh.html', 'group': '人类视角'}
}

def get_lang(filename):
    if filename.endswith('-nl.html') or filename == 'nl.html': return 'nl'
    if filename.endswith('-fr.html') or filename == 'fr.html': return 'fr'
    if filename.endswith('-it.html') or filename == 'it.html': return 'it'
    if filename.endswith('-de.html') or filename == 'de.html': return 'de'
    if filename.endswith('-es.html') or filename == 'es.html': return 'es'
    if filename.endswith('-pt.html') or filename == 'pt.html': return 'pt'
    if filename.endswith('-ar.html') or filename == 'ar.html': return 'ar'
    if filename.endswith('-zh.html') or filename == 'zh.html': return 'zh'
    return 'en'

directory = '/Users/u0174419/manifest'
files = [f for f in os.listdir(directory) if f.endswith('.html') and f != 'philosophy.html' and not f.startswith('philosophy-')]

for filename in files:
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lang = get_lang(filename)
    m = mappings[lang]
    
    if f'href="{m["link"]}"' in content:
        continue
        
    group_pattern = re.escape(m['group'])
    # Allow for optional classes on the nav-item div
    pattern = rf'(<div class="nav-item[^"]*">[^<]*{group_pattern}[^<]*</div>\s*<div class="dropdown-content">)'
    
    match = re.search(pattern, content)
    if match:
        start_pos = match.end()
        end_div_pos = content.find('</div>', start_pos)
        
        if end_div_pos != -1:
            # Check indentation of the previous line to match it
            # Actually, the files seem to have a consistent indentation.
            new_link = f'\n                    <a href="{m["link"]}">{m["label"]}</a>'
            new_content = content[:end_div_pos] + new_link + content[end_div_pos:]
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            # print(f"Updated {filename}")
        else:
            print(f"Could not find end of dropdown for {filename}")
    else:
        # Fallback: some files might have slightly different spacing or attributes
        print(f"Could not find Human Lens group for {filename} (lang: {lang})")
