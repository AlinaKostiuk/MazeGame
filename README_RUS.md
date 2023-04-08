# MAZE TEXT GAME
### Видио демо:  <https://youtu.be/TgwzuXTsVyc>
## Содержание
* [Общая информация](#Общая информация)
* [Запуск](#Запуск)
* [Файлы](#Файлы)
    * [mazegame.py](#mazegame.py)
    * [Maze.py](#Maze.py)
    * [params.py](#params.py)
    * [instructions.txt](#instructions.txt)
    * [instructions_rus.txt](#instructions_rus.txt)

## Общая информация
В этой игре вам необходимо пройти через процедурно сгенерированный лабиринт при помощи текстовых команд

По умолчанию, игрок может выьрать один из 3 уровней сложности, но это можно изменить вручную в файле [params.py](#params.py).

Дополнительное усложнение состоит в том, что карта не рисуется заново после каждого передвижения игрока. Не смотря на это, игрок может в любой момент попросить посмотреть на карту и свою текущую позицию.

## Запуск

#### **Требования**
*Для запуска игры необходимо, чтобы был установлен Python3*

Для запуска полного графического режима, необходимо выполнить одну из следующих команд в терминале IDE:

```
$ python mazegame.py -r
```
или 
```
$ python mazegame.py --rus
```
Системная командная строка может не поддерживать отображение символов, использованных при созданиии изображения лабиринта. Если вы запускаете игру из командной строки системы, рекоммендуется необходимо выполнить одну из следующих команд:
```
$ python mazegame.py -r -l
```
или
```
$ python mazegame.py -r --line
```
В этом случае, стены будут отображаться как '#', проходы - '_', игрок - 'u' и выход как 'e'

#


## Файлы
### **mazegame.py**
Основной файл проекта, который выполняет всю работу - определение уровня сложности, создание объекта лабиринта, отображение инструкций и обработка команд игрока.

Когда игрок достигает финиша, отображается сообщение с поздравлением и предложение сыграть еще раз.

### **Maze.py**
Создает и хранит карту лабиринта, влючая его внешний вид, расположение игрока и выхода.

### **params.py**
Содержит размеры лабиринта для всех доступных уровней сложности, дизайны лабиринта и другие параметры в виде словарей. Также, здесь случайно выирается внешний вид лабиринта (если не был указан аргумент -l)

### **instructions.txt**
Содержит инструкции для англоязычной версии игры. Инструкции по запуску этой версии находятся в файле *README.md*

### **instructions_rus.txt**
Содержит инструкции для игрока и список доступных команд для передвижения по лабиринту.