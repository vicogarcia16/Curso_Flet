import flet as ft
from config import config_page_sf

def main(page: ft.Page):
    page.title = "Control Ref"
    config_page_sf(page)
    
    txt_first_name = ft.Ref[ft.TextField]()
    txt_last_name = ft.Ref[ft.TextField]()
    col_controles = ft.Ref[ft.Column]()
    
    def saludar_clicked(e):
        col_controles.current.controls.append(ft.Text(f'Hola {txt_first_name.current.value} {txt_last_name.current.value}', 
                                              theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
                                              text_align=ft.TextAlign.CENTER))
        txt_first_name.current.value = ""
        txt_last_name.current.value = ""
        page.update()
        txt_first_name.current.focus()
    
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

    page.add(
        ft.TextField(ref=txt_first_name, label="First Name", autofocus=True),
        ft.TextField(ref=txt_last_name, label="Last Name", 
                     on_submit = lambda e: saludar_clicked(e)),
        btn_saludar,
        ft.Column(ref=col_controles, controls=[ft.Container(
        content=ft.Row(alignment="center")
        )], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        , btn_close)
    
ft.app(target=main)