# EulerProject
Решение задач из проекта [Euler] на языке Python


# Настройка окружения и инструментарий: 

[Точка входа](https://www.youtube.com/watch?v=P0czP5MEbYQ), показан некий roadmap при постановке задачи - обучение языку Питон. В данном видео предлагается установка PyCharm (тяжелая программа на Java), но я использую [Sublime Text] и Sublime Merge т.к. только это смогло заработать на Sway (+ pure Wayland). Для MacOSX рекомендую [VSCode](https://code.visualstudio.com/)
Для меня киллер-фича именно [Sublime Text] - то, что он сразу показывет проблемы в строках кода на несоотвествие [PEP8](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html). ОЧЕНЬ полезно для новичка и приучает сразу писать чистый и понятный код. 

Единственно, что нужно сделать в Sublime это прикрутить интерактивную консоль Python: 
+ [REPL](https://gist.github.com/simplesasha/73005e8e08065d8c360dba09dc86626b)
+ [REPL, вторая инструкция](https://ru.stackoverflow.com/questions/529699/%D0%9A%D0%B0%D0%BA-%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D1%82%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D0%B4-python3-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-sublimerepl)
+ Вид панелей (Layout) выбрать "Rows: 2" (Alt+Shift+8)

Также, нужно уточнить, что материалы ниже показывают в [Jupiter Notebook](https://sky.pro/media/jupyter-notebook-chto-eto-takoe-i-kak-im-polzovatsya/). Можно поставить у себя, можно использовать стороннего хостера, например, [CoLab](https://colab.research.google.com/) Всегда помните, какие данные вы выгружаете на сторонние ресурсы, сделайте правильный выбор. Данные Notebooks удобны для анализа данных, когда вы работаете с Pandas, но для изучения достаточно писать и запускать программы внутри IDE.

Возвращаясь к проекту [Euler] - для себя ставил цель решения данных задач: понять какие конструкции языка наиболее "нативны" в выбранном языке, поэтому сперва пробовал решать сам (иногда размышляя понятиями и алгоритмикой другого языка - Си), затем искал наиболее интересные решения в Интернете, которые тоже переносил в код. По мере выполнения задач (и это видно по ходу :) ) сразу писал "однострочники", которые решают задачу. Также уже несколько раз проводил рефакторинг кода. Для подключения повторящихся стандартных библиотек, выделил их в отдельный файл [project_euler_defs.py](https://github.com/nebulosa2007/EulerProject/blob/main/project_euler_defs.py) Может быть, не самая лучшая организация пакетов кода, возможен рефакторинг!



# Материалы по языку Python

## Питон в научных вычислениях
+ [Ссылка](https://www.inp.nsk.su/~grozin/python/) Начиная с самых основ и вплоть до написания программ. Язык изложения и показывание практических примеров кода - решает.


## Лекции от Тимофея Хирьянова (МФТИ) 
+ [2017-2018 Алгоритмы и структуры данных на Python 3](https://www.youtube.com/playlist?list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0) - Погружение в специфику языка через алгоритмику. Смотреть на скорости х2: 
+ [Курс информатики на Python 3](https://mipt-cs.github.io/python3-2017-2018/)  - структурированная практика, для понимания решения типичных алгоритмов на языке
+ [2021 Анализ данных на Python](https://www.youtube.com/playlist?list=PLRDzFCPr95fIgPrFFW-0nXT5YH6ZnjRM6) - для закрепления материала.
## Еще один сборник-справочник
+ [Документация по языку Python3](https://docs-python.ru/)

# Прочее полезное:
## Pandas
+ [Чтение и запись файлов Excel (XLSX) на Python с помощью библиотеки Pandas](https://pythobyte.com/reading-and-writing-excel-files-in-python-with-the-pandas-library-8358adce/)
+ [Как автоматизировать подготовку отчетов по рекламе с помощью Python](https://ppc.world/articles/kak-ya-avtomatiziroval-podgotovku-30-otchetov-s-pomoschyu-python-i-sekonomil-12-chasov-v-nedelyu/)

## Бот телеграм
+ [Асинхронный Telegram бот на языке Python 3 с использованием библиотеки aiogram](https://surik00.gitbooks.io/aiogram-lessons/content/)


[Euler]: https://euler.jakumo.org/
[Sublime Text]: https://www.sublimetext.com/