
import os

languages = {
    "nl": {
        "lang_attr": 'lang="nl"',
        "title": "Liefde als Wraak - De Cirkel van Geweld Doorbreken",
        "h1": "Liefde is de Enige Wraak",
        "h2": "De Cirkel van Systemisch Geweld Doorbreken",
        "h3_1": "Het Falen van Geweld",
        "p1": 'De geschiedenis heeft ons een herhalende, brute les geleerd: geweld leidt alleen tot meer geweld. De "Wapenhandel" en het 1%-systeem gedijen bij conflict omdat het hun bestaan rechtvaardigt en hun winsten voedt. Wanneer we geweld met geweld bestrijden, spelen we volgens de regels van de machine die ons onderdrukt. We worden het spiegelbeeld van het roofdier.',
        "h3_2": "Liefde als Radicale Daad",
        "p2": 'In een wereld die ontworpen is om ons in de "Overlevingsstand" en "Verdeel en Heers"-silo\'s te houden, is liefde de ultieme daad van rebellie. Het is de weigering om de ander te dehumaniseren, zelfs wanneer het systeem dat eist. Radicale liefde is het besef dat onze bevrijding verbonden is met de bevrijding van ieder ander menselijk wezen, van Gaza tot de straat waar je woont.',
        "h3_3": "Pacifisme is Geen Passiviteit",
        "p3": 'Een pacifist zijn betekent niet niets doen. Het betekent weigeren deel te nemen aan de "Extractiemachine". Het betekent het bouwen van "Radicale Gemeenschappen" en "Wederzijdse Hulp"-netwerken die de 1% overbodig maken. Het is de kracht om in het "licht van de grot" te staan en anderen uit te nodigen, zonder de noodzaak van een "Heldencultus" of een wapen.',
        "li1": "<strong>Collectieve Veerkracht:</strong> We winnen door bij elkaar te blijven, niet door elkaar uit elkaar te drijven.",
        "li2": '<strong>De Kracht van Empathie:</strong> Empathie is het enige "Neuro-divergente" hulpmiddel dat de 1% niet kan kopiëren of controleren.',
        "li3": "<strong>De Keten Doorbreken:</strong> Door voor liefde te kiezen, stoppen we de overdracht van systemisch trauma naar de volgende generatie.",
        "quote": "Liefde is de enige kracht die in staat is een vijand in een vriend te veranderen. Het is de enige wraak die de wereld daadwerkelijk verandert.",
        "footer_about": "Over & Herpubliceren",
        "footer_source": "Broncode",
        "lang_name": "Nederlands"
    },
    "fr": {
        "lang_attr": 'lang="fr"',
        "title": "L'Amour comme Vengeance - Briser le Cycle de la Violence",
        "h1": "L'Amour est la Seule Vengeance",
        "h2": "Briser le Cycle de la Violence Systémique",
        "h3_1": "L'Échec de la Violence",
        "p1": "L'histoire nous a enseigné une leçon répétitive et brutale : la violence ne mène qu'à plus de violence. Le « Commerce des Armes » et le système des 1 % prospèrent sur le conflit car il justifie leur existence et alimente leurs profits. Lorsque nous répondons à la violence par la violence, nous jouons selon les règles de la machine même qui nous opprime. Nous devenons l'image miroir du prédateur.",
        "h3_2": "L'Amour comme Acte Radical",
        "p2": "Dans un monde conçu pour nous maintenir en « Mode Survie » et dans des silos « Diviser pour Régner », l'amour est l'acte de rébellion ultime. C'est le refus de déshumaniser l'autre, même lorsque le système l'exige. L'amour radical est la réalisation que notre libération est liée à la libération de tout autre être humain, de Gaza à la rue où vous vivez.",
        "h3_3": "Le Pacifisme n'est pas la Passivité",
        "p3": "Être pacifiste ne signifie pas ne rien faire. Cela signifie refuser de participer à la « Machine d'Extraction ». Cela signifie construire des « Communautés Radicales » et des réseaux d'« Entraide » qui rendent les 1 % obsolètes. C'est la force de se tenir dans la « lumière de la caverne » et d'y inviter les autres, sans avoir besoin d'un « Mythe du Héros » ou d'une arme.",
        "li1": "<strong>Résilience Collective :</strong> Nous gagnons en restant ensemble, pas en nous déchirant.",
        "li2": "<strong>Le Pouvoir de l'Empathie :</strong> L'empathie est le seul outil « neuro-divergent » que les 1 % ne peuvent ni reproduire ni contrôler.",
        "li3": "<strong>Briser la Chaîne :</strong> En choisissant l'amour, nous arrêtons la transmission du traumatisme systémique à la génération suivante.",
        "quote": "« L'amour est la seule force capable de transformer un ennemi en ami. C'est la seule vengeance qui change réellement le monde. »",
        "footer_about": "À Propos & Republication",
        "footer_source": "Code Source",
        "lang_name": "Français"
    },
    "it": {
        "lang_attr": 'lang="it"',
        "title": "L'Amore come Vendetta - Rompere il Ciclo della Violenza",
        "h1": "L'Amore è l'Unica Vendetta",
        "h2": "Rompere il Ciclo della Violenza Sistemica",
        "h3_1": "Il Fallimento della Violenza",
        "p1": 'La storia ci ha insegnato una lezione ripetitiva e brutale: la violenza porta solo ad altra violenza. Il "Commercio delle Armi" e il sistema dell\'1% prosperano sul conflitto perché giustifica la loro esistenza e alimenta i loro profitti. Quando rispondiamo alla violenza con la violenza, stiamo giocando secondo le regole della stessa macchina che ci opprime. Diventiamo l\'immagine speculare del predatore.',
        "h3_2": "L'Amore come Atto Radicale",
        "p2": 'In un mondo progettato per mantenerci in "Modalità Sopravvivenza" e in silos "Dividi e Domina", l\'amore è l\'atto finale di ribellione. È il rifiuto di deumanizzare l\'altro, anche quando il sistema lo richiede. L\'amore radicale è la consapevolezza che la nostra liberazione è legata alla liberazione di ogni altro essere umano, da Gaza alla strada in cui vivi.',
        "h3_3": "Il Pacifismo non è Passività",
        "p3": 'Essere pacifisti non significa non fare nulla. Significa rifiutarsi di partecipare alla "Macchina da Estrazione". Significa costruire "Comunità Radicali" e reti di "Mutuo Soccorso" che rendano l\'1% obsoleto. È la forza di stare nella "luce della caverna" e invitare gli altri a entrare, senza bisogno di un "Mito dell\'Eroe" o di un\'arma.',
        "li1": "<strong>Resilienza Collettiva:</strong> Vinciamo restando uniti, non dilaniandoci a vicenda.",
        "li2": '<strong>Il Potere dell\'Empatia:</strong> L\'empatia è l\'unico strumento "neuro-divergente" che l\'1% non può replicare o controllare.',
        "li3": "<strong>Rompere la Catena:</strong> Scegliendo l'amore, fermiamo la trasmissione del trauma sistemico alla prossima generazione.",
        "quote": '"L\'amore è l\'unica forza capace di trasformare un nemico in un amico. È l\'unica vendetta che cambia davvero il mondo."',
        "footer_about": "Informazioni & Ripubblicazione",
        "footer_source": "Codice Sorgente",
        "lang_name": "Italiano"
    },
    "de": {
        "lang_attr": 'lang="de"',
        "title": "Liebe als Rache - Den Kreislauf der Gewalt durchbrechen",
        "h1": "Liebe ist die einzige Rache",
        "h2": "Den Kreislauf systemischer Gewalt durchbrechen",
        "h3_1": "Das Scheitern der Gewalt",
        "p1": "Die Geschichte hat uns eine sich wiederholende, brutale Lektion gelehrt: Gewalt führt nur zu mehr Gewalt. Der „Waffenhandel“ und das 1%-System gedeihen durch Konflikte, weil diese ihre Existenz rechtfertigen und ihre Gewinne anheizen. Wenn wir Gewalt mit Gewalt begegnen, spielen wir nach den Regeln genau der Maschine, die uns unterdrückt. Wir werden zum Spiegelbild des Raubtiers.",
        "h3_2": "Liebe als radikaler Akt",
        "p2": "In einer Welt, die darauf ausgelegt ist, uns im „Überlebensmodus“ und in „Teile & Herrsche“-Silos zu halten, ist Liebe der ultimative Akt der Rebellion. Es ist die Weigerung, den anderen zu entmenschlichen, selbst wenn das System es verlangt. Radikale Liebe ist die Erkenntnis, dass unsere Befreiung an die Befreiung jedes anderen Menschen gebunden ist, von Gaza bis zu der Straße, in der du lebst.",
        "h3_3": "Pazifismus ist nicht Passivität",
        "p3": "Pazifist zu sein bedeutet nicht, nichts zu tun. Es bedeutet, die Teilnahme an der „Extraktionsmaschine“ zu verweigern. Es bedeutet, „Radikale Gemeinschaften“ und Netzwerke der „Gegenseitigen Hilfe“ aufzubauen, die das 1%-System überflüssig machen. Es ist die Stärke, im „Licht der Höhle“ zu stehen und andere hereinzubitten, ohne die Notwendigkeit eines „Heldenmythos“ oder einer Waffe.",
        "li1": "<strong>Kollektive Resilienz:</strong> Wir gewinnen, indem wir zusammenhalten, nicht indem wir uns gegenseitig zerfleischen.",
        "li2": "<strong>Die Macht der Empathie:</strong> Empathie ist das einzige „neurodivergente“ Werkzeug, das die 1 % nicht replizieren oder kontrollieren können.",
        "li3": "<strong>Die Kette durchbrechen:</strong> Indem wir uns für die Liebe entscheiden, stoppen wir die Übertragung systemischer Traumata auf die nächste Generation.",
        "quote": "„Liebe ist die einzige Kraft, die in der Lage ist, einen Feind in einen Freund zu verwandeln. Es ist die einzige Rache, die die Welt tatsächlich verändert.“",
        "footer_about": "Über & Wiederveröffentlichung",
        "footer_source": "Quellcode",
        "lang_name": "Deutsch"
    },
    "es": {
        "lang_attr": 'lang="es"',
        "title": "El Amor como Venganza - Rompiendo el Ciclo de la Violencia",
        "h1": "El Amor es la Única Venganza",
        "h2": "Rompiendo el Ciclo de la Violencia Sistémica",
        "h3_1": "El Fracaso de la Violencia",
        "p1": 'La historia nos ha enseñado una lección repetitiva y brutal: la violencia solo conduce a más violencia. El "Comercio de Armas" y el sistema del 1% prosperan con el conflicto porque justifica su existencia y alimenta sus ganancias. Cuando respondemos a la violencia con violencia, estamos jugando con las reglas de la misma máquina que nos oprime. Nos convertimos en la imagen especular del depredador.',
        "h3_2": "El Amor como Acto Radical",
        "p2": 'En un mundo diseñado para mantenernos en "Modo Supervivencia" y en silos de "Divide y Vencerás", el amor es el último acto de rebelión. Es la negativa a deshumanizar al otro, incluso cuando el sistema lo exige. El amor radical es la comprensión de que nuestra liberación está ligada a la liberación de cualquier otro ser humano, desde Gaza hasta la calle donde vives.',
        "h3_3": "El Pacifismo no es Pasividad",
        "p3": 'Ser pacifista no significa no hacer nada. Significa negarse a participar en la "Máquina de Extracción". Significa construir "Comunidades Radicales" y redes de "Ayuda Mutua" que hagan que el 1% sea obsoleto. Es la fuerza para estar en la "luz de la cueva" e invitar a otros a entrar, sin necesidad de un "Mito del Héroe" o un arma.',
        "li1": "<strong>Resiliencia Collectiva:</strong> Ganamos manteniéndonos unidos, no destrozándonos unos a otros.",
        "li2": '<strong>El Poder de la Empatía:</strong> La empatía es la única herramienta "neurodivergente" que el 1% no puede replicar ni controlar.',
        "li3": "<strong>Romper la Cadena:</strong> Al elegir el amor, detenemos la transmisión del trauma sistémico a la siguiente generación.",
        "quote": '"El amor es la única fuerza capaz de transformar a un enemigo en un amigo. Es la única venganza que realmente cambia el mundo".',
        "footer_about": "Acerca de & Republicación",
        "footer_source": "Código Fuente",
        "lang_name": "Español"
    },
    "pt": {
        "lang_attr": 'lang="pt"',
        "title": "O Amor como Vingança - Quebrando o Ciclo da Violência",
        "h1": "O Amor é a Única Vingança",
        "h2": "Quebrando o Ciclo da Violência Sistêmica",
        "h3_1": "O Fracasso da Violência",
        "p1": 'A história ensinou-nos uma lição repetitiva e brutal: a violência só leva a mais violência. O "Comércio de Armas" e o sistema do 1% prosperam no conflito porque este justifica a sua existência e alimenta os seus lucros. Quando respondemos à violência com violência, estamos a jogar pelas regras da própria máquina que nos oprime. Tornamo-nos a imagem espelhada do predador.',
        "h3_2": "O Amor como Ato Radical",
        "p2": 'Num mundo desenhado para nos manter em "Modo de Sobrevivência" e em silos de "Dividir e Conquistar", o amor é o ato final de rebeldia. É a recusa em desumanizar o outro, mesmo quando o sistema o exige. O amor radical é a percepção de que a nossa libertação está ligada à libertação de todos os outros seres humanos, de Gaza à rua onde vivemos.',
        "h3_3": "O Pacifismo Não é Passividade",
        "p3": 'Ser pacifista não significa não fazer nada. Significa recusar participar na "Máquina de Extração". Significa construir "Comunidades Radicais" e redes de "Ajuda Mútua" que tornem o 1% obsoleto. É a força para estar na "luz da caverna" e convidar outros a entrar, sem a necessidade de um "Mito do Herói" ou de uma arma.',
        "li1": "<strong>Resiliência Coletiva:</strong> Ganhamos mantendo-nos unidos, não nos destruindo uns aos outros.",
        "li2": '<strong>O Poder da Empatia:</strong> A empatia é a única ferramenta "neurodivergente" que o 1% não consegue replicar ou controlar.',
        "li3": "<strong>Quebrar a Corrente:</strong> Ao escolher o amor, travamos a transmissão do trauma sistémico para a geração seguinte.",
        "quote": '"O amor é la única força capaz de transformar um inimigo num amigo. É a única vingança que realmente muda o mundo."',
        "footer_about": "Sobre & Republicação",
        "footer_source": "Código Fonte",
        "lang_name": "Português"
    },
    "ar": {
        "lang_attr": 'lang="ar" dir="rtl"',
        "title": "الحب كأنتقام - كسر حلقة العنف",
        "h1": "الحب هو الانتقام الوحيد",
        "h2": "كسر حلقة العنف المنهجي",
        "h3_1": "فشل العنف",
        "p1": 'لقد علمنا التاريخ درساً وحشياً متكرراً: العنف لا يؤدي إلا إلى مزيد من العنف. تزدهر "تجارة الأسلحة" ونظام الـ 1% بالصراعات لأنها تبرر وجودهم وتغذي أرباحهم. عندما نواجه العنف بالعنف، فإننا نلعب وفقاً لقواعد الآلة نفسها التي تضطهدنا. نصبح صورة طبق الأصل للمفترس.',
        "h3_2": "الحب كفعل جذري",
        "p2": 'في عالم صُمم لإبقائنا في "وضع البقاء" وفي صوامع "فرق تسد"، فإن الحب هو أسمى فعل من أفعال التمرد. إنه رفض تجريد الآخر من إنسانيته، حتى عندما يطالب النظام بذلك. الحب الجذري هو الإدراك بأن تحررنا مرتبط بتحرر كل إنسان آخر، من غزة إلى الشارع الذي تعيش فيه.',
        "h3_3": "المسالمة ليست سلبية",
        "p3": 'كونك مسالماً لا يعني عدم القيام بأي شيء. بل يعني رفض المشاركة في "آلة الاستخراج". يعني بناء "مجتمعات جذرية" وشبكات "دعم متبادل" تجعل الـ 1% عفا عليها الزمن. إنها القوة للوقوف في "نور الكهف" ودعوة الآخرين للدخول، دون الحاجة إلى "أسطورة البطل" أو سلاح.',
        "li1": "<strong>المرونة الجماعية:</strong> ننتصر بالبقاء معاً، وليس بتمزيق بعضنا البعض.",
        "li2": '<strong>قوة التعاطف:</strong> التعاطف هو الأداة "العصبية المتنوعة" الوحيدة التي لا يستطيع الـ 1% محاكاتها أو التحكم فيها.',
        "li3": "<strong>كسر السلسلة:</strong> باختيار الحب، نوقف انتقال الصدمات المنهجية إلى الجيل القادم.",
        "quote": '"الحب هو القوة الوحيدة القادرة على تحويل العدو إلى صديق. إنه الانتقام الوحيد الذي يغير العالم حقاً."',
        "footer_about": "حول وإعادة النشر",
        "footer_source": "كود المصدر",
        "lang_name": "العربية",
        "extra_head": '<link href="https://fonts.googleapis.com/css2?family=Amiri&family=Inter:wght@300;400;700&display=swap" rel="stylesheet">\n    <style>\n        body { font-family: \'Amiri\', serif, \'Inter\', sans-serif; }\n    </style>'
    },
    "zh": {
        "lang_attr": 'lang="zh-CN"',
        "title": "爱作为报复 - 打破暴力循环",
        "h1": "爱是唯一的报复",
        "h2": "打破系统性暴力的循环",
        "h3_1": "暴力的失败",
        "p1": "历史教会了我们一个重复而残酷的教训：暴力只会导致更多的暴力。“武器贸易”和1%的系统在冲突中茁壮成长，因为冲突证明了它们存在的合理性并增加了它们的利润。当我们用暴力回击暴力时，我们就是在按照压迫我们的机器的规则行事。我们成了掠夺者的镜像。",
        "h3_2": "爱作为一种激进的行为",
        "p2": "在一个旨在让我们处于“生存模式”和“分而治之”孤岛的世界中，爱是终极的背叛行为。它是拒绝将他人非人化，即使系统要求这样做。激进的爱是意识到我们的解放与每一个其他人的解放息息相关，从加沙到你居住的街道。",
        "h3_3": "和平主义不是被动",
        "p3": "成为和平主义者并不意味着无所作为。它意味着拒绝参与“提取机器”。它意味着建立“激进社区”和“互助”网络，使那1%变得过时。它是站在“洞穴之光”中并邀请他人加入的力量，而不需要“英雄神话”或武器。",
        "li1": "<strong>集体韧性：</strong>我们通过团结一致而获胜，而不是通过互相撕裂。",
        "li2": "<strong>共情的力量：</strong>共情是那1%无法复制或控制的唯一“神经多样性”工具。",
        "li3": "<strong>打破连锁：</strong>通过选择爱，我们停止了系统性创伤向下一代的传递。",
        "quote": "“爱是唯一能够将敌人转化为朋友的力量。它是唯一能真正改变世界的报复。”",
        "footer_about": "关于和重新发布",
        "footer_source": "源代码",
        "lang_name": "中文",
        "extra_head": '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;700&display=swap" rel="stylesheet">\n    <style>\n        body { font-family: \'Noto Sans SC\', sans-serif, \'Inter\'; }\n    </style>'
    }
}

template = """<!DOCTYPE html>
<html {lang_attr}>
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
        <img src="https://s.france24.com/media/display/c5d994bc-8632-11f0-9045-005056bf30b7/w:1280/p:16x9/000-72WT8F3.jpg" alt="Love as Revenge" class="header-image">
        <h1>{h1}</h1>
        <h2>{h2}</h2>
    </header>

    <nav class="navbar">
        <!-- Placeholder for Nav -->
    </nav>

    <main>
        <section>
            <h3>{h3_1}</h3>
            <p>{p1}</p>
        </section>

        <section>
            <h3>{h3_2}</h3>
            <p>{p2}</p>
        </section>

        <section>
            <h3>{h3_3}</h3>
            <p>{p3}</p>
            <ul>
                <li>{li1}</li>
                <li>{li2}</li>
                <li>{li3}</li>
            </ul>
        </section>

        <blockquote>
            {quote}
        </blockquote>
    </main>

    <footer>
        <p>&copy; 2026 Justice For Gaza Manifesto | <a href="republish-{lang}.html">{footer_about}</a> | <a href="https://github.com/TimGeyssens/JusticeForGaza">{footer_source}</a></p>
    </footer>
</body>
</html>
"""

for lang, data in languages.items():
    file_path = f"/Users/u0174419/manifest/love-revenge-{lang}.html"
    content = template.format(
        lang_attr=data["lang_attr"],
        title=data["title"],
        h1=data["h1"],
        h2=data["h2"],
        h3_1=data["h3_1"],
        p1=data["p1"],
        h3_2=data["h3_2"],
        p2=data["p2"],
        h3_3=data["h3_3"],
        p3=data["p3"],
        li1=data["li1"],
        li2=data["li2"],
        li3=data["li3"],
        quote=data["quote"],
        lang=lang,
        footer_about=data["footer_about"],
        footer_source=data["footer_source"],
        extra_head=data.get("extra_head", "")
    )
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {file_path}")
