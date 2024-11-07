import PyPDF2


def extraer_paginas(input_pdf, output_pdf, paginas):
    # Abre el archivo PDF de entrada
    with open(input_pdf, 'rb') as archivo_entrada:
        # Crea un lector de PDF
        lector_pdf = PyPDF2.PdfReader(archivo_entrada)

        # Crea un escritor de PDF
        escritor_pdf = PyPDF2.PdfWriter()

        # Añade las páginas especificadas al escritor de PDF
        for pagina in paginas:
            escritor_pdf.add_page(lector_pdf.pages[pagina])

        # Guarda las páginas seleccionadas en un nuevo archivo PDF
        with open(output_pdf, 'wb') as archivo_salida:
            escritor_pdf.write(archivo_salida)


# Uso del ejemplo
input_pdf = 'PDF/Ajuste.pdf'
output_pdf = 'paginas_extraidas-ajuste.pdf'
paginas = [36,37,38,40,41]  # Índices de las páginas a extraer (empezando desde 0)

extraer_paginas(input_pdf, output_pdf, paginas)

input_pdf = 'PDF/Rumi-Setiembre2024.pdf'
output_pdf = 'paginas_extraidas-rumi.pdf'
paginas = [19,20,21]  # Índices de las páginas a extraer (empezando desde 0)

extraer_paginas(input_pdf, output_pdf, paginas)

input_pdf = 'PDF/Multistock.pdf'
output_pdf = 'paginas_extraida-multistock.pdf'
paginas = [15, 16]  # Índices de las páginas a extraer (empezando desde 0)

extraer_paginas(input_pdf, output_pdf, paginas)
