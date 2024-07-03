import flet as ft
import time

def splash(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    progress_bar = ft.ProgressBar(width=page.width, color=ft.colors.PURPLE_400)
    page.add(
        ft.Row(
            [ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Loading...",
                                    theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
                                    color=ft.colors.PURPLE_400,
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
        ),
        progress_bar,
    )

    for i in range(100):
        progress_bar.value = i/100
        page.update()
        time.sleep(0.03)

    main(page)

def main(page):
    page.clean()
    page.title = "Application"
    gradient_container = ft.Container(
        width = page.window_width,
        height = page.window_height,
        gradient = ft.LinearGradient(
            colors=["#049578", "#AF87FF"],
            begin=ft.Alignment(1,-1),
            end=ft.Alignment(-1,1)
        )
    )

    gradient_container.content = ft.Container(
        content = ft.Column(
            [
                ft.Text(),
                ft.Text(value = "Log in",
                        style = ft.TextThemeStyle.DISPLAY_LARGE,
                        color = ft.colors.WHITE,
                        ),
                ft.TextField(
                    label="User",
                    width=300,
                    color=ft.colors.WHITE,
                    border_color=ft.colors.WHITE,
                    label_style=ft.TextStyle(color="#ffffff"),
                    helper_style=ft.TextStyle(color="#ffffff"),
                    hint_style=ft.TextStyle(color="#888888"),
                    autofocus = True,
                ),
                ft.TextField(
                    label="Password",
                    width=300,
                    color=ft.colors.WHITE,
                    border_color=ft.colors.WHITE,
                    label_style=ft.TextStyle(color="#ffffff"),
                    helper_style=ft.TextStyle(color="#ffffff"),
                    hint_style=ft.TextStyle(color="#888888"),
                    autofocus = True,
                ),
                ft.Row([
                    ft.ElevatedButton(
                        text = "Log in",
                        on_click=lambda e:print("Login button clicked"),
                        bgcolor="#ffffff",
                        color="#000000",
                    ),
                    ft.ElevatedButton(
                        text = "Sign up",
                        bgcolor="#ffffff",
                        color="#000000",
                        on_click = signup_display
                    ),
                ], width = page.width, alignment = ft.MainAxisAlignment.CENTER),
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            spacing=50,
        )
    )

    page.add(gradient_container)


def signup_display(e):
    sign_up(e.page)

def login_display(e):
    main(e.page)

def sign_up(page):
    page.clean()
    page.title = "Sign-up"
    gradient_container = ft.Container(
        width = page.window_width,
        height = page.window_height,
        gradient = ft.LinearGradient(
            colors=["#049578", "#AF87FF"],
            begin=ft.Alignment(-1,1),
            end=ft.Alignment(1,-1)
        )
    )

    gradient_container.content = ft.Container(
        content = ft.Column(
            [
                ft.Text(),
                ft.Text(value = "Sign up",
                        style = ft.TextThemeStyle.DISPLAY_LARGE,
                        color = ft.colors.WHITE,
                        ),
                ft.TextField(
                    label="User",
                    width=300,
                    color=ft.colors.WHITE,
                    border_color=ft.colors.WHITE,
                    label_style=ft.TextStyle(color="#ffffff"),
                    helper_style=ft.TextStyle(color="#ffffff"),
                    hint_style=ft.TextStyle(color="#888888"),
                    autofocus = True,
                ),
                ft.TextField(
                    label="Password",
                    width=300,
                    color=ft.colors.WHITE,
                    border_color=ft.colors.WHITE,
                    label_style=ft.TextStyle(color="#ffffff"),
                    helper_style=ft.TextStyle(color="#ffffff"),
                    hint_style=ft.TextStyle(color="#888888"),
                    autofocus = True,
                ),
                ft.TextField(
                    label="Confirm Password",
                    width=300,
                    color=ft.colors.WHITE,
                    border_color=ft.colors.WHITE,
                    label_style=ft.TextStyle(color="#ffffff"),
                    helper_style=ft.TextStyle(color="#ffffff"),
                    hint_style=ft.TextStyle(color="#888888"),
                    autofocus = True,
                ),
                ft.Row([
                    ft.ElevatedButton(
                        text = "Sign up",
                        bgcolor="#ffffff",
                        color="#000000",
                        on_click=lambda e:print("Signup button clicked"),
                    ),
                    ft.ElevatedButton(
                        text = "Log in",
                        on_click = login_display,
                        bgcolor="#ffffff",
                        color="#000000",
                    ),
                ], width = page.width, alignment = ft.MainAxisAlignment.CENTER),
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            spacing=50,
        )
    )

    page.add(gradient_container)

ft.app(splash)
