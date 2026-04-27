
import os
import re

base_dir = "/Users/u0174419/manifest"
languages = ["en", "nl", "fr", "it", "de", "es", "pt", "ar", "zh"]

# Mapping from base filename to localized labels
labels = {}

topics = [
    "index.html", "history.html", "genocide-convention.html", "democracy-illusion.html",
    "money-evolution.html", "tax-avoidance.html", "wealth-gap.html", "social-mobility.html",
    "arms-trade.html", "climate-justice.html", "water-apartheid.html", "waste-crisis.html",
    "food-sovereignty.html", "modern-slavery.html", "medical-apartheid.html", "prison-industrial.html",
    "symptom-trap.html", "neurodiversity.html", "survival-mode.html", "the-mindset.html",
    "education-factory.html", "board-games.html", "mental-health.html", "philosophy.html",
    "human-nature.html", "hero-myth.html", "propaganda.html", "tech-surveillance.html",
    "divide-conquer.html", "bullshit-jobs.html", "love-revenge.html", "take-action.html",
    "radical-community.html", "glossary.html", "references.html", "further-reading.html",
    "republish.html"
]

for topic in topics:
    labels[topic] = {}
    for lang in languages:
        if lang == "en":
            filename = topic
        elif topic == "index.html":
            filename = f"{lang}.html"
        else:
            filename = topic.replace(".html", f"-{lang}.html")
        
        file_path = os.path.join(base_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Find the label in the navigation: <a href="filename">Label</a>
                match = re.search(f'href="{filename}"[^>]*>([^<]+)</a>', content)
                if match:
                    labels[topic][lang] = match.group(1).strip()
                else:
                    # Try finding it in another file of the same language
                    pass
        else:
            # print(f"File not found: {file_path}")
            pass

# Manual fixes and additions
love_revenge_labels = {
    "en": "Love as Revenge",
    "nl": "Liefde als Wraak",
    "fr": "L'Amour comme Vengeance",
    "it": "L'Amore come Vendetta",
    "de": "Liebe als Rache",
    "es": "El Amor como Venganza",
    "pt": "O Amor como Vingança",
    "ar": "الحب كأنتقام",
    "zh": "爱作为报复"
}
labels["love-revenge.html"] = love_revenge_labels

# Fallback for missing labels using common sense or other files
for topic in topics:
    for lang in languages:
        if lang not in labels[topic] or not labels[topic][lang]:
            # Try to find the label for this topic in index.html of that language
            if lang == "en":
                idx_file = "index.html"
            else:
                idx_file = f"{lang}.html"
            
            idx_path = os.path.join(base_dir, idx_file)
            if os.path.exists(idx_path):
                with open(idx_path, "r", encoding="utf-8") as f:
                    idx_content = f.read()
                    topic_file = topic if lang == "en" else (f"{lang}.html" if topic == "index.html" else topic.replace(".html", f"-{lang}.html"))
                    match = re.search(f'href="{topic_file}"[^>]*>([^<]+)</a>', idx_content)
                    if match:
                        labels[topic][lang] = match.group(1).strip()

import json
print(json.dumps(labels, indent=2, ensure_ascii=False))
