import os

TITULO = "Fundación SCP"

CSS = """
body{
background:#000;
color:white;
font-family:Arial;
margin:0;
padding:0;
}

header{
background:#111;
padding:20px;
text-align:center;
border-bottom:2px solid #333;
}

header h1{
margin:0;
font-size:40px;
}

.container{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
gap:20px;
padding:20px;
}

.card{
background:#111;
border:1px solid #333;
padding:10px;
text-align:center;
transition:0.3s;
}

.card:hover{
transform:scale(1.03);
border-color:white;
}

.card img{
width:100%;
height:250px;
object-fit:cover;
}

.card h2{
margin-top:10px;
font-size:24px;
}

a{
color:white;
text-decoration:none;
}

.scp-page{
padding:20px;
}

.scp-page img{
width:100%;
max-width:500px;
display:block;
margin:auto;
}

.documentacion{
background:#111;
padding:20px;
margin-top:20px;
border:1px solid #333;
white-space:pre-wrap;
}

.volver{
display:inline-block;
margin-bottom:20px;
font-size:28px;
font-weight:bold;
color:white;
text-decoration:none;
}

.categoria{
margin-top:15px;
font-size:22px;
color:#aaa;
text-align:center;
}

.popup{
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
background:rgba(0,0,0,0.85);
display:flex;
justify-content:center;
align-items:center;
z-index:9999;
}

.popup-box{
background:#111;
border:1px solid #444;
padding:30px;
width:90%;
max-width:400px;
text-align:center;
}

.popup-box h2{
font-size:32px;
margin-bottom:15px;
}

.popup-box p{
color:#aaa;
font-size:18px;
}

.popup-buttons{
margin-top:20px;
display:flex;
justify-content:center;
gap:20px;
}

.popup-buttons button{
background:#000;
color:white;
border:1px solid #555;
padding:15px 25px;
font-size:18px;
cursor:pointer;
}

.popup-buttons button:hover{
border-color:white;
}
"""

with open("style.css","w",encoding="utf-8") as f:
    f.write(CSS)

scp_folders = []

for item in os.listdir():
    if os.path.isdir(item) and item.startswith("SCP-"):
        scp_folders.append(item)

scp_folders.sort()

cards = ""

for scp in scp_folders:

    numero = scp

    imagen = None

    for archivo in os.listdir(scp):
        if archivo.lower().endswith((".png",".jpg",".jpeg",".webp")):
            imagen = archivo
            break

    if imagen is None:
        continue

    categoria = "Sin categoría"

    categoria_path = os.path.join(scp,"categoria.txt")

    if os.path.exists(categoria_path):
        with open(categoria_path,"r",encoding="utf-8") as f:
            categoria = f.read().strip()

    cards += f"""
    <a href="{scp}/index.html">
    <div class="card">
    <img src="{scp}/{imagen}">
    <h2>{numero}</h2>
    <p>{categoria}</p>
    </div>
    </a>
    """

INDEX = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{TITULO}</title>
<link rel="stylesheet" href="style.css">
</head>

<body>

<header>
<h1>{TITULO}</h1>
</header>

<div class="container">
{cards}
</div>

</body>
</html>
"""

with open("index.html","w",encoding="utf-8") as f:
    f.write(INDEX)

for scp in scp_folders:

    archivos = os.listdir(scp)

    imagen = None

    for archivo in archivos:
        if archivo.lower().endswith((".png",".jpg",".jpeg",".webp")):
            imagen = archivo
            break

    if imagen is None:
        continue

    documentacion = "Sin documentación"

    doc_path = os.path.join(scp,"documentacion.txt")

    if os.path.exists(doc_path):
        with open(doc_path,"r",encoding="utf-8") as f:
            documentacion = f.read()

    categoria = "Sin categoría"

    categoria_path = os.path.join(scp,"categoria.txt")

    if os.path.exists(categoria_path):
        with open(categoria_path,"r",encoding="utf-8") as f:
            categoria = f.read().strip()

    SCP_HTML = f"""
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">

<title>{scp}</title>

<link rel="stylesheet" href="../style.css">

<script src="https://pl29475754.effectivecpmnetwork.com/7b/95/37/7b953705d79ce2bb7250c4338d6c2a42.js"></script>

</head>

<body>

<div id="popup" class="popup">

<div class="popup-box">

<h2>Apoya al creador</h2>

<p>
¿Quieres ver un anuncio para apoyar al creador?
</p>

<div class="popup-buttons">

<button onclick="aceptarAnuncio()">
Sí
</button>

<button onclick="cerrarPopup()">
No
</button>

</div>

</div>

</div>

<script>

function cerrarPopup(){{
document.getElementById("popup").style.display = "none";
}}

function aceptarAnuncio(){{
document.getElementById("popup").style.display = "none";
}}

</script>

<div class="scp-page">

<a class="volver" href="../index.html">
⬅ Volver
</a>

<h1>{scp}</h1>

<img src="{imagen}">

<div class="categoria">
Categoría: {categoria}
</div>

<div class="documentacion">
{documentacion}
</div>

</div>

</body>
</html>
"""

    with open(os.path.join(scp,"index.html"),"w",encoding="utf-8") as f:
        f.write(SCP_HTML)

print("Web SCP generada correctamente.")
