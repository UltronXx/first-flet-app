import flet as ft
from flet import (
    app,
    Page,
    MainAxisAlignment,
    CrossAxisAlignment,
    Column,
    SafeArea,
    Text,
    Container,
    Colors,
    padding,
    SnackBar
)

def main(page: Page):
    page.title = "mirageOS"

    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    page.fonts = {
        "bold": "fonts/AmpleSoftPro-Bold.ttf",
        "medium": "fonts/AmpleSoftPro-Medium.ttf",
    }

    def on_hover(e):
        button.bgcolor = Colors.BLUE_400 if button.bgcolor == Colors.BLUE_500 else Colors.BLUE_500
        if button.shadow == []:
            button.shadow = ft.BoxShadow(
                color=Colors.BLUE_200,
                blur_radius=12,
                offset=ft.Offset(0, 5),
            )
        else:
            button.shadow = []
        page.update()

    def on_click(e):
        page.open(
            control=SnackBar(
                bgcolor=Colors.BLUE_500,
                content=Text(
                    value="Welcome to mirageOS!",
                    font_family="medium",
                    size=16,
                    color=Colors.WHITE
                ),
                duration=2000,
                behavior=ft.SnackBarBehavior.FLOATING,
            )
        )
        page.update()

    button = Container(
        bgcolor=Colors.BLUE_500,
        border_radius=30,
        padding=padding.symmetric(vertical=10, horizontal=40),
        content=Text(
            value="Start",
            font_family="medium",
            color=Colors.WHITE,
            size=20,
        ),
        shadow=[],
        animate=ft.Animation(200),
        on_hover=on_hover,
        on_click=on_click
    )
    
    page.add(
        SafeArea(
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Text(
                        value="mirageOS",
                        font_family="bold",
                        size=64,
                    ),
                    button
                ],
            )
        )
    )

    page.update()

app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
    