import os
import re

languages = {
    "en": {"bipolar_label": "Bipolar Excellence", "bipolar_file": "bipolar-excellence.html", "stanford_file": "stanford-experiment.html"},
    "nl": {"bipolar_label": "Bipolaire Excellentie", "bipolar_file": "bipolar-excellence-nl.html", "stanford_file": "stanford-experiment-nl.html"},
    "fr": {"bipolar_label": "Excellence Bipolaire", "bipolar_file": "bipolar-excellence-fr.html", "stanford_file": "stanford-experiment-fr.html"},
    "it": {"bipolar_label": "Eccellenza Bipolare", "bipolar_file": "bipolar-excellence-it.html", "stanford_file": "stanford-experiment-it.html"},
    "de": {"bipolar_label": "Bipolare Exzellenz", "bipolar_file": "bipolar-excellence-de.html", "stanford_file": "stanford-experiment-de.html"},
    "es": {"bipolar_label": "Excelencia Bipolar", "bipolar_file": "bipolar-excellence-es.html", "stanford_file": "stanford-experiment-es.html"},
    "pt": {"bipolar_label": "Excelência Bipolar", "bipolar_file": "bipolar-excellence-pt.html", "stanford_file": "stanford-experiment-pt.html"},
    "ar": {"bipolar_label": "التميز ثنائي القطب", "bipolar_file": "bipolar-excellence-ar.html", "stanford_file": "stanford-experiment-ar.html"},
    "zh": {"bipolar_label": "双相情感障碍的卓越", "bipolar_file": "bipolar-excellence-zh.html", "stanford_file": "stanford-experiment-zh.html"}
}

def get_lang(filename):
    if filename.endswith("-ar.html") or filename == "ar.html": return "ar"
    if filename.endswith("-zh.html") or filename == "zh.html": return "zh"
    if filename.endswith("-nl.html") or filename == "nl.html": return "nl"
    if filename.endswith("-fr.html") or filename == "fr.html": return "fr"
    if filename.endswith("-it.html") or filename == "it.html": return "it"
    if filename.endswith("-de.html") or filename == "de.html": return "de"
    if filename.endswith("-es.html") or filename == "es.html": return "es"
    if filename.endswith("-pt.html") or filename == "pt.html": return "pt"
    return "en"

count = 0
for filename in os.listdir("."):
    if not filename.endswith(".html"):
        continue
    
    # Skip the new files as they already have the link
    if "bipolar-excellence" in filename:
        continue

    lang = get_lang(filename)
    lang_info = languages[lang]
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    stanford_file = lang_info["stanford_file"]
    bipolar_file = lang_info["bipolar_file"]
    bipolar_label = lang_info["bipolar_label"]

    # We want to match the link in the navigation. 
    # Usually it looks like: <a href="stanford-experiment[-lang].html">...</a>
    # We'll look for it specifically inside the nav-links div or dropdown-content.
    # To be safe, we match the one that is NOT in <select> or <link> or <meta>.
    
    # We can use a regex that matches the <a> tag and check its context if possible, 
    # but a simpler way is to look for the one that is indented with spaces.
    
    pattern = rf'( {8,16}| {4,16})<a href="{stanford_file}"([^>]*)>(.*?)</a>'
    
    def replacement(match):
        indent = match.group(1)
        attrs = match.group(2)
        label = match.group(3)
        
        # If the file being edited IS the stanford-experiment file, 
        # the link might have class="active". 
        # We don't want to copy that class to the new link.
        
        return f'{indent}<a href="{stanford_file}"{attrs}>{label}</a>\n{indent}<a href="{bipolar_file}">{bipolar_label}</a>'

    if re.search(pattern, content):
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
        else:
            print(f"No change for {filename}")
    else:
        # Try a more relaxed pattern if the indented one fails
        pattern_relaxed = rf'<a href="{stanford_file}"([^>]*)>(.*?)</a>'
        # But only if it's NOT inside a <select> or <meta> or <link>
        # This is harder with regex alone, but let's try to match it if it's not followed by </option>
        
        def replacement_relaxed(match):
            attrs = match.group(1)
            label = match.group(2)
            # Check if it's followed by </option> - if so, skip
            # Actually, the <a> tag itself won't be inside <option>
            return f'<a href="{stanford_file}"{attrs}>{label}</a>\n                    <a href="{bipolar_file}">{bipolar_label}</a>'
            
        # We'll just stick to the indented one for now and see how many we get.
        print(f"Stanford link not found in {filename} (lang: {lang})")

print(f"Updated {count} files.")
