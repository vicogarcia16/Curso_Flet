import flet as ft

def config_page (page: ft.Page):
    page.window.width = 400
    page.window.height = 800
    page.window.resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.expand = True
    return page

def config_page_sf (page: ft.Page):
    page.window.width = 400
    page.window.height = 800
    page.window.resizable = False
    page.expand = True
    return page
