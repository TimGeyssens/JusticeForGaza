import os

# Translations for Greta Thunberg page content
translations = {
    "en": {
        "lang": "en",
        "title": "Greta Thunberg - The Power of the Unfiltered Mind",
        "subtitle": "The Voice That Refuses to Blink",
        "h1": "Greta Thunberg",
        "h2": "The Voice That Refuses to Blink",
        "sec1_h3": "A Single Voice in Stockholm",
        "sec1_p": "In August 2018, a 15-year-old girl sat outside the Swedish Parliament with a handmade sign: <em>\"Skolstrejk för klimatet\"</em> (School strike for climate). What began as a solitary act of defiance against political inaction on the climate crisis quickly ignited a global movement. Greta Thunberg became the spark for millions of children and adults to demand a future that the 1% system was actively destroying.",
        "sec2_h3": "Neurodiversity as a Superpower",
        "sec2_p": "Greta has often referred to her diagnosis of Asperger's syndrome as her \"superpower.\" While the system views neurodivergent traits as deficits, Greta demonstrated that the ability to see things in black and white—without the social filters that allow \"normal\" adults to accept the unacceptable—is a vital tool for survival. Her \"unfiltered mind\" refused to blink in the face of the raw data of planetary destruction.",
        "sec3_h3": "Evolution of a Revolutionary",
        "sec3_p": "Greta's activism has evolved from a singular focus on carbon emissions to a comprehensive critique of the \"Extraction Machine.\" She has drawn clear lines between climate justice, economic exploitation, and the liberation of the oppressed. Her outspoken solidarity with Palestine and her condemnation of the \"Genocide\" in Gaza have shown that she understands the struggle for the planet is inseparable from the struggle for human rights.",
        "li1": "<strong>The 'Waanzin' (Madness):</strong> The system calls her \"extreme\" or \"unstable\" because she speaks with a clarity that threatens the status quo. In a sick world, the person telling the truth is always labeled as the \"mad\" one.",
        "li2": "<strong>Systemic Linkage:</strong> Greta connects the dots between the \"Arms Trade,\" \"Waste Crisis,\" and the destruction of indigenous lands, exposing the 1% system's holistic failure.",
        "quote": "\"The eyes of all future generations are upon you. And if you choose to fail us, I say: We will never forgive you.\"",
        "footer_text": "&copy; 2026 Justice For Gaza Manifesto | <a href=\"republish.html\">About & Republishing</a> | <a href=\"https://github.com/TimGeyssens/JusticeForGaza\">Source Code</a>",
        "nav_manifesto": "Manifesto",
        "nav_systems": "Systems of Power",
        "nav_extraction": "Extraction",
        "nav_human_lens": "The Human Lens",
        "nav_truth": "Truth & Myth",
        "nav_solidarity": "Solidarity",
        "menu": "MENU"
    },
    "nl": {
        "lang": "nl",
        "title": "Greta Thunberg - De Kracht van de Ongefilterde Geest",
        "subtitle": "De Stem Die Weigert te Knipperen",
        "h1": "Greta Thunberg",
        "h2": "De Stem Die Weigert te Knipperen",
        "sec1_h3": "Een Eenzame Stem in Stockholm",
        "sec1_p": "In augustus 2018 zat een 15-jarig meisje voor het Zweedse parlement met een handgemaakt bord: <em>\"Skolstrejk för klimatet\"</em> (Schoolstaking voor het klimaat). Wat begon als een eenzame daad van verzet tegen politieke inactiviteit op de klimaatcrisis, ontketende al snel een wereldwijde beweging. Greta Thunberg werd de vonk voor miljoenen kinderen en volwassenen om een toekomst te eisen die het 1%-systeem actief aan het vernietigen was.",
        "sec2_h3": "Neurodiversiteit als Superkracht",
        "sec2_p": "Greta heeft vaak naar haar diagnose van het syndroom van Asperger verwezen als haar \"superkracht\". Terwijl het systeem neurodivergente eigenschappen als tekortkomingen ziet, toonde Greta aan dat het vermogen om dingen in zwart-wit te zien — zonder de sociale filters die \"normale\" volwassenen toelaten het onaanvaardbare te accepteren — een essentieel hulpmiddel is om te overleven. Haar \"ongefilterde geest\" weigerde te knipperen in het zicht van de harde gegevens van de planetaire vernietiging.",
        "sec3_h3": "Evolutie van een Revolutionair",
        "sec3_p": "Greta's activisme is geëvolueerd van een eenzijdige focus op koolstofemissies naar een uitgebreide kritiek op de \"Extractiemachine\". Ze heeft duidelijke lijnen getrokken tussen klimaatgerechtigheid, economische uitbuiting en de bevrijding van de onderdrukten. Haar uitgesproken solidariteit met Palestina en haar veroordeling van de \"Genocide\" in Gaza hebben aangetoond dat ze begrijpt dat de strijd voor de planeet onlosmakelijk verbonden is met de strijd voor mensenrechten.",
        "li1": "<strong>De 'Waanzin':</strong> Het systeem noemt haar \"extreem\" of \"onstabiel\" omdat ze spreekt met een helderheid die de status quo bedreigt. In een zieke wereld wordt de persoon die de waarheid spreekt altijd als de \"gekke\" bestempeld.",
        "li2": "<strong>Systemische Koppeling:</strong> Greta legt de verbanden tussen de \"Wapenhandel\", \"Afvalcrisis\" en de vernietiging van inheemse gebieden, waarmee ze het holistische falen van het 1%-systeem blootlegt.",
        "quote": "\"De ogen van alle toekomstige generaties zijn op jullie gericht. En als jullie ervoor kiezen om ons in de steek te laten, zeg ik: we zullen het jullie nooit vergeven.\"",
        "footer_text": "&copy; 2026 Manifest van de Ongefilterde Waarheid | <a href=\"republish-nl.html\">Over & Herpubliceren</a> | <a href=\"https://github.com/TimGeyssens/JusticeForGaza\">Broncode</a>",
        "nav_manifesto": "Manifest",
        "nav_systems": "Machtssystemen",
        "nav_extraction": "Extractie",
        "nav_human_lens": "De Menselijke Lens",
        "nav_truth": "Waarheid & Mythe",
        "nav_solidarity": "Solidariteit",
        "menu": "MENU"
    },
    "fr": {
        "lang": "fr",
        "title": "Greta Thunberg - Le Pouvoir de l'Esprit Sans Filtre",
        "subtitle": "La Voix Qui Refuse de Ciller",
        "h1": "Greta Thunberg",
        "h2": "La Voix Qui Refuse de Ciller",
        "sec1_h3": "Une Voix Solitaire à Stockholm",
        "sec1_p": "En août 2018, une jeune fille de 15 ans s'est assise devant le Parlement suédois avec une pancarte faite à la main : <em>\"Skolstrejk för klimatet\"</em> (Grève scolaire pour le climat). Ce qui a commencé comme un acte solitaire de défi contre l'inaction politique face à la crise climatique a rapidement déclenché un mouvement mondial. Greta Thunberg est devenue l'étincelle pour des millions d'enfants et d'adultes exigeant un avenir que le système des 1 % détruisait activement.",
        "sec2_h3": "La Neurodiversité comme Superpouvoir",
        "sec2_p": "Greta a souvent qualifié son diagnostic de syndrome d'Asperger de \"superpouvoir\". Alors que le système considère les traits neurodivergents comme des déficits, Greta a démontré que la capacité de voir les choses en noir et blanc — sans les filtres sociaux qui permettent aux adultes \"normaux\" d'accepter l'inacceptable — est un outil de survie vital. Son \"esprit sans filtre\" a refusé de ciller face aux données brutes de la destruction planétaire.",
        "sec3_h3": "Évolution d'une Révolutionnaire",
        "sec3_p": "L'activisme de Greta a évolué d'une focalisation unique sur les émissions de carbone vers une critique complète de la \"Machine d'Extraction\". Elle a tracé des lignes claires entre la justice climatique, l'exploitation économique et la libération des opprimés. Sa solidarité affichée avec la Palestine et sa condamnation du \"Génocide\" à Gaza ont montré qu'elle comprend que la lutte pour la planète est inséparable de la lutte pour les droits de l'homme.",
        "li1": "<strong>La 'Folie' :</strong> Le système la qualifie d'\"extrême\" ou d'\"instable\" parce qu'elle parle avec une clarté qui menace le statu quo. Dans un monde malade, celui qui dit la vérité est toujours étiqueté comme le \"fou\".",
        "li2": "<strong>Lien Systémique :</strong> Greta relie les points entre le \"Commerce des Armes\", la \"Crise des Déchets\" et la destruction des terres indigènes, exposant l'échec holistique du système des 1 %.",
        "quote": "\"Les yeux de toutes les générations futures sont tournés vers vous. Et si vous choisissez de nous faire défaut, je vous le dis : nous ne vous pardonnerons jamais.\"",
        "footer_text": "&copy; 2026 Manifeste de la Vérité Sans Filtre | <a href=\"republish-fr.html\">À Propos & Republication</a> | <a href=\"https://github.com/TimGeyssens/JusticeForGaza\">Code Source</a>",
        "nav_manifesto": "Manifeste",
        "nav_systems": "Systèmes de Pouvoir",
        "nav_extraction": "Extraction",
        "nav_human_lens": "La Lentille Humaine",
        "nav_truth": "Vérité & Mythe",
        "nav_solidarity": "Solidarité",
        "menu": "MENU"
    },
    "it": {
        "lang": "it",
        "title": "Greta Thunberg - Il Potere della Mente Senza Filtri",
        "subtitle": "La Voce Che Rifiuta di Battere Ciglio",
        "h1": "Greta Thunberg",
        "h2": "La Voce Che Rifiuta di Battere Ciglio",
        "sec1_h3": "Una Voce Solitaria a Stoccolma",
        "sec1_p": "Nell'agosto 2018, una ragazza di 15 anni si sedette fuori dal Parlamento svedese con un cartello fatto a mano: <em>\"Skolstrejk för klimatet\"</em> (Sciopero scolastico per il clima). Quello che era iniziato come un atto solitario di sfida contro l'inazione politica sulla crisi climatica ha rapidamente acceso un movimento globale. Greta Thunberg è diventata la scintilla per milioni di bambini e adulti che chiedevano un futuro che il sistema dell'1% stava attivamente distruggendo.",
        "sec2_h3": "La Neurodiversità come Superpotere",
        "sec2_p": "Greta si è spesso riferita alla sua diagnosi di sindrome di Asperger come al suo \"superpotere\". Mentre il sistema vede i tratti neurodivergenti come deficit, Greta ha dimostrato che la capacità di vedere le cose in bianco e nero — senza i filtri sociali che permettono agli adulti \"normali\" di accettare l'inaccettabile — è uno strumento vitale per la sopravvivenza. La sua \"mente senza filtri\" ha rifiutato di battere ciglio di fronte ai dati crudi della distruzione planetaria.",
        "sec3_h3": "Evoluzione di una Rivoluzionaria",
        "sec3_p": "L'attivismo di Greta si è evoluto da una focalizzazione singolare sulle emissioni di carbonio a una critica completa della \"Macchina da Estrazione\". Ha tracciato linee chiare tra giustizia climatica, sfruttamento economico e liberazione degli oppressi. La sua esplicita solidarietà con la Palestina e la sua condmana del \"Genocidio\" a Gaza hanno dimostrato che comprende che la lotta per il pianeta è inseparabile dalla lotta per i diritti umani.",
        "li1": "<strong>La 'Follia':</strong> Il sistema la definisce \"estrema\" o \"instabile\" perché parla con una chiarezza che minaccia lo status quo. In un mondo malato, la persona che dice la verità viene sempre etichettata come quella \"pazza\".",
        "li2": "<strong>Collegamento Sistemico:</strong> Greta collega i punti tra il \"Commercio di Armi\", la \"Crisi dei Rifiuti\" e la distruzione delle terre indigene, esponendo il fallimento olistico del sistema dell'1%.",
        "quote": "\"Gli occhi di tutte le generazioni future sono su di voi. E se sceglierete di fallire, io dico: non vi perdoneremo mai.\"",
        "footer_text": "&copy; 2026 Manifesto della Verità Senza Filtri | <a href=\"republish-it.html\">Informazioni e Ripubblicazione</a> | <a href=\"https://github.com/TimGeyssens/JusticeForGaza\">Codice Sorgente</a>",
        "nav_manifesto": "Manifesto",
        "nav_systems": "Sistemi di Potere",
        "nav_extraction": "Estrazione",
        "nav_human_lens": "La Lente Umana",
        "nav_truth": "Verità e Mito",
        "nav_solidarity": "Solidarietà",
        "menu": "MENU"
    },
    "de": {
        "lang": "de",
        "title": "Greta Thunberg - Die Kraft des ungefilterten Geistes",
        "subtitle": "Die Stimme, die sich weigert zu blinzeln",
        "h1": "Greta Thunberg",
        "h2": "Die Stimme, die sich weigert zu blinzeln",
        "sec1_h3": "Eine einzelne Stimme in Stockholm",
        "sec1_p": "Im August 2018 saß ein 15-jähriges Mädchen vor dem schwedischen Parlament mit einem handgemachten Schild: <em>\"Skolstrejk för klimatet\"</em> (Schulstreik für das Klima). Was als einsame Tat des Trotzes gegen die politische Untätigkeit in der Klimakrise begann, entfachte schnell eine globale Bewegung. Greta Thunberg wurde zum Funken für Millionen von Kindern und Erwachsenen, die eine Zukunft forderten, die das 1%-System aktiv zerstörte.",
        "sec2_h3": "Neurodiversität als Superkraft",
        "sec2_p": "Greta hat ihre Diagnose des Asperger-Syndroms oft als ihre \"Superkraft\" bezeichnet. Während das System neurodivergente Merkmale als Defizite betrachtet, hat Greta bewiesen, dass die Fähigkeit, die Dinge in Schwarz und Weiß zu sehen — ohne die sozialen Filter, die es \"normalen\" Erwachsenen ermöglichen, das Unannehmbare zu akzeptieren — ein lebenswichtiges Instrument zum Überleben ist. Ihr \"ungefilterter Geist\" weigerte sich, angesichts der nackten Daten der planetaren Zerstörung zu blinzeln.",
        "sec3_h3": "Evolution einer Revolutionärin",
        "sec3_p": "Gretas Aktivismus hat sich von einer einseitigen Konzentration auf Kohlenstoffemissionen zu einer umfassenden Kritik an der \"Extraktionsmaschine\" entwickelt. Sie hat klare Linien zwischen Klimagerechtigkeit, wirtschaftlicher Ausbeutung und der Befreiung der Unterdrückten gezogen. Ihre ausgesprochene Solidarität mit Palästina und ihre Verurteilung des \"Völkermords\" im Gazastreifen haben gezeigt, dass sie versteht, dass der Kampf für den Planeten untrennbar mit dem Kampf für die Menschenrechte verbunden ist.",
        "li1": "<strong>Der 'Wahnsinn':</strong> Das System nennt sie \"extrem\" oder \"instabil\", weil sie mit einer Klarheit spricht, die den Status quo bedroht. In einer kranken Welt wird die Person, die die Wahrheit sagt, immer als die \"Verrückte\" abgestempelt.",
        "li2": "<strong>Systemische Verknüpfung:</strong> Greta verbindet die Punkte zwischen dem \"Waffenhandel\", der \"Abfallkrise\" und der Zerstörung indigener Gebiete und deckt damit das ganzheitliche Versagen des 1%-Systems auf.",
        "quote": "\"Die Augen aller zukünftigen Generationen sind auf euch gerichtet. Und wenn ihr euch entscheidet, uns im Stich zu lassen, sage ich euch: Wir werden euch niemals verzeihen.\"",
        "footer_text": "&copy; 2026 Manifest der Ungefilterten Wahrheit | <a href=\"republish-de.html\">Über & Wiederveröffentlichung</a> | <a href=\"https://github.com/TimGeyssens/JusticeForGaza\">Quellcode</a>",
        "nav_manifesto": "Manifest",
        "nav_systems": "Machtssysteme",
        "nav_extraction": "Extraktion",
        "nav_human_lens": "Die menschliche Linse",
        "nav_truth": "Wahrheit & Mythos",
        "nav_solidarity": "Solidarität",
        "menu": "MENÜ"
    },
    "es": {
        "lang": "es",
        "title": "Greta Thunberg - El Poder de la Mente Sin Filtros",
        "subtitle": "La Voz Que Se Niega a Parpadear",
        "h1": "Greta Thunberg",
        "h2": "La Voz Que Se Niega a Parpadear",
        "sec1_h3": "Una Sola Voz en Estocolmo",
        "sec1_p": "En agosto de 2018, una niña de 15 años se sentó frente al Parlamento sueco con un cartel hecho a mano: <em>\"Skolstrejk för klimatet\"</em> (Huelga escolar por el clima). Lo que comenzó como un acto solitario de desafío contra la inacción política ante la crisis climática, pronto encendió un movimiento global. Greta Thunberg se convirtió en la chispa para millones de niños y adultos que exigían un futuro que el sistema del 1% estaba destruyendo activamente.",
        "sec2_h3": "La Neurodiversidad como Superpoder",
        "sec2_p": "Greta se ha referido a menudo a su diagnóstico de síndrome de Asperger como su \"superpoder\". Mientras que el sistema ve los rasgos neurodivergentes como déficits, Greta demostró que la capacidad de ver las cosas en blanco y negro —sin los filtros sociales que permiten a los adultos \"normales\" aceptar lo inaceptable— es una herramienta vital para la supervivencia. Su \"mente sin filtros\" se negó a parpadear ante los datos crudos de la destrucción planetaria.",
        "sec3_h3": "Evolución de una Revolucionaria",
        "sec3_p": "El activismo de Greta ha evolucionado de un enfoque singular en las emisiones de carbono a una crítica integral de la \"Máquina de Extracción\". Ha trazado líneas claras entre la justicia climática, la explotación económica y la liberación de los oprimidos. Su solidaridad declarada con Palestina y su condena del \"Genocidio\" en Gaza han demostrado que comprende que la lucha por el planeta es inseparable de la lucha por los derechos humanos.",
        "li1": "<strong>La 'Locura':</strong> El sistema la califica de \"extrema\" o \"inestable\" porque habla con una claridad que amenaza el statu quo. En un mundo enfermo, la persona que dice la verdad siempre es etiquetada como la \"loca\".",
        "li2": "<strong>Vínculo Sistémico:</strong> Greta conecta los puntos entre el \"Comercio de Armas\", la \"Crisis de Residuos\" y la destrucción de tierras indígenas, exponiendo el fracaso holístico del sistema del 1%.",
        "quote": "\"Los ojos de todas las generaciones futuras están puestos en vosotros. Y si elegís fallarnos, os digo: nunca os lo perdonaremos.\"",
        "footer_text": "&copy; 2026 Manifiesto de la Verdad Sin Filtros | <a href=\"republish-es.html\">Acerca de y Republicación</a> | <a href=\"https://github.com/TimGeyssens/JusticeForGaza\">Código Fuente</a>",
        "nav_manifesto": "Manifiesto",
        "nav_systems": "Sistemas de Poder",
        "nav_extraction": "Extracción",
        "nav_human_lens": "La Lente Humana",
        "nav_truth": "Verdad y Mito",
        "nav_solidarity": "Solidaridad",
        "menu": "MENÚ"
    },
    "pt": {
        "lang": "pt",
        "title": "Greta Thunberg - O Poder da Mente Sem Filtros",
        "subtitle": "A Voz Que Se Recusa a Piscar",
        "h1": "Greta Thunberg",
        "h2": "A Voz Que Se Recusa a Piscar",
        "sec1_h3": "Uma Voz Solitária em Estocolmo",
        "sec1_p": "Em agosto de 2018, uma menina de 15 anos sentou-se em frente ao Parlamento sueco com um cartaz feito à mão: <em>\"Skolstrejk för klimatet\"</em> (Greve escolar pelo clima). O que começou como um ato solitário de desafio contra a inação política perante a crise climática, rapidamente acendeu um movimento global. Greta Thunberg tornou-se a faísca para milhões de crianças e adultos que exigiam um futuro que o sistema do 1% estava ativamente a destruir.",
        "sec2_h3": "Neurodiversidade como Superpoder",
        "sec2_p": "Greta referiu-se frequentemente ao seu diagnóstico de síndrome de Asperger como o seu \"superpoder\". Enquanto o sistema vê os traços neurodivergentes como déficits, Greta demonstrou que a capacidade de ver as coisas em preto e branco — sem os filtros sociais que permitem aos adultos \"normais\" aceitar o inaceitável — é uma ferramenta vital para the sobrevivência. A sua \"mente sem filtros\" recusou-se a piscar perante os dados crus da destruição planetária.",
        "sec3_h3": "Evolução de uma Revolucionária",
        "sec3_p": "O ativismo de Greta evoluiu de um foco singular nas emissões de carbono para uma crítica abrangente da \"Máquina de Extração\". Ela traçou linhas claras entre a justiça climática, a exploração económica e a libertação dos oprimidos. A sua solidariedade declarada com a Palestina e a sua condenação do \"Genocídio\" em Gaza demonstraram que ela compreende que a luta pelo planeta é inseparável da luta pelos direitos humanos.",
        "li1": "<strong>A 'Loucura':</strong> O sistema chama-lhe \"extrema\" ou \"instável\" porque fala com uma clareza que ameaça o status quo. Num mundo doente, a pessoa que diz a verdade é sempre rotulada como a \"louca\".",
        "li2": "<strong>Ligação Sistémica:</strong> Greta liga os pontos entre o \"Comércio de Armas\", a \"Crise de Resíduos\" e a destruição de terras indígenas, expondo a falha holística do sistema do 1%.",
        "quote": "\"Os olhos de todas as gerações futuras estão voltados para vocês. E se optarem por falhar connosco, eu digo: nunca vos perdoaremos.\"",
        "footer_text": "&copy; 2026 Manifesto da Verdade Sem Filtros | <a href=\"republish-pt.html\">Sobre e Republicação</a> | <a href=\"https://github.com/TimGeyssens/JusticeForGaza\">Código Fonte</a>",
        "nav_manifesto": "Manifesto",
        "nav_systems": "Sistemas de Poder",
        "nav_extraction": "Extração",
        "nav_human_lens": "A Lente Humana",
        "nav_truth": "Verdade e Mito",
        "nav_solidarity": "Solidariedade",
        "menu": "MENU"
    },
    "ar": {
        "lang": "ar",
        "title": "غريتا تونبرغ - قوة العقل غير المصفى",
        "subtitle": "الصوت الذي يرفض أن يغمض له جفن",
        "h1": "غريتا تونبرغ",
        "h2": "الصوت الذي يرفض أن يغمض له جفن",
        "sec1_h3": "صوت واحد في ستوكهولم",
        "sec1_p": "في أغسطس 2018، جلست فتاة تبلغ من العمر 15 عاماً خارج البرلمان السويدي مع لافتة مصنوعة يدوياً: <em>\"Skolstrejk för klimatet\"</em> (إضراب مدرسي من أجل المناخ). ما بدأ كفعل فردي من التحدي ضد التقاعس السياسي بشأن أزمة المناخ سرعان ما أشعل حركة عالمية. أصبحت غريتا تونبرغ الشرارة لملايين الأطفال والبالغين للمطالبة بمستقبل كان نظام الـ 1% يدمره بنشاط.",
        "sec2_h3": "التنوع العصبي كقوة خارقة",
        "sec2_p": "غالباً ما أشارت غريتا إلى تشخيصها بمتلازمة أسبرجر على أنها \"قوتها الخارقة\". وبينما يرى النظام السمات العصبية المتنوعة على أنها أوجه قصور، أثبتت غريتا أن القدرة على رؤية الأشياء بالأبيض والأسود — بدون الفلاتر الاجتماعية التي تسمح للبالغين \"الطبيعيين\" بقبول ما لا يمكن قبوله — هي أداة حيوية للبقاء. رفض \"عقلها غير المصفى\" أن يغمض له جفن في مواجهة البيانات الخام للدمار الكوكبي.",
        "sec3_h3": "تطور ثورية",
        "sec3_p": "تطور نشاط غريتا من التركيز الفردي على انبعاثات الكربون إلى نقد شامل لـ \"آلة الاستخراج\". لقد رسمت خطوطاً واضحة بين العدالة المناخية، والاستغلال الاقتصادي، وتحرير المظلومين. أظهر تضامنها الصريح مع فلسطين وإدانتها لـ \"الإبادة الجماعية\" في غزة أنها تدرك أن النضال من أجل الكوكب لا ينفصل عن النضال من أجل حقوق الإنسان.",
        "li1": "<strong>'الجنون':</strong> يصفها النظام بـ \"المتطرفة\" أو \"غير المستقرة\" لأنها تتحدث بوضوح يهدد الوضع الراهن. في عالم مريض، الشخص الذي يقول الحقيقة دائماً ما يوصف بأنه \"المجنون\".",
        "li2": "<strong>الارتباط النظامي:</strong> تربط غريتا النقاط بين \"تجارة الأسلحة\" و \"أزمة النفايات\" وتدمير أراضي السكان الأصليين، مما يكشف عن الفشل الكلي لنظام الـ 1%.",
        "quote": "\"عيون جميع الأجيال القادمة عليكم. وإذا اخترتم أن تخذلونا، فأنا أقول: لن نسامحكم أبداً.\"",
        "footer_text": "&copy; 2026 بيان الحقيقة غير المفلترة | <a href=\"republish-ar.html\">حول وإعادة النشر</a> | <a href=\"https://github.com/TimGeyssens/JusticeForGaza\">كود المصدر</a>",
        "nav_manifesto": "البيان",
        "nav_systems": "أنظمة القوة",
        "nav_extraction": "الاستخراج",
        "nav_human_lens": "العدسة البشرية",
        "nav_truth": "الحقيقة والأسطورة",
        "nav_solidarity": "التضامن",
        "menu": "القائمة"
    },
    "zh": {
        "lang": "zh-CN",
        "title": "格蕾塔·通贝里 - 未经过滤的心灵力量",
        "subtitle": "拒绝眨眼的呼声",
        "h1": "格蕾塔·通贝里",
        "h2": "拒绝眨眼的呼声",
        "sec1_h3": "斯德哥尔摩的一个人的声音",
        "sec1_p": "2018年8月，一名15岁的少女坐在瑞典议会外，手里拿着一块手工制作的牌子：<em>“Skolstrejk för klimatet”</em>（为气候罢课）。这场最初针对政治在气候危机上无所作为的孤独反抗，很快引发了一场全球运动。格蕾塔·通贝里成为了数百万儿童和成年人的火花，他们要求一个那 1% 的系统正在积极摧毁的未来。",
        "sec2_h3": "神经多样性作为超能力",
        "sec2_p": "格蕾塔经常将她被诊断出的阿斯伯格综合症称为她的“超能力”。当系统将神经多样性特征视为缺陷时，格蕾塔证明了非黑即白地看待事物的能力——没有那些让“正常”成年人接受不可接受之事的社会过滤器——是生存的重要工具。面对行星毁灭的原始数据，她那“未经过滤的心灵”拒绝眨眼。",
        "sec3_h3": "一个革命者的进化",
        "sec3_p": "格蕾塔的行动主义已经从单一关注碳排放演变为对“榨取机器”的全面批判。她在气候正义、经济剥削和被压迫者的解放之间划出了清晰的界限。她对巴勒斯坦的公开声援以及她对加沙“种族灭绝”的谴责表明，她明白为地球而战与为人权而战是不可分割的。",
        "li1": "<strong>“疯狂”：</strong> 系统称她“极端”或“不稳定”，因为她的言论具有威胁现状的清晰度。在一个病态的世界里，说出真相的人总是被贴上“疯子”的标签。",
        "li2": "<strong>系统性联系：</strong> 格蕾塔将“军火贸易”、“垃圾危机”与原住民土地的破坏联系起来，揭露了 1% 系统的全面失败。",
        "quote": "“所有子孙后代的眼睛都在注视着你们。如果你们选择辜负我们，我说：我们永远不会原谅你们。”",
        "footer_text": "&copy; 2026 未经过滤的真理宣言 | <a href=\"republish-zh.html\">关于和重新发布</a> | <a href=\"https://github.com/TimGeyssens/JusticeForGaza\">源代码</a>",
        "nav_manifesto": "宣言",
        "nav_systems": "权力体系",
        "nav_extraction": "榨取",
        "nav_human_lens": "人类视角",
        "nav_truth": "真理与神话",
        "nav_solidarity": "团结",
        "menu": "菜单"
    }
}

dropdown_translations = {
    "en": ("The Internal Mind", "The Human Lens"),
    "nl": ("Interne Geest", "De Menselijke Lens"),
    "fr": ("Esprit Interne", "La Lentille Humaine"),
    "it": ("Mente Interna", "La Lente Umana"),
    "de": ("Innerer Geist", "Die menschliche Linse"),
    "es": ("Mente Interna", "La Lente Humana"),
    "pt": ("Mente Interna", "A Lente Humana"),
    "ar": ("العقل الداخلي", "العدسة البشرية"),
    "zh": ("内心世界", "人类视角")
}

def get_nav(lang_code, active_page="greta-thunberg.html"):
    is_rtl = lang_code == "ar"
    nav_lang = lang_code if lang_code != "en" else ""
    suffix = f"-{nav_lang}" if nav_lang else ""
    
    t = translations.get(lang_code if lang_code != "zh-CN" else "zh")
    if not t: t = translations["nl"] # fallback
    
    # Dropdown names
    systems_name = t["nav_systems"]
    extraction_name = t["nav_extraction"]
    human_lens_name = t["nav_human_lens"]
    truth_name = t["nav_truth"]
    solidarity_name = t["nav_solidarity"]
    manifesto_name = t["nav_manifesto"]
    menu_label = t["menu"]

    nav_html = f"""
    <nav class="navbar {'rtl' if is_rtl else ''}">
        <input type="checkbox" id="nav-toggle" class="nav-toggle">
        <label for="nav-toggle" class="nav-toggle-label">{menu_label}</label>
        <div class="nav-links">
            <a href="{'index.html' if lang_code == 'en' else lang_code + '.html'}" class="nav-item"> {manifesto_name} </a>
            <div class="nav-dropdown">
                <div class="nav-item"> {systems_name} </div>
                <div class="dropdown-content">
                    <a href="history{suffix}.html">History</a>
                    <a href="genocide-convention{suffix}.html">Genocide Convention</a>
                    <a href="democracy-illusion{suffix}.html">Democracy Illusion</a>
                    <a href="money-evolution{suffix}.html">Evolution of Money</a>
                    <a href="tax-avoidance{suffix}.html">Tax Avoidance</a>
                    <a href="wealth-gap{suffix}.html">Wealth Gap</a>
                    <a href="social-mobility{suffix}.html">Social Mobility</a>
                    <a href="arms-trade{suffix}.html">Arms Trade</a>
                </div>
            </div>
            <div class="nav-dropdown">
                <div class="nav-item"> {extraction_name} </div>
                <div class="dropdown-content">
                    <a href="climate-justice{suffix}.html">Climate Justice</a>
                    <a href="water-apartheid{suffix}.html">Water Apartheid</a>
                    <a href="waste-crisis{suffix}.html">Waste Crisis</a>
                    <a href="food-sovereignty{suffix}.html">Food Sovereignty</a>
                    <a href="modern-slavery{suffix}.html">Modern Slavery</a>
                    <a href="medical-apartheid{suffix}.html">Medical Apartheid</a>
                    <a href="prison-industrial{suffix}.html">Prison Industrial</a>
                    <a href="symptom-trap{suffix}.html">Symptom Trap</a>
                </div>
            </div>
            <div class="nav-dropdown active">
                <div class="nav-item active"> {human_lens_name} </div>
                <div class="dropdown-content">
                    <a href="neurodiversity{suffix}.html">Neurodiversity</a>
                    <a href="survival-mode{suffix}.html">Survival Mode</a>
                    <a href="the-mindset{suffix}.html">The Mindset</a>
                    <a href="education-factory{suffix}.html">Education Factory</a>
                    <a href="board-games{suffix}.html">Board Games</a>
                    <a href="mental-health{suffix}.html">Mental Health</a>
                    <a href="greta-thunberg{suffix}.html" class="active">Greta Thunberg</a>
                </div>
            </div>
            <div class="nav-dropdown">
                <div class="nav-item"> {truth_name} </div>
                <div class="dropdown-content">
                    <a href="philosophy{suffix}.html">Philosophy</a>
                    <a href="human-nature{suffix}.html">Human Nature</a>
                    <a href="hero-myth{suffix}.html">Hero Myth</a>
                    <a href="propaganda{suffix}.html">Information War</a>
                    <a href="tech-surveillance{suffix}.html">Tech & Surveillance</a>
                    <a href="divide-conquer{suffix}.html">Divide & Conquer</a>
                    <a href="bullshit-jobs{suffix}.html">Bullshit Jobs</a>
                    <a href="love-revenge{suffix}.html">Love as Revenge</a>
                </div>
            </div>
            <div class="nav-dropdown">
                <div class="nav-item"> {solidarity_name} </div>
                <div class="dropdown-content">
                    <a href="take-action{suffix}.html">Take Action</a>
                    <a href="radical-community{suffix}.html">Radical Community</a>
                    <a href="glossary{suffix}.html">Glossary</a>
                    <a href="references{suffix}.html">References</a>
                    <a href="further-reading{suffix}.html">Read Further</a>
                </div>
            </div>
        </div>
        <div class="lang-switcher">
            <select onchange="window.location.href=this.value">
                <option value="greta-thunberg.html" {'selected' if lang_code == 'en' else ''}>English</option>
                <option value="greta-thunberg-nl.html" {'selected' if lang_code == 'nl' else ''}>Nederlands</option>
                <option value="greta-thunberg-fr.html" {'selected' if lang_code == 'fr' else ''}>Français</option>
                <option value="greta-thunberg-it.html" {'selected' if lang_code == 'it' else ''}>Italiano</option>
                <option value="greta-thunberg-de.html" {'selected' if lang_code == 'de' else ''}>Deutsch</option>
                <option value="greta-thunberg-es.html" {'selected' if lang_code == 'es' else ''}>Español</option>
                <option value="greta-thunberg-pt.html" {'selected' if lang_code == 'pt' else ''}>Português</option>
                <option value="greta-thunberg-ar.html" {'selected' if lang_code == 'ar' else ''}>العربية</option>
                <option value="greta-thunberg-zh.html" {'selected' if lang_code == 'zh-CN' else ''}>中文</option>
            </select>
        </div>
    </nav>
"""
    return nav_html

def create_greta_file(lang_code):
    t = translations.get(lang_code if lang_code != "zh-CN" else "zh")
    is_rtl = lang_code == "ar"
    is_zh = lang_code == "zh-CN"
    
    head_extra = ""
    if is_rtl:
        head_extra = """
    <link href="https://fonts.googleapis.com/css2?family=Amiri&family=Inter:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Amiri', serif, 'Inter', sans-serif; }
    </style>"""
    elif is_zh:
        head_extra = """
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: "Noto Sans SC", sans-serif; }
        body { font-family: 'Noto Sans SC', sans-serif, 'Inter'; }
    </style>"""

    content = f"""<!DOCTYPE html>
<html lang="{lang_code}" {'dir="rtl"' if is_rtl else ''}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']}</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📢</text></svg>">
{head_extra}
</head>
<body>
    <header>
        <img src="https://s.france24.com/media/display/c5d994bc-8632-11f0-9045-005056bf30b7/w:1280/p:16x9/000-72WT8F3.jpg" alt="Greta Thunberg" class="header-image">
        <h1>{t['h1']}</h1>
        <h2>{t['h2']}</h2>
    </header>

{get_nav(lang_code)}

    <main>
        <section>
            <h3>{t['sec1_h3']}</h3>
            <p>{t['sec1_p']}</p>
        </section>

        <section>
            <h3>{t['sec2_h3']}</h3>
            <p>{t['sec2_p']}</p>
        </section>

        <section>
            <h3>{t['sec3_h3']}</h3>
            <p>{t['sec3_p']}</p>
            <ul>
                <li>{t['li1']}</li>
                <li>{t['li2']}</li>
            </ul>
        </section>

        <blockquote>
            {t['quote']}
        </blockquote>
    </main>

    <footer>
        <p>{t['footer_text']}</p>
    </footer>
</body>
</html>
"""
    filename = f"greta-thunberg-{lang_code}.html" if lang_code != "en" else "greta-thunberg.html"
    if lang_code == "zh-CN": filename = "greta-thunberg-zh.html"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

# Create the 8 translations
for lang in ["nl", "fr", "it", "de", "es", "pt", "ar", "zh-CN", "en"]:
    create_greta_file(lang)

# Now update all other files
all_files = [f for f in os.listdir(".") if f.endswith(".html") and not f.startswith("greta-thunberg") and f != "republish.html"]

for filename in all_files:
    # Determine language of the file
    lang = "en"
    for l in dropdown_translations.keys():
        if filename.endswith(f"-{l}.html"):
            lang = l
            break
    
    old_dropdown_name, new_dropdown_name = dropdown_translations.get(lang, ("The Internal Mind", "The Human Lens"))
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 1. Rename dropdown
        content = content.replace(f'<div class="nav-item">{old_dropdown_name}</div>', f'<div class="nav-item">{new_dropdown_name}</div>')
        content = content.replace(f'<div class="nav-item active">{old_dropdown_name}</div>', f'<div class="nav-item active">{new_dropdown_name}</div>')
        
        # 2. Add Greta Thunberg link as last item in that dropdown
        search_str = f'<div class="nav-item">{new_dropdown_name}</div>'
        if search_str not in content:
            search_str = f'<div class="nav-item active">{new_dropdown_name}</div>'
            
        if search_str in content:
            parts = content.split(search_str, 1)
            if len(parts) > 1:
                # Find the end of dropdown-content
                dc_start = parts[1].find('<div class="dropdown-content">')
                if dc_start != -1:
                    dc_end = parts[1].find('</div>', dc_start)
                    if dc_end != -1:
                        localized_greta = "Greta Thunberg"
                        greta_filename = f"greta-thunberg-{lang}.html" if lang != "en" else "greta-thunberg.html"
                        new_link = f'                    <a href="{greta_filename}">{localized_greta}</a>\n                '
                        
                        updated_dc = parts[1][:dc_end] + new_link + parts[1][dc_end:]
                        content = parts[0] + search_str + updated_dc
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Error processing {filename}: {e}")
