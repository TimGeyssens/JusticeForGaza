import os

languages = {
    "nl": {
        "title": "De Symptoomval - Oorzaken vs. Pleisters",
        "h1": "De Symptoomval",
        "h2": "De Wonden Behandelen, de Machine Negeren",
        "h3_1": "De Winstgevende Wond Beheren",
        "p_1": "Onze huidige economische en medische systemen zijn ontworpen om symptomen te bestrijden in plaats van de oorzaken weg te nemen. Of het nu gaat om geestelijke gezondheidszorg, armoede of chronische ziekten, het 1%-systeem vindt het lucratiever om \"pleisters\" te verkopen—medicijnen, tijdelijke hulp of producten voor stressvermindering—dan de giftige omgevingen aan te pakken die mensen in de eerste plaats ziek maken.",
        "h3_2": "Kanker: Een Industriële Epidemie",
        "p_2": "De incidentie van kanker is de afgelopen eeuw spectaculair gestegen. Hoewel de medische vooruitgang de overlevingskansen heeft verbeterd (de \"pleister\"), wordt het ontstaan van kanker gedreven door precies die \"extractiemachine\" waarin we leven. We worden blootgesteld aan milieugifstoffen, microplastics uit de \"Afvalcrisis\" en chemicaliën die nooit deel uitmaakten van de menselijke evolutionaire weg.",
        "li_2_1": "<strong>Stijgende Cijfers:</strong> Wereldwijd zal het aantal kankergevallen naar verwachting met 77% stijgen tegen 2050. Dit is niet alleen \"veroudering\"; het is een mismatch tussen onze omgeving en levensstijl.",
        "li_2_2": "<strong>De Toxiciteit van Groei:</strong> De drang naar oneindige winst leidt tot de deregulering van industriële chemicaliën die in onze lucht, water en bodem terechtkomen.",
        "h3_3": "De Bewerkte Voedselmachine",
        "p_3": "Wij zijn de eerste generaties in de geschiedenis die \"voedsel\" consumeren dat zo industrieel bewerkt is dat het biologisch onherkenbaar is geworden. Ultrabewerkte voeding (UPF) is ontworpen voor maximale winst en houdbaarheid, niet voor menselijke voeding. Ze zijn de belangrijkste veroorzakers van obesitas, diabetes en systemische ontstekingen.",
        "li_3_1": "<strong>Gemanipuleerde Verslaving:</strong> De 1% profiteert van onze verslaving aan goedkope, ontstekingsbevorderende calorieën, en profiteert vervolgens opnieuw van de medicatie die nodig is om de resulterende ziekten te behandelen.",
        "li_3_2": "<strong>Nutritionele Extractie:</strong> De industriële landbouw onttrekt voedingsstoffen aan de bodem zonder deze aan te vullen, waardoor zelfs onze \"verse\" voeding uitgeput en arm aan voedingsstoffen is.",
        "quote": "\"Het systeem wil niet dat je geneest; het wil je als levenslange klant. Het aanpakken van de bronoorzaak is slecht voor de winstcijfers.\"",
        "nav_manifesto": "Manifest",
        "nav_crisis": "De Crisis",
        "nav_human_lens": "De Menselijke Lens",
        "nav_solidarity": "Solidariteit",
        "nav_resources": "Bronnen",
        "nav_symptom_trap": "De Symptoomval",
        "lang_name": "Nederlands",
        "footer_about": "Over & Herpubliceren"
    },
    "fr": {
        "title": "Le Piège des Symptômes - Causes Racines vs Pansements",
        "h1": "Le Piège des Symptômes",
        "h2": "Gérer les Blessures, Ignorer la Machine",
        "h3_1": "Gérer la Blessure Rentable",
        "p_1": "Nos systèmes économiques et médicaux actuels sont conçus pour gérer les symptômes plutôt que de guérir les causes. Qu'il s'agisse de santé mentale, de pauvreté ou de maladies chroniques, le système du 1 % trouve plus rentable de vendre des « pansements » — médicaments, aide temporaire ou produits de soulagement du stress — que de s'attaquer aux environnements toxiques qui rendent les gens malades en premier lieu.",
        "h3_2": "Le Cancer : Une Épidémie Industrielle",
        "p_2": "Les taux de cancer ont augmenté de façon spectaculaire au cours du dernier siècle. Alors que les progrès médicaux ont amélioré les taux de survie (le « pansement »), l'incidence du cancer est alimentée par la « machine d'extraction » même dans laquelle nous vivons. Nous sommes exposés à des toxines environnementales, des microplastiques issus de la « Crise des Déchets » et des produits chimiques qui n'ont jamais fait partie du chemin évolutif humain.",
        "li_2_1": "<strong>Taux en hausse :</strong> Les cas mondiaux de cancer devraient augmenter de 77 % d'ici 2050. Ce n'est pas seulement le « vieillissement » ; c'est un décalage environnemental et de mode de vie.",
        "li_2_2": "<strong>La toxicité de la croissance :</strong> La recherche du profit infini mène à la déréglementation des produits chimiques industriels qui finissent dans notre air, notre eau et notre sol.",
        "h3_3": "La Machine Alimentaire Transformée",
        "p_3": "Nous sommes les premières générations de l'histoire à consommer des « aliments » transformés industriellement au point d'être biologiquement méconnaissables. Les aliments ultra-transformés (AUT) sont conçus pour un profit et une durée de conservation maximum, et non pour la nutrition humaine. Ils sont les principaux moteurs de l'obésité, du diabète et de l'inflammation systémique.",
        "li_3_1": "<strong>Addiction programmée :</strong> Le 1 % profite de notre dépendance aux calories bon marché et inflammatoires, puis profite à nouveau des médicaments utilisés pour traiter les maladies qui en résultent.",
        "li_3_2": "<strong>Extraction nutritionnelle :</strong> L'agriculture industrielle extrait les nutriments du sol sans les remplacer, laissant même nos aliments « frais » appauvris et faibles.",
        "quote": "« Le système ne veut pas que vous soyez guéri ; il veut que vous soyez un client à vie. S'attaquer à la cause racine est mauvais pour les affaires. »",
        "nav_manifesto": "Manifeste",
        "nav_crisis": "La Crise",
        "nav_human_lens": "Le Prisme Humain",
        "nav_solidarity": "Solidarité",
        "nav_resources": "Ressources",
        "nav_symptom_trap": "Le Piège des Symptômes",
        "lang_name": "Français",
        "footer_about": "À propos & Republipostage"
    },
    "it": {
        "title": "La Trappola dei Sintomi - Cause Profonde vs Cerotti",
        "h1": "La Trappola dei Sintomi",
        "h2": "Gestire le Ferite, Ignorare la Macchina",
        "h3_1": "Gestire la Ferita Redditizia",
        "p_1": "I nostri attuali sistemi economici e medici sono progettati per gestire i sintomi piuttosto che curare le cause. Che si tratti di salute mentale, povertà o malattie croniche, il sistema dell'1% trova più redditizio vendere \"cerotti\" — farmaci, aiuti temporanei o prodotti per alleviare lo stress — piuttosto che affrontare gli ambienti tossici che fanno ammalare le persone in primo luogo.",
        "h3_2": "Cancro: Un'Epidemia Industriale",
        "p_2": "I tassi di cancro sono aumentati drasticamente nell'ultimo secolo. Mentre i progressi medici hanno migliorato i tassi di sopravvivenza (il \"cerotto\"), l'incidenza del cancro è guidata dalla stessa \"macchina di estrazione\" in cui viviamo. Siamo esposti a tossine ambientali, microplastiche della \"Crisi dei Rifiuti\" e sostanze chimiche che non hanno mai fatto parte del percorso evolutivo umano.",
        "li_2_1": "<strong>Tassi in crescita:</strong> Si prevede che i casi globali di cancro aumenteranno del 77% entro il 2050. Non si tratta solo di \"invecchiamento\"; è un disallineamento ambientale e di stile di vita.",
        "li_2_2": "<strong>La tossicità della crescita:</strong> La spinta al profitto infinito porta alla deregolamentazione delle sostanze chimiche industriali che finiscono nell'aria, nell'acqua e nel suolo.",
        "h3_3": "La Macchina del Cibo Processato",
        "p_3": "Siamo le prime generazioni nella storia a consumare \"cibo\" che è industrialmente processato al punto da essere biologicamente irriconoscibile. I cibi ultra-processati (UPF) sono progettati per il massimo profitto e durata, non per la nutrizione umana. Sono i principali motori di obesità, diabete e infiammazione sistemica.",
        "li_3_1": "<strong>Dipendenza Progettata:</strong> L'1% guadagna rendendoci dipendenti da calorie economiche e infiammatorie, e guadagna di nuovo dai farmaci usati per trattare le malattie che ne derivano.",
        "li_3_2": "<strong>Estrazione Nutrizionale:</strong> L'agricoltura industriale estrae nutrienti dal suolo senza reintegrarli, lasciando anche il nostro cibo \"fresco\" impoverito e debole.",
        "quote": "\"Il sistema non vuole che tu sia guarito; ti vuole come cliente a vita. Affrontare la causa profonda fa male ai profitti.\"",
        "nav_manifesto": "Manifesto",
        "nav_crisis": "La Crisi",
        "nav_human_lens": "La Lente Umana",
        "nav_solidarity": "Solidarietà",
        "nav_resources": "Risorse",
        "nav_symptom_trap": "La Trappola dei Sintomi",
        "lang_name": "Italiano",
        "footer_about": "Info & Ripubblicazione"
    },
    "de": {
        "title": "Die Symptomfalle - Ursachen vs. Pflaster",
        "h1": "Die Symptomfalle",
        "h2": "Die Wunden verwalten, die Maschine ignorieren",
        "h3_1": "Die profitable Wunde verwalten",
        "p_1": "Unsere gegenwärtigen Wirtschafts- und Medizinsysteme sind darauf ausgelegt, Symptome zu verwalten, anstatt Ursachen zu heilen. Ob es um psychische Gesundheit, Armut oder chronische Krankheiten geht – das 1%-System findet es profitabler, „Pflaster“ zu verkaufen – Medikamente, temporäre Hilfe oder Stressabbauprodukte –, als die toxischen Umgebungen anzugehen, die die Menschen überhaupt erst krank machen.",
        "h3_2": "Krebs: Eine industrielle Epidemie",
        "p_2": "Die Krebsraten sind im letzten Jahrhundert dramatisch gestiegen. Während medizinische Fortschritte die Überlebensraten verbessert haben (das „Pflaster“), wird das Auftreten von Krebs durch genau jene „Extraktionsmaschine“ vorangetrieben, in der wir leben. Wir sind Umweltgiften, Mikroplastik aus der „Abfallkrise“ und Chemikalien ausgesetzt, die niemals Teil des menschlichen Evolutionswegs waren.",
        "li_2_1": "<strong>Steigende Raten:</strong> Die weltweiten Krebsfälle werden bis 2050 voraussichtlich um 77 % steigen. Das ist nicht nur „Altern“; es ist ein Missverhältnis zwischen Umwelt und Lebensstil.",
        "li_2_2": "<strong>Die Toxizität des Wachstums:</strong> Das Streben nach unendlichem Profit führt zur Deregulierung von Industriechemikalien, die in unserer Luft, unserem Wasser und unserem Boden landen.",
        "h3_3": "Die Maschine für verarbeitete Lebensmittel",
        "p_3": "Wir sind die ersten Generationen in der Geschichte, die „Lebensmittel“ konsumieren, die industriell so stark verarbeitet sind, dass sie biologisch nicht mehr wiedererkennbar sind. Hochverarbeitete Lebensmittel (UPFs) sind auf maximalen Profit und Haltbarkeit ausgelegt, nicht auf menschliche Ernährung. Sie sind die Hauptursachen für Fettleibigkeit, Diabetes und systemische Entzündungen.",
        "li_3_1": "<strong>Manipulierte Sucht:</strong> Das 1 % profitiert davon, uns von billigen, entzündungsfördernden Kalorien abhängig zu machen, und profitiert dann erneut von den Medikamenten, die zur Behandlung der resultierenden Krankheiten eingesetzt werden.",
        "li_3_2": "<strong>Nährstoffextraktion:</strong> Die industrielle Landwirtschaft entzieht dem Boden Nährstoffe, ohne sie zu ersetzen, wodurch selbst unsere „frischen“ Lebensmittel ausgelaugt und schwach werden.",
        "quote": "„Das System will nicht, dass du geheilt wirst; es will dich als lebenslangen Kunden. Die Ursache anzugehen, ist schlecht für den Gewinn.“",
        "nav_manifesto": "Manifest",
        "nav_crisis": "Die Krise",
        "nav_human_lens": "Die menschliche Perspektive",
        "nav_solidarity": "Solidarität",
        "nav_resources": "Ressourcen",
        "nav_symptom_trap": "Die Symptomfalle",
        "lang_name": "Deutsch",
        "footer_about": "Über & Wiederveröffentlichung"
    },
    "es": {
        "title": "La Trampa de los Síntomas - Causas Raíz vs. Parches",
        "h1": "La Trampa de los Síntomas",
        "h2": "Gestionar las Heridas, Ignorar la Máquina",
        "h3_1": "Gestionar la Herida Rentable",
        "p_1": "Nuestros sistemas económicos y médicos actuales están diseñados para gestionar los síntomas en lugar de curar las causas. Ya sea en salud mental, pobreza o enfermedades crónicas, el sistema del 1% considera más rentable vender \"parches\" —medicamentos, ayuda temporal o productos para aliviar el estrés— que abordar los entornos tóxicos que enferman a las personas en primer lugar.",
        "h3_2": "Cáncer: Una Epidemia Industrial",
        "p_2": "Las tasas de cáncer han aumentado drásticamente durante el último siglo. Si bien los avances médicos han mejorado las tasas de supervivencia (el \"parche\"), la incidencia de cáncer es impulsada por la misma \"máquina de extracción\" en la que vivimos. Estamos expuestos a toxinas ambientales, microplásticos de la \"Crisis de los Residuos\" y productos químicos que nunca formaron parte del camino evolutivo humano.",
        "li_2_1": "<strong>Tasas en aumento:</strong> Se proyecta que los casos globales de cáncer aumenten un 77% para 2050. Esto no es solo \"envejecimiento\"; es un desajuste ambiental y de estilo de vida.",
        "li_2_2": "<strong>La toxicidad del crecimiento:</strong> El impulso por el beneficio infinito conduce a la desregulación de los productos químicos industriales que terminan en nuestro aire, agua y suelo.",
        "h3_3": "La Máquina de Alimentos Procesados",
        "p_3": "Somos las primeras generaciones en la historia que consumen \"alimentos\" procesados industrialmente hasta el punto de ser biológicamente irreconocibles. Los alimentos ultraprocesados (AUP) están diseñados para obtener el máximo beneficio y vida útil, no para la nutrición humana. Son los principales impulsores de la obesidad, la diabetes y la inflamación sistémica.",
        "li_3_1": "<strong>Adicción Diseñada:</strong> El 1% se beneficia al hacernos adictos a calorías baratas e inflamatorias, y luego se beneficia nuevamente de los medicamentos utilizados para tratar las enfermedades resultantes.",
        "li_3_2": "<strong>Extracción Nutricional:</strong> La agricultura industrial extrae nutrientes del suelo sin reemplazarlos, dejando incluso nuestros alimentos \"frescos\" agotados y débiles.",
        "quote": "\"El sistema no quiere que te cures; te quiere como cliente de por vida. Abordar la causa raíz es malo para los resultados económicos.\"",
        "nav_manifesto": "Manifiesto",
        "nav_crisis": "La Crisis",
        "nav_human_lens": "El Lente Humano",
        "nav_solidarity": "Solidaridad",
        "nav_resources": "Recursos",
        "nav_symptom_trap": "La Trampa de los Síntomas",
        "lang_name": "Español",
        "footer_about": "Acerca de & Republicación"
    },
    "pt": {
        "title": "A Armadilha dos Sintomas - Causas Raiz vs. Paliativos",
        "h1": "A Armadilha dos Sintomas",
        "h2": "Gerindo as Feridas, Ignorando a Máquina",
        "h3_1": "Gerindo a Ferida Lucrativa",
        "p_1": "Nossos sistemas econômicos e médicos atuais são projetados para gerir sintomas em vez de curar as causas. Seja na saúde mental, na pobreza ou em doenças crônicas, o sistema do 1% considera mais lucrativo vender \"paliativos\" — medicamentos, ajuda temporária ou produtos para alívio do estresse — do que enfrentar os ambientes tóxicos que adoecem as pessoas em primeiro lugar.",
        "h3_2": "Câncer: Uma Epidemia Industrial",
        "p_2": "As taxas de câncer aumentaram drasticamente no último século. Embora os avanços médicos tenham melhorado as taxas de sobrevivência (o \"paliativo\"), a incidência de câncer é impulsionada pela própria \"máquina de extração\" em que vivemos. Estamos expostos a toxinas ambientais, microplásticos da \"Crise dos Resíduos\" e produtos químicos que nunca fizeram parte do caminho evolutivo humano.",
        "li_2_1": "<strong>Taxas Crescentes:</strong> Projeta-se que os casos globais de câncer aumentem 77% até 2050. Isso não é apenas \"envelhecimento\"; é um desajuste ambiental e de estilo de vida.",
        "li_2_2": "<strong>A Toxicidade do Crescimento:</strong> A busca pelo lucro infinito leva à desregulamentação de produtos químicos industriais que acabam no nosso ar, água e solo.",
        "h3_3": "A Máquina de Alimentos Processados",
        "p_3": "Somos as primeiras gerações na história a consumir \"alimentos\" processados industrialmente ao ponto de serem biologicamente irreconhecíveis. Alimentos ultraprocessados (AUPs) são projetados para o máximo lucro e vida útil, não para a nutrição humana. Eles são os principais impulsionadores da obesidade, diabetes e inflamação sistêmica.",
        "li_3_1": "<strong>Vício Projetado:</strong> O 1% lucra ao nos tornar viciados em calorias baratas e inflamatórias, e lucra novamente com os medicamentos usados para tratar as doenças resultantes.",
        "li_3_2": "<strong>Extração Nutricional:</strong> A agricultura industrial extrai nutrientes do solo sem substituí-los, deixando até mesmo nossos alimentos \"frescos\" empobrecidos e fracos.",
        "quote": "\"O sistema não quer que você seja curado; ele quer você como um cliente vitalício. Abordar a causa raiz é ruim para o faturamento.\"",
        "nav_manifesto": "Manifesto",
        "nav_crisis": "A Crise",
        "nav_human_lens": "A Lente Humana",
        "nav_solidarity": "Solidariedade",
        "nav_resources": "Recursos",
        "nav_symptom_trap": "A Armadilha dos Sintomas",
        "lang_name": "Português",
        "footer_about": "Sobre & Republicação"
    },
    "ar": {
        "title": "فخ الأعراض - الأسباب الجذرية مقابل الحلول المؤقتة",
        "h1": "فخ الأعراض",
        "h2": "إدارة الجروح وتجاهل الآلة",
        "h3_1": "إدارة الجرح المربح",
        "p_1": "أنظمتنا الاقتصادية والطبية الحالية مصممة لإدارة الأعراض بدلاً من علاج الأسباب. وسواء كان الأمر يتعلق بالصحة النفسية أو الفقر أو الأمراض المزمنة، فإن نظام الـ 1% يجد أنه من المربح بيع \"الحلول المؤقتة\" - الأدوية، أو المساعدات المؤقتة، أو منتجات تخفيف التوتر - بدلاً من معالجة البيئات السامة التي تسبب المرض للناس في المقام الأول.",
        "h3_2": "السرطان: وباء صناعي",
        "p_2": "ارتفعت معدلات السرطان بشكل كبير خلال القرن الماضي. وبينما أدى التقدم الطبي إلى تحسين معدلات البقاء على قيد الحياة (الحل المؤقت)، فإن الإصابة بالسرطان مدفوعة بـ \"آلة الاستخراج\" ذاتها التي نعيش فيها. نحن معرضون للسموم البيئية، واللدائن الدقيقة من \"أزمة النفايات\"، والمواد الكيميائية التي لم تكن أبداً جزءاً من المسار التطوري البشري.",
        "li_2_1": "<strong>معدلات متزايدة:</strong> من المتوقع أن ترتفع حالات السرطان العالمية بنسبة 77% بحلول عام 2050. هذا ليس مجرد \"شيخوخة\"؛ إنه عدم توافق بين البيئة ونمط الحياة.",
        "li_2_2": "<strong>سميّة النمو:</strong> إن السعي وراء الربح اللانهائي يؤدي إلى إلغاء القيود التنظيمية على المواد الكيميائية الصناعية التي تنتهي في الهواء والماء والتربة.",
        "h3_3": "آلة الغذاء المعالج",
        "p_3": "نحن الأجيال الأولى في التاريخ التي تستهلك \"طعاماً\" معالجاً صناعياً إلى درجة أنه أصبح غير قابل للتمييز بيولوجياً. تم تصميم الأطعمة فائقة المعالجة (UPFs) لتحقيق أقصى قدر من الربح ومدة الصلاحية، وليس للتغذية البشرية. إنها المحركات الرئيسية للسمنة والسكري والالتهابات الجهازية.",
        "li_3_1": "<strong>إدمان هندسي:</strong> يربح الـ 1% من جعلنا مدمنين على سعرات حرارية رخيصة ومسببة للالتهابات، ثم يربحون مرة أخرى من الأدوية المستخدمة لعلاج الأمراض الناتجة.",
        "li_3_2": "<strong>الاستخراج الغذائي:</strong> تستخرج الزراعة الصناعية العناصر الغذائية من التربة دون استبدالها، مما يترك حتى طعامنا \"الطازج\" مستنفداً وضعيفاً.",
        "quote": "\"النظام لا يريدك أن تُشفى؛ إنه يريدك كعميل مدى الحياة. معالجة السبب الجذري سيئة للأرباح.\"",
        "nav_manifesto": "البيان",
        "nav_crisis": "الأزمة",
        "nav_human_lens": "المنظور الإنساني",
        "nav_solidarity": "التضامن",
        "nav_resources": "الموارد",
        "nav_symptom_trap": "فخ الأعراض",
        "lang_name": "العربية",
        "footer_about": "حول وإعادة النشر",
        "dir": "rtl",
        "font": "Amiri"
    },
    "zh": {
        "title": "症状陷阱 - 根本原因 vs. 创可贴",
        "h1": "症状陷阱",
        "h2": "管理伤口，忽视机器",
        "h3_1": "管理有利可图的伤口",
        "p_1": "我们当前的经济和医疗系统旨在管理症状而非治愈原因。无论是精神健康、贫困还是慢性疾病，1% 的系统发现销售“创可贴”——药物、临时援助或缓解压力的产品——比解决首先导致人们生病的毒性环境更有利可图。",
        "h3_2": "癌症：一场工业瘟疫",
        "p_2": "在过去的一个世纪里，癌症发病率急剧上升。虽然医学进步提高了生存率（“创可贴”），但癌症的发病率是由我们生活的“提取机器”驱动的。我们暴露在环境毒素、来自“垃圾危机”的微塑料以及从未属于人类进化路径的化学物质中。",
        "li_2_1": "<strong>发病率上升：</strong> 预计到 2050 年，全球癌症病例将增长 77%。这不仅仅是“衰老”；这是环境与生活方式的不匹配。",
        "li_2_2": "<strong>增长的毒性：</strong> 对无限利润的追求导致了工业化学品的监管放松，这些化学品最终进入了我们的空气、水和土壤中。",
        "h3_3": "加工食品机器",
        "p_3": "我们是历史上第一代食用经过工业加工、甚至在生物学上无法辨认的“食物”的人。超加工食品 (UPFs) 的设计是为了获得最大的利润和保质期，而不是为了人类的营养。它们是肥胖、糖尿病和系统性炎症的主要驱动因素。",
        "li_3_1": "<strong>设计的成瘾：</strong> 1% 的人通过让我们对廉价、引发炎症的热量成瘾而获利，然后又从用于治疗由此产生的疾病的药物中再次获利。",
        "li_3_2": "<strong>营养提取：</strong> 工业农业从土壤中提取养分而不进行补充，甚至让我们“新鲜”的食物也变得营养匮乏、虚弱无力。",
        "quote": "“系统不希望你痊愈；它希望你成为终身客户。解决根本原因对利润不利。”",
        "nav_manifesto": "宣言",
        "nav_crisis": "危机",
        "nav_human_lens": "人类视角",
        "nav_solidarity": "团结",
        "nav_resources": "资源",
        "nav_symptom_trap": "症状陷阱",
        "lang_name": "中文",
        "footer_about": "关于 & 重新发布"
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
        <img src="https://s.france24.com/media/display/c5d994bc-8632-11f0-9045-005056bf30b7/w:1280/p:16x9/000-72WT8F3.jpg" alt="{h1}" class="header-image">
        <h1>{h1}</h1>
        <h2>{h2}</h2>
    </header>

    <nav class="navbar{rtl_class}">
        <input type="checkbox" id="nav-toggle" class="nav-toggle">
        <label for="nav-toggle" class="nav-toggle-label">{menu_label}</label>
        <div class="nav-links">
            <a href="{manifesto_link}" class="nav-item">{nav_manifesto}</a>
            <div class="nav-dropdown active">
                <div class="nav-item active">{nav_crisis}</div>
                <div class="dropdown-content">
                    <a href="history{suffix}.html">{history_label}</a>
                    <a href="mental-health{suffix}.html">{mental_health_label}</a>
                    <a href="wealth-gap{suffix}.html">{wealth_gap_label}</a>
                    <a href="arms-trade{suffix}.html">{arms_trade_label}</a>
                    <a href="climate-justice{suffix}.html">{climate_justice_label}</a>
                    <a href="water-apartheid{suffix}.html">{water_apartheid_label}</a>
                    <a href="medical-apartheid{suffix}.html">{medical_apartheid_label}</a>
                    <a href="modern-slavery{suffix}.html">{modern_slavery_label}</a>
                    <a href="prison-industrial{suffix}.html">{prison_industrial_label}</a>
                    <a href="food-sovereignty{suffix}.html">{food_sovereignty_label}</a>
                    <a href="social-mobility{suffix}.html">{social_mobility_label}</a>
                    <a href="symptom-trap{suffix}.html" class="active">{nav_symptom_trap}</a>
                    <a href="genocide-convention{suffix}.html">{genocide_convention_label}</a>
                    <a href="waste-crisis{suffix}.html">{waste_crisis_label}</a>
                    <a href="money-evolution{suffix}.html">{money_evolution_label}</a>
                    <a href="tax-avoidance{suffix}.html">{tax_avoidance_label}</a>
                    <a href="democracy-illusion{suffix}.html">{democracy_illusion_label}</a>
                </div>
            </div>
            <div class="nav-dropdown">
                <div class="nav-item">{nav_human_lens}</div>
                <div class="dropdown-content">
                    <a href="neurodiversity{suffix}.html">{neurodiversity_label}</a>
                    <a href="survival-mode{suffix}.html">{survival_mode_label}</a>
                    <a href="the-mindset{suffix}.html">{the_mindset_label}</a>
                    <a href="hero-myth{suffix}.html">{hero_myth_label}</a>
                    <a href="propaganda{suffix}.html">{propaganda_label}</a>
                    <a href="tech-surveillance{suffix}.html">{tech_surveillance_label}</a>
                    <a href="bullshit-jobs{suffix}.html">{bullshit_jobs_label}</a>
                    <a href="human-nature{suffix}.html">{human_nature_label}</a>
                    <a href="education-factory{suffix}.html">{education_factory_label}</a>
                    <a href="divide-conquer{suffix}.html">{divide_conquer_label}</a>
                    <a href="philosophy{suffix}.html">{philosophy_label}</a>
                    <a href="board-games.html">Board Games</a>
                </div>
            </div>
            <div class="nav-dropdown">
                <div class="nav-item">{nav_solidarity}</div>
                <div class="dropdown-content">
                    <a href="take-action{suffix}.html">{take_action_label}</a>
                    <a href="radical-community{suffix}.html">{radical_community_label}</a>
                </div>
            </div>
            <div class="nav-dropdown">
                <div class="nav-item">{nav_resources}</div>
                <div class="dropdown-content">
                    <a href="glossary{suffix}.html">{glossary_label}</a>
                    <a href="references{suffix}.html">{references_label}</a>
                    <a href="further-reading{suffix}.html">{further_reading_label}</a>
                </div>
            </div>
        </div>
        <div class="lang-switcher">
            <select onchange="window.location.href=this.value">
                <option value="symptom-trap.html"{sel_en}>English</option>
                <option value="symptom-trap-nl.html"{sel_nl}>Nederlands</option>
                <option value="symptom-trap-fr.html"{sel_fr}>Français</option>
                <option value="symptom-trap-it.html"{sel_it}>Italiano</option>
                <option value="symptom-trap-de.html"{sel_de}>Deutsch</option>
                <option value="symptom-trap-es.html"{sel_es}>Español</option>
                <option value="symptom-trap-pt.html"{sel_pt}>Português</option>
                <option value="symptom-trap-ar.html"{sel_ar}>العربية</option>
                <option value="symptom-trap-zh.html"{sel_zh}>中文</option>
            </select>
        </div>
    </nav>

    <main>
        <section>
            <h3>{h3_1}</h3>
            <p>{p_1}</p>
        </section>

        <section>
            <h3>{h3_2}</h3>
            <p>{p_2}</p>
            <ul>
                <li>{li_2_1}</li>
                <li>{li_2_2}</li>
            </ul>
        </section>

        <section>
            <h3>{h3_3}</h3>
            <p>{p_3}</p>
            <ul>
                <li>{li_3_1}</li>
                <li>{li_3_2}</li>
            </ul>
        </section>

        <blockquote>
            {quote}
        </blockquote>
    </main>

    <footer>
        <p>&copy; 2026 Justice For Gaza Manifesto | <a href="republish{suffix}.html">{footer_about}</a> | <a href="https://github.com/TimGeyssens/JusticeForGaza">Source Code</a></p>
    </footer>
</body>
</html>
"""

labels = {
    "nl": {"menu": "MENU", "history": "Geschiedenis", "mental-health": "Mentale Gezondheid", "wealth-gap": "Vermogenskloof", "arms-trade": "Wapenhandel", "climate-justice": "Klimaatgerechtigheid", "water-apartheid": "Waterapartheid", "medical-apartheid": "Medische Apartheid", "modern-slavery": "Moderne Slavernij", "prison-industrial": "Gevangenis-industrieel Complex", "food-sovereignty": "Voedselsoevereiniteit", "social-mobility": "Sociale Mobiliteit", "genocide-convention": "Genocideverdrag", "waste-crisis": "Afvalcrisis", "money-evolution": "Evolutie van Geld", "tax-avoidance": "Belastingontwijking", "democracy-illusion": "Democratie-illusie", "neurodiversity": "Neurodiversiteit", "survival-mode": "Overlevingsstand", "the-mindset": "De Mentaliteit", "hero-myth": "Heldencultus", "propaganda": "Informatie-oorlog", "tech-surveillance": "Technologie & Surveillance", "bullshit-jobs": "Bullshitbanen", "human-nature": "Menselijke Natuur", "education-factory": "Onderwijsfabriek", "divide-conquer": "Verdeel en Heers", "philosophy": "Filosofie", "take-action": "Onderneem Actie", "radical-community": "Radicale Gemeenschap", "glossary": "Woordenlijst", "references": "Referenties", "further-reading": "Verder Lezen"},
    "fr": {"menu": "MENU", "history": "Histoire", "mental-health": "Santé Mentale", "wealth-gap": "Écart de Richesse", "arms-trade": "Commerce des Armes", "climate-justice": "Justice Climatique", "water-apartheid": "Apartheid de l'Eau", "medical-apartheid": "Apartheid Médical", "modern-slavery": "Esclavage Moderne", "prison-industrial": "Complexe Pénitentiaire", "food-sovereignty": "Souveraineté Alimentaire", "social-mobility": "Mobilité Sociale", "genocide-convention": "Convention sur le Génocide", "waste-crisis": "Crise des Déchets", "money-evolution": "Évolution de la Monnaie", "tax-avoidance": "Évasion Fiscale", "democracy-illusion": "Illusion de la Démocratie", "neurodiversity": "Neurodiversité", "survival-mode": "Mode Survie", "the-mindset": "L'État d'Esprit", "hero-myth": "Mythe du Héros", "propaganda": "Guerre de l'Information", "tech-surveillance": "Tech & Surveillance", "bullshit-jobs": "Jobs à la con", "human-nature": "Nature Humaine", "education-factory": "Usine à Éducation", "divide-conquer": "Diviser pour Régner", "philosophy": "Philosophie", "take-action": "Agir", "radical-community": "Communauté Radicale", "glossary": "Glossaire", "references": "Références", "further-reading": "Lire plus"},
    "it": {"menu": "MENU", "history": "Storia", "mental-health": "Salute Mentale", "wealth-gap": "Divario di Ricchezza", "arms-trade": "Commercio di Armi", "climate-justice": "Giustizia Climatica", "water-apartheid": "Apartheid dell'Acqua", "medical-apartheid": "Apartheid Medico", "modern-slavery": "Schiavitù Moderna", "prison-industrial": "Complesso Industriale Carcerario", "food-sovereignty": "Sovranità Alimentare", "social-mobility": "Mobilità Sociale", "genocide-convention": "Convenzione sul Genocidio", "waste-crisis": "Crisi dei Rifiuti", "money-evolution": "Evoluzione del Denaro", "tax-avoidance": "Elusione Fiscale", "democracy-illusion": "Illusione della Democrazia", "neurodiversity": "Neurodiversità", "survival-mode": "Modalità Sopravvivenza", "the-mindset": "La Mentalità", "hero-myth": "Mito dell'Eroe", "propaganda": "Guerra dell'Informazione", "tech-surveillance": "Tecnologia e Sorveglianza", "bullshit-jobs": "Lavori del Cazzo", "human-nature": "Natura Umana", "education-factory": "Fabbrica dell'Istruzione", "divide-conquer": "Dividi e Domina", "philosophy": "Filosofia", "take-action": "Agisci", "radical-community": "Comunità Radicale", "glossary": "Glossario", "references": "Riferimenti", "further-reading": "Letture Ulteriori"},
    "de": {"menu": "MENÜ", "history": "Geschichte", "mental-health": "Psychische Gesundheit", "wealth-gap": "Vermögenskluft", "arms-trade": "Waffenhandel", "climate-justice": "Klimagerechtigkeit", "water-apartheid": "Wasser-Apartheid", "medical-apartheid": "Medizinische Apartheid", "modern-slavery": "Moderne Sklaverei", "prison-industrial": "Gefängnis-Industrie-Komplex", "food-sovereignty": "Ernährungssouveränität", "social-mobility": "Soziale Mobilität", "genocide-convention": "Genozid-Konvention", "waste-crisis": "Abfallkrise", "money-evolution": "Entwicklung des Geldes", "tax-avoidance": "Steuervermeidung", "democracy-illusion": "Demokratie-Illusion", "neurodiversity": "Neurodiversität", "survival-mode": "Überlebensmodus", "the-mindset": "Die Mentalität", "hero-myth": "Heldenmythos", "propaganda": "Informationskrieg", "tech-surveillance": "Tech & Überwachung", "bullshit-jobs": "Bullshit-Jobs", "human-nature": "Menschliche Natur", "education-factory": "Bildungsfabrik", "divide-conquer": "Teile & Herrsche", "philosophy": "Philosophie", "take-action": "Handeln", "radical-community": "Radikale Gemeinschaft", "glossary": "Glossar", "references": "Referenzen", "further-reading": "Weiterführende Lektüre"},
    "es": {"menu": "MENÚ", "history": "Historia", "mental-health": "Salud Mental", "wealth-gap": "Brecha de Riqueza", "arms-trade": "Comercio de Armas", "climate-justice": "Justicia Climática", "water-apartheid": "Apartheid del Agua", "medical-apartheid": "Apartheid Médico", "modern-slavery": "Esclavitud Moderna", "prison-industrial": "Complejo Industrial de Prisiones", "food-sovereignty": "Soberanía Alimentaria", "social-mobility": "Movilidad Social", "genocide-convention": "Convención sobre el Genocidio", "waste-crisis": "Crisis de los Residuos", "money-evolution": "Evolución del Dinero", "tax-avoidance": "Evasión Fiscal", "democracy-illusion": "Ilusión de la Democracia", "neurodiversity": "Neurodiversidad", "survival-mode": "Modo de Supervivencia", "the-mindset": "La Mentalidad", "hero-myth": "Mito del Héroe", "propaganda": "Guerra de Información", "tech-surveillance": "Tecnología y Vigilancia", "bullshit-jobs": "Trabajos de Mierda", "human-nature": "Naturaleza Humana", "education-factory": "Fábrica de Educación", "divide-conquer": "Divide y Vencerás", "philosophy": "Filosofía", "take-action": "Tomar Acción", "radical-community": "Comunidad Radical", "glossary": "Glosario", "references": "Referencias", "further-reading": "Lectura Adicional"},
    "pt": {"menu": "MENU", "history": "História", "mental-health": "Saúde Mental", "wealth-gap": "Desigualdade de Riqueza", "arms-trade": "Comércio de Armas", "climate-justice": "Justiça Climática", "water-apartheid": "Apartheid da Água", "medical-apartheid": "Apartheid Médico", "modern-slavery": "Escravidão Moderna", "prison-industrial": "Complexo Industrial Prisional", "food-sovereignty": "Soberania Alimentar", "social-mobility": "Mobilidade Social", "genocide-convention": "Convenção sobre o Genocídio", "waste-crisis": "Crise de Resíduos", "money-evolution": "Evolução do Dinheiro", "tax-avoidance": "Evasão Fiscal", "democracy-illusion": "Ilusão da Democracia", "neurodiversity": "Neurodiversidade", "survival-mode": "Modo de Sobrevivência", "the-mindset": "A Mentalidade", "hero-myth": "Mito do Herói", "propaganda": "Guerra de Informação", "tech-surveillance": "Tecnologia e Vigilância", "bullshit-jobs": "Trabalhos de Merda", "human-nature": "Natureza Humana", "education-factory": "Fábrica de Educação", "divide-conquer": "Dividir e Conquistar", "philosophy": "Filosofia", "take-action": "Agir", "radical-community": "Comunidade Radical", "glossary": "Glossário", "references": "Referências", "further-reading": "Leituras Adicionais"},
    "ar": {"menu": "القائمة", "history": "التاريخ", "mental-health": "الصحة النفسية", "wealth-gap": "فجوة الثروة", "arms-trade": "تجارة الأسلحة", "climate-justice": "العدالة المناخية", "water-apartheid": "الفصل العنصري للمياه", "medical-apartheid": "الأبارتهايد الطبي", "modern-slavery": "العبودية الحديثة", "prison-industrial": "المجمع الصناعي للسجون", "food-sovereignty": "السيادة الغذائية", "social-mobility": "الحراك الاجتماعي", "genocide-convention": "اتفاقية منع الإبادة الجماعية", "waste-crisis": "أزمة النفايات", "money-evolution": "تطور المال", "tax-avoidance": "التهرب الضريبي", "democracy-illusion": "وهم الديمقراطية", "neurodiversity": "التنوع العصبي", "survival-mode": "وضع البقاء", "the-mindset": "العقلية", "hero-myth": "أسطورة البطل", "propaganda": "حرب المعلومات", "tech-surveillance": "التكنولوجيا والمراقبة", "bullshit-jobs": "وظائف تافهة", "human-nature": "الطبيعة البشرية", "education-factory": "مصنع التعليم", "divide-conquer": "فرق تسد", "philosophy": "الفلسفة", "take-action": "اتخذ إجراءً", "radical-community": "المجتمع الراديكالي", "glossary": "قاموس المصطلحات", "references": "المراجع", "further-reading": "اقرأ المزيد"},
    "zh": {"menu": "菜单", "history": "历史", "mental-health": "心理健康", "wealth-gap": "财富差距", "arms-trade": "武器贸易", "climate-justice": "气候正义", "water-apartheid": "水资源隔离", "medical-apartheid": "医疗隔离", "modern-slavery": "现代奴隶制", "prison-industrial": "监狱工业复合体", "food-sovereignty": "粮食主权", "social-mobility": "社会流动性", "genocide-convention": "种族灭绝公约", "waste-crisis": "垃圾危机", "money-evolution": "货币演变", "tax-avoidance": "税务规避", "democracy-illusion": "民主幻象", "neurodiversity": "神经多样性", "survival-mode": "生存模式", "the-mindset": "思维方式", "hero-myth": "英雄神话", "propaganda": "信息战争", "tech-surveillance": "技术与监控", "bullshit-jobs": "狗屁工作", "human-nature": "人类本性", "education-factory": "教育工厂", "divide-conquer": "分而治之", "philosophy": "哲学", "take-action": "采取行动", "radical-community": "激进社区", "glossary": "术语表", "references": "参考文献", "further-reading": "延伸阅读"}
}

for lang, content in languages.items():
    suffix = f"-{lang}"
    manifesto_link = f"{lang}.html"
    if lang == "en": # Should not happen based on languages dict but for safety
        suffix = ""
        manifesto_link = "index.html"
    
    extra_head = ""
    dir_attr = ""
    rtl_class = ""
    if lang == "ar":
        extra_head = '<link href="https://fonts.googleapis.com/css2?family=Amiri&family=Inter:wght@300;400;700&display=swap" rel="stylesheet">\n    <style>\n        body { font-family: \'Amiri\', serif, \'Inter\', sans-serif; }\n    </style>'
        dir_attr = ' dir="rtl"'
        rtl_class = ' rtl'
    elif lang == "zh":
        extra_head = '<style>\n        body { font-family: "PingFang SC", "Microsoft YaHei", sans-serif; }\n    </style>'

    l = labels[lang]
    
    html = template.format(
        lang=lang,
        dir_attr=dir_attr,
        title=content["title"],
        extra_head=extra_head,
        h1=content["h1"],
        h2=content["h2"],
        rtl_class=rtl_class,
        menu_label=l["menu"],
        manifesto_link=manifesto_link,
        nav_manifesto=content["nav_manifesto"],
        nav_crisis=content["nav_crisis"],
        nav_human_lens=content["nav_human_lens"],
        nav_solidarity=content["nav_solidarity"],
        nav_resources=content["nav_resources"],
        suffix=suffix,
        history_label=l["history"],
        mental_health_label=l["mental-health"],
        wealth_gap_label=l["wealth-gap"],
        arms_trade_label=l["arms-trade"],
        climate_justice_label=l["climate-justice"],
        water_apartheid_label=l["water-apartheid"],
        medical_apartheid_label=l["medical-apartheid"],
        modern_slavery_label=l["modern-slavery"],
        prison_industrial_label=l["prison-industrial"],
        food_sovereignty_label=l["food-sovereignty"],
        social_mobility_label=l["social-mobility"],
        nav_symptom_trap=content["nav_symptom_trap"],
        genocide_convention_label=l["genocide-convention"],
        waste_crisis_label=l["waste-crisis"],
        money_evolution_label=l["money-evolution"],
        tax_avoidance_label=l["tax-avoidance"],
        democracy_illusion_label=l["democracy-illusion"],
        neurodiversity_label=l["neurodiversity"],
        survival_mode_label=l["survival-mode"],
        the_mindset_label=l["the-mindset"],
        hero_myth_label=l["hero-myth"],
        propaganda_label=l["propaganda"],
        tech_surveillance_label=l["tech-surveillance"],
        bullshit_jobs_label=l["bullshit-jobs"],
        human_nature_label=l["human-nature"],
        education_factory_label=l["education-factory"],
        divide_conquer_label=l["divide-conquer"],
        philosophy_label=l["philosophy"],
        take_action_label=l["take-action"],
        radical_community_label=l["radical-community"],
        glossary_label=l["glossary"],
        references_label=l["references"],
        further_reading_label=l["further-reading"],
        sel_en="", sel_nl=" selected" if lang=="nl" else "", sel_fr=" selected" if lang=="fr" else "",
        sel_it=" selected" if lang=="it" else "", sel_de=" selected" if lang=="de" else "",
        sel_es=" selected" if lang=="es" else "", sel_pt=" selected" if lang=="pt" else "",
        sel_ar=" selected" if lang=="ar" else "", sel_zh=" selected" if lang=="zh" else "",
        h3_1=content["h3_1"], p_1=content["p_1"],
        h3_2=content["h3_2"], p_2=content["p_2"],
        li_2_1=content["li_2_1"], li_2_2=content["li_2_2"],
        h3_3=content["h3_3"], p_3=content["p_3"],
        li_3_1=content["li_3_1"], li_3_2=content["li_3_2"],
        quote=content["quote"],
        footer_about=content["footer_about"]
    )
    
    with open(f"symptom-trap-{lang}.html", "w") as f:
        f.write(html)

