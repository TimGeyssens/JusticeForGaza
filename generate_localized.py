import os

translations = {
    'nl': {
        'lang': 'nl',
        'dir': 'ltr',
        'title': 'Niemand is Illegaal - Migratie en Wereldwijde Onrechtvaardigheid',
        'h1': 'Niemand is Illegaal',
        'h2': 'Grenzen zijn voor Kapitaal, Niet voor Mensen',
        's1_t': 'Het Verlangen naar een Beter Leven',
        's1_p': 'Migratie is zo oud als de mensheid zelf. Het is het fundamentele recht om veiligheid, waardigheid en een betere toekomst te zoeken voor jezelf en je gezin. In het 1%-systeem wordt migratie geframed als een "crisis" of een "bedreiging", maar de echte crisis is de systemische ongelijkheid die mensen in de eerste plaats dwingt hun huis te verlaten.',
        's2_t': 'De Hypocrisie van Grenzen',
        's2_p': 'De wereldwijde extractiemachine vertrouwt op het vrije verkeer van kapitaal, hulpbronnen en wapens over grenzen heen. Maar wanneer mensen—vaak op de vlucht voor dezelfde "Ecocide", "Moderne Slavernij" en "Wapenhandel" gevoed door de 1%—proberen te bewegen, worden ze geconfronteerd met muren, drones en het ontmenselijkende label "illegaal". Grenzen zijn niet ontworpen om mensen te beschermen; ze zijn ontworpen om eigendom te beschermen en de "Kloof tussen Arm en Rijk" in stand te houden.',
        's3_t': 'De Ontmenselijkingsmachine',
        's3_l1_t': 'Angst Produceren',
        's3_l1_b': 'Zoals besproken in de "Informatieoorlog", gebruiken bedrijfsmedia migratie om "Verdeel & Heers"-narratieven te voeden, waardoor de arbeidersklasse wordt afgeleid van de echte schurken door degenen met de minste macht de schuld te geven.',
        's3_l2_t': 'De Criminalisering van Overleven',
        's3_l2_b': 'Een persoon als "illegaal" bestempelen is een biologische en morele onmogelijkheid. Het is een juridische fictie die wordt gebruikt om het "Gevangenis-Industrieel Complex" en de ontzegging van zorg op het niveau van "Medische Apartheid" aan degenen in nood te rechtvaardigen.',
        's3_l3_t': 'Klimaatontheemding',
        's3_l3_b': 'Naarmate de klimaatcrisis versnelt, zullen nog miljoenen mensen tot migratie worden gedwongen. "Klimaatgerechtigheid" is onmogelijk zonder de erkenning dat geen enkel mens illegaal is op een stervende planeet.',
        'quote': '"Geen enkel mens is illegaal. Het enige dat illegaal is, is een systeem dat leven onttrekt aan het Mondiale Zuiden en dan een muur bouwt om de slachtoffers buiten te houden."',
        'footer_republish': 'Over & Herpubliceren',
        'footer_submit': 'Ideeën Indienen',
        'footer_source': 'Broncode',
        'nav_manifesto': 'Manifest',
        'nav_systems': 'Systemen van Macht',
        'nav_extraction': 'Extractie',
        'nav_lens': 'De Menselijke Lens',
        'nav_truth': 'Waarheid & Mythe',
        'nav_solidarity': 'Solidariteit',
        'menu': 'MENU'
    },
    'fr': {
        'lang': 'fr',
        'dir': 'ltr',
        'title': 'Personne n\'est Illégal - Migration et Injustice Mondiale',
        'h1': 'Personne n\'est Illégal',
        'h2': 'Les Frontières sont pour le Capital, Pas pour les Gens',
        's1_t': 'Le Désir d\'une Vie Meilleure',
        's1_p': 'La migration est aussi vieille que l\'humanité elle-même. C\'est le droit fondamental de chercher la sécurité, la dignité et un avenir meilleur pour soi-même et sa famille. Dans le système des 1 %, la migration est présentée comme une "crise" ou une "menace", mais la véritable crise est l\'inégalité systémique qui force les gens à quitter leur foyer en premier lieu.',
        's2_t': 'L\'Hypocrisie des Frontières',
        's2_p': 'La machine d\'extraction mondiale repose sur la libre circulation des capitaux, des ressources et des armes à travers les frontières. Pourtant, lorsque des êtres humains—fuyant souvent l\'"Écocide", l\'"Esclavage Moderne" et le "Commerce des Armes" alimentés par les 1 %—tentent de se déplacer, ils se heurtent à des murs, des drones et à l\'étiquette déshumanisante d\'"illégal". Les frontières ne sont pas conçues pour protéger les gens ; elles sont conçues pour protéger la propriété et maintenir l\'"Écart de Richesse".',
        's3_t': 'La Machine à Déshumaniser',
        's3_l1_t': 'Fabriquer la Peur',
        's3_l1_b': 'Comme nous l\'avons vu dans la "Guerre de l\'Information", les médias d\'entreprise utilisent la migration pour alimenter les récits "Diviser pour Régner", détournant la classe ouvrière des véritables coupables en blâmant ceux qui ont le moins de pouvoir.',
        's3_l2_t': 'La Criminalisation de la Survie',
        's3_l2_b': 'Étiqueter une personne comme "illégale" est une impossibilité biologique et morale. C\'est une fiction juridique utilisée pour justifier le "Complexe Militaro-Industriel" et le déni de soins de niveau "Apartheid Médical" à ceux qui sont dans le besoin.',
        's3_l3_t': 'Déplacement Climatique',
        's3_l3_b': 'À mesure que la crise climatique s\'accélère, des millions d\'autres personnes seront contraintes à la migration. La "Justice Climatique" est impossible sans la reconnaissance qu\'aucun être humain n\'est illégal sur une planète à l\'agonie.',
        'quote': '"Aucun être humain n\'est illégal. La seule chose qui soit illégale est un système qui extrait la vie du Sud Global et construit ensuite un mur pour empêcher les victimes d\'entrer."',
        'footer_republish': 'À propos & République',
        'footer_submit': 'Soumettre des Idées',
        'footer_source': 'Code Source',
        'nav_manifesto': 'Manifeste',
        'nav_systems': 'Systèmes de Pouvoir',
        'nav_extraction': 'Extraction',
        'nav_lens': 'Le Prisme Humain',
        'nav_truth': 'Vérité & Mythe',
        'nav_solidarity': 'Solidarité',
        'menu': 'MENU'
    },
    'it': {
        'lang': 'it',
        'dir': 'ltr',
        'title': 'Nessun Umano è Illegale - Migrazione e Ingiustizia Globale',
        'h1': 'Nessun Umano è Illegale',
        'h2': 'I Confini sono per il Capitale, Non per le Persone',
        's1_t': 'Il Desiderio di una Vita Migliore',
        's1_p': 'La migrazione è vecchia quanto l\'umanità stessa. È il diritto fondamentale di cercare sicurezza, dignità e un futuro migliore per sé e per la propria famiglia. Nel sistema dell\'1%, la migrazione è inquadrata come una "crisi" o una "minaccia", ma la vera crisi è la disuguaglianza sistemica che costringe le persone a lasciare le proprie case in primo luogo.',
        's2_t': 'L\'Ipocrisia dei Confini',
        's2_p': 'La macchina dell\'estrazione globale si basa sul libero flusso di capitali, risorse e armi attraverso i confini. Eppure, quando gli esseri umani—spesso in fuga proprio da "Ecocidio", "Schiavitù Moderna" e "Commercio di Armi" alimentati dall\'1%—cercano di spostarsi, incontrano muri, droni e l\'etichetta deumanizzante di "illegale". I confini non sono progettati per proteggere le persone; sono progettati per proteggere la proprietà e mantenere il "Divario di Ricchezza".',
        's3_t': 'La Macchina della Deumanizzazione',
        's3_l1_t': 'Fabbricare Paura',
        's3_l1_b': 'Come discusso nella "Guerra dell\'Informazione", i media aziendali usano la migrazione per alimentare narrazioni "Divide et Impera", distraendo la classe operaia dai veri cattivi incolpando coloro che hanno meno potere.',
        's3_l2_t': 'La Criminalizzazione della Sopravvivenza',
        's3_l2_b': 'Etichettare una persona come "illegale" è un\'impossibilità biologica e morale. È una finzione giuridica usata per giustificare il complesso "Industriale Carcerario" e la negazione di cure a livello di "Apartheid Medico" a chi ne ha bisogno.',
        's3_l3_t': 'Spostamento Climatico',
        's3_l3_b': 'Con l\'accelerazione della crisi climatica, altri milioni di persone saranno costrette a migrare. La "Giustizia Climatica" è impossibile senza il riconoscimento che nessun essere umano è illegale su un pianeta morente.',
        'quote': '"Nessun essere umano è illegale. L\'unica cosa illegale è un sistema che estrae vita dal Sud del mondo e poi costruisce un muro per tenere fuori le vittime."',
        'footer_republish': 'Informazioni & Ripubblicazione',
        'footer_submit': 'Invia Idee',
        'footer_source': 'Codice Sorgente',
        'nav_manifesto': 'Manifesto',
        'nav_systems': 'Sistemi di Potere',
        'nav_extraction': 'Estrazione',
        'nav_lens': 'La Lente Umana',
        'nav_truth': 'Verità e Mito',
        'nav_solidarity': 'Solidarietà',
        'menu': 'MENU'
    },
    'de': {
        'lang': 'de',
        'dir': 'ltr',
        'title': 'Kein Mensch ist illegal - Migration und globale Ungerechtigkeit',
        'h1': 'Kein Mensch ist illegal',
        'h2': 'Grenzen sind für Kapital, nicht für Menschen',
        's1_t': 'Der Wunsch nach einem besseren Leben',
        's1_p': 'Migration ist so alt wie die Menschheit selbst. Es ist das Grundrecht, Sicherheit, Würde und eine bessere Zukunft für sich und seine Familie zu suchen. Im 1%-System wird Migration als "Krise" oder "Bedrohung" gerahmt, aber die eigentliche Krise ist die systemische Ungleichheit, die Menschen erst dazu zwingt, ihre Heimat zu verlassen.',
        's2_t': 'Die Heuchelei der Grenzen',
        's2_p': 'Die globale Extraktionsmaschine verlässt sich auf den freien Fluss von Kapital, Ressourcen und Waffen über Grenzen hinweg. Doch wenn Menschen—oft auf der Flucht vor genau dem "Ökozid", der "modernen Sklaverei" und dem "Waffenhandel", die von den 1% geschürt werden—versuchen, sich zu bewegen, stoßen sie auf Mauern, Drohnen und das entmenschlichende Etikett "illegal". Grenzen sind nicht dazu da, Menschen zu schützen; sie sind dazu da, Eigentum zu schützen und die "Wohlstandsschere" aufrechtzuerhalten.',
        's3_t': 'Die Entmenschlichungsmaschine',
        's3_l1_t': 'Angst produzieren',
        's3_l1_b': 'Wie im "Informationskrieg" besprochen, nutzen Konzernmedien Migration, um "Divide & Conquer"-Narrative zu befeuern und die Arbeiterklasse von den wahren Schurken abzulenken, indem sie denjenigen die Schuld geben, die am wenigsten Macht haben.',
        's3_l2_t': 'Die Kriminalisierung des Überlebens',
        's3_l2_b': 'Einen Menschen als "illegal" zu bezeichnen, ist eine biologische und moralische Unmöglichkeit. Es ist eine rechtliche Fiktion, die dazu dient, den "Gefängnis-Industrie-Komplex" und die Verweigerung einer Versorgung auf dem Niveau der "medizinischen Apartheid" für Bedürftige zu rechtfertigen.',
        's3_l3_t': 'Klimabedingte Vertreibung',
        's3_l3_b': 'Während sich die Klimakrise beschleunigt, werden Millionen weitere zur Migration gezwungen sein. "Klimagerechtigkeit" ist unmöglich ohne die Anerkennung, dass auf einem sterbenden Planeten kein Mensch illegal ist.',
        'quote': '"Kein Mensch ist illegal. Das einzige, was illegal ist, ist ein System, das dem Globalen Süden das Leben entzieht und dann eine Mauer baut, um die Opfer draußen zu halten."',
        'footer_republish': 'Über & Wiederveröffentlichung',
        'footer_submit': 'Ideen Einreichen',
        'footer_source': 'Quellcode',
        'nav_manifesto': 'Manifest',
        'nav_systems': 'Systeme der Macht',
        'nav_extraction': 'Extraktion',
        'nav_lens': 'Die menschliche Linse',
        'nav_truth': 'Wahrheit & Mythos',
        'nav_solidarity': 'Solidarität',
        'menu': 'MENÜ'
    },
    'es': {
        'lang': 'es',
        'dir': 'ltr',
        'title': 'Nadie es Ilegal - Migración e Injusticia Global',
        'h1': 'Nadie es Ilegal',
        'h2': 'Las Fronteras son para el Capital, No para las Personas',
        's1_t': 'El Deseo de una Vida Mejor',
        's1_p': 'La migración es tan antigua como la propia humanidad. Es el derecho fundamental a buscar seguridad, dignidad y un futuro mejor para uno mismo y su familia. En el sistema del 1%, la migración se enmarca como una "crisis" o una "amenaza", pero la verdadera crisis es la desigualdad sistémica que obliga a las personas a abandonar sus hogares en primer lugar.',
        's2_t': 'La Hipocresía de las Fronteras',
        's2_p': 'La máquina de extracción global depende del libre flujo de capital, recursos y armas a través de las fronteras. Sin embargo, cuando los seres humanos—que a menudo huyen del "Ecocidio", la "Esclavitud Moderna" y el "Comercio de Armas" alimentados por el 1%—intentan moverse, se encuentran con muros, drones y la etiqueta deshumanizadora de "ilegal". Las fronteras no están diseñadas para proteger a las personas; están diseñadas para proteger la propiedad y mantener la "Brecha de Riqueza".',
        's3_t': 'La Máquina de Deshumanización',
        's3_l1_t': 'Fabricar Miedo',
        's3_l1_b': 'Como se discute en la "Guerra de la Información", los medios corporativos utilizan la migración para alimentar las narrativas de "Divide y Vencerás", distrayendo a la clase trabajadora de los verdaderos villanos al culpar a quienes tienen menos poder.',
        's3_l2_t': 'La Criminalización de la Supervivencia',
        's3_l2_b': 'Etiquetar a una persona como "ilegal" es una imposibilidad biológica y moral. Es una ficción legal utilizada para justificar el complejo "Industrial Penitenciario" y la negación de atención de nivel de "Apartheid Médico" a quienes lo necesitan.',
        's3_l3_t': 'Desplazamiento Climático',
        's3_l3_b': 'A medida que se acelera la crisis climática, millones más se verán obligados a migrar. La "Justicia Climática" es imposible sin el reconocimiento de que ningún ser humano es ilegal en un planeta que agoniza.',
        'quote': '"Ningún ser humano es ilegal. Lo único que es ilegal es un sistema que extrae la vida del Sur Global y luego construye un muro para mantener fuera a las víctimas."',
        'footer_republish': 'Acerca de y Republicación',
        'footer_submit': 'Enviar Ideas',
        'footer_source': 'Código Fuente',
        'nav_manifesto': 'Manifiesto',
        'nav_systems': 'Sistemas de Poder',
        'nav_extraction': 'Extracción',
        'nav_lens': 'El Lente Humano',
        'nav_truth': 'Verdad y Mito',
        'nav_solidarity': 'Solidaridad',
        'menu': 'MENÚ'
    },
    'pt': {
        'lang': 'pt',
        'dir': 'ltr',
        'title': 'Ninguém é Ilegal - Migração e Injustiça Global',
        'h1': 'Ninguém é Ilegal',
        'h2': 'Fronteiras são para o Capital, Não para as Pessoas',
        's1_t': 'O Desejo por uma Vida Melhor',
        's1_p': 'A migração é tão antiga quanto a própria humanidade. É o direito fundamental de buscar segurança, dignidade e um futuro melhor para si e para sua família. No sistema do 1%, a migração é enquadrada como uma "crise" ou uma "ameaça", mas a verdadeira crise é a desigualdade sistêmica que força as pessoas a deixarem suas casas em primeiro lugar.',
        's2_t': 'A Hipocrisia das Fronteiras',
        's2_p': 'A máquina de extração global depende do livre fluxo de capital, recursos e armas através das fronteiras. No entanto, quando seres humanos—muitas vezes fugindo do próprio "Ecocídio", "Escravidão Moderna" e "Comércio de Armas" alimentados pelo 1%—tentam se mudar, são recebidos com muros, drones e o rótulo desumanizante de "ilegal". As fronteiras não são projetadas para proteger as pessoas; são projetadas para proteger a propriedade e manter o "Abismo de Riqueza".',
        's3_t': 'A Máquina de Desumanização',
        's3_l1_t': 'Fabricar Medo',
        's3_l1_b': 'Como discutido na "Guerra da Informação", a mídia corporativa usa a migração para alimentar narrativas de "Dividir e Conquistar", distraindo a classe trabalhadora dos verdadeiros vilões, culpando aqueles com menos poder.',
        's3_l2_t': 'A Criminalização da Sobrevivência',
        's3_l2_b': 'Rotular uma pessoa como "ilegal" é uma impossibilidade biológica e moral. É uma ficção jurídica usada para justificar o complexo "Industrial Prisional" e a negação de cuidados de nível de "Apartheid Médico" àqueles que precisam.',
        's3_l3_t': 'Deslocamento Climático',
        's3_l3_b': 'À medida que a crise climática acelera, milhões de pessoas serão forçadas a migrar. A "Justiça Climática" é impossível sem o reconhecimento de que nenhum ser humano é ilegal em um planeta que está morrendo.',
        'quote': '"Nenhum ser humano é ilegal. A única coisa ilegal é um sistema que extrai vida do Sul Global e depois constrói um muro para manter as vítimas fora."',
        'footer_republish': 'Sobre & Republicação',
        'footer_submit': 'Enviar Ideias',
        'footer_source': 'Código Fonte',
        'nav_manifesto': 'Manifesto',
        'nav_systems': 'Sistemas de Poder',
        'nav_extraction': 'Extração',
        'nav_lens': 'A Lente Humana',
        'nav_truth': 'Verdade & Mito',
        'nav_solidarity': 'Solidariedade',
        'menu': 'MENU'
    },
    'ar': {
        'lang': 'ar',
        'dir': 'rtl',
        'title': 'لا يوجد إنسان غير قانوني - الهجرة والظلم العالمي',
        'h1': 'لا يوجد إنسان غير قانوني',
        'h2': 'الحدود لرأس المال، وليس للبشر',
        's1_t': 'الرغبة في حياة أفضل',
        's1_p': 'الهجرة قديمة قدم الإنسانية نفسها. إنها الحق الأساسي في البحث عن الأمان والكرامة ومستقبل أفضل للفرد وعائلته. في نظام الـ 1%، يتم تصوير الهجرة على أنها "أزمة" أو "تهديد"، لكن الأزمة الحقيقية هي عدم المساواة النظامية التي تجبر الناس على ترك منازلهم في المقام الأول.',
        's2_t': 'نفاق الحدود',
        's2_p': 'تعتمد آلة الاستخراج العالمية على التدفق الحر لرأس المال والموارد والأسلحة عبر الحدود. ومع ذلك، عندما يحاول البشر—الذين يفرون غالباً من "الإبادة البيئية" و"العبودية الحديثة" و"تجارة الأسلحة" التي يغذيها الـ 1%—التحرك، فإنهم يواجهون بالجدران والطائرات بدون طيار ووصف "غير قانوني" المهين. لم يتم تصميم الحدود لحماية الناس؛ لقد صُممت لحماية الممتلكات والحفاظ على "فجوة الثروة".',
        's3_t': 'آلة نزع الإنسانية',
        's3_l1_t': 'صناعة الخوف',
        's3_l1_b': 'كما نوقش في "حرب المعلومات"، تستخدم وسائل الإعلام التابعة للشركات الهجرة لتغذية روايات "فرق تسد"، مما يصرف انتباه الطبقة العاملة عن الأشرار الحقيقيين من خلال إلقاء اللوم على أولئك الذين يملكون أقل قدر من السلطة.',
        's3_l2_t': 'تجريم البقاء على قيد الحياة',
        's3_l2_b': 'إن وصف الشخص بأنه "غير قانوني" هو استحالة بيولوجية وأخلاقية. إنه خيال قانوني يُستخدم لتبرير المجمع "الصناعي للسجون" وحرمان المحتاجين من الرعاية التي تصل إلى مستوى "الأبارتهايد الطبي".',
        's3_l3_t': 'النزوح المناخي',
        's3_l3_b': 'مع تسارع أزمة المناخ، سيُجبر ملايين آخرون على الهجرة. "العدالة المناخية" مستحيلة دون الاعتراف بأنه لا يوجد إنسان غير قانوني على كوكب يحتضر.',
        'quote': '"لا يوجد إنسان غير قانوني. الشيء الوحيد غير القانوني هو النظام الذي يستنزف الحياة من الجنوب العالمي ثم يبني جداراً لإبقاء الضحايا في الخارج."',
        'footer_republish': 'حول وإعادة النشر',
        'footer_submit': 'تقديم الأفكار',
        'footer_source': 'كود المصدر',
        'nav_manifesto': 'البيان',
        'nav_systems': 'أنظمة القوة',
        'nav_extraction': 'الاستخراج',
        'nav_lens': 'التجربة الإنسانية',
        'nav_truth': 'معركة الحقيقة',
        'nav_solidarity': 'التضامن',
        'menu': 'القائمة'
    },
    'zh': {
        'lang': 'zh-CN',
        'dir': 'ltr',
        'title': '没有人是非法的 - 移民与全球不公',
        'h1': '没有人是非法的',
        'h2': '边界是为资本而设，而非为人而设',
        's1_t': '对美好生活的向往',
        's1_p': '移民与人类本身一样古老。寻求安全、尊严和为自己及家人创造更美好未来的权利是基本人权。在 1% 的体制下，移民被定性为“危机”或“威胁”，但真正的危机是迫使人们首先离开家园的系统性不平等。',
        's2_t': '边界的虚伪',
        's2_p': '全球榨取机器依赖于资本、资源和武器跨越国界的自由流动。然而，当人类——通常是为了逃离由 1% 助长的“生态灭绝”、“现代奴隶制”和“军火贸易”——试图移动时，他们面临的是围墙、无人机和“非法”这种去人性化的标签。边界的设计不是为了保护人；它们是为了保护财产并维持“贫富差距”。',
        's3_t': '去人性化机器',
        's3_l1_t': '制造恐惧',
        's3_l1_b': '正如“信息战”中所讨论的，企业媒体利用移民来助长“分而治之”的叙事，通过指责权力最小的人来分散工人阶级对真正恶棍的注意力。',
        's3_l2_t': '生存的有罪化',
        's3_l2_b': '将一个人贴上“非法”标签在生物学和道德上都是不可能 circulation 的。这是一种法律虚构，用于为“监狱工业综合体”辩护，并剥夺有需要的人获得“医疗隔离”级别的护理。',
        's3_l3_t': '气候流离失所',
        's3_l3_b': '随着气候危机加速，数以百万计的人将被迫移民。“气候正义”是不可能的，除非承认在一个垂死的星球上，没有人是非法的。',
        'quote': '“没有人是非法的。唯一非法的是一个从全球南方榨取生命，然后筑起围墙将受害者拒之门外的系统。”',
        'footer_republish': '关于和重新发布',
        'footer_submit': '提交创意',
        'footer_source': '源代码',
        'nav_manifesto': '宣言',
        'nav_systems': '权力体系',
        'nav_extraction': '提取',
        'nav_lens': '人类体验',
        'nav_truth': '真理之战',
        'nav_solidarity': '团结',
        'menu': '菜单'
    }
}

template = """<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📢</text></svg>">
    {extra_head}
</head>
<body>
    <header>
        <a href="{index_link}"><img src="https://s.france24.com/media/display/c5d994bc-8632-11f0-9045-005056bf30b7/w:1280/p:16x9/000-72WT8F3.jpg" alt="{h1}" class="header-image"></a>
        <h1>{h1}</h1>
        <h2>{h2}</h2>
    </header>

    <nav class="navbar{nav_rtl}">
        <input type="checkbox" id="nav-toggle" class="nav-toggle">
        <label for="nav-toggle" class="nav-toggle-label">{menu}</label>
        <div class="nav-links">
            <a href="{index_link}" class="nav-item">{nav_manifesto}</a>
            <div class="nav-dropdown active">
                <div class="nav-item active">{nav_systems}</div>
                <div class="dropdown-content">
                    <a href="history{suffix}.html">{nav_history}</a>
                    <a href="genocide-convention{suffix}.html">{nav_genocide}</a>
                    <a href="democracy-illusion{suffix}.html">{nav_democracy}</a>
                    <a href="money-evolution{suffix}.html">{nav_money}</a>
                    <a href="tax-avoidance{suffix}.html">{nav_tax}</a>
                    <a href="wealth-gap{suffix}.html">{nav_wealth}</a>
                    <a href="social-mobility{suffix}.html">{nav_social}</a>
                    <a href="land-ownership{suffix}.html">{nav_land}</a>
                    <a href="no-human-illegal{suffix}.html" class="active">{h1}</a>
                    <a href="arms-trade{suffix}.html">{nav_arms}</a>
                </div>
            </div>
            <div class="nav-dropdown">
                <div class="nav-item">{nav_extraction}</div>
                <div class="dropdown-content">
                    <a href="climate-justice{suffix}.html">{nav_climate}</a>
                    <a href="water-apartheid{suffix}.html">{nav_water}</a>
                    <a href="waste-crisis{suffix}.html">{nav_waste}</a>
                    <a href="food-sovereignty{suffix}.html">{nav_food}</a>
                    <a href="modern-slavery{suffix}.html">{nav_slavery}</a>
                    <a href="medical-apartheid{suffix}.html">{nav_medical}</a>
                    <a href="prison-industrial{suffix}.html">{nav_prison}</a>
                    <a href="symptom-trap{suffix}.html">{nav_symptom}</a>
                    <a href="greenwashing{suffix}.html">{nav_greenwashing}</a>
                </div>
            </div>
            <div class="nav-dropdown">
                <div class="nav-item">{nav_lens}</div>
                <div class="dropdown-content">
                    <a href="neurodiversity{suffix}.html">{nav_neuro}</a>
                    <a href="survival-mode{suffix}.html">{nav_survival}</a>
                    <a href="the-mindset{suffix}.html">{nav_mindset}</a>
                    <a href="education-factory{suffix}.html">{nav_education}</a>
                    <a href="board-games{suffix}.html">{nav_board}</a>
                    <a href="mental-health{suffix}.html">{nav_mental}</a>
                    <a href="greta-thunberg{suffix}.html">{nav_greta}</a>
                    <a href="stanford-experiment{suffix}.html">{nav_stanford}</a>
                </div>
            </div>
            <div class="nav-dropdown">
                <div class="nav-item">{nav_truth}</div>
                <div class="dropdown-content">
                    <a href="philosophy{suffix}.html">{nav_philosophy}</a>
                    <a href="human-nature{suffix}.html">{nav_human_nature}</a>
                    <a href="hero-myth{suffix}.html">{nav_hero}</a>
                    <a href="propaganda{suffix}.html">{nav_propaganda}</a>
                    <a href="tech-surveillance{suffix}.html">{nav_tech}</a>
                    <a href="divide-conquer{suffix}.html">{nav_divide}</a>
                    <a href="bullshit-jobs{suffix}.html">{nav_bullshit}</a>
                    <a href="love-revenge{suffix}.html">{nav_love}</a>
                </div>
            </div>
            <div class="nav-dropdown">
                <div class="nav-item">{nav_solidarity}</div>
                <div class="dropdown-content">
                    <a href="take-action{suffix}.html">{nav_take_action}</a>
                    <a href="radical-community{suffix}.html">{nav_radical}</a>
                    <a href="must-watch{suffix}.html">{nav_watch}</a>
                    <a href="glossary{suffix}.html">{nav_glossary}</a>
                    <a href="references{suffix}.html">{nav_references}</a>
                    <a href="further-reading{suffix}.html">{nav_reading}</a>
                    <a href="submit-ideas{suffix}.html">{nav_submit_nav}</a>
                </div>
            </div>
        </div>
        <div class="lang-switcher">
            <select onchange="window.location.href=this.value">
                <option value="no-human-illegal.html"{sel_en}>English</option>
                <option value="no-human-illegal-nl.html"{sel_nl}>Nederlands</option>
                <option value="no-human-illegal-fr.html"{sel_fr}>Français</option>
                <option value="no-human-illegal-it.html"{sel_it}>Italiano</option>
                <option value="no-human-illegal-de.html"{sel_de}>Deutsch</option>
                <option value="no-human-illegal-es.html"{sel_es}>Español</option>
                <option value="no-human-illegal-pt.html"{sel_pt}>Português</option>
                <option value="no-human-illegal-ar.html"{sel_ar}>العربية</option>
                <option value="no-human-illegal-zh.html"{sel_zh}>中文</option>
            </select>
        </div>
    </nav>

    <main>
        <section>
            <h3>{s1_t}</h3>
            <p>{s1_p}</p>
        </section>

        <section>
            <h3>{s2_t}</h3>
            <p>{s2_p}</p>
        </section>

        <section>
            <h3>{s3_t}</h3>
            <ul>
                <li><strong>{s3_l1_t}:</strong> {s3_l1_b}</li>
                <li><strong>{s3_l2_t}:</strong> {s3_l2_b}</li>
                <li><strong>{s3_l3_t}:</strong> {s3_l3_b}</li>
            </ul>
        </section>

        <blockquote>
            {quote}
        </blockquote>
    </main>

    <footer>
        <p>&copy; 2026 Justice For Gaza Manifesto | <a href="republish{suffix}.html">{footer_republish}</a> | <a href="submit-ideas{suffix}.html">{footer_submit}</a> | <a href="https://github.com/TimGeyssens/JusticeForGaza">{footer_source}</a></p>
    </footer>
</body>
</html>
"""

# Helper to get navigation labels from another file
def get_nav_labels(lang):
    suffix = f"-{lang}" if lang != 'en' else ""
    filename = f"arms-trade{suffix}.html"
    if not os.path.exists(filename):
        # try lang.html
        filename = f"{lang}.html"
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    labels = {}
    # This is a bit hacky but should work for this project's structure
    import re
    
    # Systems of Power
    labels['nav_history'] = re.search(r'href="history'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_genocide'] = re.search(r'href="genocide-convention'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_democracy'] = re.search(r'href="democracy-illusion'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_money'] = re.search(r'href="money-evolution'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_tax'] = re.search(r'href="tax-avoidance'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_wealth'] = re.search(r'href="wealth-gap'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_social'] = re.search(r'href="social-mobility'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_land'] = re.search(r'href="land-ownership'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_arms'] = re.search(r'href="arms-trade'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    
    # Extraction
    labels['nav_climate'] = re.search(r'href="climate-justice'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_water'] = re.search(r'href="water-apartheid'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_waste'] = re.search(r'href="waste-crisis'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_food'] = re.search(r'href="food-sovereignty'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_slavery'] = re.search(r'href="modern-slavery'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_medical'] = re.search(r'href="medical-apartheid'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_prison'] = re.search(r'href="prison-industrial'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_symptom'] = re.search(r'href="symptom-trap'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_greenwashing'] = re.search(r'href="greenwashing'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    
    # Human Lens
    labels['nav_neuro'] = re.search(r'href="neurodiversity'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_survival'] = re.search(r'href="survival-mode'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_mindset'] = re.search(r'href="the-mindset'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_education'] = re.search(r'href="education-factory'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_board'] = re.search(r'href="board-games'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_mental'] = re.search(r'href="mental-health'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_greta'] = re.search(r'href="greta-thunberg'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_stanford'] = re.search(r'href="stanford-experiment'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    
    # Truth & Myth
    labels['nav_philosophy'] = re.search(r'href="philosophy'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_human_nature'] = re.search(r'href="human-nature'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_hero'] = re.search(r'href="hero-myth'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_propaganda'] = re.search(r'href="propaganda'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_tech'] = re.search(r'href="tech-surveillance'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_divide'] = re.search(r'href="divide-conquer'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_bullshit'] = re.search(r'href="bullshit-jobs'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_love'] = re.search(r'href="love-revenge'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    
    # Solidarity
    labels['nav_take_action'] = re.search(r'href="take-action'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_radical'] = re.search(r'href="radical-community'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_watch'] = re.search(r'href="must-watch'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_glossary'] = re.search(r'href="glossary'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_references'] = re.search(r'href="references'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_reading'] = re.search(r'href="further-reading'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)
    labels['nav_submit_nav'] = re.search(r'href="submit-ideas'+suffix+r'\.html"(?:\s+[^>]+)?>([^<]+)</a>', content).group(1)

    return labels

for lang, data in translations.items():
    suffix = f"-{lang}"
    labels = get_nav_labels(lang)
    
    context = data.copy()
    context.update(labels)
    context['suffix'] = suffix
    context['dir_attr'] = f' dir="{data["dir"]}"' if data['dir'] == 'rtl' else ''
    context['nav_rtl'] = ' rtl' if data['dir'] == 'rtl' else ''
    context['index_link'] = f'{lang}.html'
    context['extra_head'] = ''
    if lang == 'ar':
        context['extra_head'] = """<link href="https://fonts.googleapis.com/css2?family=Amiri&family=Inter:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Amiri', serif, 'Inter', sans-serif; }
    </style>"""
    elif lang == 'zh':
        context['extra_head'] = """<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Noto Sans SC', sans-serif, 'Inter'; }
    </style>"""
    
    for l in translations.keys():
        context[f'sel_{l}'] = ' selected' if l == lang else ''
    context['sel_en'] = '' # for non-en languages
    
    filename = f"no-human-illegal-{lang}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template.format(**context))
    print(f"Created {filename}")
