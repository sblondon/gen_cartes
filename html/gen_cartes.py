from jinja2 import Template
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


CARTES = [
    {
        "gauche": "./icones/baseline_home_black_24dp.png",
        "droite": "./icones/baseline_home_black_24dp.png",
        "haut": "./icones/baseline_home_black_24dp.png",
        "bas": "./icones/baseline_home_black_24dp.png",
        "contenu": {"titre": "Admunsen", "image": "./icones/baseline_home_black_24dp.png"}
    },
    {
        "gauche": "./icones/baseline_home_black_24dp.png",
        "droite": "./icones/baseline_home_black_24dp.png",
        "haut": "./icones/baseline_home_black_24dp.png",
        "bas": "./icones/baseline_home_black_24dp.png",
        "contenu": {"titre": "Admunsen", "image": "./icones/baseline_home_black_24dp.png"}
    },
    {
        "gauche": "./icones/baseline_home_black_24dp.png",
        "droite": "./icones/baseline_home_black_24dp.png",
        "haut": "./icones/baseline_home_black_24dp.png",
        "bas": "./icones/baseline_home_black_24dp.png",
        "contenu": {"titre": "Admunsen", "image": "./icones/baseline_home_black_24dp.png"}
    },
]



def create_html():
    jinja_content = open("html/index.jinja.html").read()
    template = Template(jinja_content)
    html_content = template.render(cartes=CARTES)
    open("html/index.html", "w").write(html_content)



def create_pdf():
    create_html()

    font_config = FontConfiguration()
    html = HTML(filename="html/index.html")
    css = CSS(filename="html/style.css",
        font_config=font_config)
    html.write_pdf(
        'example.pdf', stylesheets=[css],
        font_config=font_config)

create_pdf()