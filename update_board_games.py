import os
import re

languages = {
    'nl': {'label': 'Bordspellen', 'group': 'De Menselijke Lens', 'file_suffix': '-nl', 'manifesto': 'nl.html', 'about': 'republish-nl.html'},
    'fr': {'label': 'Jeux de Société', 'group': 'La Lentille Humaine', 'file_suffix': '-fr', 'manifesto': 'fr.html', 'about': 'republish-fr.html'},
    'it': {'label': 'Giochi da Tavolo', 'group': 'La Lente Umana', 'file_suffix': '-it', 'manifesto': 'it.html', 'about': 'republish-it.html'},
    'de': {'label': 'Brettspiele', 'group': 'Die Menschliche Linse', 'file_suffix': '-de', 'manifesto': 'de.html', 'about': 'republish-de.html'},
    'es': {'label': 'Juegos de Mesa', 'group': 'La Lente Humana', 'file_suffix': '-es', 'manifesto': 'es.html', 'about': 'republish-es.html'},
    'pt': {'label': 'Jogos de Tabuleiro', 'group': 'A Lente Humana', 'file_suffix': '-pt', 'manifesto': 'pt.html', 'about': 'republish-pt.html'},
    'ar': {'label': 'ألعاب الطاولة', 'group': 'المنظور الإنساني', 'file_suffix': '-ar', 'manifesto': 'ar.html', 'about': 'republish-ar.html', 'dir': 'rtl'},
    'zh': {'label': '桌面游戏', 'group': '人类视角', 'file_suffix': '-zh', 'manifesto': 'zh.html', 'about': 'republish-zh.html'},
}

all_langs = languages.copy()
all_langs['en'] = {'label': 'Board Games', 'group': 'The Human Lens', 'file_suffix': '', 'manifesto': 'index.html', 'about': 'republish.html'}

base_file = '/Users/u0174419/manifest/board-games.html'
with open(base_file, 'r', encoding='utf-8') as f:
    base_content = f.read()

translations = {
    'nl': {
        'title': 'Bordspellen & Conditionering - De Spellen Die We Spelen',
        'header_h1': 'Bordspellen & Conditionering',
        'header_h2': 'Hoe we de regels van het 1%-systeem leren',
        'blueprint_h3': 'De Speelse Blauwdruk',
        'blueprint_p': 'Vanaf jonge leeftijd dienen de spelletjes die we met onze kinderen spelen als een subtiele blauwdruk voor hoe de wereld werkt. Voordat ze zelfs maar "Belastingontwijking" of de "Wapenhandel" van de echte wereld begrijpen, oefenen ze de logica van extractie, hiërarchie en competitie op de woonkamervloer.',
        'monopoly_h3': 'Monopoly: De Gestolen Kritiek',
        'monopoly_p': 'Het beroemdste voorbeeld is <strong>Monopoly</strong>. Het is een wrede ironie van de geschiedenis dat het oorspronkelijk door Elizabeth Magie werd gecreëerd als <em>"The Landlord\'s Game"</em> om te <strong>waarschuwen tegen</strong> de gevaren van landroof en monopolies. Tegenwoordig wordt het gebruikt om precies datgene te vieren wat het bedoelde te bekritiseren: het verpletteren van tegenstanders totdat één persoon alles bezit en de rest failliet is.',
        'logic_h3': 'De Logica van Oorlog en Opoffering',
        'chess_li': '<strong>Schaken & Stratego:</strong> Deze spellen leren de "Neuro-typische" logica van hiërarchie en oorlog. In schaken zijn de "Pionnen" de eersten die worden opgeofferd om de elite-stukken te beschermen. Het normaliseert het idee dat some lives inherent waardevoller zijn dan andere, een kernbegrip van het 1%-systeem.',
        'risk_li': '<strong>Risk:</strong> Een spel dat volledig draait om wereldheerschappij en kolonisatie. Het leert dat het pad naar de overwinning is om zoveel mogelijk land te bezetten, wat de logica van de "Geschiedenis van Palestina" en de "Wapenhandel" weerspiegelt.',
        'catan_li': '<strong>Settlers of Catan:</strong> Dit spel versterkt het idee van <strong>Extractie</strong>. De natuur wordt gereduceerd tot "hexen" van grondstoffen (graan, erts, hout) die geconsumeerd moeten worden voor de uitbreiding van nederzettingen, wat de thema\'s van "Ecocide" en de "Afvalcrisis" weerspiegelt.',
        'life_h3': 'Het Script van het Leven',
        'life_p': '<strong>Levensweg</strong> leert kinderen een heel specifiek, lineair pad: ga naar school, zoek een goedbetaalde baan, koop een huis en vergaar bezittingen. Het reduceert het menselijk bestaan tot een reeks financiële transacties en statusmijlpalen, waardoor het model van de "Onderwijsfabriek" en de "Overlevingsstand"-mentaliteit worden versterkt voordat een kind zelfs maar naar de middelbare school gaat.',
        'quote': 'Als je wilt begrijpen waarom volwassenen een systeem van uitbuiting accepteren, kijk dan naar de spelletjes die ze als kind leerden te winnen.',
        'footer': '&copy; 2026 Justice For Gaza Manifest | <a href="republish-nl.html">Over & Herpubliceren</a> | <a href="https://github.com/TimGeyssens/JusticeForGaza">Broncode</a>',
        'nav_menu': 'MENU'
    },
    'fr': {
        'title': 'Jeux de Société & Conditionnement - Les Jeux auxquels nous jouons',
        'header_h1': 'Jeux de Société & Conditionnement',
        'header_h2': 'Comment nous apprenons les règles du système des 1%',
        'blueprint_h3': 'Le Schéma Ludique',
        'blueprint_p': 'Dès le plus jeune âge, les jeux auxquels nous jouons avec nos enfants servent de schéma subtil sur la façon dont le monde fonctionne. Avant même qu\'ils ne comprennent l\'« Évasion Fiscale » ou le « Commerce des Armes » du monde réel, ils pratiquent la logique de l\'extraction, de la hiérarchie et de la compétition sur le sol du salon.',
        'monopoly_h3': 'Monopoly : La Critique Volée',
        'monopoly_p': 'L\'exemple le plus célèbre est le <strong>Monopoly</strong>. C\'est une cruelle ironie de l\'histoire qu\'il ait été initialement créé par Elizabeth Magie sous le nom de <em>"The Landlord\'s Game"</em> (Le Jeu du Propriétaire) pour <strong>mettre en garde</strong> contre les dangers de l\'accaparement des terres et des monopoles. Aujourd\'hui, il est utilisé pour célébrer ce qu\'il était censé critiquer : l\'écrasement des adversaires jusqu\'à ce qu\'une personne possède tout et que les autres soient en faillite.',
        'logic_h3': 'La Logique de la Guerre et du Sacrifice',
        'chess_li': '<strong>Échecs & Stratego :</strong> Ces jeux enseignent la logique « neurotypique » de la hiérarchie et de la guerre. Aux Échecs, les « Pions » sont les premiers à être sacrifiés pour protéger les pièces de l\'élite. Cela normalise l\'idée que certaines vies ont intrinsèquement plus de valeur que d\'autres, un principe fondamental du système des 1%.',
        'risk_li': '<strong>Risk :</strong> Un jeu entièrement centré sur la domination mondiale et la colonisation. Il enseigne que le chemin de la victoire consiste à occuper autant de terres que possible, reflétant la logique de l\'« Histoire de la Palestine » et du « Commerce des Armes ».',
        'catan_li': '<strong>Settlers of Catan :</strong> Ce jeu renforce l\'idée d\'<strong>Extraction</strong>. La nature est réduite à des « hexagones » de ressources (blé, minerai, bois) à consommer pour l\'expansion des colonies, faisant écho aux thèmes de l\'« Écocide » et de la « Crise des Déchets ».',
        'life_h3': 'Le Scénario de la Vie',
        'life_p': '<strong>Destins</strong> enseigne aux enfants un parcours très spécifique et linéaire : aller à l\'école, obtenir un emploi bien rémunéré, acheter une maison et accumuler des actifs. Il réduit l\'existence humaine à une série de transactions financières et d\'étapes de statut, renforçant le modèle de l\'« Usine à Éducation » et la mentalité du « Mode Survie » avant même qu\'un enfant n\'entre au lycée.',
        'quote': '« Si vous voulez comprendre pourquoi les adultes acceptent un système d\'exploitation, regardez les jeux qu\'on leur a appris à gagner quand ils étaient enfants. »',
        'footer': '&copy; 2026 Manifeste Justice Pour Gaza | <a href="republish-fr.html">À Propos & Republication</a> | <a href="https://github.com/TimGeyssens/JusticeForGaza">Code Source</a>',
        'nav_menu': 'MENU'
    },
    'it': {
        'title': 'Giochi da Tavolo e Condizionamento - I giochi a cui giochiamo',
        'header_h1': 'Giochi da Tavolo e Condizionamento',
        'header_h2': 'Come impariamo le regole del sistema dell\'1%',
        'blueprint_h3': 'Il Progetto Ludico',
        'blueprint_p': 'Fin da piccoli, i giochi che facciamo con i nostri bambini servono come un sottile progetto di come funziona il mondo. Prima ancora di comprendere l\'"Evasione Fiscale" o il "Comercio di Armi" del mondo reale, stanno praticando la logica dell\'estrazione, della gerarchia e della competizione sul pavimento del soggiorno.',
        'monopoly_h3': 'Monopoly: La Critica Rubata',
        'monopoly_p': 'L\'esempio più famoso è il <strong>Monopoly</strong>. È una crudele ironia della storia che sia stato originariamente creato da Elizabeth Magie come <em>"The Landlord\'s Game"</em> per <strong>ammonire</strong> contro i pericoli dell\'accaparramento delle terre e dei monopoli. Oggi viene usato per celebrare proprio ciò che intendeva criticare: lo schiacciamento degli avversari finché una persona non possiede tutto e gli altri sono in bancarotta.',
        'logic_h3': 'La Logica della Guerra e del Sacrificio',
        'chess_li': '<strong>Scacchi & Stratego:</strong> Questi giochi insegnano la logica "neurotipica" della gerarchia e della guerra. Negli scacchi, i "Pedoni" sono i primi a essere sacrificati per proteggere i pezzi d\'élite. Normalizza l\'idea che alcune vite siano intrinsecamente più preziose di altre, un principio cardine del sistema dell\'1%.',
        'risk_li': '<strong>Risk:</strong> Un gioco incentrato interamente sulla dominazione globale e sulla colonizzazione. Insegna che la via della vittoria è occupare più terra possibile, rispecchiando la logica della "Storia della Palestina" e del "Commercio di Armi".',
        'catan_li': '<strong>Settlers of Catan:</strong> Questo gioco rafforza l\'idea di <strong>Estrazione</strong>. La natura è ridotta a "esagoni" di risorse (grano, minerale, legno) da consumare per l\'espansione degli insediamenti, riecheggiando i temi dell\'"Ecocidio" e della "Crisi dei Rifiuti".',
        'life_h3': 'Il Copione della Vita',
        'life_p': '<strong>The Game of Life</strong> insegna ai bambini un percorso molto specifico e lineare: andare a scuola, ottenere un lavoro ben pagato, comprare una casa e accumulare beni. Riduce l\'esistenza umana a una serie di transazioni finanziarie e traguardi di status, rafforzando il modello della "Fabbrica dell\'Istruzione" e la mentalità della "Modalità Sopravvivenza" prima ancora che un bambino entri alle superiori.',
        'quote': '"Se vuoi capire perché gli adulti accettano un sistema di sfruttamento, guarda i giochi che è stato insegnato loro a vincere da bambini."',
        'footer': '&copy; 2026 Manifesto Justice For Gaza | <a href="republish-it.html">Informazioni e Ripubblicazione</a> | <a href="https://github.com/TimGeyssens/JusticeForGaza">Codice Sorgente</a>',
        'nav_menu': 'MENU'
    },
    'de': {
        'title': 'Brettspiele & Konditionierung - Die Spiele, die wir spielen',
        'header_h1': 'Brettspiele & Konditionierung',
        'header_h2': 'Wie wir die Regeln des 1%-Systems lernen',
        'blueprint_h3': 'Der spielerische Entwurf',
        'blueprint_p': 'Von klein auf dienen die Spiele, die wir mit unseren Kindern spielen, als subtiler Entwurf dafür, wie die Welt funktioniert. Bevor sie überhaupt die „Steuervermeidung“ oder den „Waffenhandel“ der realen Welt verstehen, üben sie auf dem Wohnzimmerboden die Logik von Extraktion, Hierarchie und Wettbewerb.',
        'monopoly_h3': 'Monopoly: Die gestohlene Kritik',
        'monopoly_p': 'Das bekannteste Beispiel ist <strong>Monopoly</strong>. Es ist eine grausame Ironie der Geschichte, dass es ursprünglich von Elizabeth Magie als <em>„The Landlord\'s Game“</em> geschaffen wurde, um vor den Gefahren von Landraub und Monopolen zu <strong>warnen</strong>. Heute wird es verwendet, um genau das zu feiern, was es eigentlich kritisieren sollte – das Zerschlagen von Gegnern, bis eine Person alles besitzt und der Rest bankrott ist.',
        'logic_h3': 'Die Logik von Krieg und Opfer',
        'chess_li': '<strong>Schach & Stratego:</strong> Diese Spiele lehren die „neurotypische“ Logik von Hierarchie und Krieg. Im Schach sind die „Bauern“ die ersten, die geopfert werden, um die Elitefiguren zu schützen. Es normalisiert die Vorstellung, dass manche Leben von Natur aus wertvoller sind als andere, ein Kerngedanke des 1%-Systems.',
        'risk_li': '<strong>Risiko:</strong> Ein Spiel, das sich ausschließlich um Weltherrschaft und Kolonialisierung dreht. Es lehrt, dass der Weg zum Sieg darin besteht, so viel Land wie möglich zu besetzen, was die Logik der „Geschichte Palästinas“ und des „Waffenhandels“ widerspiegelt.',
        'catan_li': '<strong>Die Siedler von Catan:</strong> Dieses Spiel verstärkt die Idee der <strong>Extraktion</strong>. Die Natur wird auf „Sechsecke“ aus Ressourcen (Weizen, Erz, Holz) reduziert, die für den Ausbau von Siedlungen verbraucht werden, was die Themen „Ökozid“ und „Abfallkrise“ widerspiegelt.',
        'life_h3': 'Das Skript des Lebens',
        'life_p': '<strong>Spiel des Lebens</strong> lehrt Kinder einen sehr spezifischen, linearen Weg: Geh zur Schule, suche dir einen gut bezahlten Job, kaufe ein Haus und häufe Vermögen an. Es reduziert die menschliche Existenz auf eine Abfolge von Finanztransaktionen und Status-Meilensteinen und verstärkt das Modell der „Bildungsfabrik“ und die „Überlebensmodus“-Mentalität, noch bevor ein Kind in die High School kommt.',
        'quote': '„Wenn Sie verstehen wollen, warum Erwachsene ein System der Ausbeutung akzeptieren, schauen Sie sich die Spiele an, die man ihnen als Kinder beibrachte zu gewinnen.“',
        'footer': '&copy; 2026 Justice For Gaza Manifest | <a href="republish-de.html">Über & Wiederveröffentlichung</a> | <a href="https://github.com/TimGeyssens/JusticeForGaza">Quellcode</a>',
        'nav_menu': 'MENU'
    },
    'es': {
        'title': 'Juegos de Mesa y Condicionamiento - Los juegos a los que jugamos',
        'header_h1': 'Juegos de Mesa y Condicionamiento',
        'header_h2': 'Cómo aprendemos las reglas del sistema del 1%',
        'blueprint_h3': 'El Plano Lúdico',
        'blueprint_p': 'Desde una edad temprana, los juegos que jugamos con nuestros hijos sirven como un sutil plano de cómo funciona el mundo. Antes de que comprendan siquiera la "Evasión Fiscal" o el "Comercio de Armas" del mundo real, están practicando la lógica de la extracción, la jerarquía y la competencia en el suelo del salón.',
        'monopoly_h3': 'Monopoly: La Crítica Robada',
        'monopoly_p': 'El ejemplo más famoso es el <strong>Monopoly</strong>. Es una cruel ironía de la historia que fuera creado originalmente por Elizabeth Magie como <em>"The Landlord\'s Game"</em> para <strong>advertir contra</strong> los peligros del acaparamiento de tierras y los monopolios. Hoy en día, se utiliza para celebrar precisamente lo que pretendía criticar: el aplastamiento de los oponentes hasta que una persona lo posee todo y los demás están en bancarrota.',
        'logic_h3': 'La Lógica de la Guerra y el Sacrificio',
        'chess_li': '<strong>Ajedrez & Stratego:</strong> Estos juegos enseñan la lógica "neurotípica" de la jerarquía y la guerra. En el ajedrez, los "Peones" son los primeros en ser sacrificados para proteger a las piezas de la élite. Normaliza la idea de que algunas vidas son inherentemente más valiosas que otras, un principio fundamental del sistema del 1%.',
        'risk_li': '<strong>Risk:</strong> Un juego centrado enteramente en la dominación global y la colonización. Enseña que el camino a la victory es ocupar tanta tierra como sea posible, reflejando la lógica de la "Historia de Palestina" y del "Comercio de Armas".',
        'catan_li': '<strong>Catan:</strong> Este juego refuerza la idea de la <strong>Extracción</strong>. La naturaleza se reduce a "hexágonos" de recursos (trigo, mineral, madera) para ser consumidos en la expansión de los asentamientos, haciendo eco de los temas del "Ecocidio" y la "Crisis de los Residuos".',
        'life_h3': 'El Guion de la Vida',
        'life_p': '<strong>El Juego de la Vida</strong> enseña a los niños un camino muy específico y lineal: ir a la escuela, conseguir un trabajo bien remunerado, comprar una casa y acumular bienes. Reduce la existencia humana a una serie de transacciones financieras e hitos de estatus, reforzando el modelo de la "Fábrica de Educación" y la mentalidad de "Modo Supervivencia" antes de que un niño entre en la escuela secundaria.',
        'quote': '"Si quieres entender por qué los adultos aceptan un sistema de explotación, mira los juegos que se les enseñó a ganar cuando eran niños".',
        'footer': '&copy; 2026 Manifiesto Justice For Gaza | <a href="republish-es.html">Acerca de y Republicación</a> | <a href="https://github.com/TimGeyssens/JusticeForGaza">Código Fuente</a>',
        'nav_menu': 'MENU'
    },
    'pt': {
        'title': 'Jogos de Tabuleiro e Condicionamento - Os jogos que jogamos',
        'header_h1': 'Jogos de Tabuleiro e Condicionamento',
        'header_h2': 'Como aprendemos as regras do sistema do 1%',
        'blueprint_h3': 'O Projeto Lúdico',
        'blueprint_p': 'Desde cedo, os jogos que jogamos com nossos filhos servem como um projeto sutil de como o mundo funciona. Antes mesmo de entenderem a "Evasão Fiscal" ou o "Comercio de Armas" do mundo real, eles estão praticando la lógica da extração, hierarquia e competição no chão da sala.',
        'monopoly_h3': 'Monopoly: A Crítica Roubada',
        'monopoly_p': 'O exemplo mais famoso é o <strong>Monopoly</strong>. É uma ironia cruel da história que tenha sido originalmente criado por Elizabeth Magie como <em>"The Landlord\'s Game"</em> para <strong>alertar contra</strong> os perigos da apropriação de terras e dos monopólios. Hoje, é usado para celebrar exatamente o que pretendia criticar — o esmagamento dos oponentes até que uma pessoa seja dona de tudo e o resto esteja falido.',
        'logic_h3': 'A Lógica da Guerra e do Sacrificio',
        'chess_li': '<strong>Xadrez & Stratego:</strong> Esses jogos ensinam a lógica "neurotípica" de hierarquia e guerra. No Xadrez, os "Peões" são los primeiros a serem sacrificados para proteger as peças de elite. Normaliza a ideia de que algumas vidas são inerentemente mais valiosas do que outras, um princípio fundamental do sistema do 1%.',
        'risk_li': '<strong>Risk:</strong> Um jogo centrado inteiramente na dominação global e na colonização. Ensina que o caminho para a vitória é ocupar o máximo de terra possível, espelhando a lógica da "História da Palestina" e do "Comercio de Armas".',
        'catan_li': '<strong>Catan:</strong> Este jogo reforça a ideia de <strong>Extração</strong>. A natureza é reduzida a "hexágonos" de recursos (trigo, minério, madeira) para serem consumidos pela expansão dos assentamentos, ecoando os temas de "Ecocídio" e "Crise de Resíduos".',
        'life_h3': 'O Roteiro da Vida',
        'life_p': '<strong>O Jogo da Vida</strong> ensina às crianças um caminho muito específico e linear: ir à escola, conseguir um emprego bem remunerado, comprar uma casa e acumular bens. Reduz a existência humana a uma serie de transações financeiras e marcos de status, reforçando o modelo da "Fábrica de Educação" e a mentalidade de "Modo Sobrevivência" antes que uma criança entre no ensino médio.',
        'quote': '"Se você quer entender por que os adultos aceitam um sistema de exploração, olhe para os jogos que eles foram ensinados a ganhar quando crianças."',
        'footer': '&copy; 2026 Manifesto Justice For Gaza | <a href="republish-pt.html">Sobre e Republicação</a> | <a href="https://github.com/TimGeyssens/JusticeForGaza">Código Fonte</a>',
        'nav_menu': 'MENU'
    },
    'ar': {
        'title': 'ألعاب الطاولة والتكييف - الألعاب التي نلعبها',
        'header_h1': 'ألعاب الطاولة والتكييف',
        'header_h2': 'كيف نتعلم قواعد نظام الـ 1%',
        'blueprint_h3': 'المخطط اللعبي',
        'blueprint_p': 'منذ سن مبكرة، تعمل الألعاب التي نلعبها مع أطفالنا كمخطط خفي لكيفية عمل العالم. قبل أن يفهموا حتى "التهرب الضريبي" أو "تجارة الأسلحة" في العالم الحقيقي، فإنهم يمارسون منطق الاستخراج، والتسلسل الهرمي، والمنافسة على أرضية غرفة المعيشة.',
        'monopoly_h3': 'مونوبولي: النقد المسروق',
        'monopoly_p': 'المثال الأكثر شهرة هو <strong>مونوبولي</strong>. من المفارقات القاسية في التاريخ أنها أنشئت في الأصل من قبل إليزابيث ماجي باسم <em>"The Landlord\'s Game"</em> (لعبة المالك) لـ <strong>للتحذير من</strong> مخاطر الاستيلاء على الأراضي والاحتكارات. اليوم، يتم استخدامها للاحتفال بالشيء نفسه الذي كان من المفترض انتقاده - سحق المعارضين حتى يمتلك شخص واحد كل شيء ويفلس الباقون.',
        'logic_h3': 'منطق الحرب والتضحية',
        'chess_li': '<strong>الشطرنج وStratego:</strong> تعلم هذه الألعاب منطق التسلسل الهرمي والحرب "النمطي العصبي". في الشطرنج، "البيادق" هم أول من يتم التضحية بهم لحماية قطع النخبة. إنها تطبع فكرة أن بعض الأرواح ذات قيمة أكبر بطبيعتها من غيرها، وهي عقيدة أساسية لنظام الـ 1%.',
        'risk_li': '<strong>Risk:</strong> لعبة تتمحور بالكامل حول الهيمنة العالمية والاستعمار. تعلم أن الطريق إلى النصر هو احتلال أكبر قدر ممكن من الأرض، مما يعكس منطق "تاريخ فلسطين" و"تجارة الأسلحة".',
        'catan_li': '<strong>Settlers of Catan:</strong> تعزز هذه اللعبة فكرة <strong>الاستخراج</strong>. يتم اختزال الطبيعة في "سداسيات" من الموارد (القمح، المعدن، الخشب) ليتم استهلاكها لتوسيع المستوطنات، مما يردد صدى موضوعات "الإبادة البيئية" و"أزمة النفايات".',
        'life_h3': 'نص الحياة',
        'life_p': 'تعلم <strong>لعبة الحياة</strong> الأطفال مسارًا محددًا للغاية وخطيًا: الذهاب إلى المدرسة، والحصول على وظيفة ذات دخل مرتفع، وشراء منزل، وتجميع الأصول. إنها تختزل الوجود الإنساني في سلسلة من المعاملات المالية ومعالم المكانة، مما يعزز نموذج "مصنع التعليم" وعقلية "وضع البقاء" قبل أن يدخل الطفل المدرسة الثانوية.',
        'quote': '"إذا كنت تريد أن تفهم لماذا يقبل الكبار نظام الاستغلال، فأنظر إلى الألعاب التي تعلموا الفوز بها عندما كانوا أطفالاً."',
        'footer': '&copy; 2026 بيان العدالة لغزة | <a href="republish-ar.html">حول وإعادة النشر</a> | <a href="https://github.com/TimGeyssens/JusticeForGaza">كود المصدر</a>',
        'nav_menu': 'MENU'
    },
    'zh': {
        'title': '桌面游戏与驯化 - 我们玩的游戏',
        'header_h1': '桌面游戏与驯化',
        'header_h2': '我们如何学习 1% 系统的规则',
        'blueprint_h3': '游戏蓝图',
        'blueprint_p': '从很小的时候起，我们和孩子一起玩的游戏就成为了世界运作方式的微妙蓝图。在他们还没理解现实世界中的“税收回避”或“军火贸易”之前，他们就在客厅的地板上练习榨取、等级制度和竞争的逻辑。',
        'monopoly_h3': '大富翁：被盗的批判',
        'monopoly_p': '最著名的例子是 <strong>大富翁 (Monopoly)</strong>。历史的一个残酷讽刺是，它最初是由伊丽莎白·马吉创作的，名为 <em>“地主游戏” (The Landlord\'s Game)</em>，旨在 <strong>警告</strong> 土地掠夺和垄断的危险。今天，它却被用来庆祝它原本打算批判的事物——击垮对手，直到一个人拥有了一切，而其他人全都破产。',
        'logic_h3': '战争与牺牲的逻辑',
        'chess_li': '<strong>国际象棋与 Stratego：</strong> 这些游戏教导了等级制度和战争的“神经典型”逻辑。在国际象棋中，“兵”是第一个被牺牲以保护精英棋子的。它使“某些生命本质上比其他生命更有价值”这一观念正常化，而这正是 1% 系统的核心宗旨。',
        'risk_li': '<strong>Risk：</strong> 一个完全以全球霸权和殖民为中心的游戏。它教导人们，获胜的途径是占领尽可能多的土地，这反映了“巴勒斯坦历史”和“军火贸易”的逻辑。',
        'catan_li': '<strong>卡坦岛：</strong> 这个游戏强化了 <strong>榨取</strong> 的观念。自然被简化为用于定居点扩张的各种资源（小麦、矿石、木材）“六角格”，呼应了“生态灭绝”和“垃圾危机”的主题。',
        'life_h3': '人生脚本',
        'life_p': '<strong>《人生游戏》</strong>教给孩子们一条非常具体、线性的道路：上学、找一份高薪工作、买房并积累资产。它将人类的生存简化为一系列财务交易和地位里程碑，在孩子进入高中之前就强化了“教育工厂”模式和“生存模式”心态。',
        'quote': '“如果你想了解为什么成年人会接受剥削制度，看看他们小时候被教导要赢的游戏。”',
        'footer': '&copy; 2026 正义加沙宣言 | <a href="republish-zh.html">关于和重新发布</a> | <a href="https://github.com/TimGeyssens/JusticeForGaza">源代码</a>',
        'nav_menu': 'MENU'
    }
}

def localize_board_games(lang, data):
    content = base_content
    if lang == 'ar':
        content = content.replace('<html lang="en">', '<html lang="ar" dir="rtl">')
        extra_head = '''    <link href="https://fonts.googleapis.com/css2?family=Amiri&family=Inter:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Amiri', serif, 'Inter', sans-serif; }
    </style>\n'''
        if '</head>' in content:
            content = content.replace('</head>', extra_head + '</head>')
    elif lang == 'zh':
        content = content.replace('<html lang="en">', '<html lang="zh-CN">')
        extra_head = '''    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Noto Sans SC', sans-serif, 'Inter'; }
    </style>\n'''
        if '</head>' in content:
            content = content.replace('</head>', extra_head + '</head>')
    else:
        content = content.replace('<html lang="en">', f'<html lang="{lang}">')

    content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', content)
    content = content.replace('<h1>Board Games & Conditioning</h1>', f'<h1>{data["header_h1"]}</h1>')
    content = content.replace('<h2>How We Learn the Rules of the 1% System</h2>', f'<h2>{data["header_h2"]}</h2>')
    content = content.replace('alt="Board Games and Conditioning"', f'alt="{data["header_h1"]}"')
    content = content.replace('<label for="nav-toggle" class="nav-toggle-label">MENU</label>', f'<label for="nav-toggle" class="nav-toggle-label">{data["nav_menu"]}</label>')

    hist_file = f'/Users/u0174419/manifest/history-{lang}.html'
    with open(hist_file, 'r', encoding='utf-8') as f:
        hist_content = f.read()
    
    nav_links_match = re.search(r'<div class="nav-links">(.*?)</div>\s*<div class="lang-switcher">', hist_content, re.DOTALL)
    if nav_links_match:
        new_nav_inner = nav_links_match.group(1)
        new_nav_inner = new_nav_inner.replace('nav-dropdown active', 'nav-dropdown')
        new_nav_inner = new_nav_inner.replace('nav-item active', 'nav-item')
        new_nav_inner = re.sub(r'class="active"', '', new_nav_inner)
        
        group_name = languages[lang]['group']
        # Fixed regex for group activation
        new_nav_inner = re.sub(r'(<div class="nav-dropdown">)(\s*<div class="nav-item">)(' + re.escape(group_name) + r'</div>)', 
                               r'<div class="nav-dropdown active">\2 active">\3', new_nav_inner)
        
        bg_file = f'board-games-{lang}.html'
        new_nav_inner = new_nav_inner.replace(f'href="{bg_file}"', f'href="{bg_file}" class="active"')
        
        content = re.sub(r'<div class="nav-links">.*?</div>\s*<div class="lang-switcher">', 
                         f'<div class="nav-links">{new_nav_inner}</div>\n        <div class="lang-switcher">', content, flags=re.DOTALL)

    content = content.replace('<h3>The Playful Blueprint</h3>', f'<h3>{data["blueprint_h3"]}</h3>')
    content = content.replace('<p>From a young age, the games we play with our children serve as a subtle blueprint for how the world works. Before they even understand the "Tax Avoidance" or the "Arms Trade" of the real world, they are practicing the logic of extraction, hierarchy, and competition on the living room floor.</p>', f'<p>{data["blueprint_p"]}</p>')
    content = content.replace('<h3>Monopoly: The Stolen Critique</h3>', f'<h3>{data["monopoly_h3"]}</h3>')
    content = content.replace('<p>The most famous example is <strong>Monopoly</strong>. It is a cruel irony of history that it was originally created by Elizabeth Magie as <em>"The Landlord\'s Game"</em> to <strong>warn against</strong> the dangers of land grabbing and monopolies. Today, it is used to celebrate the very thing it meant to critique—the crushing of opponents until one person owns everything and the rest are bankrupt.</p>', f'<p>{data["monopoly_p"]}</p>')
    content = content.replace('<h3>The Logic of War and Sacrifice</h3>', f'<h3>{data["logic_h3"]}</h3>')
    content = content.replace('<li><strong>Chess & Stratego:</strong> These games teach the "Neuro-typical" logic of hierarchy and war. In Chess, the "Pawns" are the first to be sacrificed to protect the elite pieces. It normalizes the idea that some lives are inherently more valuable than others, a core tenet of the 1% system.</li>', f'<li>{data["chess_li"]}</li>')
    content = content.replace('<li><strong>Risk:</strong> A game centered entirely on global domination and colonization. It teaches that the path to victory is to occupy as much land as possible, mirroring the "History of Palestine" and the "Arms Trade" logic.</li>', f'<li>{data["risk_li"]}</li>')
    content = content.replace('<li><strong>Settlers of Catan:</strong> This game reinforces the idea of <strong>Extraction</strong>. Nature is reduced to "hexes" of resources (wheat, ore, wood) to be consumed for settlement expansion, echoing the themes of "Ecocide" and "Waste Crisis."</li>', f'<li>{data["catan_li"]}</li>')
    content = content.replace('<h3>The Script of Life</h3>', f'<h3>{data["life_h3"]}</h3>')
    content = content.replace('<p><strong>The Game of Life</strong> teaches children a very specific, linear path: go to school, get a high-paying job, buy a house, and accumulate assets. It reduces human existence to a series of financial transactions and status milestones, reinforcing the "Education Factory" model and the "Survival Mode" mentality before a child even enters high school.</p>', f'<p>{data["life_p"]}</p>')
    content = content.replace('"If you want to understand why adults accept a system of exploitation, look at the games they were taught to win as children."', f'"{data["quote"]}"')

    content = content.replace('selected', '')
    content = content.replace(f'value="board-games-{lang}.html"', f'value="board-games-{lang}.html" selected')

    content = re.sub(r'<footer>.*?</footer>', f'<footer>\n        <p>{data["footer"]}</p>\n    </footer>', content, flags=re.DOTALL)

    return content

for lang, data in translations.items():
    new_content = localize_board_games(lang, data)
    new_file = f'/Users/u0174419/manifest/board-games-{lang}.html'
    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Created {new_file}")

html_files = [f for f in os.listdir('/Users/u0174419/manifest') if f.endswith('.html')]
for filename in html_files:
    if filename.startswith('board-games'):
        continue
    
    file_path = os.path.join('/Users/u0174419/manifest', filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    file_lang = 'en'
    for lang, info in languages.items():
        if filename.endswith(f'{info["file_suffix"]}.html'):
            file_lang = lang
            break
    
    link_label = all_langs[file_lang]['label']
    link_href = f'board-games{all_langs[file_lang]["file_suffix"]}.html'
    
    phil_labels = ['Filosofie', 'Philosophie', 'Filosofía', 'Filosofia', 'الفلسفة', '哲学', 'Philosophy']
    updated = False
    for pl in phil_labels:
        pattern = re.escape(f'>{pl}</a>')
        if re.search(pattern, content):
            new_link = f'>{pl}</a>\n                    <a href="{link_href}">{link_label}</a>'
            if f'href="{link_href}"' not in content:
                content = content.replace(f'>{pl}</a>', new_link)
                updated = True
            break
    
    if updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done.")
