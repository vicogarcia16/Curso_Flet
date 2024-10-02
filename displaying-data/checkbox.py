import flet as ft
from config import config_page_sf

def main(page: ft.Page):
    page.title = "Checkbox"
    page = config_page_sf(page)
    
    def tarea_checked(e):
        if e.control.value:
            lbl_resultado.value = f"Has marcado la tarea"
            lbl_resultado.visible = True
        else:
            lbl_resultado.visible = False
        page.update()
        
    lbl_resultado = ft.Text()
    chk_tarea = ft.Row(
            controls=[
                ft.Checkbox(
                    label="Marcar la tarea",
                    value=False,
                    on_change=tarea_checked,
                    
                )
            ],
            alignment="center",  
        )

    page.add(chk_tarea, ft.Row(controls=[lbl_resultado], alignment="center"))
    
ft.app(target=main)