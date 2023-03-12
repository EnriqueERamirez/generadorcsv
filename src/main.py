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
                'title_tecno': "Lenguages programacion",
            },
             '2':{
                'title_project': "Proyecto",
                'title_edu': "Proyecto",
                'title_works': "Proyecto",
                'title_about': "Proyecto",
                'title_social': "Proyecto",
                'title_knows': "Proyecto",
                'title_skill': "Proyecto",
                'title_tecno': "Lenguages programacion",
            }

        }
icondict = {
        'Localitation': 'map-signs',
        'mobile': 'mobile-alt',
        'Email': 'envelope',
        'Facebook': 'facebook-square',
        'Twitter': 'twitter-square',
        }
def CreateContext(datayaml, listargs):
    context = { 
        'listsocial': [
                {
                'icon': 'facebook-square',
                'name': 'Facebook',
                'data': "enrique@facebook",
                },
                {
                'icon': 'twitter-square',
                'name': 'Twitter',
                'data': "enrique@twitter",
                },
            ],

            }
    _listtitle = titlelist[str(listargs.lenguage)]
    for key in _listtitle:
        context[key] = _listtitle[key]
    #create basic info
    for databasic in datayaml['BasicInfo']:
        if databasic['Leng'] == listargs.lenguage:
            context['my_name'] = databasic['Name']
            context['my_degree'] = databasic['Degree']
            break
    for about in datayaml['About']:
        if about['Leng'] == listargs.lenguage and about['categoria'] == listargs.typework:
            context['my_about'] = about['texto']
            break
    #lenguage list create
    lenp = []
    for lprogram in datayaml['LenguagePrograming']:
        if listargs.lenguageProgram in lprogram['Category']:
            lenp.append(lprogram['name'])
    context['listlendev'] = lenp
    teorylist = []
    for teory in datayaml['TeoryManage']:
        if listargs.lenguageProgram in teory['Category']:
            teorylist.append(teory['name'])
    context['listknows'] = teorylist
    tecnologylist = []
    for tecn in datayaml['TecnologiUse']:
        if listargs.lenguageProgram in tecn['Category']:
            tecnologylist.append(tecn['name'])
    context['listtecno'] = tecnologylist
    ListEduc = []
    for edu in datayaml['Study']:
       auxdic = {}
       auxdic['datestart'] = edu['DateRange'][0]
       auxdic['dateend'] = edu['DateRange'][1]
       auxdic['title'] = edu['Name']
       auxdic['data'] = edu['Data']
       ListEduc.append(auxdic)
    context['listedu'] = ListEduc
    ListJobs = []
    for job in datayaml['Jobs']:
       auxdic = {}
       auxdic['datestart'] = job['RangeDate'][0]
       auxdic['dateend'] = job['RangeDate'][1]
       auxdic['title'] = job['Posicion']
       auxdic['data'] = job['Description']
       ListJobs.append(auxdic)
    context['listworks'] = ListJobs
    print(datayaml['BasicInfo'][0]['Localitation'])
    context['metadata'] = [
                    {
                    'icon': 'map-signs',
                    'data': datayaml['BasicInfo'][0]['Localitation'],
                    },
                    {
                    'icon': 'mobile-alt',
                    'data': datayaml['BasicInfo'][0]['mobile'],
                    },
                    {
                    'icon': 'envelope',
                    'data': datayaml['BasicInfo'][0]['Email'],
                    },
                ]
 
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
    parser.add_argument('-lngp','--lenguageProgram', type=int, default=6, help='Lenguajes de programacion segun area')
    parser.add_argument('-o','--out', type=str, default='out', help='directorio de salida')
    return parser.parse_args()
if __name__=='__main__':
    request = getargscommandline()
    yamlfile = openyaml(request.file)
    context = CreateContext(yamlfile, request)
    rendercv(context)


