import sys
import csv

from jinja2 import Template
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


CSV_CARTES = "html/cartes.exemple.csv"

ILLUSTRATIONS = {
    "exploration": "../images/illustration_exploration.png",
    "preparation": "../images/illustration_preparation.png",
}

ICONES = {
    "vide": "../images/icones/vide_black_24dp.png",
    "effet": "../images/icones/effet_court.png",
    "ou": "../images/icones/ou_black_court.png",
    "autresJoueurs": "../material-design-icons/png/social/groups/materialicons/24dp/2x/baseline_groups_black_24dp.png",
    "sacADos": "../material-design-icons/png/places/backpack/materialicons/24dp/2x/baseline_backpack_black_24dp.png",
    "capitaine": "../images/icones/capitaine.png",
    "bateau": "../material-design-icons//png/maps/directions_boat/materialiconsround/24dp/2x/round_directions_boat_black_24dp.png",
    "chien": "../material-design-icons/png/action/pets/materialicons/24dp/2x/baseline_pets_black_24dp.png",
    "finChien": "../images/icones/baseline_pets_off_black_24dp.png",
    "nourriture": "../material-design-icons/png/maps/restaurant/materialicons/24dp/2x/baseline_restaurant_black_24dp.png",
    "finNourriture": "../material-design-icons/png/maps/no_meals/materialicons/24dp/2x/baseline_no_meals_black_24dp.png",
    "traineau": "../material-design-icons/png/action/shopping_cart/materialicons/24dp/2x/baseline_shopping_cart_black_24dp.png",
    "finTraineau": "../material-design-icons/png/action/remove_shopping_cart/materialicons/24dp/2x/baseline_remove_shopping_cart_black_24dp.png",
    "homme": "../material-design-icons/png/social/person/materialicons/24dp/2x/baseline_person_black_24dp.png",
    "finHomme": "../images/icones/baseline_person_off_black_24dp.png",
    "arme": "../material-design-icons/png/hardware/security/materialicons/24dp/2x/baseline_security_black_24dp.png",
    "vetement": "../images/icones/beanie.png",
    "explore": "../material-design-icons/png/action/explore/materialicons/24dp/2x/baseline_explore_black_24dp.png",
    "deplacement": "../material-design-icons/png/maps/directions_walk/materialicons/24dp/2x/baseline_directions_walk_black_24dp.png",
    "finDeplacement": "../images/icones/walk_off.png",
    "tempete": "../material-design-icons/png/places/ac_unit/materialicons/24dp/2x/baseline_ac_unit_black_24dp.png",
}



def _icone(donnees, emplacement):
    nom = donnees[emplacement] or "vide"
    return ICONES[nom]

def _icones(donnees, emplacement):
    icones = []
    for donnee in donnees[emplacement].split("|"):
        nom = donnee or "vide"
        icones.append(ICONES[nom])
    return icones

def _cartes():
    with open(CSV_CARTES) as f:
        cartes = []
        csv_reader = csv.DictReader(f)
        for ligne in csv_reader:
            if not ligne["pile"].startswith("#"):
                carte = {
                    "gauche": _icones(ligne, "gauche"),
                    "droite": _icones(ligne, "droite"),
                    "haut": _icone(ligne, "haut"),
                    "bas": _icone(ligne, "bas"),
                    "contenu": {
                        "titre": ligne["titre"],
                        "image": _icones(ligne, "centre"),
                        "fond": ILLUSTRATIONS[ligne["pile"]]
                    },
                }
                cartes.append(carte)
    return cartes

def _cartes_par_lignes():
    cartes = _cartes()
    CARTES_PAR_LIGNE = 3
    return [
        cartes[i:i+CARTES_PAR_LIGNE]
        for i
        in range(0, len(cartes), CARTES_PAR_LIGNE)
    ]

    return cartes

def _create_html():
    jinja_content = open("html/index.jinja.html").read()
    template = Template(jinja_content)
    html_content = template.render(lignes_cartes=_cartes_par_lignes())
    open("build/body.html", "w").write(html_content)
    return html_content


def create_browsable_html():
    html_content = _create_html()
    css = open("html/style.css").read()
    browsable_content = f"<html><head><style>{css}</style></head><body>{html_content}</body></hmtl>"
    open("build/index.browsable.html", "w").write(browsable_content)


def create_pdf():
    _create_html()

    font_config = FontConfiguration()
    html = HTML(filename="build/body.html")
    css = CSS(filename="html/style.css",
        font_config=font_config)
    html.write_pdf(
        'build/cartes.pdf', stylesheets=[css],
        font_config=font_config)

if __name__ == "__main__":
    if sys.argv[1] == "browsable":
        create_browsable_html()
    else:
        create_pdf()
