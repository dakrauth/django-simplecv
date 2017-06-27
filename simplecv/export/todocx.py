from datetime import datetime
from docx import Document
from docx.shared import Inches, Pt
from ..utils import load_cv, max_column_length

def convert(cv, stream):
    doc = Document()
    
    doc.core_properties.author = cv['name']
    doc.core_properties.author = 'CV'
    doc.core_properties.comments = 'Generated via Python 3 and `docx`'
    doc.core_properties.created = datetime.utcnow()
    doc.core_properties.keywords = 'résumé cv'
    
    lb2_style = doc.styles['List Bullet 2']
    lb2_style.paragraph_format.left_indent = 0
    lb2_style.paragraph_format.space_after = 0

    bt_style = doc.styles['Body Text']
    bt_style.paragraph_format.space_after = 0

    sec = doc.sections[-1]
    sec.top_margin = Inches(.5)
    sec.bottom_margin = Inches(.5)
    sec.left_margin = Inches(.5)
    sec.right_margin = Inches(.5)
        
    # if image: {image}

    doc.add_heading(cv['name'])
    doc.add_paragraph('e: {email} · w: {url} · m: {tel}'.format(**cv))
    
    doc.add_heading('Summary', level=2)
    doc.add_paragraph(cv['summary'])
    
    doc.add_heading('Skills', level=2)
    mx = 1 + max_column_length(cv['skills'], 'key')
    p = doc.add_paragraph()
    for i, skill in enumerate(cv['skills']):
        p.add_run('{}{:{}}'.format(
            '\n' if i else '',
            '{}:'.format(skill['key']),
            mx
        )).bold = True
        p.add_run('\t{}'.format(skill['value']))

    doc.add_heading('Work Experience', level=2)
    for exp in cv['experience']:
        p = doc.add_paragraph()
        p.style = bt_style
        r = p.add_run('{} '.format(exp['org']))
        r.bold = True
        r.font.size = Pt(13)
        p.add_run('· {}\n'.format(exp['location'])).italic = True

        for i,pos in enumerate(exp['positions']):
            if i:
                p = doc.add_paragraph()
                p.style = bt_style

            p.add_run('{} '.format(pos['title'])).bold = True
            p.add_run('· {} - {}'.format(
                pos['period']['from'],
                pos['period']['to']
            )).italic = True

            desc = pos.get('description')
            if desc:
                p.add_run('\n{}'.format(desc)).italic = True
            
            achs = pos.get('achievements', [])
            if achs:
                for ach in achs:
                    p = doc.add_paragraph(ach)
                    p.style = lb2_style

                p.style  = 'List Bullet'
            else:
                p.add_run('\n')

    if cv['education']:
        doc.add_heading('Education', level=2)
        p = doc.add_paragraph()
        for i, edu in enumerate(cv['education']):
            deg = edu.get('degree', '')
            dis = edu.get('descipline', '')
            p.add_run('{}{}, {}{}{}'.format(
                '\n' if i else '',
                edu['entity'],
                edu['location'],
                ', {}'.format(deg) if deg else '',
                ', {}'.format(dis) if dis else ''
            ))

    p = doc.add_paragraph()
    p.add_run('Last Modified: {}'.format(cv['last_mod'])).italic = True
    doc.save(stream)

