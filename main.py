import flet as ft
from flet import UrlTarget

URL = "https://sites.google.com/view/amr-app?usp=sharing"

def main(page: ft.Page):
    page.title = "الشهرة"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    btn = ft.ElevatedButton(
        text="اضغط على الزر لعرض إعلانات التطبيق الشهرة",
        on_click=lambda e: ft.launch_url(URL, target=UrlTarget.BLANK)
    )

    page.add(
        ft.Column(
            [
                ft.Text("الشهرة", size=28),
                ft.Container(height=20),  # مسافة بين العنوان والزر
                btn
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
