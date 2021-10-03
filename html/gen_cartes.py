from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


font_config = FontConfiguration()

html = HTML(filename="index.html")

css = CSS(filename="style.css",
    font_config=font_config)
html.write_pdf(
    'example.pdf', stylesheets=[css],
    font_config=font_config)