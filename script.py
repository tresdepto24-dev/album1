import os
from PIL import Image, ImageDraw

def generar_pagina_bronceada(estampillas_paths, datos_usuario, archivo_salida="hoja_bronceada_final.png"):
    # Dimensiones de la lámina vintage
    width, height = 1200, 1600
    canvas = Image.new('RGB', (width, height), color='#f4ebd0') # Tono pergamino
    draw = ImageDraw.Draw(canvas)
    
    # Encabezado estilo guía telefónica antigua
    # Usamos texto básico integrado para evitar errores de fuentes externas
    draw.text((width // 2 - 250, 60), "PAGINAS BRONCEADAS -- DIRECTORIO DE COLECCION", fill='#2c1810')
    draw.text((width // 2 - 200, 100), "Su Registro Historico y Caja de Ahorros BonusCom", fill='#5c3a21')

    # Grilla de 2 columnas x 5 filas para las 10 piezas
    start_x, start_y = 100, 180
    ancho_tarjeta, alto_tarjeta = 190, 240
    gap_x, gap_y = 50, 40
    
    for i in range(min(10, len(estampillas_paths))):
        col = i % 5
        row = i // 5
        x = start_x + col * (ancho_tarjeta + gap_x)
        y = start_y + row * (alto_tarjeta + gap_y)
        
        # Marco del aviso clasificado
        draw.rectangle([x, y, x + ancho_tarjeta, y + alto_tarjeta], outline='#5c3a21', width=3)
        
        # Espacio para la estampilla o postal (placeholder interno)
        draw.rectangle([x + 15, y + 15, x + 175, y + 115], fill='#e3d2b0', outline='#5c3a21')
        
        # Inyectar datos debajo de la imagen
        texto_id = f"ID: {datos_usuario['id']}-0{i}"
        texto_geo = f"GEO: {datos_usuario['geo']}"
        texto_peso = f"PESO: {datos_usuario['peso']}MB"
        texto_msg = f"MSG: {datos_usuario['mensaje'][:15]}"
        
        draw.text((x + 15, y + 125), "Aviso Destacado", fill='#2c1810')
        draw.text((x + 15, y + 145), texto_id, fill='#475569')
        draw.text((x + 15, y + 165), texto_geo, fill='#475569')
        draw.text((x + 15, y + 185), texto_peso, fill='#475569')
        draw.text((x + 15, y + 205), texto_msg, fill='#0f172a')

    # Pie de página oficial
    draw.text((width // 2 - 300, height - 50), "(c) 2026 VentaniYA! Cinemascopado -- Guia Interactiva", fill='#5c3a21')

    # Guardar resultado final
    canvas.save(archivo_salida)
    print(f"¡Hoja generada con exito: {archivo_salida}!")

# Datos de prueba locales automáticos
mock_images = ["img.png"] * 10
mock_data = {
    'id': '2026-X100',
    'geo': 'MAR DEL PLATA',
    'peso': '15',
    'mensaje': 'Captura de esencia'
}

generar_pagina_bronceada(mock_images, mock_data)
