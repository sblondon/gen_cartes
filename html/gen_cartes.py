from jinja2 import Template
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration



illusExploration = "illustration_exploration"
illusPreparation = "illustration_preparation"
iconeVide = "images/icones/vide_black_24dp.png"
iconeEffet = "material-design-icons/png/navigation/east/materialicons/24dp/2x/baseline_east_black_24dp.png"
iconeOu = "images/icones/ou_black_24dp.png"
iconeAutresJoueurs = "material-design-icons/png/social/groups/materialicons/24dp/2x/baseline_groups_black_24dp.png"
iconeSacADos = "material-design-icons/png/places/backpack/materialicons/24dp/2x/baseline_backpack_black_24dp.png"
iconeCapitaine = "images/icones/capitaine.png"
iconeBateau = "material-design-icons//png/maps/directions_boat/materialiconsround/24dp/2x/round_directions_boat_black_24dp.png"
iconeChien = "material-design-icons/png/action/pets/materialicons/24dp/2x/baseline_pets_black_24dp.png"
iconeFinChien = "images/icones/baseline_pets_off_black_24dp.png"
iconeNourriture = "material-design-icons/png/maps/restaurant/materialicons/24dp/2x/baseline_restaurant_black_24dp.png"
iconeFinNourriture = "material-design-icons/png/maps/no_meals/materialicons/24dp/2x/baseline_no_meals_black_24dp.png"
iconeTraineau = "material-design-icons/png/action/shopping_cart/materialicons/24dp/2x/baseline_shopping_cart_black_24dp.png"
iconeFinTraineau = "material-design-icons/png/action/remove_shopping_cart/materialicons/24dp/2x/baseline_remove_shopping_cart_black_24dp.png"
iconeHomme = "material-design-icons/png/social/person/materialicons/24dp/2x/baseline_person_black_24dp.png"
iconeFinHomme = "images/icones/baseline_person_off_black_24dp.png"
iconeArme = "material-design-icons/png/hardware/security/materialicons/24dp/2x/baseline_security_black_24dp.png"
iconeVetement = "images/icones/beanie.png"
iconeExplore = "material-design-icons/png/action/explore/materialicons/24dp/2x/baseline_explore_black_24dp.png"
iconeDeplacement = "material-design-icons/png/maps/directions_walk/materialicons/24dp/2x/baseline_directions_walk_black_24dp.png"
iconeFinDeplacement = "images/icones/walk_off.png"
iconeTempete = "material-design-icons/png/places/ac_unit/materialicons/24dp/2x/baseline_ac_unit_black_24dp.png"


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
        "contenu": {"titre": "AA", "image": "./icones/baseline_home_black_24dp.png"}
    },
    {
        "gauche": "./icones/baseline_home_black_24dp.png",
        "droite": "./icones/baseline_home_black_24dp.png",
        "haut": "./icones/baseline_home_black_24dp.png",
        "bas": "./icones/baseline_home_black_24dp.png",
        "contenu": {"titre": "BB", "image": "./icones/baseline_home_black_24dp.png"}
    },
]


def _cartes_par_lignes(cartes):
    CARTES_PAR_LIGNE = 3
    return [
        cartes[i:i+CARTES_PAR_LIGNE]
        for i
        in range(0, len(cartes), CARTES_PAR_LIGNE)
    ]

    return cartes

def create_html():
    jinja_content = open("html/index.jinja.html").read()
    template = Template(jinja_content)
    html_content = template.render(lignes_cartes=_cartes_par_lignes(CARTES))
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