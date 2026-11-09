# -*- coding: utf-8 -*-
"""Dalîl — cartes de preuves : Coran et Sunna uniquement.
Aucune citation de prédicateur contemporain, aucun avis personnel.
Référence toujours indiquée ; numéro seulement quand il est certain.
"""

STACKS = [
 {"id":"usul","n":"Les trois fondements","e":"①","c":"#0E7C5A",
  "d":"Le parcours d'entrée : qui est ton Seigneur, quelle est ta religion, qui est ton prophète."},
 {"id":"kitab","n":"Kitâb at-Tawhîd","e":"②","c":"#127A6B",
  "d":"Ce qui établit l'unicité, et ce qui l'annule — chapitre par chapitre."},
 {"id":"aqida","n":"La 'aqîda","e":"③","c":"#2E6B8F",
  "d":"Les piliers de la foi, le décret, les anges, le Jour dernier, la voie des premières générations."},
 {"id":"sira","n":"La Sîra","e":"④","c":"#8A6A2F",
  "d":"La vie du Prophète ﷺ, étape par étape, appuyée sur le Coran et les récits authentiques."},
 {"id":"prophetes","n":"Les prophètes","e":"⑤","c":"#6B5B95",
  "d":"D'Âdam à 'Îsâ : ce que le Coran rapporte de chacun, et ce qu'il en tire."},
 {"id":"tahara","n":"La purification","e":"⑥","c":"#1F7A9B",
  "d":"Wudû', ghusl, tayammum : les textes qui fixent les conditions."},
 {"id":"salat","n":"La prière","e":"⑦","c":"#B4652F",
  "d":"Les horaires, les piliers, la communauté, le rattrapage — par les textes."},
 {"id":"ibadat","n":"Jeûne, zakât, hajj","e":"⑧","c":"#5B7C3F",
  "d":"Les trois autres piliers, avec leurs versets et leurs hadiths."},
 {"id":"rappel","n":"Rappels","e":"⑨","c":"#A03A5B",
  "d":"Ce qui remet le cœur en place : la mort, la balance, le dhikr, la confiance."},
 {"id":"hadiths","n":"Hadiths fondateurs","e":"⑩","c":"#7A6A4F",
  "d":"Les hadiths qui résument la religion, texte par texte."},
 {"id":"famille","n":"Mariage & famille","e":"⑪","c":"#B05070",
  "d":"Le contrat, les droits, la vie commune : ce que disent les textes."},
 {"id":"akhlaq","n":"Caractère & éducation","e":"⑫","c":"#3F7A6B",
  "d":"L'akhlâq du Prophète ﷺ et la manière d'élever un enfant."},
]

C = []
def c(s, t, q, a, src, act="", ty="Coran"):
    C.append({"id":f"{s}{len(C)+1:03d}", "s":s, "t":t, "q":q, "a":a, "src":src, "act":act, "ty":ty})

# ═══════════ 1. LES TROIS FONDEMENTS ═══════════
c("usul","Les quatre obligations",
  "Quelles sont les quatre choses que tout musulman doit connaître et pratiquer ?",
  "La science, l'action, l'appel à Allah, et la patience dans l'épreuve. La sourate al-'Asr les réunit en trois versets : croire, agir, s'enjoindre mutuellement la vérité et la patience.",
  "Coran, 103:1-3","Réciter al-'Asr et nommer les quatre obligations.")
c("usul","Le but de la création",
  "Pourquoi Allah a-t-il créé les hommes et les djinns ?",
  "Pour être adoré seul : « Je n'ai créé les djinns et les hommes que pour qu'ils M'adorent. » L'adoration est la fonction de la créature, pas un supplément.",
  "Coran, 51:56","Écrire ce verset et le garder visible.")
c("usul","Le premier fondement",
  "Quel est le premier des trois fondements ?",
  "La connaissance d'Allah : savoir qu'Il est le Seigneur, le Créateur, Celui qui pourvoit — et qu'Il n'a aucun associé dans l'adoration.",
  "Al-Usûl ath-Thalâtha, Muhammad ibn 'Abd al-Wahhâb","Citer trois signes de la création qui prouvent Son existence.")
c("usul","Le deuxième fondement",
  "Quel est le deuxième fondement ?",
  "La connaissance de l'islam, avec ses cinq piliers : la double attestation, la prière, la zakât, le jeûne, le pèlerinage.",
  "Al-Usûl ath-Thalâtha ; Coran, 2:43","Vérifier lequel des cinq je pratique le moins bien.")
c("usul","Le troisième fondement",
  "Quel est le troisième fondement ?",
  "La connaissance du Prophète Muhammad ﷺ : son nom, sa lignée, sa naissance, sa mission, et ce qu'il a apporté.",
  "Al-Usûl ath-Thalâtha ; Coran, 33:40","Raconter en trois phrases qui il était.")
c("usul","Les cinq piliers",
  "Sur quoi l'islam est-il bâti ?",
  "« L'islam est bâti sur cinq : l'attestation qu'il n'y a de divinité qu'Allah et que Muhammad est Son messager, la prière, la zakât, le jeûne du Ramadan et le pèlerinage. »",
  "Sahîh al-Bukhârî, n° 8 ; Sahîh Muslim, n° 16","Les réciter dans l'ordre du hadith.","Hadith")
c("usul","Les six piliers de la foi",
  "Quels sont les six piliers de l'iman ?",
  "Croire en Allah, en Ses anges, en Ses livres, en Ses messagers, au Jour dernier, et au décret — le bon et le mauvais.",
  "Sahîh Muslim, n° 8 (hadith Jibrîl)","Écrire celui qui me pose le plus de difficulté.","Hadith")
c("usul","L'ihsân",
  "Qu'est-ce que l'ihsân ?",
  "« Adorer Allah comme si tu Le voyais, car si tu ne Le vois pas, Lui te voit. » Le degré le plus haut : l'adoration en conscience.",
  "Sahîh Muslim, n° 8","Prier une fois aujourd'hui en pensant qu'Allah me voit.","Hadith")
c("usul","Le pacte originel",
  "Quel pacte avons-nous tous pris avant notre venue ici-bas ?",
  "« Ne suis-je pas votre Seigneur ? Ils dirent : si, nous en témoignons. » Témoignage tiré de nous-mêmes, pour que nul ne puisse dire qu'il l'ignorait.",
  "Coran, 7:172","Se rappeler ce pacte avant un choix difficile.")
c("usul","Connaître Allah par Ses signes",
  "Comment le Coran invite-t-il à connaître Allah ?",
  "Par la réflexion sur la création : « Nous leur montrerons Nos signes dans les horizons et en eux-mêmes, jusqu'à ce qu'il leur apparaisse que c'est la vérité. »",
  "Coran, 41:53","Observer un signe aujourd'hui : ciel, plante, corps.")
c("usul","La science obligatoire",
  "Quelle est la première science à acquérir ?",
  "« Sache donc qu'il n'y a de divinité qu'Allah, et implore le pardon pour ton péché. » La connaissance de l'unicité précède l'action.",
  "Coran, 47:19","Apprendre une preuve de l'unicité aujourd'hui.")
c("usul","L'appel commence par le tawhîd",
  "Par quoi le Prophète ﷺ a-t-il ordonné de commencer l'appel ?",
  "« Que la première chose à laquelle tu les appelles soit qu'ils n'adorent qu'Allah. »",
  "Sahîh al-Bukhârî, n° 4347 ; Sahîh Muslim, n° 19","Corriger une idée fausse sur l'unicité chez un proche.","Hadith")
c("usul","Les trois questions du tombeau",
  "Quelles sont les trois questions posées après la mort ?",
  "Qui est ton Seigneur ? Quelle est ta religion ? Qui est ton prophète ? Et les réponses sont exactement les trois fondements.",
  "Sunan Abî Dâwûd, n° 4753 ; hadith de la fitra","Répéter les trois réponses à voix haute aujourd'hui.","Hadith")
c("usul","La résurrection",
  "Quelle preuve du Coran sur la résurrection ?",
  "« Allah vous fera mourir, puis vous ressuscitera au Jour de la Résurrection, sans aucun doute. »",
  "Coran, 22:7","Retenir : la résurrection est citée avec la création.")
c("usul","La constance dans le peu",
  "Que vaut un petit acte constant ?",
  "« Les actes les plus aimés d'Allah sont les plus constants, même s'ils sont peu. » La quantité ne sauve pas, la régularité oui.",
  "Sahîh al-Bukhârî, n° 6464 ; Sahîh Muslim, n° 783","Choisir un acte minuscule et le faire 7 jours.","Hadith")

# ═══════════ 2. KITÂB AT-TAWHÎD ═══════════
c("kitab","Le du'â est adoration",
  "Quel est le statut de l'invocation ?",
  "« L'invocation, c'est l'adoration. » Le du'â est l'acte même de la servitude : l'adresser à un autre qu'Allah, c'est lui donner une part du droit d'Allah.",
  "Jâmi' at-Tirmidhî, n° 3372 ; Coran, 40:60","Formuler une du'â aujourd'hui sans demander de bien matériel.","Hadith")
c("kitab","Invoquer autre qu'Allah",
  "Que dit le Coran de celui qui invoque autre qu'Allah ?",
  "« Ce que vous invoquez en dehors d'Allah ne peut vous créer une mouche, même s'ils s'y mettaient ensemble. » L'impuissance de l'objet adoré prouve l'absurdité du shirk.",
  "Coran, 22:73","Relire le verset en pensant aux « idoles » d'aujourd'hui.")
c("kitab","L'amulette",
  "Peut-on porter un objet pour se protéger ?",
  "« Celui qui porte une amulette a commis du shirk. » L'objet ne protège pas ; y attacher son cœur, c'est en faire une divinité.",
  "Musnad Ahmad, n° 17422 ; jugé sahîh par al-Albânî","Regarder ce que je porte ou garde « pour la chance ».","Hadith")
c("kitab","La peur du shirk",
  "Pourquoi Ibrâhîm craignait-il le shirk pour lui-même ?",
  "« Seigneur, éloigne-moi et mes fils de l'adoration des idoles. » Si l'ami d'Allah demande protection, personne ne peut se croire à l'abri.",
  "Coran, 14:35","Demander la préservation du shirk matin et soir.")
c("kitab","Le mot « et »",
  "Peut-on dire « ce que Allah et untel ont voulu » ?",
  "Non. Le Prophète ﷺ a interdit cette formule et l'a remplacée : « ce qu'Allah a voulu, puis ce qu'untel a voulu ». Le « et » met le serviteur à côté d'Allah.",
  "Sunan Abî Dâwûd, n° 4980","Repérer ce « et » dans mes phrases.","Hadith")
c("kitab","La sorcellerie",
  "Quel est le statut de la sorcellerie ?",
  "C'est une mécréance, et l'un des sept péchés destructeurs : elle prétend agir sur le destin par un pouvoir autre que celui d'Allah.",
  "Coran, 2:102 ; Sahîh al-Bukhârî, n° 2766","Ne pas consulter de voyant, même sans y croire.")
c("kitab","Juger par autre qu'Allah",
  "Que dit le Coran sur le jugement par autre chose que la révélation ?",
  "« Ceux qui ne jugent pas selon ce qu'Allah a révélé, ceux-là sont les mécréants. » Le verset est général, il ne distingue pas le détail du principe.",
  "Coran, 5:44","Vérifier à qui je demande de trancher mes conflits.")
c("kitab","L'amour prouvé",
  "Comment prouve-t-on l'amour d'Allah ?",
  "« Si vous aimez Allah, suivez-moi : Allah vous aimera. » L'amour se prouve par le suivi de la sunna, pas par l'émotion.",
  "Coran, 3:31","Choisir une sunna que je ne pratique pas et la faire.")
c("kitab","L'ostentation",
  "Quel shirk est le plus à craindre pour les croyants ?",
  "« Ce que je crains le plus pour vous, c'est le shirk mineur. » Ils dirent : et qu'est-ce ? Il dit : « l'ostentation » — prier ou donner pour être vu.",
  "Musnad Ahmad ; al-Adab al-Mufrad","Faire une action de bien aujourd'hui sans en parler.","Hadith")
c("kitab","Le tawakkul",
  "La confiance dispense-t-elle d'agir ?",
  "Non. À celui qui laissait sa monture sans l'attacher, il dit : « Attache-la, puis place ta confiance en Allah. »",
  "Jâmi' at-Tirmidhî, n° 2517 (hasan)","Nommer l'action que je remets à demain.","Hadith")
c("kitab","Où est Allah ?",
  "Que répondit le Prophète ﷺ à la servante qui parlait de l'élévation ?",
  "Il nous a enseigné qu'Allah est au-dessus de Sa création — et il a confirmé la réponse de la servante en la faisant affranchir.",
  "Sahîh Muslim, n° 537","Retenir le principe sans se le représenter par l'imagination.","Hadith")
c("kitab","Les noms parfaits",
  "Que dit le Coran des noms d'Allah ?",
  "« À Allah appartiennent les noms les plus beaux : invoquez-Le par eux. » Les noms ne sont pas des métaphores poétiques : ils sont l'objet de l'invocation.",
  "Coran, 7:180","Apprendre trois noms et les utiliser en du'â.")
c("kitab","Le premier commandement interdit",
  "Quel est le premier interdit cité dans le Coran ?",
  "« Ne placez pas à côté d'Allah des divinités : je suis pour vous, de Sa part, un avertisseur clair. » Le shirk ouvre la série des interdits.",
  "Coran, 51:51","Nommer la chose qui prend le plus de place dans mon cœur.")
c("kitab","La mosquée fondée sur la piété",
  "Quel verset distingue la mosquée de Qubâ' ?",
  "« Une mosquée fondée sur la piété dès le premier jour est plus digne que tu y fasses la prière. » Le lieu compte, l'intention aussi.",
  "Coran, 9:108","Vérifier l'intention avec laquelle j'entre à la mosquée.")
c("kitab","Le droit du voisin",
  "Quel est le droit du voisin ?",
  "« Il n'est pas croyant, celui qui passe la nuit rassasié alors que son voisin a faim. » La foi ne se sépare pas de la faim de l'autre.",
  "Al-Adab al-Mufrad, al-Bukhârî, n° 112","Demander à mon voisin s'il a besoin de quelque chose.","Hadith")
c("kitab","Les trois catégories",
  "Quelles sont les trois catégories du tawhîd ?",
  "Ar-Rubûbiyya (créer, pourvoir), al-Ulûhiyya (adorer), al-Asmâ' wa-s-Sifât (connaître). Les associateurs reconnaissaient la première et rejetaient la deuxième.",
  "Kitâb at-Tawhîd ; Coran, 29:61-63","Écrire un exemple de chaque catégorie dans ma vie.")

# ═══════════ 3. 'AQÎDA ═══════════
c("aqida","Le décret",
  "Que dit le Coran du décret ?",
  "« Nous avons créé toute chose selon un décret. » Rien n'échappe à la mesure et à la volonté d'Allah, y compris ce qui nous paraît injuste.",
  "Coran, 54:49","Distinguer ce que je peux changer de ce que je dois accepter.")
c("aqida","Voir Allah",
  "Les croyants verront-ils Allah au Paradis ?",
  "« Ce jour-là, il y aura des visages resplendissants, regardant leur Seigneur. » C'est une vision réelle, sans embrasser Allah dans un corps.",
  "Coran, 75:22-23 ; Sahîh Muslim, n° 267","Retenir : la vision est réelle, sans comparaison.")
c("aqida","Les anges",
  "Que dit le Coran des anges ?",
  "« Ils ne désobéissent pas à Allah pour ce qu'Il leur ordonne, et font ce qui leur est commandé. » Des créatures de lumière, sans sexe, sans descendance.",
  "Coran, 66:6 ; 35:1","Retenir : deux gardiens écrivent mes actes.")
c("aqida","Les livres révélés",
  "Que dit le Coran des livres révélés ?",
  "« Il a fait descendre sur toi le Livre avec la vérité, confirmant ce qui était avant lui : la Thora et l'Évangile. » Le Coran confirme et clôt.",
  "Coran, 3:3 ; 5:48","Retenir : le Coran est le critère, pas l'inverse.")
c("aqida","L'innovation",
  "Que dit le Prophète ﷺ de l'innovation en religion ?",
  "« Toute innovation est un égarement, et tout égarement est dans le Feu. » Ce qui n'a pas de fondement dans la révélation ne devient pas une adoration par la bonne intention.",
  "Sahîh Muslim, n° 867 ; Sunan Abî Dâwûd, n° 4607","Vérifier qu'un acte que je fais a bien un fondement.","Hadith")
c("aqida","S'attacher à la sunna",
  "Que recommande le Prophète ﷺ dans son dernier discours ?",
  "« Je vous laisse deux choses : le Livre d'Allah et ma Sunna ; vous ne vous égarerez pas tant que vous vous y tiendrez. »",
  "Al-Muwatta' ; Sahîh Muslim, n° 1218","Choisir une sunna délaissée et la pratiquer.","Hadith")
c("aqida","Les trois générations",
  "Quelles générations servent de référence ?",
  "« Les meilleurs des gens sont ma génération, puis ceux qui les suivent, puis ceux qui les suivent. » La compréhension des salaf est le critère de l'innovation.",
  "Sahîh al-Bukhârî, n° 2652 ; Sahîh Muslim, n° 2533","Comparer une pratique avec ce que les salaf en ont dit.","Hadith")
c("aqida","L'iman augmente",
  "La foi peut-elle augmenter et diminuer ?",
  "Oui : « Ceux dont les cœurs frémissent quand on mentionne Allah, et dont la foi augmente à la lecture de Ses versets. » L'iman est parole, acte et état du cœur.",
  "Coran, 8:2","Évaluer honnêtement mon iman cette semaine.")
c("aqida","Ne pas se précipiter sur le takfîr",
  "Que dit le Prophète ﷺ du jugement sur la foi d'autrui ?",
  "« Celui qui traite son frère de mécréant, et il ne l'est pas, le propos retombe sur lui. » La prudence est une obligation, pas une politesse.",
  "Sahîh al-Bukhârî, n° 6104 ; Sahîh Muslim, n° 60","S'abstenir de juger la foi d'une personne.","Hadith")
c("aqida","Les annulatifs",
  "Quel est le seul péché que Allah ne pardonne pas ?",
  "« Allah ne pardonne pas qu'on Lui associe quoi que ce soit, mais Il pardonne ce qui est moindre, à qui Il veut. » Le shirk non suivi de repentir est la seule porte fermée.",
  "Coran, 4:48","Faire istighfâr pour tout ce qui touche à l'unicité.")
c("aqida","L'unité des croyants",
  "Que dit le Coran de l'unité ?",
  "« Attachez-vous tous à la corde d'Allah, et ne vous divisez pas. » L'unité a un critère : la corde d'Allah, pas la ressemblance.",
  "Coran, 3:103","Reparer un lien rompu avec un frère.")
c("aqida","Le Jour dernier",
  "Que dit le Coran du Jour de la Résurrection ?",
  "« Tout ce qui est sur elle disparaîtra, et seule restera la Face de ton Seigneur, plein de majesté et de noblesse. » Tout ce qui est créé s'efface.",
  "Coran, 55:26-27","Nommer une chose dont je m'occupe trop.")
c("aqida","Le sirât et la balance",
  "Comment le Coran décrit-il la pesée ?",
  "« Celui dont les balances seront lourdes aura une vie agréable ; et celui dont les balances seront légères, sa mère sera Hâwiya. »",
  "Coran, 101:6-9","Faire un petit acte dont le poids sera lourd.")
c("aqida","Al-walâ' wa-l-barâ'",
  "Quel est le principe d'alliance et de désaveu ?",
  "« Ô vous qui croyez, prenez pour alliés Allah, Son messager et les croyants. » L'alliance se fonde sur la foi, pas sur la famille ou l'origine.",
  "Coran, 5:55-56 ; 60:4","Vérifier sur quoi se fonde une de mes amitiés.")
c("aqida","Les limites de la raison",
  "La raison contredit-elle la révélation ?",
  "Non : « Ce que le Messager vous donne, prenez-le ; et ce qu'il vous interdit, abstenez-vous. » La raison comprend l'ordre, elle ne le remplace pas.",
  "Coran, 59:7 ; Ibn Taymiyya, Dar' Ta'ârud al-'Aql wa-n-Naql","Accepter aujourd'hui un texte qui me résiste.")
c("aqida","La prière du malade",
  "Comment prier en cas de maladie ?",
  "Le Prophète ﷺ a ordonné : « Prie debout ; si tu ne peux pas, assis ; si tu ne peux pas, sur le côté. » La facilité est prévue, le texte le dit.",
  "Sahîh al-Bukhârî, n° 1117","Retenir la gradation : debout, assis, sur le côté.","Hadith")

# ═══════════ 4. SÎRA ═══════════
c("sira","La naissance",
  "Où et quand le Prophète ﷺ est-il né ?",
  "À La Mecque, en l'an de l'Éléphant (vers 570). Son père 'Abdullâh meurt avant sa naissance.",
  "Ar-Rahîq al-Makhtûm ; Ibn Kathîr, Al-Bidâya wa-n-Nihâya","Retenir les quatre dates : 570, 610, 622, 632.","Hadith")
c("sira","L'orphelin",
  "Quel verset rappelle l'enfance du Prophète ﷺ ?",
  "« Ne t'a-t-Il pas trouvé orphelin, et Il t'a donné refuge ? » Sa propre histoire est un rappel de la miséricorde.",
  "Coran, 93:6","Lire la sourate 93 en entier.")
c("sira","Le premier verset",
  "Quel est le premier verset révélé ?",
  "« Lis, au nom de ton Seigneur qui a créé, qui a créé l'homme d'une adhérence. Lis, et ton Seigneur est le plus généreux. »",
  "Coran, 96:1-3 ; Sahîh al-Bukhârî, n° 3","Lire ces versets à voix haute.")
c("sira","La grotte de Hirâ",
  "Que s'est-il passé dans la grotte de Hirâ ?",
  "À quarante ans, Jibrîl vient et lui dit : « Lis ! » Il répondit : « Je ne sais pas lire. » L'ange le serra trois fois, puis récita les premiers versets.",
  "Sahîh al-Bukhârî, n° 3","Se rappeler : la révélation commence par un ordre de lecture.","Hadith")
c("sira","Avertir les proches",
  "Quel est le premier appel public ?",
  "« Lève-toi et avertis ! » — d'abord les proches, puis la ville. La méthode prophétique commence par le proche.",
  "Coran, 74:1-2 ; 26:214","Parler de l'unicité à un membre de ma famille.","Hadith")
c("sira","L'opposition",
  "Sur quoi portait la première opposition ?",
  "Sur l'unicité, pas sur la morale : « Il ne fait que vous diviser », disaient-ils. Le tawhîd est ce qui dérange le plus.",
  "Coran, 38:4-5","Analyser où se situe la vraie résistance chez moi.")
c("sira","L'émigration en Abyssinie",
  "Pourquoi les premiers musulmans ont-ils émigré en Abyssinie ?",
  "Pour fuir la persécution : le Négus était juste et n'opprimait personne. La hijra fut un refuge, pas une fuite de la foi.",
  "Ar-Rahîq al-Makhtûm","Retenir : chercher un lieu où l'on peut pratiquer.")
c("sira","Al-Isrâ' wa-l-Mi'râj",
  "Que dit le Coran du voyage nocturne ?",
  "« Gloire à Celui qui a fait voyager de nuit Son serviteur de la Mosquée sacrée à la Mosquée lointaine. » Un miracle, et l'occasion des cinq prières.",
  "Coran, 17:1","Retenir le lien : voyage nocturne → cinq prières.")
c("sira","Les serments d'al-'Aqaba",
  "Qu'ont fait les gens de Médine avant la hijra ?",
  "Ils ont prêté serment de soutenir le Prophète ﷺ et de le défendre, puis ils l'ont accueilli. La hijra est préparée par des engagements tenus.",
  "Ar-Rahîq al-Makhtûm","Tenir un engagement que j'ai pris.")
c("sira","La caverne de Thawr",
  "Que dit Abû Bakr dans la grotte ?",
  "Il s'inquiéta pour le Prophète ﷺ, qui répondit : « Ne t'afflige pas, Allah est avec nous. » Le verset est dans le Coran.",
  "Coran, 9:40 ; Sahîh al-Bukhârî, n° 3653","Relire 9:40 et le mémoriser.","Hadith")
c("sira","La mosquée de Médine",
  "Quelle est la première construction à Médine ?",
  "La mosquée, avant même la maison. Le centre du message est le lieu de l'adoration et de l'enseignement.",
  "Ar-Rahîq al-Makhtûm","Évaluer la place de la mosquée dans ma semaine.")
c("sira","Badr",
  "Que dit le Coran de la victoire de Badr ?",
  "« Allah vous a secourus à Badr alors que vous étiez humiliés. » 313 hommes face à un millier : la victoire n'est attribuée ni au nombre ni à l'habileté.",
  "Coran, 3:123","Retenir : 313, an 2 H.")
c("sira","Uhud",
  "Quelle leçon tire le Coran d'Uhud ?",
  "« Vous avez désobéi au Messager après qu'il vous eut montré ce que vous aimez. » L'épreuve vient après la victoire, quand on abandonne l'ordre pour le gain.",
  "Coran, 3:152","Identifier une règle que j'abandonne pour un profit.")
c("sira","Al-Hudaybiyya",
  "Que dit Allah du traité d'al-Hudaybiyya ?",
  "« Nous t'avons accordé une victoire éclatante. » Une paix aux conditions difficiles, et pourtant une victoire : la sagesse ne se voit pas dans l'instant.",
  "Coran, 48:1","Retenir : une paix imparfaite peut valoir mieux qu'un conflit gagné.")
c("sira","La conquête de La Mecque",
  "Que dit le Prophète ﷺ aux Mecquois vaincus ?",
  "« Allez, vous êtes libres. » Il pardonne à ceux qui l'ont persécuté pendant vingt ans.",
  "Ar-Rahîq al-Makhtûm ; Ibn Hishâm","Pardonner à une personne qui m'a fait du tort.")
c("sira","Le pèlerinage d'adieu",
  "Que dit-il dans son dernier sermon ?",
  "Il déclare sacrés le sang, les biens et l'honneur, rappelle qu'aucun n'est supérieur à un autre sinon par la piété, et laisse le Livre et la Sunna.",
  "Sahîh Muslim, n° 1218 ; Sahîh al-Bukhârî, n° 1739","Relire l'idée d'égalité : c'est un principe, pas un sentiment.","Hadith")
c("sira","La mort",
  "Quand le Prophète ﷺ est-il mort ?",
  "En l'an 11 de l'hégire, à Médine, à 63 ans. Ses dernières paroles évoquent la prière et ce que la communauté doit à ses proches.",
  "Ar-Rahîq al-Makhtûm ; Sahîh al-Bukhârî","Retenir : 632, à 63 ans.","Hadith")

# ═══════════ 5. LES PROPHÈTES ═══════════
c("prophetes","Âdam",
  "Quelle est la parole d'Âdam après la faute ?",
  "« Seigneur, nous avons été injustes envers nous-mêmes ; si Tu ne nous pardonnes pas et ne nous fais pas miséricorde, nous serons parmi les perdants. » Le modèle est la reconnaissance, pas l'excuse.",
  "Coran, 7:23","Reconnaître une faute sans la justifier.")
c("prophetes","Nûh",
  "Combien de temps Nûh a-t-il appelé son peuple ?",
  "« Il demeura parmi eux mille ans moins cinquante. » Et peu crurent. La constance n'est pas jugée au résultat.",
  "Coran, 29:14","Reprendre une action juste abandonnée trop vite.")
c("prophetes","Ibrâhîm et les idoles",
  "Comment Ibrâhîm a-t-il réfuté l'adoration des idoles ?",
  "En brisant les idoles sauf la plus grande, pour forcer son peuple à reconnaître leur impuissance : ce qui ne peut se défendre ne peut rien pour vous.",
  "Coran, 21:51-67","Nommer une « idole » moderne à laquelle je tiens.")
c("prophetes","Le feu qui refroidit",
  "Que dit Allah au feu d'Ibrâhîm ?",
  "« Ô feu, sois fraîcheur et paix sur Ibrâhîm. » La protection vient de l'ordre d'Allah, pas de la force de la créature.",
  "Coran, 21:69","Retenir l'image : le feu perd sa nature par l'ordre d'Allah.")
c("prophetes","Le sacrifice",
  "Quel acte d'Ibrâhîm est retenu par le Coran ?",
  "Sa disposition à sacrifier son fils, et la substitution : « Nous l'avons racheté par un sacrifice solennel. » L'obéissance passe avant l'attachement.",
  "Coran, 37:102-107","Nommer une attache qui m'empêche d'obéir.")
c("prophetes","Yûsuf et le pardon",
  "Que dit Yûsuf à ses frères ?",
  "« Il n'y a pas de reproche contre vous aujourd'hui. » Il avait le pouvoir de punir, et il a choisi de libérer.",
  "Coran, 12:92","Pardonner une petite chose explicitement.")
c("prophetes","Ayyûb",
  "Quelle est la parole d'Ayyûb dans l'épreuve ?",
  "« Le mal m'a touché, et Tu es le plus miséricordieux des miséricordieux. » Il se plaint à Allah, jamais d'Allah.",
  "Coran, 21:83","Distinguer : à qui est adressée ma plainte ?")
c("prophetes","Mûsâ envoyé",
  "Quelle du'â fait Mûsâ avant d'aller vers Pharaon ?",
  "« Seigneur, élargis ma poitrine, facilite ma tâche, dénoue ma langue. » Il demande d'abord les moyens intérieurs.",
  "Coran, 20:25-28","Réciter cette du'â avant une épreuve.")
c("prophetes","Mûsâ et le serviteur d'Allah",
  "Quelle leçon sort du récit de Mûsâ avec al-Khidr ?",
  "Que l'on ne comprend pas tout sur le moment : l'apparente injustice peut être une protection. La science d'Allah dépasse la nôtre.",
  "Coran, 18:60-82","Repenser à une épreuve dont j'ai compris le sens après.")
c("prophetes","Yûnus",
  "Que dit Yûnus dans le ventre du poisson ?",
  "« Il n'y a de divinité que Toi, gloire à Toi ! J'ai été du nombre des injustes. » C'est le tahlîl suivi de la reconnaissance de la faute.",
  "Coran, 21:87","Réciter ce rappel dans une difficulté.")
c("prophetes","'Îsâ dans le berceau",
  "Que dit 'Îsâ enfant ?",
  "« Je suis un serviteur d'Allah ; Il m'a donné le Livre et m'a fait prophète. » Un serviteur, jamais une divinité.",
  "Coran, 19:30","Retenir : serviteur et prophète.")
c("prophetes","Les 25 nommés",
  "Combien de prophètes le Coran nomme-t-il ?",
  "Vingt-cinq sont cités, et il y en a d'autres : « Nous avons envoyé des messagers dont Nous ne t'avons pas raconté l'histoire. »",
  "Coran, 6:83-86 ; 4:164","En citer dix de mémoire.")
c("prophetes","Le sceau",
  "Quel est le statut de Muhammad ﷺ ?",
  "« Muhammad n'est le père d'aucun de vos hommes, mais il est le Messager d'Allah et le sceau des prophètes. » La prophétie est close.",
  "Coran, 33:40","Retenir : aucune prophétie après lui.")
c("prophetes","Le meilleur récit",
  "Quel récit le Coran appelle-t-il « le plus beau » ?",
  "L'histoire de Yûsuf : « Nous te racontons le plus beau des récits. » Elle enseigne la patience, la jalousie, le pardon et la justice.",
  "Coran, 12:3","Lire un passage de la sourate 12 aujourd'hui.")

# ═══════════ 6. PURIFICATION ═══════════
c("tahara","Le verset de l'ablution",
  "Quel verset fixe les parties du wudû' ?",
  "« Ô vous qui croyez, quand vous vous levez pour la prière, lavez vos visages, vos mains jusqu'aux coudes, passez vos mains humides sur vos têtes, et lavez vos pieds jusqu'aux chevilles. »",
  "Coran, 5:6","Faire le wudû' en nommant chaque partie.")
c("tahara","Sans purification",
  "Que dit le Prophète ﷺ de celui qui prie sans être purifié ?",
  "« Allah n'accepte pas la prière de celui qui est en état d'impureté jusqu'à ce qu'il se purifie. » La purification n'est pas une formalité.",
  "Sahîh al-Bukhârî, n° 135 ; Sahîh Muslim, n° 224","Vérifier avant chaque prière.","Hadith")
c("tahara","Le ghusl obligatoire",
  "Dans quels cas le ghusl est-il obligatoire ?",
  "Après la relation conjugale, après la fin des menstrues et des lochies, et à l'émission de liquide séminal. Sans lui, la prière n'est pas valable.",
  "Coran, 4:43 ; 5:6","Retenir les quatre causes.")
c("tahara","Le tayammum",
  "Quand remplace-t-on l'eau par la terre ?",
  "En l'absence d'eau ou en cas de maladie : « Si vous ne trouvez pas d'eau, faites le tayammum avec une terre pure, en essuyant vos visages et vos mains. »",
  "Coran, 4:43 ; 5:6","Mémoriser les gestes, sans les improviser.")
c("tahara","Le mas-h sur les khuffayn",
  "Combien de temps peut-on essuyer les chaussettes de cuir ?",
  "Un jour et une nuit pour le résident, trois jours et trois nuits pour le voyageur, à partir du premier essuyage après des ablutions complètes.",
  "Sahîh Muslim, n° 276","Retenir les deux durées.","Hadith")
c("tahara","La propreté",
  "Quelle est la place de la purification dans la foi ?",
  "« La purification est la moitié de la foi. » « La propreté fait partie de la foi » est également rapporté ; la propreté corporelle n'est pas secondaire.",
  "Sahîh Muslim, n° 223 ; Sahîh Muslim, n° 328","Vérifier la propreté de mes vêtements pour la prière.","Hadith")
c("tahara","Le siwâk",
  "Que dit le Prophète ﷺ du brossage des dents ?",
  "« Si je ne craignais de charger ma communauté, j'aurais ordonné le siwâk à chaque prière. » La bouche propre prépare à la parole de la prière.",
  "Sahîh al-Bukhârî, n° 887 ; Sahîh Muslim, n° 252","Se brosser les dents avant la prière de l'aube.","Hadith")
c("tahara","Les ablutions avant le sommeil",
  "Que faire avant de dormir ?",
  "« Quand tu vas te coucher, fais tes ablutions comme pour la prière, puis couche-toi sur le côté droit. »",
  "Sahîh al-Bukhârî, n° 247 ; Sahîh Muslim, n° 2710","Faire le wudû' ce soir.","Hadith")
c("tahara","L'eau",
  "Quelle est la règle sur l'eau disponible ?",
  "L'eau reste pure tant que rien ne la change : couleur, goût ou odeur. La règle par défaut est la pureté, pas la suspicion.",
  "Sunan Abî Dâwûd ; Ibn 'Uthaymîn, ash-Sharh al-Mumti'","Ne pas compliquer : l'eau du robinet est pure.","Hadith")
c("tahara","Le doute après l'ablution",
  "Que faire si je doute d'avoir annulé mes ablutions ?",
  "La règle prophétique : « Qu'il ne sorte pas [de la mosquée] tant qu'il n'entend pas un son ou ne sent pas une odeur. » Le doute ne défait pas la certitude.",
  "Sahîh al-Bukhârî, n° 137","Ne pas refaire le wudû' sur un simple doute.","Hadith")

# ═══════════ 7. LA PRIÈRE ═══════════
c("salat","Les horaires",
  "Quel verset fixe les temps de prière ?",
  "« Accomplis la prière au déclin du soleil jusqu'à la nuit, et la lecture de l'aube. » Les horaires sont fixés par le texte, pas par l'habitude.",
  "Coran, 17:78","Écrire mes horaires de prière de la semaine.")
c("salat","Ce qu'on rendra en premier",
  "Quel acte est jugé en premier ?",
  "« La première chose dont le serviteur rendra compte le Jour de la Résurrection, c'est sa prière. »",
  "Jâmi' at-Tirmidhî, n° 413 ; Sunan an-Nasâ'î","Vérifier mes cinq prières trois jours de suite.","Hadith")
c("salat","Les piliers",
  "Quels sont les actes obligatoires de la prière ?",
  "La station debout, le takbîr d'entrée, la Fâtiha, l'inclinaison, le redressement, la prosternation, l'assise entre les deux, la salutation et l'ordre.",
  "Sahîh al-Bukhârî, n° 793 (hadith du mendiant)","Refaire une prière en vérifiant un pilier à la fois.","Hadith")
c("salat","La Fâtiha",
  "Que dit le Prophète ﷺ de celui qui ne récite pas la Fâtiha ?",
  "« Pas de prière pour celui qui ne récite pas la Fâtiha du Livre. » Elle est le dialogue de la prière.",
  "Sahîh al-Bukhârî, n° 756 ; Sahîh Muslim, n° 394","Réciter la Fâtiha en regardant le sens.","Hadith")
c("salat","La prière en commun",
  "Quel est le mérite de la prière en communauté ?",
  "« Elle dépasse la prière individuelle de vingt-sept degrés. » Le chiffre est précis, l'effort d'organisation est récompensé.",
  "Sahîh al-Bukhârî, n° 645 ; Sahîh Muslim, n° 650","Faire une prière à la mosquée cette semaine.","Hadith")
c("salat","Les cinq prières",
  "Que dit le hadith des cinq prières et des péchés ?",
  "« Les cinq prières, la prière du vendredi jusqu'à l'autre, et le Ramadan jusqu'à l'autre, effacent ce qui est entre eux, si l'on évite les grands péchés. »",
  "Sahîh Muslim, n° 233","Faire mes cinq prières aujourd'hui.","Hadith")
c("salat","Rattraper une prière",
  "Que faire d'une prière oubliée ?",
  "« Celui qui oublie une prière ou dort par-dessus, son expiation est de la prier quand il s'en souvient. » Pas de compensation financière, la prière.",
  "Sahîh Muslim, n° 684","Compter les prières manquées cette semaine.","Hadith")
c("salat","Le vendredi",
  "Quel est le statut de la prière du vendredi ?",
  "« Que ceux qui délaissent trois vendredis par négligence sachent qu'Allah scellera leur cœur. » C'est un rendez-vous hebdomadaire obligatoire.",
  "Sahîh Muslim, n° 865 ; Sunan Abî Dâwûd, n° 1052","Arriver tôt vendredi, téléphone éteint.","Hadith")
c("salat","Le takbîr",
  "Par quoi la prière commence-t-elle et finit-elle ?",
  "Elle commence par le takbîr et se termine par la salutation : « La clé de la prière, c'est la purification ; son entrée, le takbîr ; sa sortie, la salutation. »",
  "Sunan Abî Dâwûd, n° 61 ; at-Tirmidhî","Prier une fois en ralentissant le takbîr.","Hadith")
c("salat","La concentration",
  "Quel verset décrit les croyants qui réussissent ?",
  "« Bienheureux sont les croyants, ceux qui sont humbles dans leur prière. » La khushû' est la première qualité citée, avant les autres.",
  "Coran, 23:1-2","Prier une fois deux fois plus lentement.")
c("salat","La prière du voyageur",
  "Que fait-on en voyage ?",
  "On raccourcit les prières de quatre unités à deux (qasr), et on peut les regrouper. La facilité est légiférée pour le voyageur.",
  "Sahîh Muslim, n° 685 ; Sunan Abî Dâwûd","Retenir : qasr pour le voyageur.")
c("salat","Le witr",
  "Le witr est-il obligatoire ?",
  "Il est une sunna fortement recommandée : « Faites le witr, ô gens du Coran. » Le Prophète ﷺ ne le délaissait ni en voyage ni à la maison.",
  "Sunan Abî Dâwûd, n° 1416 ; Sahîh al-Bukhârî","Faire le witr ce soir.","Hadith")

# ═══════════ 8. JEÛNE, ZAKÂT, HAJJ ═══════════
c("ibadat","Le jeûne prescrit",
  "Quel verset institue le jeûne ?",
  "« Ô vous qui croyez, le jeûne vous a été prescrit comme il a été prescrit à ceux avant vous, afin que vous atteigniez la piété. »",
  "Coran, 2:183","Retenir la finalité : la taqwâ, pas la performance.")
c("ibadat","Le Ramadan",
  "Que dit le Coran du mois de Ramadan ?",
  "« Le mois de Ramadan, celui où le Coran a été descendu comme guidance pour les gens. » Le jeûne et la révélation sont liés.",
  "Coran, 2:185","Préparer un objectif de lecture du Coran pour le Ramadan.")
c("ibadat","Rompre par oubli",
  "Que faire si l'on mange en oubliant pendant le jeûne ?",
  "« Que celui qui mange ou boit en oubliant termine son jeûne : c'est Allah qui l'a nourri. » L'oubli n'annule pas.",
  "Sahîh al-Bukhârî, n° 1933 ; Sahîh Muslim, n° 1155","Retenir : l'oubli n'invalide pas.","Hadith")
c("ibadat","La nuit du destin",
  "Que dit le Coran de Laylat al-Qadr ?",
  "« La nuit du destin est meilleure que mille mois. » Une nuit dont la valeur dépasse une vie entière.",
  "Coran, 97:1-3","Retenir : meilleure que mille mois.")
c("ibadat","Les huit catégories",
  "À qui la zakât est-elle destinée ?",
  "« Les aumônes sont pour les pauvres, les indigents, ceux qui travaillent à leur collecte, ceux dont les cœurs sont à gagner, pour affranchir les captifs, les endettés, la cause d'Allah et le voyageur. »",
  "Coran, 9:60","Vérifier à qui je donne réellement.")
c("ibadat","La zakât, droit des pauvres",
  "Comment le Coran nomme-t-il la part des pauvres ?",
  "Un droit : « Et dans leurs biens, il y a un droit pour le mendiant et le démuni. » Ce n'est pas une générosité, c'est une dette.",
  "Coran, 51:19","Calculer ma zakât si elle est due.")
c("ibadat","L'aumône continue",
  "Quelle aumône profite après la mort ?",
  "« Quand l'homme meurt, ses actes cessent sauf trois : une aumône continue, une science dont on profite, un enfant vertueux qui prie pour lui. »",
  "Sahîh Muslim, n° 1631","Choisir une des trois et l'entreprendre.","Hadith")
c("ibadat","Le hajj",
  "Quel verset rend le pèlerinage obligatoire ?",
  "« C'est un devoir envers Allah que le pèlerinage à la Maison, pour celui qui en a les moyens. » La condition de capacité est dans le verset.",
  "Coran, 3:97","Vérifier si les conditions sont réunies pour moi.")
c("ibadat","Les dix jours",
  "Quel est le mérite des dix premiers jours de Dhû al-Hijja ?",
  "« Il n'y a pas de jours où les œuvres sont plus aimées d'Allah que ces dix jours. » Ils sont supérieurs aux autres jours de l'année.",
  "Sahîh al-Bukhârî, n° 969","Choisir une œuvre à multiplier pendant ces jours.","Hadith")
c("ibadat","Le jeûne du lundi et du jeudi",
  "Quels jours le Prophète ﷺ jeûnait-il régulièrement ?",
  "Le lundi et le jeudi : « Ce sont deux jours où les œuvres sont présentées au Seigneur de l'univers, et j'aime que mes œuvres soient présentées tandis que je jeûne. »",
  "Jâmi' at-Tirmidhî, n° 747","Jeûner un lundi ou un jeudi ce mois.","Hadith")

# ═══════════ 9. RAPPELS ═══════════
c("rappel","La mort",
  "Que dit le Coran de la mort ?",
  "« Toute âme goûtera la mort. » Ce n'est pas une menace pour les autres : c'est une certitude pour soi.",
  "Coran, 3:185","Retenir : la certitude, pas la date.")
c("rappel","Le poids d'un atome",
  "Que pèse un acte minuscule ?",
  "« Quiconque fait un atome de bien le verra, et quiconque fait un atome de mal le verra. » Rien n'est perdu, ni dans un sens ni dans l'autre.",
  "Coran, 99:7-8","Faire un atome de bien aujourd'hui.")
c("rappel","Allah n'impose rien d'impossible",
  "Que dit le Coran de la charge ?",
  "« Allah n'impose à aucune âme une charge supérieure à sa capacité. » La difficulté est réelle, mais jamais au-delà du possible.",
  "Coran, 2:286","Nommer ce que je crois impossible et le réduire à une étape.")
c("rappel","Le dhikr apaise",
  "Que dit le Coran de l'apaisement du cœur ?",
  "« N'est-ce point par l'évocation d'Allah que les cœurs se tranquillisent ? » Pas par le divertissement : par le dhikr.",
  "Coran, 13:28","Faire 33 fois subhânallâh, 33 alhamdulillâh, 34 allâhu akbar.")
c("rappel","Se souvenir et être mentionné",
  "Que promet Allah à celui qui se souvient de Lui ?",
  "« Souvenez-vous de Moi, Je Me souviendrai de vous ; soyez reconnaissants envers Moi, et ne soyez pas ingrats. »",
  "Coran, 2:152","Noter trois choses pour lesquelles je remercie Allah.")
c("rappel","La confiance et la provision",
  "Que promet Allah à celui qui se confie à Lui ?",
  "« Quiconque place sa confiance en Allah, Il lui suffit. » La suffisance vient d'Allah, pas de l'absence de difficulté.",
  "Coran, 65:3","Nommer une inquiétude et la remettre.")
c("rappel","Vous détestez une chose",
  "Que dit le Coran de ce que nous n'aimons pas ?",
  "« Il se peut que vous détestiez une chose alors qu'elle est un bien pour vous. » Le regard court, la science d'Allah est globale.",
  "Coran, 2:216","Repenser à une chose que je détestais et qui m'a servie.")
c("rappel","Avec la difficulté",
  "Que dit la sourate 94 de la difficulté ?",
  "« À côté de la difficulté, il y a une facilité. » Répété deux fois : la facilité est annoncée, pas seulement espérée.",
  "Coran, 94:5-6","Réciter la sourate 94 dans une difficulté.")
c("rappel","Ne désespérez pas",
  "Que dit Allah aux pécheurs ?",
  "« Ne désespérez pas de la miséricorde d'Allah : Allah pardonne tous les péchés. » La miséricorde précède le désespoir, jamais l'inverse.",
  "Coran, 39:53","Faire istighfâr pour un péché que je cache.")
c("rappel","Appelez-Moi",
  "Que dit Allah de l'invocation ?",
  "« Votre Seigneur a dit : appelez-Moi, Je vous répondrai. » L'invocation est un ordre, pas une option offerte.",
  "Coran, 40:60","Faire une du'â aujourd'hui sans demande matérielle.")
c("rappel","Le chemin du savoir",
  "Que promet le hadith à celui qui cherche la science ?",
  "« Celui qui emprunte un chemin à la recherche d'une science, Allah lui facilite un chemin vers le Paradis. »",
  "Sahîh Muslim, n° 2699","Lire une page de science aujourd'hui.","Hadith")
c("rappel","Le regret du temps",
  "Que dit le Prophète ﷺ du temps libre ?",
  "« Profite de cinq choses avant cinq autres : ta jeunesse avant ta vieillesse, ta santé avant ta maladie, ta richesse avant ta pauvreté, ton temps libre avant ton occupation, ta vie avant ta mort. »",
  "Al-Hâkim ; rapporté aussi par al-Bukhârî dans ses commentaires","Choisir une des cinq et l'utiliser aujourd'hui.","Hadith")

# ═══════════ 10. HADITHS FONDATEURS ═══════════
c("hadiths","L'intention",
  "Que dit le premier hadith du Sahîh ?",
  "« Les actes ne valent que par les intentions, et chacun n'a que ce qu'il a intentionné. » Le même geste peut monter ou ne rien valoir.",
  "Sahîh al-Bukhârî, n° 1 ; Sahîh Muslim, n° 1907","Formuler l'intention avant une action.","Hadith")
c("hadiths","Le licite et l'illicite",
  "Que dit le hadith du doute ?",
  "« Le licite est clair, l'illicite est clair, et entre les deux des choses douteuses. Celui qui s'en préserve protège sa religion et son honneur. »",
  "Sahîh al-Bukhârî, n° 52 ; Sahîh Muslim, n° 1599","Identifier un doute dans mes revenus.","Hadith")
c("hadiths","La religion est le conseil",
  "Que signifie « la religion, c'est le nasîha » ?",
  "La loyauté sincère envers Allah, Son Livre, Son Messager, les musulmans et leurs dirigeants. Un conseil qui humilie n'est plus un conseil.",
  "Sahîh Muslim, n° 55","Donner un conseil utile sans rabaisser.","Hadith")
c("hadiths","Aimer pour son frère",
  "Quel est le signe de la foi complète ?",
  "« Nul d'entre vous ne croit vraiment jusqu'à ce qu'il aime pour son frère ce qu'il aime pour lui-même. » La jalousie est le révélateur.",
  "Sahîh al-Bukhârî, n° 13 ; Sahîh Muslim, n° 45","Faire du'â pour un proche comme pour moi.","Hadith")
c("hadiths","La parole",
  "Que dit le hadith de la parole inutile ?",
  "« Que celui qui croit en Allah et au Jour dernier dise du bien ou se taise. »",
  "Sahîh al-Bukhârî, n° 6018 ; Sahîh Muslim, n° 47","S'abstenir d'un commentaire inutile.","Hadith")
c("hadiths","La force",
  "Qui est le fort ?",
  "« Le fort n'est pas celui qui terrasse les autres, mais celui qui se maîtrise quand il est en colère. »",
  "Sahîh al-Bukhârî, n° 6114 ; Sahîh Muslim, n° 2609","Ressentir la colère et se taire 10 secondes.","Hadith")
c("hadiths","Ce qu'Allah regarde",
  "Que regarde Allah dans nos actes ?",
  "« Allah ne regarde pas votre apparence ni vos corps, mais Il regarde vos cœurs et vos actes. »",
  "Sahîh Muslim, n° 2564","Faire un acte que personne ne verra.","Hadith")
c("hadiths","Le meilleur",
  "Qui est le meilleur des hommes ?",
  "« Le meilleur d'entre vous est celui qui apprend le Coran et l'enseigne. »",
  "Sahîh al-Bukhârî, n° 5027","Apprendre un verset et l'enseigner.","Hadith")
c("hadiths","Laisse ce qui doute",
  "Quel critère pour les situations ambiguës ?",
  "« Laisse ce qui te fait douter pour ce qui ne te fait pas douter ; la vérité est tranquillité et le mensonge est doute. »",
  "Jâmi' at-Tirmidhî, n° 2518 (hasan)","Choisir l'option qui apaise.","Hadith")
c("hadiths","La douceur",
  "Que fait la douceur ?",
  "« La douceur n'est jamais dans une chose sans l'embellir, et n'en est jamais retirée sans l'enlaidir. »",
  "Sahîh Muslim, n° 2594","Remplacer une réprimande par une explication.","Hadith")
c("hadiths","Le mensonge",
  "Où mène le mensonge ?",
  "« Le mensonge mène à la perversité, et la perversité mène au Feu. » Ce n'est pas un défaut véniel : c'est un chemin.",
  "Sahîh al-Bukhârî, n° 6094 ; Sahîh Muslim, n° 2607","Ne pas arrondir la vérité une fois aujourd'hui.","Hadith")
c("hadiths","La miséricorde",
  "Qui obtient la miséricorde ?",
  "« Faites miséricorde à ceux qui sont sur terre : Celui qui est au ciel vous fera miséricorde. »",
  "Sunan Abî Dâwûd, n° 4941 ; Jâmi' at-Tirmidhî, n° 1924","Faire une chose miséricordieuse aujourd'hui.","Hadith")

# ═══════════ 11. MARIAGE & FAMILLE ═══════════
c("famille","Une seule âme",
  "Que dit le Coran de l'origine du couple ?",
  "« Ô gens, craignez votre Seigneur qui vous a créés d'une seule âme, et a créé d'elle son épouse, et a fait proliférer d'eux hommes et femmes. »",
  "Coran, 4:1","Retenir : une même origine, donc une même dignité.")
c("famille","La sakîna",
  "Quel est le but du mariage selon le Coran ?",
  "« Il a mis entre vous affection et miséricorde. » Le couple est un lieu de tranquillité (sakîna), pas un contrat de services.",
  "Coran, 30:21","Nommer ce qui crée la sakîna chez moi.")
c("famille","Une sunna",
  "Le mariage est-il une sunna ?",
  "« Le mariage fait partie de ma sunna ; celui qui ne suit pas ma sunna n'est pas des miens. »",
  "Sunan Ibn Mâja, n° 1846 (sahîh selon al-Albânî)","Retenir : sunna, pas coutume.","Hadith")
c("famille","Le mahr",
  "À qui appartient le mahr ?",
  "À l'épouse : « Donnez aux femmes leur mahr de bon gré. » Ce n'est pas un prix versé à la famille.",
  "Coran, 4:4","Comprendre : c'est un droit de la femme.")
c("famille","Le choix",
  "Quel critère pour choisir son conjoint ?",
  "« On épouse une femme pour quatre : ses biens, sa noblesse, sa beauté et sa religion — choisis celle qui a la religion. »",
  "Sahîh al-Bukhârî, n° 5090 ; Sahîh Muslim, n° 1466","Lister mes trois critères réels.","Hadith")
c("famille","Le meilleur des maris",
  "Quel est le critère du bon mari ?",
  "« Le meilleur d'entre vous est le meilleur envers sa famille, et je suis le meilleur d'entre vous envers ma famille. »",
  "Jâmi' at-Tirmidhî, n° 3895 (hasan sahîh)","Demander une chose à améliorer à la maison.","Hadith")
c("famille","La délibération",
  "Que dit le Coran de la décision dans le couple ?",
  "« Délibérez entre vous de bonne manière. » La consultation n'est pas une concession, c'est la règle.",
  "Coran, 65:6","Prendre une décision familiale après avoir demandé l'avis de l'autre.")
c("famille","Les droits réciproques",
  "Les droits des époux sont-ils identiques ?",
  "« Les femmes ont des droits équivalents à leurs obligations, conformément à ce qui est convenable. » Équivalents, pas identiques : chacun a sa charge.",
  "Coran, 2:228","Lister mes obligations concrètes.")
c("famille","La charge du foyer",
  "Qui doit la dépense du foyer ?",
  "Le mari : « Que celui qui a de l'aisance dépense selon son aisance. » La nafaqa est une obligation, pas une faveur.",
  "Coran, 65:7 ; 4:34","Vérifier que la charge est assurée sans reproche.")
c("famille","La bénédiction",
  "Quelle formule pour un mariage ?",
  "« Bârakallâhu laka wa bâraka 'alayka wa jama'a baynakumâ fî khayr » — qu'Allah te bénisse et vous réunisse dans le bien.",
  "Sunan Abî Dâwûd, n° 2130 ; at-Tirmidhî","La mémoriser pour un mariage.","Hadith")

# ═══════════ 12. CARACTÈRE & ÉDUCATION ═══════════
c("akhlaq","Le caractère du Prophète ﷺ",
  "Que dit le Coran de son caractère ?",
  "« Tu es d'une moralité éminente. » Le Coran qualifie directement son comportement, avant toute description physique.",
  "Coran, 68:4","Lire la sourate 68 en entier.")
c("akhlaq","Ce qui pèse le plus",
  "Qu'est-ce qui pèse le plus dans la balance ?",
  "« La crainte d'Allah et le bon caractère. » Deux choses, indissociables : on ne sépare pas la piété du comportement.",
  "Jâmi' at-Tirmidhî, n° 2004","Choisir une qualité à travailler cette semaine.","Hadith")
c("akhlaq","Les parents",
  "Quel est le rang des parents ?",
  "« Et ton Seigneur a décrété que vous n'adoriez que Lui, et la bonté envers les parents. » Cités juste après l'adoration.",
  "Coran, 17:23-24","Appeler ses parents aujourd'hui.")
c("akhlaq","La mauvaise langue",
  "Qu'est-ce que la ghiba ?",
  "Parler de quelqu'un en son absence de ce qu'il déteste : « Manger la chair de son frère mort » selon l'image du Coran.",
  "Coran, 49:12","Interrompre une conversation qui médit.")
c("akhlaq","Le conseil de Luqmân",
  "Quel est le premier conseil de Luqmân à son fils ?",
  "« Ô mon fils, ne fais pas d'associé à Allah : l'association est une injustice immense. » L'éducation commence par le tawhîd.",
  "Coran, 31:13","Expliquer « qui est Allah » à un enfant.")
c("akhlaq","La prière à sept ans",
  "Quand ordonne-t-on la prière à l'enfant ?",
  "« Ordonnez à vos enfants la prière à sept ans, et à dix ans séparez-les dans les lits. » Une progression, pas un ultimatum.",
  "Sunan Abî Dâwûd, n° 495","Adapter mon exigence à l'âge de l'enfant.","Hadith")
c("akhlaq","Le berger",
  "Quelle est la responsabilité du parent ?",
  "« Chacun de vous est un berger et responsable de son troupeau. » Le parent répond de l'âme qui lui est confiée.",
  "Sahîh al-Bukhârî, n° 893 ; Sahîh Muslim, n° 1829","Écrire une chose que je délègue à tort.","Hadith")
c("akhlaq","L'équité entre enfants",
  "Que dit le Prophète ﷺ du cadeau fait à un seul enfant ?",
  "Il a refusé qu'un père privilégie un enfant : « Craignez Allah et soyez justes entre vos enfants. »",
  "Sahîh al-Bukhârî, n° 2587 ; Sahîh Muslim, n° 1623","Vérifier l'équilibre de mes attentions.","Hadith")
c("akhlaq","La colère",
  "Que faire quand la colère monte ?",
  "« Quand l'un de vous se met en colère, qu'il se taise. » Et le Prophète ﷺ a enseigné de changer de position et de faire ses ablutions.",
  "Musnad Ahmad ; Sahîh al-Bukhârî","Se taire avant de répondre.","Hadith")
c("akhlaq","Le voisin",
  "Quel est le droit du voisin ?",
  "« Celui dont le mal est craint par son voisin n'entrera pas au Paradis. » Le comportement avec le voisin est un critère.",
  "Sahîh Muslim, n° 46","Saluer et demander des nouvelles de mon voisin.","Hadith")
