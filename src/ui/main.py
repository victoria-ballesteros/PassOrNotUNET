import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Académica"
    
    nota_actual = ft.TextField(label="Nota actual", keyboard_type="NUMBER")
    nota_meta = ft.TextField(label="Nota deseada", keyboard_type="NUMBER")
    resultado = ft.Text("Resultado: ")

    def calcular(event):
        if nota_actual.value and nota_meta.value:
            faltante = float(nota_meta.value) - float(nota_actual.value)
            resultado.value = f"Necesitas {faltante} más puntos."
            page.update()

    calcular_btn = ft.ElevatedButton(text="Calcular", on_click=calcular)

    page.add(nota_actual, nota_meta, calcular_btn, resultado)

ft.app(target=main)