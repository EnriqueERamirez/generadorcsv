import os
import jinja2
import pdfkit
from datetime import datetime
import argparse
import yaml
my_name = "Frank Andrade"
titlelist = { 
             '1':{
                'title_project': "Proyecto",
                'title_edu': "Educacion",
                'title_works': "Experiencia",
                'title_about': "Acerca de mi",
                'title_social': "Informcacion social",
                'title_knows': "Conocimiento",
                'title_skill': "Lenguages programacion",
            },
             '2':{
                'title_project': "Proyecto",
                'title_edu': "Proyecto",
                'title_works': "Proyecto",
                'title_about': "Proyecto",
                'title_social': "Proyecto",
                'title_knows': "Proyecto",
                'title_skill': "Proyecto",
            }

        }
context = {
        'my_name': my_name,
        'my_degree': "ingenieriai civil electronica",
        'my_about': "askdjkasjdkasjdkj ajdkjakdjakdjk kasjdlajdoqwiujeokds aksdjaosed",
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
def CreateContext(datayaml, listargs):
    context = {}
    _listtitle = titlelist[str(listargs.lenguage)]
    for key in _listtitle:
        context[key] = _listtitle[key]
    return context
def openyaml(filepath):
    with open(filepath, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded
def rendercv(context):
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
def getargscommandline():
    parser = argparse.ArgumentParser(description='Generacion de cv para postulacion')
    parser.add_argument('-f','--file', type=str, required=True,
                    help='direccion del yaml con los datos cv')
    parser.add_argument('-lng','--lenguage', type=int, default=1, help='lenguage en el que se generara el cv')
    parser.add_argument('-tpwork','--typework', type=int, default=1, help='Tipo de trabajo que se desea postular')
    parser.add_argument('-arw','--areawork', type=int, default=1, help='Area al que se desea al postular')
    parser.add_argument('-lnsp','--lenguageSpeak', type=int, default=1, help='Lenguage cultural enfoco')
    parser.add_argument('-o','--out', type=str, default='out', help='directorio de salida')
    return parser.parse_args()
if __name__=='__main__':
    request = getargscommandline()
    yamlfile = openyaml(request.file)
    context = CreateContext(yamlfile, request)

