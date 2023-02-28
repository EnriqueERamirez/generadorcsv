import os
import jinja2
import pdfkit
from datetime import datetime

my_name = "Frank Andrade"

context = {
        'my_name': my_name,
        'my_degree': "ingenieriai civil electronica",
        'my_address': "direccion de prueba",
        'my_numberphone': "+58 99123123",
        'my_email': "test@gmail.com",
        'my_about': "askdjkasjdkasjdkj ajdkjakdjakdjk kasjdlajdoqwiujeokds aksdjaosed",
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
