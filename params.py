import random

skins = {
    "forest": {"w":"🌳", "p":"🟫", "f":"🏁", "sprites":["🧙", "🐈", "🧍", "🐕", "🧚"]},
    "castle": {"w":"🔳", "p":"⬜️", "f":"🏁", "sprites":["🧙", "👻", "🧍", "🧛", "🧟"]},
}

line_skin = {"w":"#", "p":"_", "f":"e", "sprites":["u"]}

skin = random.choice(list(skins.values()))

dimensions = {"easy":13, "regular":19, "hard":25}
dimensions_rus = {"легко":13, "обычно":19, "сложно":25}

language = {
    'eng':
        {
        "instructions":"instructions.txt",
        "greeting":"\nIn your wanderings around this magical world you came across a maze.\nFind the way through it to continue your journey!\n",
        "difficulty": "Choose difficulty",
        "dimensions": dimensions,
        "where_next": "Where will you go next? ",
        "map": "map",
        "help": "help",
        "exit": "exit",
        "movements": {"up":"up", "down":"down", "left":"left", "right":"right"},
        "wall": "You can't go there!",
        "too_far": "You can't go that far!",
        "too_far_walked": "You've walked",
        "FileNotFoundError": "\nInstructions are not found\n",
        "go_back": "Are you sure you want to go back? (y/n) ",
        "bye": "Umm... okay... bye...",
        "changed_mind": "I'm glad you've changed your mind!",
        "congrats": "\n🎊🎉🎊 Congratulations! 🎊🎉🎊\nYour courage and intelligence have guided you through this maze to new adventures!\n",
        "replay": "Do you want to play again? (y/n) "
        },
    'rus':
        {
        "instructions":"instructions_rus.txt",
        "greeting":"\nВ путешествиях по волшебному миру вы натолкнулись на лабиринт.\nНайдите путь через него, чтобы продолжить путешествие!\n",
        "difficulty": "Выберите сложность",
        "dimensions": dimensions_rus,
        "where_next": "Куда вы пойдете? ",
        "map": "карта",
        "help": "помощь",
        "exit": "выход",
        "movements": {"up":"вверх", "down":"вниз", "left":"влево", "right":"вправо"},
        "wall": "Туда не пройти!",
        "too_far": "Так далеко не пройти!",
        "too_far_walked": "Вы прошли",
        "FileNotFoundError": "\nИнструкции не найдены\n",
        "go_back": "Вы уверены, что хотите вернуться? (да/нет) ",
        "bye": "Хмм... ладно... пока...",
        "changed_mind": "Я рад, что вы передумали!",
        "congrats": "\n🎊🎉🎊 Поздравляю! 🎊🎉🎊\nВаша смелость и ум провели вас чарез этот лабиринт к новым приключениям!\n",
        "replay": "Хотите попробовать еще раз? (да/нет) "
        }}