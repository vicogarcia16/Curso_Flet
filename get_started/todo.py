import flet as ft
from config import config_page_sf

def main(page: ft.Page):
    config_page_sf(page)
    page.title = "To-Do List"

    tasks = []  # Lista para almacenar las tareas (Checkbox y contenedor)

    # Crear una columna para las tareas
    task_column = ft.Column()

    def add_clicked(e):
        # Crear un checkbox para cada tarea con el valor del textfield
        checkbox = ft.Checkbox(label=new_task.value)
        
        # Crear un contenedor para cada tarea
        task_panel = ft.Card(
            content=ft.Container(
                content=ft.Row(controls=[
                    checkbox
                ],
                alignment="start"
                ),
                padding=10,
                width=345,
            ), 
            margin=ft.Margin(left=25, top=10, right=30, bottom=-10)
        )
        
        # Agregar la tarea y el contenedor a la lista de tareas
        tasks.append((checkbox, task_panel))
        
        # Agregar el panel de tarea a la columna de tareas
        task_column.controls.append(task_panel)
        
        # Limpiar el campo de texto
        new_task.value = ""
        page.update()

    def delete_checked_tasks(e):
        # Recorrer las tareas y eliminar solo las completadas (seleccionadas)
        for checkbox, task_panel in tasks[:]:  # Iteramos sobre una copia de la lista
            if checkbox.value:  # Si la tarea está seleccionada (completada)
                task_column.controls.remove(task_panel)  # Eliminar el panel de la interfaz
                tasks.remove((checkbox, task_panel))  # Remover la tarea de la lista
        
        # Actualizar la página
        page.update()

    def handle_hover(e):
        # Mostrar el botón de cerrar al pasar el mouse
        close_button.visible = e.data == "true"
        page.update()

    # Crear el botón de cerrar flotante
    close_button = ft.IconButton(
        ft.icons.CLOSE_OUTLINED,
        on_click=lambda e: page.window.close(),
        icon_size=35,
        icon_color=ft.colors.RED,
        visible=False  # Inicialmente oculto
    )
    
    # Botones para agregar y eliminar tareas
    add_button = ft.IconButton(
        ft.icons.ADD_CIRCLE_OUTLINED,
        on_click=add_clicked,
        icon_size=35,
        icon_color=ft.colors.BLUE
    )
    
    delete_button = ft.IconButton(
        ft.icons.DELETE_ROUNDED,
        on_click=delete_checked_tasks,
        icon_size=35,
        icon_color=ft.colors.GREEN
    )

    # Campo de texto para agregar tareas
    new_task = ft.TextField(hint_text="What needs to be done?", width=225, 
                            on_submit=add_clicked)

    # Controles fijos (textfield y botones) siempre visibles arriba
    control_panel = ft.Container(
        content=ft.Row(
            controls=[new_task, add_button, delete_button],
            alignment="start"
        ),
        margin=ft.Margin(left=25, top=20, right=0, bottom=0)
    )

    # Contenedor con el botón de cerrar que aparece al pasar el mouse
    close_container = ft.Container(
        content=close_button,
        alignment=ft.alignment.center,
        padding=5,
        on_hover=handle_hover  # Detectar si el mouse pasa por encima
    )

    # Organizar la interfaz en un `Column` con tareas debajo de los controles
    page.add(
        ft.Column(
            controls=[
                control_panel,  # Controles arriba
                task_column,    # Columna de tareas
                close_container # Botón flotante de cerrar
            ],
            expand=True,
        )
    )

ft.app(target=main)
