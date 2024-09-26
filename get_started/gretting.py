import flet as ft
from config import config_page_sf

def main(page: ft.Page):
    page = config_page_sf(page)
    page.title = "Saludo"
    
    # Definir estilo de texto
    text_style = ft.TextStyle(
        size=40,
        weight=ft.FontWeight.BOLD,
        foreground=ft.Paint(
            gradient=ft.PaintLinearGradient(
                (100, 0), (300, 0),
                colors=[ft.colors.RED, ft.colors.BLUE]
            ),
            style=ft.PaintingStyle.FILL,
        )
    )
    
    saludo_label = ft.Text(value="")
    
    def saludo(e):
        saludo_label.spans = [ft.TextSpan(f"Hola {nombre_field.value}", text_style)]
        nombre_field.value = ""
        page.update()
    
    def enviar_formulario(e):
        if nombre_field.value:
            snackbar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.icons.INFO, color=ft.colors.WHITE,
                                size=30),
                        ft.Text(f"Has ingresado: {nombre_field.value}", 
                                color=ft.colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                bgcolor=ft.colors.BLUE,
                duration=ft.Duration(seconds=3)
            )
            page.overlay.append(snackbar)
            snackbar.open = True
            saludo(e)
            page.update()
        
    nombre_field = ft.TextField(
        label="Escribe tu nombre",
        width=200,
        on_submit=enviar_formulario
    )
    
    # Agregar controles a la página con márgenes
    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            nombre_field,
                            ft.IconButton(ft.icons.WAVING_HAND_ROUNDED, 
                                          on_click=saludo,
                                          icon_size=35, 
                                          icon_color=ft.colors.GREEN_300)
                        ],
                        alignment="center"
                    ),
                    margin=ft.Margin(left=0, top=20, right=0, bottom=0)
                ),
                ft.Container(
                    content=saludo_label,
                    alignment=ft.alignment.center,
                    padding=5,
                    margin=ft.Margin(left=0, top=10, right=0, bottom=10)
                ),
                ft.Container(
                    content=ft.ElevatedButton("Close", 
                                              on_click=lambda e: page.window.close(),
                                              style=ft.ButtonStyle(
                                                  bgcolor=ft.colors.RED_700,
                                                  shape=ft.RoundedRectangleBorder(radius=5)
                                              ), 
                                              color=ft.colors.WHITE,
                                              icon=ft.icons.CLOSE_OUTLINED), 
                    alignment=ft.alignment.center,
                    padding=5,
                    
                ),
            ],
            expand=True
        )
    )

ft.app(target=main)
