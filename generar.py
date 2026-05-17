import os

scp_folders = []

for item in os.listdir("."):
    if os.path.isdir(item) and item.startswith("SCP-"):
        scp_folders.append(item)

scp_folders.sort()

cards = ""

for folder in scp_folders:

    image = f"{folder}/{folder}.png"

    texto = "Sin documentación"

    categoria = "Sin categoría"

    # =========================
    # DOCUMENTACION
    # =========================

    doc = os.path.join(folder, "documentacion.txt")

    if os.path.exists(doc):
        with open(doc, "r", encoding="utf-8") as f:
            texto = f.read()

    # =========================
    # CATEGORIA
    # =========================

    categoria_file = os.path.join(folder, "categoria.txt")

    if os.path.exists(categoria_file):
        with open(categoria_file, "r", encoding="utf-8") as f:
            categoria = f.read()

    # =========================
    # PAGINA SCP
    # =========================

    pagina = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{folder}</title>
<link rel="stylesheet" href="../style.css">
</head>
<body>

<div class="container">

<a class="volver-btn" href="../index.html">
← VOLVER
</a>

<img src="{folder}.png" class="imagen">

<h1 class="scp-nombre">{folder}</h1>

<div class="categoria">
Categoría: {categoria}
</div>

<div class="doc">
<pre>{texto}</pre>
</div>

</div>

</body>
</html>
"""

    with open(f"{folder}/index.html", "w", encoding="utf-8") as f:
        f.write(pagina)

    # =========================
    # TARJETAS PRINCIPALES
    # =========================

    cards += f"""
<div class="card">
<a href="{folder}/index.html">
<img src="{image}">
<h2>{folder}</h2>
</a>
</div>
"""

# =========================
# INDEX PRINCIPAL
# =========================

index = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Archivo SCP</title>
<link rel="stylesheet" href="style.css">
</head>
<body>

<header>
<h1 class="titulo">ARCHIVO SCP</h1>
<p class="subtitulo">Base de datos clasificada</p>
</header>

<div class="grid">
{cards}
</div>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index)

print("Sitio generado correctamente")