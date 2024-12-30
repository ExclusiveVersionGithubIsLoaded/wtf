init -1 python:
    # имена доступных скинов - папок, где лежит картинка телефона и деталей интерфейса
    sms_skins = ["phone", "tablet"]

    # имя текущего скина по умолчанию
    sms_skin_name = sms_skins[0]

    # заголовок в списке чатов
    sms_caption = _("Сообщения")

    ## РАЗМЕРЫ
    # если ширина единственной в сообщении картинки больше этой,
    # то картинка преобразуется в прикреплённое фото с закруглёнными краями
    sms_min_w = 200

    # отступы текста sms от краёв пузырей
    sms_xpadding, sms_ypadding = 16, 8

    # отступы пузырей sms от краёв экрана
    sms_xmargin, sms_ymargin = 24, 16

    # расстояние между сообщениями
    sms_spacing = 8

    ## ЦВЕТА И ФОНЫ
    # цвет фона для шапки
    sms_top_color = ["#4b2635", "#533956"]

    # цвет имени в шапке
    sms_chat_text_color = ["#fff", "#fff"]

    # фон экрана телефона
    sms_bg = ["#fff", "#222"]

    # обои
    sms_wallpaper = None

    # цвета фона пузырей с сообщениями
    sms_choice_bg_color = ["#09f", "#09f"]
    sms_choice_hover_bg_color = ["#fff", "#fff"]
    sms_left_bg_color = ["#09f", "#334"]
    sms_right_bg_color = ["#e5e5ea", "#8ae"]
    sms_center_bg_color = ["#0000", "#0000"]

    # цвета текста пузырей с сообщениями
    sms_choice_text_color = ["#fff", "#fff"]
    sms_choice_text_hover_color = ["#09f", "#09f"]
    sms_left_text_color = ["#fff", "#fff"]
    sms_right_text_color = ["#000", "#000"]
    sms_center_text_color = ["#aaa", "#aaa"]
    sms_center_text_hover_color = ["#09f", "#09f"]

    # цвет названий в списке чатов
    sms_list_text_color = ["#000", "#fff"]

    # цвет линий в подвале
    sms_bottom_color = ["#aaa", "#fff"]

    sms_choice_italic = True

    ## ШРИФТ
    def sms_font(font="font"):
        return "images/" + sms_skin_name + "/" + font + ".ttf"

    # размеры шрифта
    sms_text_size = {"sms_center": 22, "sms_left": 28, "sms_right": 28, "sms_choice": 30, "sms_who": 20, "sms_chat": 30, "sms_counter": 20}

    # трансформ для окна с телефоном
    # например, можно задать положение
    sms_trans = [align(.15, .5), rotate(-2.5, False)]

    # имя абонента по умолчанию
    sms_default = _("Неизвестный")

## остальное лучше не менять вручную
    # время появления смс
    sms_t = .5

    # номер текущей темы
    sms_theme = 0

    # размеры всего телефона
    sms_phone_w, sms_phone_h = 500, 960

    # размеры экрана телефона
    sms_scr_w, sms_scr_h = 480, 860

    # высота шапки и подвала
    sms_top_h = 80
    sms_bottom_w2, sms_bottom_h2 = int(sms_scr_w / 2), 40

    # размеры кружочка для счётчика непрочитанных
    sms_counter_w, sms_counter_h = 38, 38

    # максимальная ширина пузыря с сообщением
    sms_xmaximum = int(sms_scr_w * .8)

    # фиксированные углы для пузырей с сообщениями (для Frame)
    sms_corner_w, sms_corner_h = 16, 16

    # размеры видимой области viewport
    sms_view_w, sms_view_h = sms_scr_w, sms_scr_h - sms_top_h - sms_bottom_h2 * 2

    # без звука
    sms_mute_sound = False

    # идёт анимация появления новой sms
    sms_ining = False

    # имя текущего чата, куда будут попадать все сообщения,
    # кроме помеченных тегом #chat
    sms_current_chat = None

    # имя отображаемого чата или списка чатов, если 0, None или False
    sms_showed_chat = None

    # показывать ли имена
    sms_show_names = None

    # кто сейчас говорит/пишет
    sms_speaker_name = None

    # выравнивание в каждом из стилей xalign sms_xalign[i_style]
    sms_xalign = {"sms_left": .0, "sms_right": 1., "sms_center": .5, "sms_choice": .5, None: .5}


    # убрать телефон с экрана
    def sms_hide():
        global sms_visible
        sms_visible = False    
        renpy.hide_screen("sms", layer="master")

    def sms_show():
        global sms_visible
        sms_visible = True
        renpy.show_screen("sms", layer="master")
       

    # очистить сообщения абонента
    # если chat == None, очищается вся история сообщений
    def sms_clear(chat=None):
        if chat is None:
            store.sms_all = []
        else:
            sms_pop(chat)
        renpy.restart_interaction()

    # найти индекс переписки по имени/номеру
    def sms_get_index(chat=sms_default):
        for i in range(len(sms_all)):
            if sms_all[i][0] == chat:
                return i
        return -1

    # вырезаем из списка или создаём абонента, если его ещё нет
    def sms_pop(chat=sms_default, show_names=False):
        i = sms_get_index(chat)
        if i < 0:
            s = [chat, 0, show_names, []]
        else:
            s = store.sms_all.pop(i)
        return s

    # копируем переписку с абонентом
    def sms_get(chat=sms_default):
        i = sms_get_index(chat)
        if i >= 0:
            return store.sms_all[i][2], store.sms_all[i][3]
        return False, None

    # создаем новый чат в начале списка
    def sms_new_chat(chat, show_names=None, i=0):
        if show_names is None:
            show_names = sms_show_names
        store.sms_show_names = show_names
        store.sms_all.insert(i, [chat, 0, show_names, []])


    # определить размеры картинки,
    # если картинка существует
    def sms_get_size(image):
        img = sms_skin_name + " " + image.strip()
        if has_image(img):
            w, h = get_size(img)
            return w, h
        return 0, 0

    # сменить тему, 0/1 - дневная/ночная,
    # "toggle" или не указывать - переключение
    def sms_dark(theme=True):
        # новая тема
        if theme == "toggle":
            theme = sms_theme + 1
        elif theme == True:
            theme = 1
        elif theme == False:
            theme = 0
        # по идее тем может быть больше двух
        if theme >= len(sms_left_text_color) or theme < 0:
            theme = 0
        store.sms_theme = theme
        renpy.restart_interaction()
    SMSDark = renpy.curry(sms_dark)

    # сменить обои
    def sms_wall(wall=None):
        store.sms_wallpaper = wall
        renpy.restart_interaction()

    # сменить скин и пересчитать все размеры
    def sms_skin(skin=None):
        # новый скин
        if not skin:
            # если не указан, то следующий в списке
            i = sms_skins.index(sms_skin_name) + 1
            if i >= len(sms_skins):
                i = 0
            skin = sms_skins[i]
        store.sms_skin_name = skin
        # размеры всего телефона
        w, h = sms_get_size("foreground")
        if w and h:
            store.sms_phone_w, store.sms_phone_h = w, h
        # размеры экрана телефона
        w, h = sms_get_size("background")
        if w and h:
            store.sms_scr_w, store.sms_scr_h = w, h
        # размеры углов сообщений
        w, h = sms_get_size("message mask")
        if w and h:
            store.sms_corner_w, store.sms_corner_h = int(w / 2), int(h / 2)
        # высота шапки по большей из кнопок
        h = sms_get_size("btn return")[1]
        if h:
            store.sms_top_h = h
        h = sms_get_size("btn menu")[1]
        if h > sms_top_h:
            store.sms_top_h = h
        # высота подвала
        w, h = sms_get_size("bottom")
        if h:
            store.sms_bottom_w2 = int(w / 2)
            store.sms_bottom_h2 = int(h / 2)
        # размеры кружочка для счётчика непрочитанных
        store.sms_counter_w, store.sms_counter_h = int(sms_top_h / 2), int(sms_top_h / 2)
        # размеры viewport
        store.sms_view_w, store.sms_view_h = sms_scr_w, sms_scr_h - sms_top_h - sms_bottom_h2 * 2
        renpy.restart_interaction()
    SMSSkin = renpy.curry(sms_skin)

    # сделать чат активным (не путать с отображаемым)
    def sms_chat(chat, show_names=None):
        if chat:
            # если нет такого чата
            i = sms_get_index(chat)
            if i < 0:
                i = 0
                # создаем его
                if show_names is None:
                    show_names = sms_show_names
                sms_new_chat(chat, show_names, i)
            # показывать ли имена
            if show_names is not None:
                store.sms_all[i][2] = show_names
            # делаем чат активным
            store.sms_current_chat = chat
        store.sms_show_names = show_names
    SMSChat = renpy.curry(sms_chat)

    # показать другой чат или список чатов
    def sms_show(chat=None, show_names=None, clear=False):
        # если нужно, очистить всю историю сообщений
        if clear:
            sms_clear()
        # значения по-умолчанию
        store.sms_speaker_name = None
        # если чат указан
        if chat:
            i = sms_get_index(chat)
            # и если нет такого чата
            if i < 0:
                i = 0
                if show_names is None:
                    show_names = sms_show_names
                # создаем новый
                sms_new_chat(chat, show_names, i)
            # показывать ли имена
            if show_names is not None:
                store.sms_all[i][2] = show_names
            # сбрасываем счётчик непрочитанных
            store.sms_all[i][1] = 0
        # показываем указанный чат или список чатов
        store.sms_showed_chat = chat
        # если активный чат не задан
        if not sms_current_chat:
            # то задаём показанный
            store.sms_current_chat = chat
        # если активный чат всё равно не задан
        if not sms_current_chat:
            # то задаём по умолчанию
            store.sms_current_chat = sms_default
        # перемотка в конец или в начало списка
        # в зависимости от режима - чат или список чатов
        if sms_showed_chat:
            store.yadj.value = yadjValue
        else:
            store.yadj.value = 0
        store.sms_show_names = show_names
        # прячем экран, чтобы перемотать к последней sms
        renpy.hide_screen("sms", layer="master")
        # показываем экран sms
        renpy.show_screen("sms", _layer="master")
        renpy.restart_interaction()
    SMSShow = renpy.curry(sms_show)


    # посчитать все непрочитанные
    # и вернуть пустую строку, если всё прочитано
    # либо число непрочитанных
    # или "+", если их больше 9
    def sms_unread():
        s = ""
        i = sum(i[1] for i in sms_all)
        if i > 9:
            s = "+"
        elif i > 0:
            s = str(i)
        return s

    # стили, которые нужно озвучивать (собеседник и автор)
    sms_beep_styles = ["sms_left", "sms_right"]

    # добавляем сообщение в историю переписки
    def sms_add(what=None):
        # текущий чат
        chat = sms_current_chat
        # добавляем сообщение в список сообщений на экране
        if what and sms_speaker_style:
            # чат, куда пишем, можно временно сменить, не переключаясь на него,
            # если в тексте будет тег {#chat=имя чата}
            s = get_tag(what, 'chat')
            if s is not None:
                chat = s
                if "_(" in s:
                    chat = eval(s)
            # вырезаем всю переписку в текущем или указанном чате
            s = sms_pop(chat)
            # добавляем новое сообщение
            s[3].append((sms_speaker_name, what, sms_speaker_style))
            # считаем непрочитанные сообщения
            # или сбрасываем, если написали в текущий чат
            if chat == sms_showed_chat:
                s[1] = 0
                store.sms_ining = (sms_current_chat, sms_speaker_name, what, sms_speaker_style)
            elif sms_speaker_style in sms_beep_styles:
                s[1] += 1
            # вставляем дополненную переписку в начало
            store.sms_all.insert(0, s)
        
        if sms_speaker_style in sms_beep_styles and not sms_mute_sound and not ("{nw}" in what):
            splay("ReceiveText", audio_dir="images/"+sms_skin_name)
            
        store.sms_speaker_style = ""
        renpy.restart_interaction()
    SMSAdd = renpy.curry(sms_add)

    # текущее время читателя
    def time_now():
        return datetime.datetime.now().strftime("%H:%M")

init -2 python:
    # листать вниз при добавлении сообщений
    yadjValue = 10**10
    yadj = ui.adjustment()

    # все sms в формате кортежей (стиль, текст)
    sms_all = []

    # здесь будет храниться стиль текущего сообщения
    # sms_left - собеседники
    # sms_right - получатель
    # sms_center - система
    sms_speaker_style = ""

    from functools import partial

    # определяем имя и стиль текущего персонажа
    def call_f(smsstyle, smswho, event_name, *args, **kwarg):
        if event_name == "begin":
            # стиль персонажа
            store.sms_speaker_style = smsstyle
            store.sms_speaker_name = smswho

    # функция с параметрами в качестве одного параметра
    def sms_f(*args, **kwarg):
        return partial(call_f, *args, **kwarg)

    # заготовки для невидимых на экране персонажей
    def SMS(narrator=None, smsstyle="sms_center", *args, **kwarg):
        return Character(narrator=narrator, callback=sms_f(smsstyle, narrator), screen="sms_say", *args, **kwarg)
    def SMSL(narrator=None, *args, **kwarg):
        return SMS(narrator, "sms_left", *args, **kwarg)
    def SMSR(narrator=None, *args, **kwarg):
        return SMS(narrator, "sms_right", *args, **kwarg)
    def SMSC(narrator=None, *args, **kwarg):
        return SMS(narrator, *args, **kwarg)

    # получить фон пузыря с сообщением (можно задать свой цвет)
    def sms_get_bg(i_style="sms_center", i_color=None):
        if i_color is None:
            i_color = eval(i_style + "_bg_color[sms_theme]")
        return Frame(At(sms_skin_name + " message mask", color(i_color)), sms_corner_w, sms_corner_h)

    # не будет работать с пробелами, типа такого: "{ image = smile }" (лень возиться)
    # если вместо текста только картинка, то показать её с закруглёнными краями, а не пузырь
    def sms_image(i_text, i_style):
        if "{image=" in i_text and not del_tags(i_text, ""):
            imgs = get_tags(i_text, "image")
            if imgs:
                key = list(imgs.keys())
                if len(key) == 1:
                    img = imgs[key[0]]
                    w, h = get_size(img)
                    # если картинка больше указанных в настройках размеров
                    if w >= sms_min_w:
                        # вписываем картинку в сообщение
                        z = sms_xmaximum / w
                        img = Transform(img, zoom=z)
                        w2, h2 = int(w * z), int(h * z)
                        # скругляем края
                        mask = Frame(sms_skin_name + " message mask", sms_corner_w, sms_corner_h, xysize=(w2, h2))
                        return AlphaMask(img, mask)
        return None

    # возвращает растягивающийся перекрашенный по необходимости фон
    # если вместо цвета задать картинку, то её вырежет по маске первой картинки - img
    def sms_frame_bg(img, i_color=None, w=0, h=0, noskin=False):
        # добавляем префикс скина, если не запретили это на входе
        if not noskin:
            img = sms_skin_name + " " + img
        # если есть цвет, то красим картинку в него
        if i_color:
            if has_image(i_color):
                return Frame(AlphaMask(i_color, img), w, h)
            return Frame(At(img, color(i_color)), w, h)
        # просто вытянутая картинка
        return Frame(img, w, h)

init:
    # анимация появления новой sms
    transform sms_in(t=sms_t):
        rotate_pad False
        zoom .01 rotate -5
        ease_back t zoom 1 rotate 0

# замена для экрана say, чтобы считывать sms, заносить их в историю,
# но не показывать в пределах видимого экрана
screen sms_say(who, what):
    on "show" action SMSAdd(what)
    text what id "what" yoffset config.screen_height * 11 slow_cps 0

init python:
    sms_items = False

# экран телефона
screen sms(items=None, chat=None):
    on "show" action SetVariable("sms_items", not items is None)

    if sms_showed_chat:
        $ yadj.value = yadjValue
    else:
        $ yadj.value = 0

    $ u = sms_unread()

    # окончание анимации появления новой sms
    if sms_ining:
        timer sms_t repeat True action SetVariable("sms_ining", False)
    if sms_items:
        timer sms_t repeat True action SetVariable("sms_items", False)

    # окно с телефоном
    button:
        style "empty"
        xysize (sms_phone_w, sms_phone_h)
        foreground Frame(sms_skin_name + " foreground", 0, 0)
        at sms_trans

        # клик по телефону меняет скин
        #action sms_hide()

        # фрейм с экраном телефона
        button:
            style "empty"
            xysize (sms_scr_w, sms_scr_h)

            # обои-картинка
            if sms_wallpaper:
                background sms_frame_bg(sms_wallpaper, noskin=True)
            else:
                background sms_frame_bg("background", sms_bg[sms_theme])

            align(.5, .5)
            action NullAction()

            # шапка, смски и подвал
            vbox:
                xfill True
                yfill True

                # шапка с абонентом
                frame:
                    style "empty"
                    align(.5, 0)
                    xysize(sms_scr_w, sms_top_h)
                    background sms_top_color[sms_theme]

                    # если режим чата
                    if sms_showed_chat:
                        # название чата (имя абонента)
                        text sms_showed_chat:
                            align(.5, .5)
                            color sms_chat_text_color[sms_theme]
                            size sms_text_size["sms_chat"]
                            font sms_font()
                            bold True

                    # если список чатов
                    else:
                        # заголовок
                        text sms_caption:
                            align(.5, .5)
                            color sms_chat_text_color[sms_theme]
                            size sms_text_size["sms_chat"]
                            font sms_font()
                            bold True

                    # кнопка меню (переключает на тёмную тему)
                    imagebutton idle sms_skin_name + " btn menu" align(1., .5) action SMSDark("toggle") #activate_sound "images/" + sms_skin_name + "/click.ogg"

                    # кнопка «назад»
                    # если открыт чат
                    if sms_showed_chat:
                        imagebutton idle sms_skin_name + " btn return" align(.0, .5) action SMSShow() #activate_sound "images/" + sms_skin_name + "/click.ogg"

                        # в левом углу счётчик непрочитанных сообщений в других чатах
                        if u:
                            textbutton u:
                                style "empty"
                                align(.04, .5)
                                text_align(.5, .5)
                                text_font sms_font()
                                text_size sms_text_size["sms_counter"]
                                xysize (sms_counter_w, sms_counter_h)
                                text_color sms_top_color[sms_theme]
                                background sms_frame_bg("counter mask", sms_chat_text_color[sms_theme])
                                text_bold True

                # смски с прокруткой
                viewport:
                    id "sms_vp"

                    # размеры окна прокрутки с учетом шапки и подвала
                    xysize(sms_view_w, sms_view_h)
                    yinitial yadjValue
                    yfill False
                    mousewheel True
                    draggable True
                    side_xfill True
                    transclude

                    # перематываем в конец
                    yadjustment yadj

                    # контейнер для сообщений или списка чатов
                    frame:
                        style "empty"
                        xpadding sms_xmargin
                        ypadding sms_ymargin
                        xsize sms_view_w

                        vbox:
                            xfill True
                            spacing sms_spacing

                            # получить все сообщения текущего чата
                            # если открыт чат
                            if sms_showed_chat:
                                # то выводим СПИСОК СООБЩЕНИЙ ЧАТА
                                $ show_names, data = sms_get(sms_showed_chat)

                                if data is not None:
                            
                                    for i_who, i_text, i_style in data:
                                        vbox:
                                            xalign sms_xalign[i_style]
                                            spacing sms_spacing

                                            # анимация появления новой sms
                                            if sms_ining == (sms_showed_chat, i_who, i_text, i_style) and i_style != "sms_center":
                                                at sms_in()

                                            # если нужно подписать
                                            if i_who and show_names and i_style != "sms_center":
                                                text i_who:
                                                    font sms_font()
                                                    color sms_center_text_color[sms_theme]
                                                    size sms_text_size["sms_who"]

                                            # если это единственная картинка больше пузыря
                                            $ img = sms_image(i_text, i_style)

                                            if img:
                                                # вписываем её в пузырь
                                                add img

                                            # иначе просто выводим текст в пузыре
                                            else:
                                                # само сообщение
                                                button:
                                                    style "empty"
                                                    xalign sms_xalign[i_style]
                                                    xmaximum sms_xmaximum
                                                    xpadding sms_xpadding
                                                    ypadding sms_ypadding
                                                    background sms_get_bg(i_style)

                                                    text i_text:
                                                        slow_cps 0
                                                        font sms_font()
                                                        size sms_text_size[i_style]
                                                        color eval(i_style + "_text_color[sms_theme]")

                                    # если идёт выбор и открыт нужный чат
                                    if chat in (sms_showed_chat, None) and not items is None:
                                        # выводим все варианты выбора
                                        for i in items:
                                            # в стиле диалога автора, но по центру и с подсветкой при наведении
                                            button:
                                                style "empty"
                                                xalign 0.5
                                                xsize sms_xmaximum
                                                xpadding sms_xpadding
                                                ypadding sms_ypadding
                                                background sms_get_bg("sms_choice")
                                                hover_background sms_get_bg("sms_choice_hover")
                                                action i.action
                                                if sms_items:
                                                    at sms_in()

                                                text i.caption:
                                                    slow_cps 0
                                                    xalign .5
                                                    text_align .5
                                                    layout "subtitle"
                                                    font sms_font()
                                                    size sms_text_size["sms_choice"]
                                                    color eval("sms_choice_text_color[sms_theme]")
                                                    hover_color eval("sms_choice_text_hover_color[sms_theme]")
                                                    italic sms_choice_italic
                                                    hover_bold True

                            # иначе выводим СПИСОК ЧАТОВ
                            else:
                                # имя чата, количество непрочитанных
                                for chat, unread, show_names, data in sms_all:
                                    $ last_sms = ""

                                    if len(data) > 0:
                                        $ last_sms = "{b}" + data[len(data) - 1][0] + ":{/b} " + data[len(data) - 1][1]

                                    # кнопка с именем чата, чтобы его открыть
                                    button:
                                        style "empty"
                                        xfill True
                                        xpadding sms_xpadding
                                        ypadding sms_ypadding
                                        action SMSShow(chat)
                                        activate_sound "sms.ogg"

                                        hbox:
                                            xfill True

                                            vbox:
                                                # название чата
                                                text chat:
                                                    xmaximum sms_scr_w-sms_xmargin*3-sms_counter_w
                                                    align(.0, .5)
                                                    color sms_list_text_color[sms_theme]
                                                    font sms_font()
                                                    size sms_text_size["sms_chat"]
                                                    bold True

                                                # последняя sms
                                                textbutton last_sms:
                                                    style "empty"
                                                    at crop(0, 0, sms_scr_w-sms_xmargin*3-sms_counter_w, sms_text_size["sms_center"])
                                                    align(.0, .5)

                                                    text_color sms_center_text_color[sms_theme]

                                                    text_font sms_font()

                                                    text_size sms_text_size["sms_center"]

                                            # количество непрочитанных
                                            textbutton str(unread):
                                                style "empty"
                                                align(1., .5)

                                                text_align(.5, .5)

                                                text_font sms_font()

                                                text_size sms_text_size["sms_counter"]

                                                xysize (sms_counter_w, sms_counter_h)
                                                text_color sms_chat_text_color[sms_theme]
                                                background sms_frame_bg("counter mask", sms_top_color[sms_theme])
                                                text_bold True

                                                if unread <= 0:
                                                    at alpha(0)

                                                
                # подвал
                frame:
                    style "empty"
                    xysize(sms_scr_w, sms_bottom_h2 * 2)
                    align(.5, 1.)
                    #background sms_frame_bg("bottom", sms_bottom_color[sms_theme], sms_bottom_w2, sms_bottom_h2)
