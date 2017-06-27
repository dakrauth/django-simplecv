from datetime import datetime
from pdfdocument.document import PDFDocument
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus.flowables import HRFlowable

from ..utils import load_cv, max_column_length

class PDFDocumentCV(PDFDocument):

    def generate_style(self, *args, **kws):
        super().generate_style(*args, **kws)
        self.style.table = self.style.tableBase
        self.style.bullet.leftIndent = 9
        self.style.bullet.bulletIndent = 0
        self.style.smaller.alignment = TA_CENTER
        self.style.smaller.fontName = 'Helvetica-Oblique'

    def spacer(self):
        super().spacer(inch / 8)

    def h2(self, text):
        self.spacer()
        super().h2(text)

    def hr_mini(self):
        self.story.append(HRFlowable(width='100%', thickness=0.1))


def convert(cv, stream):
    doc = PDFDocumentCV(stream)
    doc.init_report()
    doc.h1(cv['name'])
    doc.p('e: {email} · w: {url} · m: {tel}'.format(**cv))
    
    doc.h2('Summary')
    doc.p(cv['summary'])
    
    doc.h2('Skills')
    mx = 1 + max_column_length(cv['skills'], 'key')
    doc.table(
        [(sk['key'], sk['value']) for sk in cv['skills']],
        [inch, inch * 5.5]
    )

    doc.h2('Work Experience')
    for i, exp in enumerate(cv['experience']):
        if i:
            doc.spacer()

        doc.h3(exp['org'])
        doc.p('{}'.format(exp['location']))

        for i,pos in enumerate(exp['positions']):
            doc.p('{} · {} - {}'.format(
                pos['title'],
                pos['period']['from'],
                pos['period']['to']
            ))

            desc = pos.get('description')
            if desc:
                doc.p(desc)
            
            achs = pos.get('achievements', [])
            if achs:
                doc.ul(achs)

    if cv['education']:
        doc.h2('Education')
        for i, edu in enumerate(cv['education']):
            deg = edu.get('degree', '')
            dis = edu.get('descipline', '')
            doc.p('{}, {}{}{}'.format(
                edu['entity'],
                edu['location'],
                ', {}'.format(deg) if deg else '',
                ', {}'.format(dis) if dis else ''
            ))

    doc.spacer()
    doc.hr_mini()
    doc.smaller('Last Modified: {}'.format(cv['last_mod']))
    doc.generate()
    return doc

