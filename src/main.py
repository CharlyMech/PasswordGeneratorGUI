import flet
from flet import *
from flet import icons, Icon, colors
from random_passwd import *
from db.classes import *
from os import getcwd
from datetime import date


def main(page: Page):

    page.window_resizable = True
    page.window_min_width = 600
    page.window_min_height = 350
    page.window_max_width = 900
    page.window_max_height = 600
    page.title = "Pysswords"
    page.vertical_alignment = "center"

    """
    - PASSWORD RANDOM GENERATION CONTENT -

    """
    passwords_TITLE = Column(
        [
            Row(
                [
                    Text(
                        value="Generate new Random Password",
                        size=30,
                        text_align="center",
                    )
                ],
                alignment="center",
            )
        ],
        alignment="center",
    )

    passwords_PASSWD_LARGE = TextField(
        value="8",
        border="underline",
        disabled=True,
        text_align="center",
        width=75,
    )
    passwords_PASSWD_GEN_TXT = TextField(
        label="Random password",
        # value="",
        read_only=True,
        text_align="center",
    )

    def minus_click_passwd(e):
        if (int(passwords_PASSWD_LARGE.value) - 1) >= 8:
            passwords_PASSWD_LARGE.value = int(passwords_PASSWD_LARGE.value) - 1
            page.update()

    def plus_click_passwd(e):
        if (int(passwords_PASSWD_LARGE.value) + 1) <= 64:
            passwords_PASSWD_LARGE.value = int(passwords_PASSWD_LARGE.value) + 1
            page.update()

    def call_random_passwd(e):
        passwords_PASSWD_GEN_TXT.value = random_passwd(
            int(passwords_PASSWD_LARGE.value)
        )
        page.update()

    passwords_GEN_BTNS = Row(
        [
            IconButton(icons.REMOVE, on_click=minus_click_passwd),
            passwords_PASSWD_LARGE,
            IconButton(icons.ADD, on_click=plus_click_passwd),
            FilledButton(
                "Generate",
                icon=icons.PASSWORD,
                on_click=call_random_passwd,
                icon_color=colors.BLUE_300,
            ),
        ],
        alignment="center",
    )

    passwords_PASSWD_GEN = Row([passwords_PASSWD_GEN_TXT], alignment="center")

    passwords_SAVE_BTN = Row(
        [
            FilledButton(
                "Save",
                icon=icons.DATA_SAVER_ON_OUTLINED,
                icon_color=colors.BLUE_300,
            )
        ],
        alignment="center",
    )

    passwords_GEN = Column(
        [passwords_GEN_BTNS, passwords_PASSWD_GEN, passwords_SAVE_BTN],
        alignment="center",
        spacing=30,
    )

    passwd_MAIN_COL = Column(
        [passwords_TITLE, passwords_GEN],
        alignment="spaceEvenly",
        spacing=80,
    )
    passwd_MAIN = Container(content=passwd_MAIN_COL)

    """
    - PIN RANDOM GENERATION CONTENT -
        
    """
    pin_TITLE = Column(
        [
            Row(
                [
                    Text(
                        value="Generate new Random Pin",
                        size=30,
                        text_align="center",
                    )
                ],
                alignment="center",
            )
        ],
        alignment="center",
    )

    pin_PIN_LARGE = TextField(
        value="4",
        border="underline",
        disabled=True,
        text_align="center",
        width=75,
    )
    pin_PIN_GEN_TXT = TextField(
        label="Random PIN",
        # value="",
        read_only=True,
        text_align="center",
    )

    def minus_click_pin(e):
        if (int(pin_PIN_LARGE.value) - 1) >= 4:
            pin_PIN_LARGE.value = int(pin_PIN_LARGE.value) - 1
            page.update()

    def plus_click_pin(e):
        if (int(pin_PIN_LARGE.value) + 1) <= 12:
            pin_PIN_LARGE.value = int(pin_PIN_LARGE.value) + 1
            page.update()

    def call_random_pin(e):
        pin_PIN_GEN_TXT.value = random_pin(int(pin_PIN_LARGE.value))
        page.update()

    pin_GEN_BTNS = Row(
        [
            IconButton(icons.REMOVE, on_click=minus_click_pin),
            pin_PIN_LARGE,
            IconButton(icons.ADD, on_click=plus_click_pin),
            FilledButton(
                "Generate",
                icon=icons.PIN,
                on_click=call_random_pin,
                icon_color=colors.BLUE_300,
            ),
        ],
        alignment="center",
    )

    pin_PASSWD_GEN = Row([pin_PIN_GEN_TXT], alignment="center")

    pin_SAVE_BTN = Row(
        [
            FilledButton(
                "Save",
                icon=icons.DATA_SAVER_ON_OUTLINED,
                icon_color=colors.BLUE_300,
            )
        ],
        alignment="center",
    )

    pin_GEN = Column(
        [pin_GEN_BTNS, pin_PASSWD_GEN, pin_SAVE_BTN],
        alignment="center",
        spacing=30,
    )

    pin_MAIN_COL = Column(
        [pin_TITLE, pin_GEN],
        alignment="spaceEvenly",
        spacing=80,
    )
    pin_MAIN = Container(content=pin_MAIN_COL)

    t = Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(
                text="Random Password",
                content=Container(
                    content=passwd_MAIN,
                    alignment=alignment.center,
                ),
            ),
            Tab(
                text="Random PIN",
                content=Container(
                    content=pin_MAIN,
                    alignment=alignment.center,
                ),
            ),
            Tab(
                text="Insert Password",
                content=Container(
                    content=Text("Custom password insert"), alignment=alignment.center
                ),
            ),
            Tab(
                text="Stored",
                content=Container(
                    content=Text("All passwords and pin stored"),
                    alignment=alignment.center,
                ),
            ),
        ],
        expand=1,
    )

    page.add(t)


flet.app(target=main)
