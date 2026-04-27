
import os
import re

base_dir = "/Users/u0174419/manifest"
languages = ["en", "nl", "fr", "it", "de", "es", "pt", "ar", "zh"]
lang_names = {
    "en": "English", "nl": "Nederlands", "fr": "Français", "it": "Italiano",
    "de": "Deutsch", "es": "Español", "pt": "Português", "ar": "العربية", "zh": "中文"
}

group_labels = {
    "en": ["Manifesto", "Systems of Power", "Extraction", "The Internal Mind", "Truth & Myth", "Solidarity"],
    "nl": ["Manifest", "Machtssystemen", "Extractie", "Interne Geest", "Waarheid & Mythe", "Solidariteit"],
    "fr": ["Manifeste", "Systèmes de Pouvoir", "Extraction", "Esprit Interne", "Vérité & Mythe", "Solidarité"],
    "it": ["Manifesto", "Sistemi di Potere", "Estrazione", "Mente Interna", "Verità e Mito", "Solidarietà"],
    "de": ["Manifest", "Machtssysteme", "Extraktion", "Innerer Geist", "Wahrheit & Mythos", "Solidarität"],
    "es": ["Manifiesto", "Sistemas de Poder", "Extracción", "Mente Interna", "Verdad y Mito", "Solidaridad"],
    "pt": ["Manifesto", "Sistemas de Poder", "Extração", "Mente Interna", "Verdade e Mito", "Solidariedade"],
    "ar": ["البيان", "أنظمة القوة", "الاستخراج", "العقل الداخلي", "الحقيقة والأسطورة", "التضامن"],
    "zh": ["宣言", "权力体系", "提取", "内心世界", "真理与神话", "团结"]
}

menu_labels = {
    "en": "MENU", "nl": "MENU", "fr": "MENU", "it": "MENU", "de": "MENÜ",
    "es": "MENÚ", "pt": "MENU", "ar": "القائمة", "zh": "菜单"
}

# Hierarchy of topics (base filenames)
hierarchy = [
    ("Manifesto", ["index.html"]),
    ("Systems of Power", ["history.html", "genocide-convention.html", "democracy-illusion.html", "money-evolution.html", "tax-avoidance.html", "wealth-gap.html", "social-mobility.html", "arms-trade.html"]),
    ("Extraction", ["climate-justice.html", "water-apartheid.html", "waste-crisis.html", "food-sovereignty.html", "modern-slavery.html", "medical-apartheid.html", "prison-industrial.html", "symptom-trap.html"]),
    ("The Internal Mind", ["neurodiversity.html", "survival-mode.html", "the-mindset.html", "education-factory.html", "board-games.html", "mental-health.html"]),
    ("Truth & Myth", ["philosophy.html", "human-nature.html", "hero-myth.html", "propaganda.html", "tech-surveillance.html", "divide-conquer.html", "bullshit-jobs.html", "love-revenge.html"]),
    ("Solidarity", ["take-action.html", "radical-community.html", "glossary.html", "references.html", "further-reading.html"])
]

# Labels extracted from files
item_labels = {
  "index.html": {"en": "Manifesto", "nl": "Manifest", "fr": "Manifeste", "it": "Manifesto", "de": "Manifest", "es": "Manifiesto", "pt": "Manifesto", "ar": "البيان", "zh": "宣言"},
  "history.html": {"en": "History", "nl": "Geschiedenis", "fr": "Histoire", "it": "Storia", "de": "Geschichte", "es": "Historia", "pt": "História", "ar": "التاريخ", "zh": "历史"},
  "genocide-convention.html": {"en": "Genocide Convention", "nl": "Genocideverdrag", "fr": "Convention sur le Génocide", "it": "Convenzione sul Genocidio", "de": "Völkermordkonvention", "es": "Convención sobre el Genocidio", "pt": "Convenção sobre el Genocídio", "ar": "اتفاقية منع الإبادة الجماعية", "zh": "种族灭绝公约"},
  "democracy-illusion.html": {"en": "Democracy Illusion", "nl": "Democratie-illusie", "fr": "Illusion de la Démocratie", "it": "Illusione della Democrazia", "de": "Demokratie-Illusion", "es": "Ilusión de la Democracia", "pt": "Ilusão da Democracia", "ar": "وهم الديمقراطية", "zh": "民主的幻想"},
  "money-evolution.html": {"en": "Evolution of Money", "nl": "Evolutie van Geld", "fr": "Évolution de l'Argent", "it": "Evoluzione del Denaro", "de": "Entwicklung des Geldes", "es": "Evolución del Dinero", "pt": "Evolução do Dinheiro", "ar": "تطور المال", "zh": "金钱的演变"},
  "tax-avoidance.html": {"en": "Tax Avoidance", "nl": "Belastingontwijking", "fr": "Évasion Fiscale", "it": "Evasione Fiscale", "de": "Steuervermeidung", "es": "Evasión de Impuestos", "pt": "Evasão Fiscal", "ar": "التهرب الضريبي", "zh": "税收回避"},
  "wealth-gap.html": {"en": "Wealth Gap", "nl": "Vermogenskloof", "fr": "Écart de Richesse", "it": "Divario di Ricchezza", "de": "Vermögenskluft", "es": "Brecha de Riqueza", "pt": "Desigualdade de Riqueza", "ar": "فجوة الثروة", "zh": "贫富差距"},
  "social-mobility.html": {"en": "Social Mobility", "nl": "Sociale Mobiliteit", "fr": "Mobilité Sociale", "it": "Mobilità Sociale", "de": "Soziale Mobilität", "es": "Movilidad Social", "pt": "Mobilidade Social", "ar": "الحراك الاجتماعي", "zh": "社会流动性"},
  "arms-trade.html": {"en": "Arms Trade", "nl": "Wapenhandel", "fr": "Commerce des Armes", "it": "Commercio di Armi", "de": "Waffenhandel", "es": "Comercio de Armas", "pt": "Comércio de Armas", "ar": "تجارة الأسلحة", "zh": "军火贸易"},
  "climate-justice.html": {"en": "Climate Justice", "nl": "Klimaatgerechtigheid", "fr": "Justice Climatique", "it": "Giustizia Climatica", "de": "Klimagerechtigkeit", "es": "Justicia Climática", "pt": "Justiça Climática", "ar": "العدالة المناخية", "zh": "气候正义"},
  "water-apartheid.html": {"en": "Water Apartheid", "nl": "Waterapartheid", "fr": "Apartheid de l'Eau", "it": "Apartheid dell'Acqua", "de": "Wasser-Apartheid", "es": "Apartheid del Agua", "pt": "Apartheid da Água", "ar": "الفصل العنصري للمياه", "zh": "水资源隔离"},
  "waste-crisis.html": {"en": "Waste Crisis", "nl": "Afvalcrisis", "fr": "Crise des Déchets", "it": "Crisi dei Rifiuti", "de": "Abfallkrise", "es": "Crisis de Residuos", "pt": "Crise de Resíduos", "ar": "أزمة النفايات", "zh": "垃圾危机"},
  "food-sovereignty.html": {"en": "Food Sovereignty", "nl": "Voedselsoevereiniteit", "fr": "Souveraineté Alimentaire", "it": "Sovranità Alimentare", "de": "Ernährungssouveränität", "es": "Soberanía Alimentaria", "pt": "Soberania Alimentar", "ar": "السيادة الغذائية", "zh": "粮食主权"},
  "modern-slavery.html": {"en": "Modern Slavery", "nl": "Moderne Slavernij", "fr": "Esclavage Moderne", "it": "Schiavitù Moderna", "de": "Moderne Sklaverei", "es": "Esclavitud Moderna", "pt": "Escravidão Moderna", "ar": "العبودية الحديثة", "zh": "现代奴隶制"},
  "medical-apartheid.html": {"en": "Medical Apartheid", "nl": "Medische Apartheid", "fr": "Apartheid Médical", "it": "Apartheid Medico", "de": "Medizinische Apartheid", "es": "Apartheid Médico", "pt": "Apartheid Médico", "ar": "الأبارتهايد الطبي", "zh": "医疗隔离"},
  "prison-industrial.html": {"en": "Prison Industrial", "nl": "Gevangenis-industrieel Complex", "fr": "Complexe Industriel Pénitentiaire", "it": "Complesso Industriale Carcerario", "de": "Gefängnis-industrieller Komplex", "es": "Complejo Industrial de Prisiones", "pt": "Complexo Industrial Prisional", "ar": "المجمع الصناعي للسجون", "zh": "监狱工业综合体"},
  "symptom-trap.html": {"en": "Symptom Trap", "nl": "De Symptoomval", "fr": "Le Piège des Symptômes", "it": "La Trappola dei Sintomi", "de": "Die Symptomfalle", "es": "La Trampa de los Síntomas", "pt": "A Armadilha dos Sintomas", "ar": "فخ الأعراض", "zh": "症状陷阱"},
  "neurodiversity.html": {"en": "Neurodiversity", "nl": "Neurodiversiteit", "fr": "Neurodiversité", "it": "Neurodiversità", "de": "Neurodiversität", "es": "Neurodiversidad", "pt": "Neurodiversidade", "ar": "التنوع العصبي", "zh": "神经多样性"},
  "survival-mode.html": {"en": "Survival Mode", "nl": "Overlevingsstand", "fr": "Mode Survie", "it": "Modalità Sopravvivenza", "de": "Überlebensmodus", "es": "Modo de Supervivencia", "pt": "Modo de Sobrevivência", "ar": "وضع البقاء", "zh": "生存模式"},
  "the-mindset.html": {"en": "The Mindset", "nl": "De Mentaliteit", "fr": "L'État d'Esprit", "it": "La Mentalità", "de": "Die Mentalität", "es": "La Mentalidad", "pt": "A Mentalidade", "ar": "العقلية", "zh": "心态"},
  "education-factory.html": {"en": "Education Factory", "nl": "Onderwijsfabriek", "fr": "L'Usine à Éducation", "it": "La Fabbrica dell'Istruzione", "de": "Bildungsfabrik", "es": "La Fábrica de Educación", "pt": "A Fábrica de Educação", "ar": "مصنع التعليم", "zh": "教育工厂"},
  "board-games.html": {"en": "Board Games", "nl": "Bordspellen", "fr": "Jeux de Société", "it": "Giochi da Tavolo", "de": "Brettspiele", "es": "Juegos de Mesa", "pt": "Jogos de Tabuleiro", "ar": "ألعاب الطاولة", "zh": "桌面游戏"},
  "mental-health.html": {"en": "Mental Health", "nl": "Mentale Gezondheid", "fr": "Santé Mentale", "it": "Salute Mentale", "de": "Psychische Gesundheit", "es": "Salud Mental", "pt": "Saúde Mental", "ar": "الصحة النفسية", "zh": "心理健康"},
  "philosophy.html": {"en": "Philosophy", "nl": "Filosofie", "fr": "Philosophie", "it": "Filosofia", "de": "Philosophie", "es": "Filosofía", "pt": "Filosofia", "ar": "الفلسفة", "zh": "哲学"},
  "human-nature.html": {"en": "Human Nature", "nl": "Menselijke Natuur", "fr": "Nature Humaine", "it": "Natura Umana", "de": "Menschliche Natur", "es": "Naturaleza Humana", "pt": "Natureza Humana", "ar": "الطبيعة البشرية", "zh": "人性"},
  "hero-myth.html": {"en": "Hero Myth", "nl": "Heldencultus", "fr": "Le Mythe du Héros", "it": "Il Mito dell'Eroe", "de": "Heldenmythos", "es": "El Mito del Héroe", "pt": "O Mito do Herói", "ar": "أسطورة البطل", "zh": "英雄神话"},
  "propaganda.html": {"en": "Information War", "nl": "Informatie-oorlog", "fr": "Guerre de l'Information", "it": "Guerra dell'Informazione", "de": "Informationskrieg", "es": "Guerra de Información", "pt": "Guerra de Informação", "ar": "حرب المعلومات", "zh": "信息战"},
  "tech-surveillance.html": {"en": "Tech & Surveillance", "nl": "Technologie & Surveillance", "fr": "Tech & Surveillance", "it": "Tecnologia e Sorveglianza", "de": "Technik & Überwachung", "es": "Tecnología y Vigilancia", "pt": "Tecnologia e Vigilância", "ar": "التكنولوجيا والمراقبة", "zh": "技术与监控"},
  "divide-conquer.html": {"en": "Divide & Conquer", "nl": "Verdeel en Heers", "fr": "Diviser pour Régner", "it": "Dividi e Domina", "de": "Teile und Herrsche", "es": "Divide y Vencerás", "pt": "Dividir e Conquistar", "ar": "فرق تسد", "zh": "分而治之"},
  "bullshit-jobs.html": {"en": "Bullshit Jobs", "nl": "Bullshitbanen", "fr": "Jobs à la con", "it": "Bullshit Jobs", "de": "Bullshit-Jobs", "es": "Trabajos de Mierda", "pt": "Trabalhos de Merda", "ar": "وظائف تافهة", "zh": "狗屁工作"},
  "love-revenge.html": {"en": "Love as Revenge", "nl": "Liefde als Wraak", "fr": "L'Amour comme Vengeance", "it": "L'Amore come Vendetta", "de": "Liebe als Rache", "es": "El Amor como Venganza", "pt": "O Amor como Vingança", "ar": "الحب كأنتقام", "zh": "爱作为报复"},
  "take-action.html": {"en": "Take Action", "nl": "Onderneem Actie", "fr": "Passer à l'Action", "it": "Agisci", "de": "Handeln", "es": "Actúa", "pt": "Agir", "ar": "اتخذ إجراءً", "zh": "采取行动"},
  "radical-community.html": {"en": "Radical Community", "nl": "Radicale Gemeenschap", "fr": "Communauté Radicale", "it": "Comunità Radicale", "de": "Radikale Gemeinschaft", "es": "Comunidad Radical", "pt": "Comunidade Radical", "ar": "المجتمع الراديكالي", "zh": "激进社区"},
  "glossary.html": {"en": "Glossary", "nl": "Woordenlijst", "fr": "Glossaire", "it": "Glossario", "de": "Glossar", "es": "Glosario", "pt": "Glossário", "ar": "قاموس المصطلحات", "zh": "词汇表"},
  "references.html": {"en": "References", "nl": "Referenties", "fr": "Références", "it": "Riferimenti", "de": "Referenzen", "es": "Referencias", "pt": "Referências", "ar": "المراجع", "zh": "参考文献"},
  "further-reading.html": {"en": "Read Further", "nl": "Verder Lezen", "fr": "Lire la Suite", "it": "Leggi Oltre", "de": "Weiterlesen", "es": "Leer Más", "pt": "Ler Mais", "ar": "اقرأ المزيد", "zh": "进一步阅读"},
  "republish.html": {"en": "About & Republishing", "nl": "Over & Herpubliceren", "fr": "À Propos & Republication", "it": "Informazioni e Ripubblicazione", "de": "Über & Wiederveröffentlichung", "es": "Acerca de y Republicación", "pt": "Sobre e Republicação", "ar": "حول وإعادة النشر", "zh": "关于和重新发布"}
}

def get_filename(base_topic, lang):
    if lang == "en":
        return base_topic
    if base_topic == "index.html":
        return f"{lang}.html"
    return base_topic.replace(".html", f"-{lang}.html")

def generate_nav(current_lang, current_topic):
    rtl_class = " rtl" if current_lang == "ar" else ""
    nav = f'    <nav class="navbar{rtl_class}">\n'
    nav += f'        <input type="checkbox" id="nav-toggle" class="nav-toggle">\n'
    nav += f'        <label for="nav-toggle" class="nav-toggle-label">{menu_labels[current_lang]}</label>\n'
    nav += f'        <div class="nav-links">\n'
    
    for i, (group_name, group_topics) in enumerate(hierarchy):
        is_group_active = current_topic in group_topics
        group_label = group_labels[current_lang][i]
        
        if group_name == "Manifesto":
            active_class = ' active' if is_group_active else ''
            nav += f'            <a href="{get_filename("index.html", current_lang)}" class="nav-item{active_class}">{group_label}</a>\n'
        else:
            dropdown_active = ' active' if is_group_active else ''
            nav += f'            <div class="nav-dropdown{dropdown_active}">\n'
            nav += f'                <div class="nav-item{dropdown_active}">{group_label}</div>\n'
            nav += f'                <div class="dropdown-content">\n'
            for topic in group_topics:
                item_active = ' class="active"' if current_topic == topic else ''
                nav += f'                    <a href="{get_filename(topic, current_lang)}"{item_active}>{item_labels[topic][current_lang]}</a>\n'
            nav += f'                </div>\n'
            nav += f'            </div>\n'
            
    nav += f'        </div>\n'
    
    # Language switcher
    nav += f'        <div class="lang-switcher">\n'
    nav += f'            <select onchange="window.location.href=this.value">\n'
    for lang in languages:
        selected = ' selected' if lang == current_lang else ''
        nav += f'                <option value="{get_filename(current_topic, lang)}"{selected}>{lang_names[lang]}</option>\n'
    nav += f'            </select>\n'
    nav += f'        </div>\n'
    nav += f'    </nav>'
    return nav

all_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

count = 0
for filename in all_files:
    # Determine lang and topic
    lang = "en"
    topic = filename
    for l in languages:
        if l == "en": continue
        if filename == f"{l}.html":
            lang = l
            topic = "index.html"
            break
        if filename.endswith(f"-{l}.html"):
            lang = l
            topic = filename.replace(f"-{l}.html", ".html")
            break
    
    # Special case for republish
    if topic not in item_labels and topic != "index.html":
        # Maybe it's a file we don't want to touch, but user said 333 files.
        # Let's see if it's one of the topics.
        pass

    if topic not in item_labels and topic != "index.html":
        continue

    file_path = os.path.join(base_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_nav = generate_nav(lang, topic)
    
    # Replace the old nav
    # Look for <nav class="navbar">...</nav> including multi-line
    new_content = re.sub(r'<nav class="navbar.*?">.*?</nav>', new_nav, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
    else:
        # If not found, try to insert it after header?
        # But all files should have it.
        # Some might have slightly different spacing.
        pass

print(f"Updated {count} files.")
