import flet as ft
from config import config_page_sf

def main(page: ft.Page):
    lenguajes = ["Python", "Flet", "Flutter"]
    etiquetas = []
    for leng in lenguajes:
        etiquetas.append(ft.Text(leng))
        
    page = config_page_sf(page)
    
    def close_page(e):
        page.window.close()
    
    close_button = ft.ElevatedButton(text="Close", on_click=close_page)
    datos = ft.Row(
        controls=etiquetas,
        alignment="center"
        )
   
    page.add(datos,
         ft.Column(
            controls=[
                ft.Container(content=close_button, alignment=ft.alignment.center),
            ]),
         )

ft.app(target=main)