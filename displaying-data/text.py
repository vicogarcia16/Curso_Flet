from config import config_page_sf
import flet as ft

def main(page: ft.Page):
    page.title = "Text"
    page =config_page_sf(page)
    
    lbl_text = ft.Container(content=ft.Text(
        value="Flet con Python",
        size=30,
        color="blue",
        bgcolor="gray",
        weight="bold",
        italic=True
        ), 
        alignment=ft.alignment.center)
    
    btn_close = ft.Container(content=ft.ElevatedButton(text="Cerrar",
                                                       icon=ft.icons.CLOSE,
                                                       on_click=lambda e:page.window.close(),
                                                       icon_color=ft.colors.WHITE,
                                                       bgcolor=ft.colors.RED_700,
                                                       color=ft.colors.WHITE), 
                             alignment=ft.alignment.center)
    page.add(lbl_text, btn_close)

ft.app(target=main)
    