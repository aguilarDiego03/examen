import flet as ft

def main(page: ft.Page):
    page.title = "Registro de participantes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    nombre = ft.TextField(
        label="Nombre completo",
        prefix_icon=ft.Icons.PERSON,
        border_color=ft.Colors.BLUE,
        bgcolor=ft.Colors.GREY_100,
        width=400
    )
    
    correo = ft.TextField(
        label="Correo electrónico",
        border_color=ft.Colors.BLUE,
        width=400
    )

    tipo = ft.Dropdown(
        label="Taller de interés",
        border_color=ft.Colors.BLUE,
        width=400,
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ],
        value="Python para Principiantes"
    )

    modalidad = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="Pago completo", label="Pago completo"),
                ft.Radio(value="Pago por cuotas", label="Pago por cuotas"),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        value="Pago completo"
    )

    inscripcion = ft.Checkbox(
        label="¿Requiere computadora portátil?",
        value=False,
        width=250
    )

    duracion = ft.Slider(
        min=1,
        max=5,
        divisions=5,
        label="{value} Nivel de experiencia",
        value=1,
        width=400
    )

    resumen = ft.Text(
        value="",
        size=16,
        weight=ft.FontWeight.BOLD
    )

    lista_eventos = ft.ListView(
        expand=True,
        spacing=15,
        auto_scroll=True,
        width=400
    )

    def mostrar(e):
        if not nombre.value or nombre.value.strip() == "":
            resumen.value = "ERROR, rellene el campo"
            resumen.color = ft.Colors.RED
        else:
            texto_evento = (
                f"Nombre: {nombre.value} | "
                f"Tipo: {tipo.value} | "
                f"Modalidad: {modalidad.value} | "
                f"Inscripción: {'Sí' if inscripcion.value else 'No'} | "
                f"Duración: {int(duracion.value)} horas"
            )

            resumen.value = texto_evento
            resumen.color = ft.Colors.BLACK

            lista_eventos.controls.append(ft.Text(texto_evento))

            nombre.value = ""

        page.update()

    boton = ft.ElevatedButton(
        "Mostrar resumen",
        on_click=mostrar
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Formulario de Registro de Eventos",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.RED_400
                ),
                nombre,
                correo,
                tipo,
                modalidad,
                inscripcion,
                duracion,
                boton,
                ft.Divider(),
                resumen,
                ft.Divider(),
                ft.Text("Eventos registrados:", weight=ft.FontWeight.BOLD),
                lista_eventos,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)