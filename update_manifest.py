import os
import re

languages = {
    'en': {'suffix': '', 'name': 'English', 'dir': 'ltr'},
    'nl': {'suffix': '-nl', 'name': 'Nederlands', 'dir': 'ltr'},
    'fr': {'suffix': '-fr', 'name': 'Français', 'dir': 'ltr'},
    'it': {'suffix': '-it', 'name': 'Italiano', 'dir': 'ltr'},
    'de': {'suffix': '-de', 'name': 'Deutsch', 'dir': 'ltr'},
    'es': {'suffix': '-es', 'name': 'Español', 'dir': 'ltr'},
    'pt': {'suffix': '-pt', 'name': 'Português', 'dir': 'ltr'},
    'ar': {'suffix': '-ar', 'name': 'العربية', 'dir': 'rtl'},
    'zh': {'suffix': '-zh', 'name': '中文', 'dir': 'ltr'}
}

# Navigation structure
nav_structure = [
    {'type': 'link', 'id': 'index', 'label': {
        'en': 'Manifesto', 'nl': 'Manifest', 'fr': 'Manifeste', 'it': 'Manifesto', 
        'de': 'Manifest', 'es': 'Manifiesto', 'pt': 'Manifesto', 'ar': 'البيان', 'zh': '宣言'
    }, 'file': 'index.html'},
    {'type': 'dropdown', 'label': {
        'en': 'Systems of Power', 'nl': 'Machtssystemen', 'fr': 'Systèmes de Pouvoir', 'it': 'Sistemi di Potere',
        'de': 'Machtsysteme', 'es': 'Sistemas de Poder', 'pt': 'Sistemas de Poder', 'ar': 'أنظمة القوة', 'zh': '权力体系'
    }, 'items': [
        {'id': 'history', 'label': {'en': 'History', 'nl': 'Geschiedenis', 'fr': 'Histoire', 'it': 'Storia', 'de': 'Geschichte', 'es': 'Historia', 'pt': 'História', 'ar': 'التاريخ', 'zh': '历史'}, 'file': 'history.html'},
        {'id': 'genocide-convention', 'label': {'en': 'Genocide Convention', 'nl': 'Genocideverdrag', 'fr': 'Convention sur le Génocide', 'it': 'Convenzione sul Genocidio', 'de': 'Völkermordkonvention', 'es': 'Convención sobre el Genocidio', 'pt': 'Convenção sobre o Genocídio', 'ar': 'اتفاقية منع الإبادة الجماعية', 'zh': '种族灭绝公约'}, 'file': 'genocide-convention.html'},
        {'id': 'democracy-illusion', 'label': {'en': 'Democracy Illusion', 'nl': 'Democratie-illusie', 'fr': 'Illusion de la Démocratie', 'it': 'Illusione della Democrazia', 'de': 'Demokratie-Illusion', 'es': 'Ilusión de la Democracia', 'pt': 'Ilusão da Democracia', 'ar': 'وهم الديمقراطية', 'zh': '民主的幻想'}, 'file': 'democracy-illusion.html'},
        {'id': 'money-evolution', 'label': {'en': 'Evolution of Money', 'nl': 'Evolutie van Geld', 'fr': 'Évolution de l\'Argent', 'it': 'Evoluzione del Denaro', 'de': 'Entwicklung des Geldes', 'es': 'Evolución del Dinero', 'pt': 'Evolução do Dinheiro', 'ar': 'تطور المال', 'zh': '金钱的演变'}, 'file': 'money-evolution.html'},
        {'id': 'tax-avoidance', 'label': {'en': 'Tax Avoidance', 'nl': 'Belastingontwijking', 'fr': 'Évasion Fiscale', 'it': 'Evasione Fiscale', 'de': 'Steuervermeidung', 'es': 'Evasión Fiscal', 'pt': 'Evasão Fiscal', 'ar': 'التهرب الضريبي', 'zh': '税收回避'}, 'file': 'tax-avoidance.html'},
        {'id': 'wealth-gap', 'label': {'en': 'Wealth Gap', 'nl': 'Vermogenskloof', 'fr': 'Écart de Richesse', 'it': 'Divario di Ricchezza', 'de': 'Wohlstandskluft', 'es': 'Brecha de Riqueza', 'pt': 'Desigualdade de Riqueza', 'ar': 'فجوة الثروة', 'zh': '贫富差距'}, 'file': 'wealth-gap.html'},
        {'id': 'social-mobility', 'label': {'en': 'Social Mobility', 'nl': 'Sociale Mobiliteit', 'fr': 'Mobilité Sociale', 'it': 'Mobilità Sociale', 'de': 'Soziale Mobilität', 'es': 'Movilidad Social', 'pt': 'Mobilidade Social', 'ar': 'الحراك الاجتماعي', 'zh': '社会流动性'}, 'file': 'social-mobility.html'},
        {'id': 'land-ownership', 'label': {'en': 'Land Ownership', 'nl': 'Grondbezit', 'fr': 'Propriété Foncière', 'it': 'Proprietà della Terra', 'de': 'Landbesitz', 'es': 'Propiedad de la Tierra', 'pt': 'Propriedade da Terra', 'ar': 'ملكية الأرض', 'zh': '土地所有权'}, 'file': 'land-ownership.html'},
        {'id': 'arms-trade', 'label': {'en': 'Arms Trade', 'nl': 'Wapenhandel', 'fr': 'Commerce des Armes', 'it': 'Commercio delle Armi', 'de': 'Waffenhandel', 'es': 'Comercio de Armas', 'pt': 'Comércio de Armas', 'ar': 'تجارة الأسلحة', 'zh': '军火贸易'}, 'file': 'arms-trade.html'},
    ]},
    {'type': 'dropdown', 'label': {
        'en': 'Extraction', 'nl': 'Extractie', 'fr': 'Extraction', 'it': 'Estrazione',
        'de': 'Extraktion', 'es': 'Extracción', 'pt': 'Extração', 'ar': 'الاستخراج', 'zh': '提取'
    }, 'items': [
        {'id': 'climate-justice', 'label': {'en': 'Climate Justice', 'nl': 'Klimaatgerechtigheid', 'fr': 'Justice Climatique', 'it': 'Giustizia Climatica', 'de': 'Klimagerechtigkeit', 'es': 'Justicia Climática', 'pt': 'Justiça Climática', 'ar': 'العدالة المناخية', 'zh': '气候正义'}, 'file': 'climate-justice.html'},
        {'id': 'water-apartheid', 'label': {'en': 'Water Apartheid', 'nl': 'Waterapartheid', 'fr': 'Apartheid de l\'Eau', 'it': 'Apartheid dell\'Acqua', 'de': 'Wasser-Apartheid', 'es': 'Apartheid del Agua', 'pt': 'Apartheid da Água', 'ar': 'الفصل العنصري للمياه', 'zh': '水资源隔离'}, 'file': 'water-apartheid.html'},
        {'id': 'waste-crisis', 'label': {'en': 'Waste Crisis', 'nl': 'Afvalcrisis', 'fr': 'Crise des Déchets', 'it': 'Crisi dei Rifiuti', 'de': 'Abfallkrise', 'es': 'Crisis de Residuos', 'pt': 'Crise de Resíduos', 'ar': 'أزمة النفايات', 'zh': '垃圾危机'}, 'file': 'waste-crisis.html'},
        {'id': 'food-sovereignty', 'label': {'en': 'Food Sovereignty', 'nl': 'Voedselsoevereiniteit', 'fr': 'Souveraineté Alimentaire', 'it': 'Sovranità Alimentare', 'de': 'Ernährungssouveränität', 'es': 'Soberanía Alimentaria', 'pt': 'Soberania Alimentar', 'ar': 'السيادة الغذائية', 'zh': '粮食主权'}, 'file': 'food-sovereignty.html'},
        {'id': 'modern-slavery', 'label': {'en': 'Modern Slavery', 'nl': 'Moderne Slavernij', 'fr': 'Esclavage Moderne', 'it': 'Schiavitù Moderna', 'de': 'Moderne Sklaverei', 'es': 'Esclavitud Moderna', 'pt': 'Escravidão Moderna', 'ar': 'العبودية الحديثة', 'zh': '现代奴隶制'}, 'file': 'modern-slavery.html'},
        {'id': 'medical-apartheid', 'label': {'en': 'Medical Apartheid', 'nl': 'Medische Apartheid', 'fr': 'Apartheid Médical', 'it': 'Apartheid Medico', 'de': 'Medizinische Apartheid', 'es': 'Apartheid Médico', 'pt': 'Apartheid Médico', 'ar': 'الأبارتهايد الطبي', 'zh': '医疗隔离'}, 'file': 'medical-apartheid.html'},
        {'id': 'prison-industrial', 'label': {'en': 'Prison Industrial', 'nl': 'Gevangenis-industrieel', 'fr': 'Complexe Industriel Carcéral', 'it': 'Complesso Industriale Carcerario', 'de': 'Gefängnis-Industrie-Komplex', 'es': 'Complejo Industrial de Prisiones', 'pt': 'Complexo Industrial Prisional', 'ar': 'المجمع الصناعي للسجون', 'zh': '监狱工业综合体'}, 'file': 'prison-industrial.html'},
        {'id': 'symptom-trap', 'label': {'en': 'Symptom Trap', 'nl': 'De Symptoomval', 'fr': 'Piège des Symptômes', 'it': 'Trappola dei Sintomi', 'de': 'Symptomfalle', 'es': 'Trampa de los Síntomas', 'pt': 'Armadilha dos Sintomas', 'ar': 'فخ الأعراض', 'zh': '症状陷阱'}, 'file': 'symptom-trap.html'},
        {'id': 'greenwashing', 'label': {'en': 'Greenwashing', 'nl': 'Greenwashing', 'fr': 'Greenwashing', 'it': 'Greenwashing', 'de': 'Greenwashing', 'es': 'Greenwashing', 'pt': 'Greenwashing', 'ar': 'الغسل الأخضر', 'zh': '漂绿'}, 'file': 'greenwashing.html'},
    ]},
    {'type': 'dropdown', 'label': {
        'en': 'The Human Lens', 'nl': 'De Menselijke Lens', 'fr': 'La Lentille Humaine', 'it': 'La Lente Umana',
        'de': 'Die Menschliche Linse', 'es': 'La Lente Humana', 'pt': 'A Lente Humana', 'ar': 'عدسة الإنسان', 'zh': '人类视角'
    }, 'items': [
        {'id': 'neurodiversity', 'label': {'en': 'Neurodiversity', 'nl': 'Neurodiversiteit', 'fr': 'Neurodiversité', 'it': 'Neurodiversità', 'de': 'Neurodiversität', 'es': 'Neurodiversidad', 'pt': 'Neurodiversidade', 'ar': 'التنوع العصبي', 'zh': '神经多样性'}, 'file': 'neurodiversity.html'},
        {'id': 'survival-mode', 'label': {'en': 'Survival Mode', 'nl': 'Overlevingsstand', 'fr': 'Mode Survie', 'it': 'Modalità Sopravvivenza', 'de': 'Überlebensmodus', 'es': 'Modo Supervivencia', 'pt': 'Modo Sobrevivência', 'ar': 'وضع البقاء', 'zh': '生存模式'}, 'file': 'survival-mode.html'},
        {'id': 'the-mindset', 'label': {'en': 'The Mindset', 'nl': 'De Mentaliteit', 'fr': 'L\'État d\'Esprit', 'it': 'La Mentalità', 'de': 'Die Mentalität', 'es': 'La Mentalidad', 'pt': 'A Mentalidade', 'ar': 'العقلية', 'zh': '心态'}, 'file': 'the-mindset.html'},
        {'id': 'education-factory', 'label': {'en': 'Education Factory', 'nl': 'Onderwijsfabriek', 'fr': 'Fabrique de l\'Éducation', 'it': 'Fabbrica dell\'Istruzione', 'de': 'Bildungsfabrik', 'es': 'Fábrica de Educación', 'pt': 'Fábrica de Educação', 'ar': 'مصنع التعليم', 'zh': '教育工厂'}, 'file': 'education-factory.html'},
        {'id': 'board-games', 'label': {'en': 'Board Games', 'nl': 'Bordspellen', 'fr': 'Jeux de Société', 'it': 'Giochi da Tavolo', 'de': 'Brettspiele', 'es': 'Juegos de Mesa', 'pt': 'Jogos de Tabuleiro', 'ar': 'ألعاب الطاولة', 'zh': '桌面游戏'}, 'file': 'board-games.html'},
        {'id': 'mental-health', 'label': {'en': 'Mental Health', 'nl': 'Mentale Gezondheid', 'fr': 'Santé Mentale', 'it': 'Salute Mentale', 'de': 'Mentale Gesundheit', 'es': 'Salud Mental', 'pt': 'Saúde Mental', 'ar': 'الصحة النفسية', 'zh': '心理健康'}, 'file': 'mental-health.html'},
        {'id': 'greta-thunberg', 'label': {'en': 'Greta Thunberg', 'nl': 'Greta Thunberg', 'fr': 'Greta Thunberg', 'it': 'Greta Thunberg', 'de': 'Greta Thunberg', 'es': 'Greta Thunberg', 'pt': 'Greta Thunberg', 'ar': 'غريتا تونبرغ', 'zh': '格蕾塔·通贝里'}, 'file': 'greta-thunberg.html'},
        {'id': 'philosophy', 'label': {'en': 'Philosophy', 'nl': 'Filosofie', 'fr': 'Philosophie', 'it': 'Filosofia', 'de': 'Philosophie', 'es': 'Filosofía', 'pt': 'Filosofia', 'ar': 'الفلسفة', 'zh': '哲学'}, 'file': 'philosophy.html'},
        {'id': 'human-nature', 'label': {'en': 'Human Nature', 'nl': 'Menselijke Natuur', 'fr': 'Nature Humaine', 'it': 'Natura Umana', 'de': 'Menschliche Natur', 'es': 'Naturaleza Humana', 'pt': 'Natureza Humana', 'ar': 'الطبيعة البشرية', 'zh': '人性'}, 'file': 'human-nature.html'},
        {'id': 'hero-myth', 'label': {'en': 'Hero Myth', 'nl': 'Heldencultus', 'fr': 'Mythe du Héros', 'it': 'Mito dell\'Eroe', 'de': 'Heldenmythos', 'es': 'Mito del Héroe', 'pt': 'Mito do Herói', 'ar': 'أسطورة البطل', 'zh': '英雄神话'}, 'file': 'hero-myth.html'},
        {'id': 'propaganda', 'label': {'en': 'Information War', 'nl': 'Informatie-oorlog', 'fr': 'Guerre de l\'Information', 'it': 'Guerra dell\'Informazione', 'de': 'Informationskrieg', 'es': 'Guerra de Información', 'pt': 'Guerra de Informação', 'ar': 'حرب المعلومات', 'zh': '信息战'}, 'file': 'propaganda.html'},
        {'id': 'tech-surveillance', 'label': {'en': 'Tech & Surveillance', 'nl': 'Technologie & Surveillance', 'fr': 'Tech & Surveillance', 'it': 'Tech e Sorveglianza', 'de': 'Tech & Überwachung', 'es': 'Tecnología y Vigilancia', 'pt': 'Tecnologia e Vigilância', 'ar': 'التكنولوجيا والمراقبة', 'zh': '技术与监控'}, 'file': 'tech-surveillance.html'},
        {'id': 'divide-conquer', 'label': {'en': 'Divide & Conquer', 'nl': 'Verdeel en Heers', 'fr': 'Diviser pour Régner', 'it': 'Dividi e Domina', 'de': 'Teile und Herrsche', 'es': 'Divide y Vencerás', 'pt': 'Dividir e Conquistar', 'ar': 'فرق تسد', 'zh': '分而治之'}, 'file': 'divide-conquer.html'},
        {'id': 'bullshit-jobs', 'label': {'en': 'Bullshit Jobs', 'nl': 'Bullshitbanen', 'fr': 'Jobs à la Con', 'it': 'Bullshit Jobs', 'de': 'Bullshit-Jobs', 'es': 'Trabajos de Mierda', 'pt': 'Empregos de Merda', 'ar': 'وظائف تافهة', 'zh': '狗屁工作'}, 'file': 'bullshit-jobs.html'},
        {'id': 'love-revenge', 'label': {'en': 'Love as Revenge', 'nl': 'Liefde als Wraak', 'fr': 'L\'Amour comme Revanche', 'it': 'L\'Amore come Vendetta', 'de': 'Liebe als Rache', 'es': 'El Amor como Venganza', 'pt': 'Amor como Vingança', 'ar': 'الحب كأنتقام', 'zh': '爱作为报复'}, 'file': 'love-revenge.html'},
    ]},
    {'type': 'dropdown', 'label': {
        'en': 'Solidarity', 'nl': 'Solidariteit', 'fr': 'Solidarité', 'it': 'Solidarietà',
        'de': 'Solidarität', 'es': 'Solidaridad', 'pt': 'Solidariedade', 'ar': 'التضامن', 'zh': '团结'
    }, 'items': [
        {'id': 'take-action', 'label': {'en': 'Take Action', 'nl': 'Onderneem Actie', 'fr': 'Passer à l\'Action', 'it': 'Agisci', 'de': 'Handeln', 'es': 'Pasar a la Acción', 'pt': 'Tomar Atitude', 'ar': 'اتخذ إجراءً', 'zh': '采取行动'}, 'file': 'take-action.html'},
        {'id': 'radical-community', 'label': {'en': 'Radical Community', 'nl': 'Radicale Gemeenschap', 'fr': 'Communauté Radicale', 'it': 'Comunità Radicale', 'de': 'Radikale Gemeinschaft', 'es': 'Comunidad Radical', 'pt': 'Comunidade Radical', 'ar': 'المجتمع الراديكالي', 'zh': '激进社区'}, 'file': 'radical-community.html'},
        {'id': 'glossary', 'label': {'en': 'Glossary', 'nl': 'Woordenlijst', 'fr': 'Glossaire', 'it': 'Glossario', 'de': 'Glossar', 'es': 'Glosario', 'pt': 'Glossário', 'ar': 'قاموس المصطلحات', 'zh': '词汇表'}, 'file': 'glossary.html'},
        {'id': 'references', 'label': {'en': 'References', 'nl': 'Referenties', 'fr': 'Références', 'it': 'Riferimenti', 'de': 'Referenzen', 'es': 'Referencias', 'pt': 'Referências', 'ar': 'المراجع', 'zh': '参考文献'}, 'file': 'references.html'},
        {'id': 'further-reading', 'label': {'en': 'Read Further', 'nl': 'Verder Lezen', 'fr': 'Lire la Suite', 'it': 'Leggi Altro', 'de': 'Weiterlesen', 'es': 'Leer Más', 'pt': 'Ler Mais', 'ar': 'اقرأ المزيد', 'zh': '进一步阅读'}, 'file': 'further-reading.html'},
        {'id': 'submit-ideas', 'label': {'en': 'Submit Ideas', 'nl': 'Ideeën Indienen', 'fr': 'Soumettre des Idées', 'it': 'Invia Idee', 'de': 'Ideen Einreichen', 'es': 'Enviar Ideas', 'pt': 'Enviar Ideias', 'ar': 'تقديم الأفكار', 'zh': '提交创意'}, 'file': 'submit-ideas.html'},
    ]},
]

labels = {
    'menu': {'en': 'MENU', 'nl': 'MENU', 'fr': 'MENU', 'it': 'MENU', 'de': 'MENÜ', 'es': 'MENÚ', 'pt': 'MENU', 'ar': 'القائمة', 'zh': '菜单'},
    'republish': {'en': 'About & Republishing', 'nl': 'Over & Herpubliceren', 'fr': 'À Propos & Republication', 'it': 'Informazioni e Ripubblicazione', 'de': 'Über & Wiederveröffentlichung', 'es': 'Sobre y Republicación', 'pt': 'Sobre e Republicação', 'ar': 'حول وإعادة النشر', 'zh': '关于和重新发布'},
    'submit_ideas': {'en': 'Submit Ideas', 'nl': 'Ideeën Indienen', 'fr': 'Soumettre des Idées', 'it': 'Invia Idee', 'de': 'Ideen Einreichen', 'es': 'Enviar Ideas', 'pt': 'Enviar Ideias', 'ar': 'تقديم الأفكار', 'zh': '提交创意'},
    'source_code': {'en': 'Source Code', 'nl': 'Broncode', 'fr': 'Code Source', 'it': 'Codice Sorgente', 'de': 'Quellcode', 'es': 'Código Fuente', 'pt': 'Código Fonte', 'ar': 'كود المصدر', 'zh': '源代码'},
}

def get_localized_filename(base_file, lang):
    if lang == 'en':
        if base_file == 'index.html': return 'index.html'
        return base_file
    name, ext = os.path.splitext(base_file)
    if name == 'index': return languages[lang]['suffix'].lstrip('-') + ext
    return name + languages[lang]['suffix'] + ext

def generate_nav(active_id, lang):
    dir_rtl = ' rtl' if languages[lang]['dir'] == 'rtl' else ''
    nav = f'    <nav class="navbar{dir_rtl}">\n'
    nav += '        <input type="checkbox" id="nav-toggle" class="nav-toggle">\n'
    nav += f'        <label for="nav-toggle" class="nav-toggle-label">{labels["menu"][lang]}</label>\n'
    nav += '        <div class="nav-links">\n'
    
    for entry in nav_structure:
        if entry['type'] == 'link':
            active_class = ' active' if active_id == entry['id'] else ''
            file = get_localized_filename(entry['file'], lang)
            nav += f'            <a href="{file}" class="nav-item{active_class}">{entry["label"][lang]}</a>\n'
        elif entry['type'] == 'dropdown':
            active_dropdown = any(item['id'] == active_id for item in entry['items'])
            dropdown_class = ' active' if active_dropdown else ''
            nav += f'            <div class="nav-dropdown{dropdown_class}">\n'
            nav += f'                <div class="nav-item{dropdown_class}">{entry["label"][lang]}</div>\n'
            nav += '                <div class="dropdown-content">\n'
            for item in entry['items']:
                active_item = ' class="active"' if active_id == item['id'] else ''
                file = get_localized_filename(item['file'], lang)
                nav += f'                    <a href="{file}"{active_item}>{item["label"][lang]}</a>\n'
            nav += '                </div>\n'
            nav += '            </div>\n'
    
    nav += '        </div>\n'
    nav += '        <div class="lang-switcher">\n'
    nav += '            <select onchange="window.location.href=this.value">\n'
    
    # We need to know the current base_file to switch languages
    # This will be handled outside
    nav += '[[LANG_SWITCHER_OPTIONS]]'
    
    nav += '            </select>\n'
    nav += '        </div>\n'
    nav += '    </nav>'
    return nav

def generate_footer(lang):
    republish_file = get_localized_filename('republish.html', lang)
    submit_file = get_localized_filename('submit-ideas.html', lang)
    footer = '    <footer>\n'
    footer += f'        <p>&copy; 2026 Justice For Gaza Manifesto | <a href="{republish_file}">{labels["republish"][lang]}</a> | <a href="{submit_file}">{labels["submit_ideas"][lang]}</a> | <a href="https://github.com/TimGeyssens/JusticeForGaza">{labels["source_code"][lang]}</a></p>\n'
    footer += '    </footer>'
    return footer

# Content for land-ownership.html and submit-ideas.html
content_translations = {
    'land-ownership.html': {
        'title': {
            'en': 'Evolution of Land Ownership - From Common Land to Private Extraction',
            'nl': 'Evolutie van Grondbezit - Van Gemeenschappelijke Grond naar Private Extractie',
            'fr': 'Évolution de la Propriété Foncière - Des Terres Communes à l\'Extraction Privée',
            'it': 'Evoluzione della Proprietà della Terra - Dalla Terra Comune all\'Estrazione Privata',
            'de': 'Entwicklung des Landbesitzes - Von Allmende zu Privater Extraktion',
            'es': 'Evolución de la Propiedad de la Tierra - De la Tierra Comunal a la Extracción Privada',
            'pt': 'Evolução da Propriedade da Terra - Da Terra Comum à Extração Privada',
            'ar': 'تطور ملكية الأرض - من المشاع إلى الاستخراج الخاص',
            'zh': '土地所有权的演变 - 从共有土地到私人开采'
        },
        'h1': {
            'en': 'Evolution of Land Ownership',
            'nl': 'Evolutie van Grondbezit',
            'fr': 'Évolution de la Propriété Foncière',
            'it': 'Evoluzione della Proprietà della Terra',
            'de': 'Entwicklung des Landbesitzes',
            'es': 'Evolución de la Propiedad de la Tierra',
            'pt': 'Evolução da Propriedade da Terra',
            'ar': 'تطور ملكية الأرض',
            'zh': '土地所有权的演变'
        },
        'h2': {
            'en': 'The Enclosure of the Commons and the Logic of Displacement',
            'nl': 'De Insluiting van de Meent en de Logica van Verdrijving',
            'fr': 'L\'Enclôture des Communs et la Logique du Déplacement',
            'it': 'La Recinzione dei Beni Comuni e la Logica dello Spostamento',
            'de': 'Die Einhegung der Allmende und die Logik der Vertreibung',
            'es': 'El Cercamiento de los Comunes y la Lógica del Desplazamiento',
            'pt': 'O Cercamento dos Comuns e a Lógica do Deslocamento',
            'ar': 'تسييج المشاع ومنطق التهجير',
            'zh': '公地的围合与流离失所的逻辑'
        },
        'sections': [
            {
                'h3': {'en': 'The Death of the Commons', 'nl': 'De Dood van de Meent', 'fr': 'La Mort des Communs', 'it': 'La Morte dei Comuni', 'de': 'Der Tod der Allmende', 'es': 'La Muerte de los Comunes', 'pt': 'A Morte dos Comuns', 'ar': 'موت المشاع', 'zh': '公地的死亡'},
                'p': {
                    'en': 'For millennia, land was viewed as a shared resource—the "Commons"—governed by collective use and stewardship. The 1% system was founded on the destruction of this model. Through the "Enclosure Acts" in Europe and the colonization of the rest of the world, land was forcibly turned into private property to be owned, traded, and extracted for profit.',
                    'nl': 'Millennia lang werd land beschouwd als een gedeelde hulpbron—de "Meent"—beheerd door collectief gebruik en rentmeesterschap. Het 1%-systeem werd gebouwd op de vernietiging van dit model. Via de "Enclosure Acts" in Europa en de kolonisatie van de rest van de wereld werd land gedwongen omgezet in privé-eigendom om te worden bezeten, verhandeld en geëxploiteerd voor winst.',
                    'fr': 'Pendant des millénaires, la terre était considérée comme une ressource partagée — les « Communs » — régie par l\'usage collectif et la gérance. Le système du 1% s\'est fondé sur la destruction de ce modèle. À travers les « Enclosure Acts » en Europe et la colonisation du reste du monde, la terre a été transformée de force en propriété privée pour être possédée, échangée et exploitée à des fins lucratives.',
                    'it': 'Per millenni, la terra è stata vista come una risorsa condivisa — i "Comuni" — governata dall\'uso collettivo e dalla gestione responsabile. Il sistema dell\'1% è stato fondato sulla distruzione di questo modello. Attraverso gli "Enclosure Acts" in Europa e la colonizzazione del resto del mondo, la terra è stata forzatamente trasformata in proprietà privata per essere posseduta, scambiata ed estratta a scopo di lucro.',
                    'de': 'Jahrtausende lang wurde Land als gemeinsame Ressource betrachtet – die „Allmende“ –, die durch kollektive Nutzung und Verwaltung geregelt wurde. Das 1%-System gründete auf der Zerstörung dieses Modells. Durch die „Enclosure Acts“ in Europa und die Kolonialisierung des Rests der Welt wurde Land gewaltsam in Privateigentum umgewandelt, um besessen, gehandelt und gewinnbringend ausgebeutet zu werden.',
                    'es': 'Durante milenios, la tierra fue vista como un recurso compartido —los "Comunes"— gobernada por el uso colectivo y la administración. El sistema del 1% se fundó en la destrucción de este modelo. A través de las "Leyes de Cercamiento" en Europa y la colonización del resto del mundo, la tierra se convirtió por la fuerza en propiedad privada para ser poseída, comercializada y extraída con fines de lucro.',
                    'pt': 'Durante milênios, a terra foi vista como um recurso compartilhado — os "Comuns" — governada pelo uso coletivo e pela gestão. O sistema do 1% foi fundado na destruição deste modelo. Através dos "Atos de Cercamento" na Europa e da colonização do resto do mundo, a terra foi forçadamente transformada em propriedade privada para ser possuída, comercializada e extraída para lucro.',
                    'ar': 'لآلاف السنين، كان يُنظر إلى الأرض على أنها مورد مشترك - "المشاع" - يحكمه الاستخدام الجماعي والإشراف. تأسس نظام الـ 1٪ على تدمير هذا النموذج. من خلال "أعمال التسييج" في أوروبا واستعمار بقية العالم، تحولت الأرض قسراً إلى ملكية خاصة ليتم امتلاكها وتداولها واستخراجها من أجل الربح.',
                    'zh': '几千年来，土地被视为一种共享资源——“公地”——由集体使用和管理。1%的系统建立在对这种模式的破坏之上。通过欧洲的《围地法案》和世界其他地区的殖民化，土地被强行转变为私人财产，以便拥有、交易并以此获取利润。'
                }
            },
            {
                'h3': {'en': 'The Logic of Displacement', 'nl': 'De Logica van Verdrijving', 'fr': 'La Logique du Déplacement', 'it': 'La Logica dello Spostamento', 'de': 'Die Logik der Vertreibung', 'es': 'La Lógica del Desplazamiento', 'pt': 'A Lógica do Deslocamento', 'ar': 'منطق التهجير', 'zh': '流离失所的逻辑'},
                'p': {
                    'en': 'Once land is reduced to an asset, the people living on it become "obstacles" to profit. This is the logic that drives the "History of Palestine," the "Ecocide" of indigenous lands, and the "Social Mobility Trap" of modern housing markets.',
                    'nl': 'Zodra land wordt gereduceerd tot een bezit, worden de mensen die erop wonen "obstakels" voor winst. Dit is de logica achter de "Geschiedenis van Palestina", de "Ecocide" op inheemse gronden en de "Sociale Mobiliteitsval" van moderne woningmarkten.',
                    'fr': 'Une fois que la terre est réduite à un actif, les personnes qui y vivent deviennent des « obstacles » au profit. C\'est la logique qui anime l\'« Histoire de la Palestine », l\'« Écocide » des terres indigènes et le « Piège de la Mobilité Sociale » des marchés du logement modernes.',
                    'it': 'Una volta che la terra viene ridotta a un bene, le persone che ci vivono diventano "ostacoli" al profitto. Questa è la logica che guida la "Storia della Palestina", l\'"Ecocidio" delle terre indigene e la "Trappola della Mobilità Sociale" dei moderni mercati immobiliari.',
                    'de': 'Sobald Land auf einen Vermögenswert reduziert wird, werden die darauf lebenden Menschen zu „Hindernissen“ für den Profit. Dies ist die Logik, die die „Geschichte Palästinas“, den „Ökozid“ an indigenen Gebieten und die „Falle der sozialen Mobilität“ moderner Wohnungsmärkte antreibt.',
                    'es': 'Una vez que la tierra se reduce a un activo, las personas que viven en ella se convierten en "obstáculos" para las ganancias. Esta es la lógica que impulsa la "Historia de Palestina", el "Ecocidio" de las tierras indígenas y la "Trampa de la Movilidad Social" de los mercados de vivienda modernos.',
                    'pt': 'Uma vez que a terra é reduzida a um ativo, as pessoas que vivem nela tornam-se "obstáculos" ao lucro. Esta é a lógica que impulsiona a "História da Palestina", o "Ecocídio" das terras indígenas e a "Armadilha da Mobilidade Social" dos mercados imobiliários modernos.',
                    'ar': 'بمجرد اختزال الأرض إلى أصل مالي، يصبح الأشخاص الذين يعيشون عليها "عقبات" أمام الربح. هذا هو المنطق الذي يحرك "تاريخ فلسطين"، و"الإبادة البيئية" لأراضي الشعوب الأصلية، و"فخ الحراك الاجتماعي" لأسواق الإسكان الحديثة.',
                    'zh': '一旦土地被简化为一种资产，生活在上面的人就成了利润的“障碍”。这就是推动“巴勒斯坦历史”、土著土地的“生态灭绝”以及现代住房市场“社会流动性陷阱”的逻辑。'
                },
                'list': [
                    {'bold': {'en': 'Colonial Dispossession:', 'nl': 'Koloniale Onteigening:', 'fr': 'Dépossession Coloniale :', 'it': 'Espropriazione Coloniale:', 'de': 'Koloniale Enteignung:', 'es': 'Despojo Colonial:', 'pt': 'Desapropriação Colonial:', 'ar': 'الحرمان الاستعماري:', 'zh': '殖民地剥夺：'}, 'text': {'en': 'Indigenous populations worldwide have been displaced from their ancestral lands through legal fictions (like <em>Terra Nullius</em>) and military force to make way for resource extraction.', 'nl': 'Inheemse bevolkingen wereldwijd zijn verdreven van hun voorouderlijke gronden via juridische ficties (zoals <em>Terra Nullius</em>) en militair geweld om plaats te maken voor extractie van hulpbronnen.', 'fr': 'Les populations indigènes du monde entier ont été déplacées de leurs terres ancestrales par des fictions juridiques (comme <em>Terra Nullius</em>) et la force militaire pour faire place à l\'extraction des ressources.', 'it': 'Le popolazioni indigene di tutto il mondo sono state allontanate dalle loro terre ancestrali attraverso finzioni legali (come <em>Terra Nullius</em>) e la forza militare per far posto all\'estrazione delle risorse.', 'de': 'Indigene Bevölkerungen weltweit wurden durch rechtliche Fiktionen (wie <em>Terra Nullius</em>) und militärische Gewalt aus ihren angestammten Gebieten vertrieben, um Platz für die Rohstoffgewinnung zu schaffen.', 'es': 'Las poblaciones indígenas de todo el mundo han sido desplazadas de sus tierras ancestrales a través de ficciones legales (como <em>Terra Nullius</em>) y la fuerza militar para dar paso a la extracción de recursos.', 'pt': 'As populações indígenas em todo o mundo foram deslocadas de suas terras ancestrais através de ficções jurídicas (como <em>Terra Nullius</em>) e força militar para dar lugar à extração de recursos.', 'ar': 'تم تهجير السكان الأصليين في جميع أنحاء العالم من أراضي أجدادهم من خلال الأساطير القانونية (مثل <em>الأرض المباحة</em>) والقوة العسكرية لإفساح المجال لاستخراج الموارد.', 'zh': '世界各地的土著居民通过法律虚构（如<em>无主地</em>）和军事力量流离失所，被迫离开祖传土地，为资源开采让路。'}},
                    {'bold': {'en': 'Gentrification as Extraction:', 'nl': 'Gentrificatie als Extractie:', 'fr': 'La Gentrification comme Extraction :', 'it': 'Gentrification come Estrazione:', 'de': 'Gentrifizierung als Extraktion:', 'es': 'Gentrificación como Extracción:', 'pt': 'Gentrificação como Extração:', 'ar': 'التحسين كاستخراج:', 'zh': '士绅化即开采：'}, 'text': {'en': 'In modern cities, the 1% use the "Evolution of Money" (debt and inflation) to price the working class out of their own neighborhoods, turning homes into speculative assets.', 'nl': 'In moderne steden gebruikt de 1% de "Evolutie van Geld" (schuld en inflatie) om de arbeidersklasse uit hun eigen wijken te prijzen, waardoor huizen speculatieve bezittingen worden.', 'fr': 'Dans les villes modernes, le 1% utilise l\'« Évolution de l\'Argent » (dette et inflation) pour exclure la classe ouvrière de ses propres quartiers, transformant les maisons en actifs spéculatifs.', 'it': 'Nelle città moderne, l\'1% usa l\'"Evoluzione del Denaro" (debito e inflazione) per escludere la classe operaia dai propri quartieri, trasformando le case in beni speculativi.', 'de': 'In modernen Städten nutzt das oberste 1 % die „Entwicklung des Geldes“ (Schulden und Inflation), um die Arbeiterklasse aus ihren eigenen Vierteln zu verdrängen und Häuser in spekulative Vermögenswerte teuer zu machen.', 'es': 'En las ciudades modernas, el 1% utiliza la "Evolución del Dinero" (deuda e inflación) para expulsar a la clase trabajadora de sus propios barrios, convirtiendo las viviendas en activos especulativos.', 'pt': 'Nas cidades modernas, o 1% usa a "Evolução do Dinheiro" (dívida e inflação) para expulsar a classe trabalhadora de seus próprios bairros, transformando as casas em ativos especulativos.', 'ar': 'في المدن الحديثة، تستخدم نسبة الـ 1٪ "تطور المال" (الديون والتضخم) لإخراج الطبقة العاملة من أحيائهم، وتحويل المنازل إلى أصول مضاربة.', 'zh': '在现代城市中，那1%的人利用“金钱的演变”（债务和通货膨胀）将工人阶级赶出他们自己的社区，将住房转变为投机资产。'}},
                    {'bold': {'en': 'Agricultural Seizure:', 'nl': 'Agrarische Inbeslagname:', 'fr': 'Saisie Agricole :', 'it': 'Sequestro Agricolo:', 'de': 'Beschlagnahme von Agrarflächen:', 'es': 'Incautación Agrícola:', 'pt': 'Apreensão Agrícola:', 'ar': 'الاستيلاء الزراعي:', 'zh': '农业征占：'}, 'text': {'en': 'As discussed in "Food Sovereignty," fertile land is increasingly seized by mega-corporations, forcing local farmers into "Survival Mode."', 'nl': 'Zoals besproken in "Voedselsoevereiniteit", wordt vruchtbare grond steeds vaker in beslag genomen door megacorporaties, waardoor lokale boeren in de "Overlevingsstand" worden gedwongen.', 'fr': 'Comme mentionné dans « Souveraineté Alimentaire », les terres fertiles sont de plus en plus saisies par des méga-corporations, forçant les agriculteurs locaux à passer en « Mode Survie ».', 'it': 'Come discusso in "Sovranità Alimentare", la terra fertile viene sempre più sequestrata da mega-corporazioni, costringendo i agricoltori locali alla "Modalità Sopravvivenza".', 'de': 'Wie in „Ernährungssouveränität“ besprochen, wird fruchtbares Land zunehmend von Mega-Konzernen beschlagnahmt, was lokale Landwirte in den „Überlebensmodus“ zwingt.', 'es': 'Como se discute en "Soberanía Alimentaria", las tierras fértiles son incautadas cada vez más por megacorporaciones, lo que obliga a los agricultores locales a entrar en "Modo Supervivencia".', 'pt': 'Como discutido em "Soberania Alimentar", terras férteis são cada vez mais apreendidas por megacorporações, forçando os agricultores locais ao "Modo Sobrevivência".', 'ar': 'كما تمت مناقشته في "السيادة الغذائية"، يتم الاستيلاء على الأراضي الخصبة بشكل متزايد من قبل الشركات العملاقة، مما يجبر المزارعين المحليين على الدخول في "وضع البقاء".', 'zh': '正如“粮食主权”中所讨论的，肥沃的土地正日益被巨型公司占领，迫使当地农民进入“生存模式”。'}}
                ]
            },
            {
                'h3': {'en': 'The Wealth Anchor', 'nl': 'Het Rijkdomsanker', 'fr': 'L\'Ancre de la Richesse', 'it': 'L\'Ancora della Ricchezza', 'de': 'Der Vermögensanker', 'es': 'El Ancla de la Riqueza', 'pt': 'A Âncora da Riqueza', 'ar': 'مرساة الثروة', 'zh': '财富之锚'},
                'p': {
                    'en': 'Land ownership is the ultimate "Glass Floor" for the elite. Because the supply of land is fixed, the 1% use it as a permanent anchor for their wealth, ensuring that those without property are forced to pay a lifetime of rent—a modern form of feudalism that prevents true social mobility.',
                    'nl': 'Grondbezit is de ultieme "Glazen Vloer" voor de elite. Omdat het aanbod van land vaststaat, gebruikt de 1% het als een permanent anker voor hun rijkdom, waardoor degenen zonder eigendom gedwongen worden een leven lang huur te betalen—een moderne vorm van feodalisme die echte sociale mobiliteit voorkomt.',
                    'fr': 'La propriété foncière est l\'ultime « Plancher de Verre » pour l\'élite. Parce que l\'offre de terres est fixe, le 1% l\'utilise comme une ancre permanente pour sa richesse, garantissant que ceux qui n\'ont pas de propriété soient forcés de payer un loyer à vie — une forme moderne de féodalisme qui empêche une véritable mobilité sociale.',
                    'it': 'La proprietà della terra è l\'ultimo "Pavimento di Vetro" per l\'élite. Poiché l\'offerta di terra è fissa, l\'1% la usa come ancora permanente per la propria ricchezza, assicurando che chi non possiede proprietà sia costretto a pagare l\'affitto per tutta la vita — una forma moderna di feudalesimo che impedisce la vera mobilità sociale.',
                    'de': 'Landbesitz ist der ultimative „gläserne Boden“ für die Elite. Da das Angebot an Land begrenzt ist, nutzt das oberste 1 % es als dauerhaften Anker für seinen Wohlstand und stellt so sicher, dass diejenigen ohne Eigentum gezwungen sind, lebenslang Miete zu zahlen – eine moderne Form des Feudalismus, die echte soziale Mobilität verhindert.',
                    'es': 'La propiedad de la tierra es el último "Suelo de Cristal" para la élite. Debido a que la oferta de tierra es fija, el 1% la utiliza como un ancla permanente para su riqueza, asegurando que quienes no tienen propiedades se vean obligados a pagar un alquiler de por vida, una forma moderna de feudalismo que impide la verdadera movilidad social.',
                    'pt': 'A propriedade da terra é o definitivo "Chão de Vidro" para a elite. Como a oferta de terra é fixa, o 1% a utiliza como uma âncora permanente para sua riqueza, garantindo que aqueles sem propriedade sejam forçados a pagar aluguel a vida toda — uma forma moderna de feudalismo que impede a verdadeira mobilidade social.',
                    'ar': 'ملكية الأرض هي "الأرضية الزجاجية" القصوى للنخبة. نظرًا لأن عرض الأرض ثابت، فإن نسبة الـ 1٪ تستخدمها كمرساة دائمة لثروتهم، مما يضمن إجبار أولئك الذين ليس لديهم ممتلكات على دفع إيجار مدى الحياة - وهو شكل حديث من الإقطاع يمنع الحراك الاجتماعي الحقيقي.',
                    'zh': '土地所有权是精英阶层最终的“玻璃地板”。由于土地供应是固定的，那1%的人将其作为财富的永久锚点，确保那些没有财产的人被迫支付终生租金——这是一种阻碍真正社会流动性的现代封建主义形式。'
                }
            }
        ],
        'quote': {
            'text': {
                'en': 'The first person who, having enclosed a plot of land, took it into his head to say this is mine and found people simple enough to believe him, was the true founder of civil society... and the origin of inequality.',
                'nl': 'De eerste persoon die, nadat hij een stuk grond had omheind, op het idee kwam om te zeggen: dit is van mij, en mensen vond die eenvoudig genoeg waren om hem te geloven, was de ware grondlegger van de burgerlijke samenleving... en de oorsprong van ongelijkheid.',
                'fr': 'Le premier qui, ayant enclos un terrain, s\'avisa de dire : Ceci est à moi, et trouva des gens assez simples pour le croire, fut le vrai fondateur de la société civile... et l\'origine de l\'inégalité.',
                'it': 'Il primo che, recintato un terreno, pensò di affermare: "Questo è mio", e trovò persone abbastanza semplici da credergli, fu il vero fondatore della società civile... e l\'origine della disuguaglianza.',
                'de': 'Der erste, der ein Stück Land eingezäunt hatte und auf die Idee kam, zu sagen: „Dies gehört mir“, und Leute fand, die einfältig genug waren, ihm zu glauben, war der wahre Gründer der bürgerlichen Gesellschaft ... und der Ursprung der Ungleichheit.',
                'es': 'El primer hombre al que, tras haber cercado un terreno, se le ocurrió decir "Esto es mío" y encontró a gentes lo bastante simples como para creerle, fue el verdadero fundador de la sociedad civil... y el origen de la desigualdad.',
                'pt': 'O primeiro que, tendo cercado um terreno, se lembrou de dizer: "Isto é meu", e encontrou pessoas suficientemente simples para acreditar nele, foi o verdadeiro fundador da sociedade civil... e a origem da desigualdade.',
                'ar': 'أول شخص، بعد أن سيج قطعة أرض، خطرت له فكرة أن يقول هذا لي ووجد أشخاصاً بسطاء بما يكفي لتصديقه، كان المؤسس الحقيقي للمجتمع المدني... وأصل عدم المساواة.',
                'zh': '第一个圈起一块土地并厚颜无耻地说“这是我的”，且发现人们竟然愚蠢到相信他的人，才是文明社会真正的奠基人……也是不平等的起源。'
            },
            'author': {'en': 'Jean-Jacques Rousseau', 'nl': 'Jean-Jacques Rousseau', 'fr': 'Jean-Jacques Rousseau', 'it': 'Jean-Jacques Rousseau', 'de': 'Jean-Jacques Rousseau', 'es': 'Jean-Jacques Rousseau', 'pt': 'Jean-Jacques Rousseau', 'ar': 'جان جاك روسو', 'zh': '让-雅克·卢梭'}
        }
    },
    'submit-ideas.html': {
        'title': {
            'en': 'Submit Ideas - Contributing to the Manifesto',
            'nl': 'Ideeën Indienen - Bijdragen aan het Manifest',
            'fr': 'Soumettre des Idées - Contribuer au Manifeste',
            'it': 'Invia Idee - Contribuire al Manifesto',
            'de': 'Ideen Einreichen - Zum Manifest Beitragen',
            'es': 'Enviar Ideas - Contribuyendo al Manifiesto',
            'pt': 'Enviar Ideias - Contribuindo para o Manifesto',
            'ar': 'تقديم الأفكار - المساهمة في البيان',
            'zh': '提交创意 - 为宣言做贡献'
        },
        'h1': {
            'en': 'Submit Ideas',
            'nl': 'Ideeën Indienen',
            'fr': 'Soumettre des Idées',
            'it': 'Invia Idee',
            'de': 'Ideen Einreichen',
            'es': 'Enviar Ideas',
            'pt': 'Enviar Ideias',
            'ar': 'تقديم الأفكار',
            'zh': '提交创意'
        },
        'h2': {
            'en': 'Shape the Future of the Unfiltered Truth',
            'nl': 'Geef Vorm aan de Toekomst van de Ongefilterde Waarheid',
            'fr': 'Façonner l\'Avenir de la Vérité non Filtrée',
            'it': 'Plasma il Futuro della Verità non Filtrata',
            'de': 'Gestalten Sie die Zukunft der Ungefilterten Wahrheit',
            'es': 'Da Forma al Futuro de la Verdad sin Filtros',
            'pt': 'Moldar o Futuro da Verdade sem Filtros',
            'ar': 'صياغة مستقبل الحقيقة غير المفلترة',
            'zh': '塑造未经过滤的真理的未来'
        },
        'sections': [
            {
                'h3': {'en': 'Collective Intelligence', 'nl': 'Collectieve Intelligentie', 'fr': 'Intelligence Collective', 'it': 'Intelligenza Collettiva', 'de': 'Kollektive Intelligenz', 'es': 'Inteligencia Colectiva', 'pt': 'Inteligência Coletiva', 'ar': 'الذكاء الجماعي', 'zh': '集体智慧'},
                'p': {
                    'en': 'This manifesto is a living resource. To truly counter the 1% system, we must pool our knowledge, statistics, and perspectives. If you have an idea for a new page, a powerful video, or data that needs to be brought to light, we want to hear from you.',
                    'nl': 'Dit manifest is een levende hulpbron. Om het 1%-systeem echt aan te pakken, moeten we onze kennis, statistieken en perspectieven bundelen. Als je een idee hebt voor een nieuwe pagina, een krachtige video of gegevens die aan het licht moeten komen, willen we van je horen.',
                    'fr': 'Ce manifeste est une ressource vivante. Pour contrer véritablement le système du 1%, nous devons mettre en commun nos connaissances, nos statistiques et nos perspectives. Si vous avez une idée de nouvelle page, une vidéo percutante ou des données qui doivent être mises en lumière, nous voulons vous entendre.',
                    'it': 'Questo manifesto è una risorsa viva. Per contrastare veramente il sistema dell\'1%, dobbiamo mettere in comune le nostre conoscenze, statistiche e prospettive. Se hai un\'idea per una nuova pagina, un video potente o dati die devono essere portati alla luce, vogliamo sentirti.',
                    'de': 'Dieses Manifest ist eine lebendige Ressource. Um dem 1%-System wirklich etwas entgegenzusetzen, müssen wir unser Wissen, unsere Statistiken und unsere Perspektiven bündeln. Wenn Sie eine Idee für eine neue Seite, ein aussagekräftiges Video oder Daten haben, die ans Licht gebracht werden müssen, möchten wir von Ihnen hören.',
                    'es': 'Este manifiesto es un recurso vivo. Para contrarrestar verdaderamente el sistema del 1%, debemos agrupar nuestros conocimientos, estadísticas y perspectivas. Si tienes una idea para una nueva página, un video impactante o datos que deban salir a la luz, queremos saber de ti.',
                    'pt': 'Este manifesto é um recurso vivo. Para contrariar verdadeiramente o sistema de 1%, devemos reunir o nosso conhecimento, estatísticas e perspetivas. Se tem uma ideia para uma nova página, um vídeo poderoso ou dados que precisam de vir à luz, queremos ouvi-lo.',
                    'ar': 'هذا البيان هو مورد حي. لمواجهة نظام الـ 1٪ حقاً، يجب أن نجمع معارفنا وإحصاءاتنا ووجهات نظرنا. إذا كانت لديك فكرة لصفحة جديدة، أو مقطع فيديو قوي، أو بيانات يجب الكشف عنها، فنحن نريد أن نسمع منك.',
                    'zh': '本宣言是一个动态资源。为了真正对抗1%的系统，我们必须汇集我们的知识、统计数据和观点。如果您对新页面、一段有力的视频或需要曝光的数据有想法，我们想听听您的意见。'
                }
            },
            {
                'h3': {'en': 'How to Contribute', 'nl': 'Hoe Bij te Dragen', 'fr': 'Comment Contribuer', 'it': 'Come Contribuire', 'de': 'Wie man Beitragen Kann', 'es': 'Cómo Contribuir', 'pt': 'Como Contribuir', 'ar': 'كيفية المساهمة', 'zh': '如何贡献'},
                'list': [
                    {'bold': {'en': 'GitHub Issues:', 'nl': 'GitHub Issues:', 'fr': 'Tickets GitHub (Issues) :', 'it': 'GitHub Issues:', 'de': 'GitHub-Issues:', 'es': 'GitHub Issues:', 'pt': 'GitHub Issues:', 'ar': 'مشكلات GitHub:', 'zh': 'GitHub 问题：'}, 'text': {'en': 'The best way to suggest new content is by opening an issue on our <a href="https://github.com/TimGeyssens/JusticeForGaza">GitHub repository</a>. You can describe your idea or provide links to resources.', 'nl': 'De beste manier om nieuwe inhoud voor te stellen is door een issue te openen op onze <a href="https://github.com/TimGeyssens/JusticeForGaza">GitHub-repository</a>. Je kunt je idee beschrijven of links naar bronnen geven.', 'fr': 'Le meilleur moyen de suggérer du nouveau contenu est d\'ouvrir un ticket sur notre <a href="https://github.com/TimGeyssens/JusticeForGaza">dépôt GitHub</a>. Vous pouvez décrire votre idée ou fournir des liens vers des ressources.', 'it': 'Il modo migliore per suggerire nuovi contenuti è aprire un issue sul nostro <a href="https://github.com/TimGeyssens/JusticeForGaza">repository GitHub</a>. Puoi descrivere la tua idea o fornire link a risorse.', 'de': 'Der beste Weg, neue Inhalte vorzuschlagen, besteht darin, ein Issue in unserem <a href="https://github.com/TimGeyssens/JusticeForGaza">GitHub-Repository</a> zu eröffnen. Sie können Ihre Idee beschreiben oder Links zu Ressourcen bereitstellen.', 'es': 'La mejor manera de sugerir contenido nuevo es abriendo un issue en nuestro <a href="https://github.com/TimGeyssens/JusticeForGaza">repositorio de GitHub</a>. Puedes describir tu idea o proporcionar enlaces a recursos.', 'pt': 'A melhor maneira de sugerir novos conteúdos é abrindo um issue no nosso <a href="https://github.com/TimGeyssens/JusticeForGaza">repositório GitHub</a>. Pode descrever a sua ideia ou fornecer links para recursos.', 'ar': 'أفضل طريقة لاقتراح محتوى جديد هي فتح مشكلة (Issue) على <a href="https://github.com/TimGeyssens/JusticeForGaza">مستودع GitHub</a> الخاص بنا. يمكنك وصف فكرتك أو تقديم روابط للموارد.', 'zh': '提出新内容建议的最佳方式是在我们的<a href="https://github.com/TimGeyssens/JusticeForGaza">GitHub 仓库</a>中提交一个 issue。您可以描述您的想法或提供资源链接。'}},
                    {'bold': {'en': 'Pull Requests:', 'nl': 'Pull Requests:', 'fr': 'Pull Requests :', 'it': 'Pull Requests:', 'de': 'Pull-Requests:', 'es': 'Pull Requests:', 'pt': 'Pull Requests:', 'ar': 'طلبات السحب (Pull Requests):', 'zh': '拉取请求 (Pull Requests)：'}, 'text': {'en': 'If you are technically inclined, you can fork the repository, add your content yourself, and submit a Pull Request. This ensures the site remains decentralized and resilient.', 'nl': 'Als je technisch onderlegd bent, kun je de repository forken, zelf je inhoud toevoegen en een Pull Request indienen. Dit zorgt ervoor dat de site gedecentraliseerd en veerkrachtig blijft.', 'fr': 'Si vous avez des compétences techniques, vous pouvez forker le dépôt, ajouter votre contenu vous-même et soumettre une Pull Request. Cela garantit que le site reste décentralisé et résilient.', 'it': 'Se sei tecnicamente portato, puoi fare il fork del repository, aggiungere i tuoi contenuti tu stesso e inviare una Pull Request. Ciò garantisce che il sito rimanga decentralizzato e resiliente.', 'de': 'Wenn Sie technisch versiert sind, können Sie das Repository forken, Ihre Inhalte selbst hinzufügen und einen Pull-Request einreichen. Dies stellt sicher, dass die Website dezentralisiert und widerstandsfähig bleibt.', 'es': 'Si tienes inclinaciones técnicas, puedes hacer un fork del repositorio, agregar tu contenido tú mismo y enviar un Pull Request. Esto garantiza que el sitio siga siendo descentralizado y resistente.', 'pt': 'Se tiver inclinação técnica, pode fazer um fork do repositório, adicionar o seu conteúdo e submeter um Pull Request. Isso garante que o site permaneça descentralizado e resiliente.', 'ar': 'إذا كنت تميل تقنياً، يمكنك عمل نسخة (Fork) للمستودع، وإضافة محتواك بنفسك، وتقديم طلب سحب (Pull Request). وهذا يضمن بقاء الموقع لا مركزياً ومرناً.', 'zh': '如果您有技术背景，可以 fork 该仓库，自行添加内容，并提交一个 Pull Request。这可以确保网站保持去中心化和韧性。'}},
                    {'bold': {'en': 'Share Resources:', 'nl': 'Deel Bronnen:', 'fr': 'Partager des Ressources :', 'it': 'Condividi Risorse:', 'de': 'Ressourcen Teilen:', 'es': 'Compartir Recursos:', 'pt': 'Partilhar Recursos:', 'ar': 'مشاركة الموارد:', 'zh': '共享资源：'}, 'text': {'en': 'We are looking for data on systemic extraction, personal stories of resistance, and educational videos that bypass corporate media filters.', 'nl': 'We zijn op zoek naar gegevens over systemische extractie, persoonlijke verhalen over verzet en educatieve video\'s die de filters van de bedrijfsmedia omzeilen.', 'fr': 'Nous recherchons des données sur l\'extraction systémique, des récits personnels de résistance et des vidéos éducatives qui contournent les filtres des médias d\'entreprise.', 'it': 'Siamo alla ricerca di dati sull\'estrazione sistemica, storie personali di resistenza e video educativi che aggirano i filtri dei media aziendali.', 'de': 'Wir suchen nach Daten zu systemischer Extraktion, persönlichen Widerstandsgeschichten und Lehrvideos, die die Filter der Konzernmedien umgehen.', 'es': 'Buscamos datos sobre extracción sistémica, historias personales de resistencia y videos educativos que eviten los filtros de los medios corporativos.', 'pt': 'Procuramos dados sobre extração sistémica, histórias pessoais de resistência e vídeos educativos que contornem os filtros dos meios de comunicação corporativos.', 'ar': 'نحن نبحث عن بيانات حول الاستخراج المنهجي، وقصص المقاومة الشخصية، ومقاطع الفيديو التعليمية التي تتجاوز فلاتر وسائل الإعلام المؤسسية.', 'zh': '我们正在寻找有关系统性开采的数据、个人的反抗故事，以及绕过企业媒体过滤的教育视频。'}}
                ]
            }
        ],
        'quote': {
            'text': {
                'en': 'The truth is a puzzle we must solve together. Every piece of data, every shared story, and every new perspective makes the picture clearer.',
                'nl': 'De waarheid is een puzzel die we samen moeten oplossen. Elk stukje data, elk gedeeld verhaal en elk nieuw perspectief maakt het beeld duidelijker.',
                'fr': 'La vérité est un puzzle que nous devons résoudre ensemble. Chaque donnée, chaque histoire partagée et chaque nouvelle perspective rend l\'image plus claire.',
                'it': 'La verità è un puzzle che dobbiamo risolvere insieme. Ogni dato, ogni storia condivisa e ogni nuova prospettiva rende l\'immagine più chiara.',
                'de': 'Die Wahrheit ist ein Puzzle, das wir gemeinsam lösen müssen. Jedes Datenstück, jede geteilte Geschichte und jede neue Perspektive macht das Bild klarer.',
                'es': 'La verdad es un rompecabezas que debemos resolver juntos. Cada dato, cada historia compartida y cada nueva perspectiva hace que la imagen sea más clara.',
                'pt': 'A verdade é um quebra-cabeça que devemos resolver juntos. Cada dado, cada história partilhada e cada nova perspetiva torna a imagem mais clara.',
                'ar': 'الحقيقة هي لغز يجب أن نحله معاً. كل قطعة من البيانات، وكل قصة مشتركة، وكل منظور جديد يجعل الصورة أوضح.',
                'zh': '真理是我们需要共同拼凑的拼图。每一份数据、每一个分享的故事、每一个新的视角都让画面更加清晰。'
            }
        }
    }
}

def generate_new_page(base_file, lang):
    config = content_translations[base_file]
    dir_rtl = ' dir="rtl"' if languages[lang]['dir'] == 'rtl' else ''
    html_lang = 'zh-CN' if lang == 'zh' else lang
    
    html = f'<!DOCTYPE html>\n<html lang="{html_lang}"{dir_rtl}>\n<head>\n'
    html += '    <meta charset="UTF-8">\n'
    html += '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    html += f'    <title>{config["title"][lang]}</title>\n'
    html += '    <link rel="stylesheet" href="style.css">\n'
    html += '    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📢</text></svg>">\n'
    
    if lang == 'ar':
        html += '    <link href="https://fonts.googleapis.com/css2?family=Amiri&family=Inter:wght@300;400;700&display=swap" rel="stylesheet">\n'
        html += '    <style>\n        body { font-family: \'Amiri\', serif, \'Inter\', sans-serif; }\n    </style>\n'
    elif lang == 'zh':
        html += '    <link href="https://fonts.googleapis.com/css2?family=Noto Sans SC:wght@300;400;700&display=swap" rel="stylesheet">\n'
        html += '    <style>\n        body { font-family: \'Noto Sans SC\', sans-serif, \'Inter\'; }\n    </style>\n'
        
    html += '</head>\n<body>\n'
    html += '    <header>\n'
    html += '        <img src="https://s.france24.com/media/display/c5d994bc-8632-11f0-9045-005056bf30b7/w:1280/p:16x9/000-72WT8F3.jpg" alt="Header Image" class="header-image">\n'
    html += f'        <h1>{config["h1"][lang]}</h1>\n'
    html += f'        <h2>{config["h2"][lang]}</h2>\n'
    html += '    </header>\n\n'
    
    active_id = os.path.splitext(base_file)[0]
    nav = generate_nav(active_id, lang)
    
    # Fill language switcher options
    options = ""
    for l_code, l_info in languages.items():
        sel = ' selected' if l_code == lang else ''
        file = get_localized_filename(base_file, l_code)
        options += f'                <option value="{file}"{sel}>{l_info["name"]}</option>\n'
    nav = nav.replace('[[LANG_SWITCHER_OPTIONS]]', options)
    
    html += nav + '\n\n'
    
    html += '    <main>\n'
    for section in config['sections']:
        html += '        <section>\n'
        html += f'            <h3>{section["h3"][lang]}</h3>\n'
        if 'p' in section:
            html += f'            <p>{section["p"][lang]}</p>\n'
        if 'list' in section:
            html += '            <ul>\n'
            for item in section['list']:
                html += f'                <li><strong>{item["bold"][lang]}</strong> {item["text"][lang]}</li>\n'
            html += '            </ul>\n'
        html += '        </section>\n\n'
        
    if 'quote' in config:
        html += '        <blockquote>\n'
        html += f'            "{config["quote"]["text"][lang]}"'
        if 'author' in config['quote']:
            html += f' — {config["quote"]["author"][lang]}'
        html += '\n        </blockquote>\n'
        
    html += '    </main>\n\n'
    html += generate_footer(lang) + '\n'
    html += '</body>\n</html>'
    
    return html

def update_file(file_path):
    # Determine language and base_file
    filename = os.path.basename(file_path)
    lang = 'en'
    base_file = filename
    for l_code, l_info in languages.items():
        if l_code == 'en': continue
        if filename.endswith(l_info['suffix'] + '.html'):
            lang = l_code
            base_file = filename.replace(l_info['suffix'], '')
            break
        if filename == l_code + '.html': # Homepages ar.html, de.html...
            lang = l_code
            base_file = 'index.html'
            break
            
    active_id = os.path.splitext(base_file)[0]
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace nav
    nav_pattern = re.compile(r'<nav.*?>.*?</nav>', re.DOTALL)
    new_nav = generate_nav(active_id, lang)
    options = ""
    for l_code, l_info in languages.items():
        sel = ' selected' if l_code == lang else ''
        file = get_localized_filename(base_file, l_code)
        options += f'                <option value="{file}"{sel}>{l_info["name"]}</option>\n'
    new_nav = new_nav.replace('[[LANG_SWITCHER_OPTIONS]]', options)
    
    if nav_pattern.search(content):
        content = nav_pattern.sub(new_nav, content)
    else:
        # If no nav, maybe it's the index and has a different structure?
        # Just try to insert before main if it exists
        if '<main>' in content:
            content = content.replace('<main>', new_nav + '\n\n    <main>')

    # Replace footer
    footer_pattern = re.compile(r'<footer>.*?</footer>', re.DOTALL)
    new_footer = generate_footer(lang)
    if footer_pattern.search(content):
        content = footer_pattern.sub(new_footer, content)
    else:
        if '</body>' in content:
            content = content.replace('</body>', new_footer + '\n</body>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Execution
if __name__ == '__main__':
    # 1. Generate new pages
    for base in ['land-ownership.html', 'submit-ideas.html']:
        for lang in languages:
            # English versions already exist but we might want to regenerate them to be consistent
            # Or just update them later. For now, create the 8 missing ones.
            file_name = get_localized_filename(base, lang)
            print(f"Generating {file_name}...")
            html = generate_new_page(base, lang)
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(html)

    # 2. Update all files
    all_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in all_files:
        print(f"Updating {file}...")
        update_file(file)

    print("Done!")
