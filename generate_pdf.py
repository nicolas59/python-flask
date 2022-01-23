import pdfkit
import os
from markdown import markdown, Markdown
from pygments.formatters import HtmlFormatter


def generate_pdf(file):
    fileName = os.path.splitext(file)[0]
    with open(file, encoding="utf-8") as data:
        text = data.read()

    style = HtmlFormatter().get_style_defs('.codehilite')
    # #Markdown → HTML conversion
    md = Markdown(extensions=['extra', 'codehilite'])
    body = md.convert(text)
    #Fit to HTML format
    html = '<html lang="fr"><meta charset="utf-8"><body>'
    #Import stylesheets created with Pygments
    html += '<style>{}</style>'.format(style)
    #Add style to add border to Table tag
    html += '''<style> table,th,td { 
        border-collapse: collapse;
        border:1px solid #333; 
        }
         pre{
            padding:10px;
           /* background: #ededed:*/
         }
         </style>'''
    html += body + '</body></html>'

    pdfkit.from_string(html, fileName+".pdf")


generate_pdf("01.flask.md")
generate_pdf("02.sql-alchemy.md")
generate_pdf("03.Flask+SQLAlchemy.md")