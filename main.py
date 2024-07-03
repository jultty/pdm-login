import flet as ft
import time

def splash(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Row(
            [ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Loading...",
                                    theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
                                    color=ft.colors.PURPLE_200,
                                    text_align=ft.TextAlign.CENTER,
                                    width=500,
                                    height=200,
                                    ),
                            ft.Image("assets/cat.png", width=500),
                        ],
                        expand = True,
                        alignment=ft.MainAxisAlignment.END
                    ),
                    expand = True,
                    alignment=ft.alignment.center,
                ),
            ],
            expand = True,
        )],
            expand=True,
        )
    )

    time.sleep(3)
    #main(page)


def main(page):
    page.clean()
    page.title = "Application"
    welcome_text = ft.Text("Welcome", style=ft.TextThemeStyle.DISPLAY_LARGE, color=ft.colors.PURPLE_200)
    page.add(welcome_text)

ft.app(splash)
