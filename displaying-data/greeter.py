import flet as ft
from config import config_page_sf

def main(page: ft.Page):
    page.title = "Greeter"
    page = config_page_sf(page)
    
    def saludar_clicked(e):
        if not txt_nombre.value:
            txt_nombre.value = "Ingresa tu nombre"
            page.update()
        else:
            nombre = txt_nombre.value
            page.clean()
            page.add(ft.Container(
                content=ft.Text(f"Hola... {nombre}", 
                                size=30,
                                color="blue",
                                bgcolor="gray",
                                weight="bold",
                                font_family="Roboto"),
                alignment=ft.alignment.center
            ), btn_close)
    txt_nombre = ft.TextField(label="Ingresa tu nombre", 
                              on_submit=saludar_clicked, width=300)
    
    btn_saludar = ft.Container(content=ft.ElevatedButton(text="Saludar",
                                                         on_click=saludar_clicked,
                                                         icon=ft.icons.SEND,
                                                         icon_color=ft.colors.WHITE,
                                                         bgcolor=ft.colors.BLUE_700,
                                                         color=ft.colors.WHITE), 
                                alignment=ft.alignment.center)
    btn_close = ft.Container(content=ft.ElevatedButton(text="Cerrar",
                                                       icon=ft.icons.CLOSE,
                                                       on_click=lambda e:page.window.close(),
                                                       icon_color=ft.colors.WHITE,
                                                       bgcolor=ft.colors.RED_700,
                                                       color=ft.colors.WHITE), 
                             alignment=ft.alignment.center)
    
    page.add(ft.Container(
        content=ft.Row(controls=[txt_nombre], alignment="center"),
        margin=ft.Margin(left=0, top=20, right=0, bottom=0)
    ),
    btn_saludar
    )

ft.app(target=main)
    