import flet as ft
import asyncio

async def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 800
    page.window.resizable = False
    
    # Función para cerrar la ventana
    def close_page(e):
        page.window.close()

    # Definir el texto
    label = ft.Text(
        font_family="Roboto", 
        size=30, 
        color="blue"
    )
    progress_bar = ft.ProgressBar(width=400, bgcolor=ft.colors.LIGHT_BLUE_100, color=ft.colors.BLUE_500)
    cancel_button = ft.ElevatedButton(text="Cancel", on_click=close_page)
    
    page.add(
        ft.Column(
            controls=[
                ft.Container(content=label, alignment=ft.alignment.center),
                ft.Container(content=progress_bar, alignment=ft.alignment.center),
                ft.Container(content=cancel_button, alignment=ft.alignment.center)
                ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

    # Bucle de 10 pasos, actualizando el texto cada segundo
    for i in range(10):
        label.value = f"Step {i+1}"
        progress_bar.value = (i+1) / 10
        page.update()
        await asyncio.sleep(1)

    # Al finalizar el bucle
    label.value = "Done!"
    label.color = "green"
    label.size = 40
    progress_bar.value = 1
    page.update()
    
    for _ in range(3):
        label.color = "green"
        label.size = 40
        page.update()
        await asyncio.sleep(0.3)
        label.color = "blue"
        label.size = 35
        page.update()
        await asyncio.sleep(0.3)
        label.color = "red"
        label.size = 30
        page.update()
        await asyncio.sleep(0.3)
    
    await asyncio.sleep(1)
    
    # Cerrar la ventana
    close_page(None)

# Ejecutar la app
ft.app(target=main)
