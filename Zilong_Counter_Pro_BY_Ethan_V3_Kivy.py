# ============================================================
# ZILONG COUNTER PRO V3
# BY ETHAN
# KIVY - ANDROID TOUCH SCROLL
#
# Jalankan di Pydroid 3.
# Jika Kivy belum tersedia, install paket "kivy" dari menu Pydroid 3.
# ============================================================

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.graphics import Color, RoundedRectangle
from kivy.properties import StringProperty, NumericProperty
import random


# ============================================================
# DATA
# ============================================================

COUNTERS = [
    ("Minsitthar","EXP",96,"Mudah","Flicker",
     "Dominance Ice, Antique Cuirass",
     "Membatasi mobilitas Zilong."),
    ("Phoveus","EXP",94,"Mudah","Flicker",
     "Dominance Ice, Antique Cuirass",
     "Dapat memanfaatkan mobilitas lawan."),
    ("Terizla","EXP",91,"Sedang","Flicker",
     "Dominance Ice, Antique Cuirass",
     "Kuat dalam pertarungan jarak dekat."),
    ("Khaleed","EXP",89,"Sedang","Flicker",
     "Dominance Ice, Antique Cuirass",
     "Memiliki sustain dan burst yang baik."),
    ("Yu Zhong","EXP",88,"Sedang","Flicker",
     "Dominance Ice, Antique Cuirass",
     "Sustain dan team fight kuat."),

    ("Kaja","ROAM",95,"Sedang","Flicker",
     "Dominance Ice, Antique Cuirass",
     "Ultimate dapat menarik Zilong."),
    ("Franco","ROAM",92,"Sedang","Flicker",
     "Dominance Ice, Antique Cuirass",
     "Hook dan crowd control dapat menghentikan Zilong."),
    ("Tigreal","ROAM",88,"Sedang","Flicker",
     "Dominance Ice, Antique Cuirass",
     "Crowd control kuat untuk mengganggu Zilong."),
    ("Ruby","ROAM",87,"Sedang","Flicker",
     "Dominance Ice, Antique Cuirass",
     "Banyak crowd control dan sustain."),

    ("Valir","MID",91,"Mudah","Flicker",
     "Glowing Wand, Ice Queen Wand",
     "Dapat menjaga jarak dan mendorong Zilong."),
    ("Nana","MID",88,"Mudah","Flicker",
     "Glowing Wand, Ice Queen Wand",
     "Crowd control mengganggu Zilong."),
    ("Aurora","MID",86,"Sedang","Flicker",
     "Glowing Wand, Divine Glaive",
     "Burst dan crowd control tinggi."),
    ("Eudora","MID",84,"Mudah","Flicker",
     "Glowing Wand, Divine Glaive",
     "Combo burst sangat kuat."),

    ("Melissa","GOLD",94,"Sedang","Flicker",
     "Wind of Nature, Sea Halberd",
     "Dapat menjaga jarak dan melindungi diri."),
    ("Wanwan","GOLD",90,"Sulit","Purify",
     "Wind of Nature, Sea Halberd",
     "Mobilitas tinggi membuatnya sulit ditangkap."),
    ("Karrie","GOLD",89,"Sedang","Flicker",
     "Wind of Nature, Sea Halberd",
     "Damage konsisten dari jarak aman."),
    ("Clint","GOLD",87,"Sedang","Flicker",
     "Wind of Nature, Sea Halberd",
     "Range dan burst membuat engage sulit."),

    ("Saber","JUNGLE",90,"Mudah","Retribution",
     "Hunter Strike, Malefic Roar",
     "Burst tinggi untuk mengunci target."),
    ("Baxia","JUNGLE",86,"Sedang","Retribution",
     "Dominance Ice, Antique Cuirass",
     "Durability tinggi menghadapi fighter.")
]


# ============================================================
# BACKGROUND WIDGET
# ============================================================

class Card(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.10, 0.12, 0.16, 1)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(8)]
            )

        self.bind(
            pos=self.update_rect,
            size=self.update_rect
        )

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


# ============================================================
# MAIN APP
# ============================================================

class ZilongCounterApp(App):

    def build(self):

        self.title = "ZILONG COUNTER PRO - BY ETHAN"

        root = BoxLayout(
            orientation="vertical",
            spacing=dp(5)
        )

        # Background
        with root.canvas.before:
            Color(0.055, 0.065, 0.09, 1)
            self.bg = RoundedRectangle(
                pos=root.pos,
                size=root.size
            )

        root.bind(
            pos=lambda obj, val:
            setattr(self.bg, "pos", val),
            size=lambda obj, val:
            setattr(self.bg, "size", val)
        )

        # ----------------------------------------------------
        # HEADER
        # ----------------------------------------------------

        header = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=dp(75),
            padding=[dp(5), dp(5)]
        )

        title = Label(
            text="[b]⚔ ZILONG COUNTER PRO[/b]",
            markup=True,
            font_size=dp(17),
            color=(1,1,1,1),
            size_hint_y=None,
            height=dp(30)
        )

        subtitle = Label(
            text="MLBB Counter Helper",
            font_size=dp(9),
            color=(0.6,0.64,0.7,1),
            size_hint_y=None,
            height=dp(17)
        )

        brand = Label(
            text="[b]✦ BY ETHAN ✦[/b]",
            markup=True,
            font_size=dp(9),
            color=(0.39,0.9,0.75,1),
            size_hint_y=None,
            height=dp(17)
        )

        header.add_widget(title)
        header.add_widget(subtitle)
        header.add_widget(brand)

        root.add_widget(header)

        # ----------------------------------------------------
        # CONTROLS
        # ----------------------------------------------------

        controls = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=dp(105),
            padding=[dp(8), dp(3)],
            spacing=dp(5)
        )

        self.role_spinner = Spinner(
            text="SEMUA",
            values=("SEMUA","EXP","JUNGLE","ROAM","MID","GOLD"),
            size_hint_y=None,
            height=dp(30),
            font_size=dp(10)
        )

        self.role_spinner.bind(
            text=lambda instance, value:
            self.refresh()
        )

        self.search = TextInput(
            hint_text="Cari hero...",
            multiline=False,
            size_hint_y=None,
            height=dp(30),
            font_size=dp(10),
            padding=[dp(8),dp(5)]
        )

        self.search.bind(
            text=lambda instance, value:
            self.refresh()
        )

        random_button = Button(
            text="🎲 RANDOM COUNTER",
            size_hint_y=None,
            height=dp(30),
            font_size=dp(9),
            background_normal="",
            background_color=(0.17,0.42,0.93,1)
        )

        random_button.bind(
            on_release=self.random_counter
        )

        controls.add_widget(self.role_spinner)
        controls.add_widget(self.search)
        controls.add_widget(random_button)

        root.add_widget(controls)

        # ----------------------------------------------------
        # TOUCH SCROLL AREA
        # ----------------------------------------------------

        self.scroll = ScrollView(
            size_hint=(1,1),
            do_scroll_x=False,
            do_scroll_y=True,
            scroll_type=["content"],
            bar_width=dp(5),
            effect_cls="ScrollEffect"
        )

        self.list_box = GridLayout(
            cols=1,
            spacing=dp(6),
            padding=[dp(8),dp(5)],
            size_hint_y=None
        )

        self.list_box.bind(
            minimum_height=self.list_box.setter(
                "height"
            )
        )

        self.scroll.add_widget(
            self.list_box
        )

        root.add_widget(self.scroll)

        self.refresh()

        return root

    # ========================================================
    # REFRESH LIST
    # ========================================================

    def refresh(self):

        self.list_box.clear_widgets()

        role = self.role_spinner.text
        query = self.search.text.lower().strip()

        data = []

        for item in COUNTERS:

            hero = item[0]
            hero_role = item[1]

            if role != "SEMUA" and hero_role != role:
                continue

            if query and query not in hero.lower():
                continue

            data.append(item)

        data.sort(
            key=lambda x:x[2],
            reverse=True
        )

        if not data:

            self.list_box.add_widget(
                Label(
                    text="Hero tidak ditemukan.",
                    color=(0.6,0.64,0.7,1),
                    font_size=dp(11),
                    size_hint_y=None,
                    height=dp(45)
                )
            )

            return

        for index, item in enumerate(data, 1):

            self.add_card(
                index,
                item
            )

        # Reset position setelah filter
        self.scroll.scroll_y = 1

    # ========================================================
    # HERO CARD
    # ========================================================

    def add_card(self, rank, item):

        hero, role, score, difficulty, spell, items, reason = item

        card = Card(
            orientation="vertical",
            size_hint_y=None,
            height=dp(105),
            padding=[dp(9),dp(6)],
            spacing=dp(2)
        )

        top = BoxLayout(
            size_hint_y=None,
            height=dp(25)
        )

        rank_label = Label(
            text=f"[color=888f9e]#{rank}[/color]",
            markup=True,
            font_size=dp(9),
            size_hint_x=None,
            width=dp(28)
        )

        hero_label = Label(
            text=f"[b]{hero}[/b]",
            markup=True,
            font_size=dp(12),
            color=(1,1,1,1),
            halign="left"
        )

        score_label = Label(
            text=f"[color=63e6be][b]{score}%[/b][/color]",
            markup=True,
            font_size=dp(10),
            size_hint_x=None,
            width=dp(45)
        )

        top.add_widget(rank_label)
        top.add_widget(hero_label)
        top.add_widget(score_label)

        info = Label(
            text=f"{role}  •  {difficulty}",
            font_size=dp(8),
            color=(0.55,0.6,0.68,1),
            halign="left",
            text_size=(None,None),
            size_hint_y=None,
            height=dp(15)
        )

        reason_label = Label(
            text=reason,
            font_size=dp(8),
            color=(0.78,0.8,0.84,1),
            halign="left",
            valign="middle",
            text_size=(dp(320),None),
            size_hint_y=None,
            height=dp(25)
        )

        detail = Label(
            text=f"⚡ {spell}    🛡 {items}",
            font_size=dp(7.5),
            color=(0.68,0.72,0.78,1),
            halign="left",
            valign="middle",
            text_size=(dp(320),None),
            size_hint_y=None,
            height=dp(20)
        )

        card.add_widget(top)
        card.add_widget(info)
        card.add_widget(reason_label)
        card.add_widget(detail)

        self.list_box.add_widget(card)

    # ========================================================
    # RANDOM
    # ========================================================

    def random_counter(self, *args):

        role = self.role_spinner.text

        data = [
            x for x in COUNTERS
            if role == "SEMUA" or x[1] == role
        ]

        if not data:
            return

        hero, hero_role, score, difficulty, spell, items, reason = random.choice(data)

        content = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(8)
        )

        content.add_widget(
            Label(
                text="[b]🎲 RANDOM COUNTER[/b]",
                markup=True,
                font_size=dp(15)
            )
        )

        content.add_widget(
            Label(
                text=f"[b]{hero}[/b]",
                markup=True,
                font_size=dp(22),
                color=(0.39,0.9,0.75,1)
            )
        )

        content.add_widget(
            Label(
                text=f"Score: {score}%\nRole: {hero_role}\nSpell: {spell}\n\n{reason}",
                font_size=dp(9)
            )
        )

        close = Button(
            text="TUTUP",
            size_hint_y=None,
            height=dp(35),
            font_size=dp(9)
        )

        content.add_widget(close)

        popup = Popup(
            title="Zilong Counter",
            content=content,
            size_hint=(0.82,0.45)
        )

        close.bind(
            on_release=popup.dismiss
        )

        popup.open()


if __name__ == "__main__":
    ZilongCounterApp().run()
