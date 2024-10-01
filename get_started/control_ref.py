import flet as ft
from config import config_page_sf

def main(page: ft.Page):
    page.title = "Control Ref"
    config_page_sf(page)
    
    txt_first_name = ft.TextField(label="First Name", autofocus=True)
    txt_last_name = ft.TextField(label="Last Name", on_submit = lambda e: saludar_clicked(e))
    col_controles = ft.Column(controls=[ft.Container(
        content=ft.Row(alignment="center")
    )], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    def saludar_clicked(e):
        col_controles.controls.append(ft.Text(f'Hola {txt_first_name.value} {txt_last_name.value}', 
                                              theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
                                              text_align=ft.TextAlign.CENTER))
        txt_first_name.value = ""
        txt_last_name.value = ""
        page.update()
        txt_first_name.focus()
    
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

    page.add(txt_first_name, txt_last_name, btn_saludar, col_controles, btn_close)
    
ft.app(target=main)