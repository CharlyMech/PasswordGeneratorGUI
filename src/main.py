import flet
from flet import *
from random_passwd import *
from db.classes import *
from os import getcwd
from datetime import date


def main(page: Page):

    page.window_width = 350
    page.window_height = 200
    page.window_resizable = False

    t = Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(
                text="Random Password",
                content=Container(
                    content=Text("Random password generation"),
                    alignment=alignment.center,
                ),
            ),
            Tab(
                text="Random Pin",
                content=Container(
                    content=Text("Random pin generation"), alignment=alignment.center
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
