import os
import jinja2
import pdfkit
from datetime import datetime

my_name = "Frank Andrade"

context = {
        'my_name': my_name,
        'my_degree': "ingenieriai civil electronica",
        'my_about': "askdjkasjdkasjdkj ajdkjakdjakdjk kasjdlajdoqwiujeokds aksdjaosed",
        'title_project': "Proyecto",
        'title_edu': "Proyecto",
        'title_works': "Proyecto",
        'title_about': "Proyecto",
        'title_social': "Proyecto",
        'title_knows': "Proyecto",
        'title_skill': "Proyecto",
        'metadata': [
                {
                'icon': 'map-signs',
                'data': "direccion de prueba",
                },
                {
                'icon': 'mobile-alt',
                'data': "+58 99123123",
                },
                {
                'icon': 'envelope',
                'data': "test@gmail.com",
                },
            ],
        'listsocial': [
                {
                'icon': 'facebook-square',
                'name': 'Facebook',
                'data': "Stephen@facebook",
                },
                {
                'icon': 'twitter-square',
                'name': 'Twitter',
                'data': "Stephen@twitter",
                },
            ],
        'listworks': [
                {
                'datestart': '2011',
                'dateend': '2012',
                'title': 'Test',
                'data': "asdasdasdasdasdasdasdasdasdasdasdasdasdasdasd",
                },
            ],
        'listedu': [
                {
                'datestart': '2011',
                'dateend': '2012',
                'title': 'Test',
                'data': "asdasdasdasdasdasdasdasdasdasdasdasdasdasdasd",
                },
            ],

        'listlendev': ['python', 'java', '.net'],
        'listknows': ['math', 'fisics', 'electronics'],
        }

template_loader = jinja2.FileSystemLoader("template")
template_env = jinja2.Environment(loader=template_loader)

html_template = 'index.html'
template = template_env.get_template(html_template)
output_text = template.render(context)
print(output_text)
# config = pdfkit.configuration(wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
# config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
# output_pdf = 'pdf_generated.pdf'
# pdfkit.from_string(output_text, output_pdf, configuration=config, css='template/style.css')
