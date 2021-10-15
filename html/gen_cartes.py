from jinja2 import Template
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration



def create_html():
    jinja_content = open("html/index.jinja.html").read()
    template = Template(jinja_content)
    html_content = template.render()
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