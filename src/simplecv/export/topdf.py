from pdfdocument.document import PDFDocument
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus.flowables import HRFlowable


class PDFDocumentCV(PDFDocument):
    def generate_style(self, *args, **kws):
        super().generate_style(*args, **kws)
        self.style.table = self.style.tableBase
        self.style.bullet.leftIndent = 9
        self.style.bullet.bulletIndent = 0
        self.style.smaller.alignment = TA_CENTER
        self.style.smaller.fontName = "Helvetica-Oblique"

    def spacer(self):
        super().spacer(inch / 8)

    def h2(self, text):
        self.spacer()
        super().h2(text)

    def hr_mini(self):
        self.story.append(HRFlowable(width="100%", thickness=0.1))


def convert(cv, stream):
    doc = PDFDocumentCV(stream)
    doc.init_report()
    doc.h1(cv.full_name)
    doc.hr_mini()

    urls = ""
    if cv.links.count():
        urls = " · ".join([l.url for l in cv.links.all()])

    doc.p(f"{cv.email} · {cv.phone}\n{urls}")
    doc.h2("Summary")
    doc.p(cv.summary)

    if cv.skills.count():
        doc.h2("Skills")
        doc.table([(sk.category, sk.values) for sk in cv.skills.all()], [inch, inch * 5.5])

    doc.h2("Work Experience")
    for i, org in enumerate(cv.organizations.all()):
        if i:
            doc.spacer()

        doc.h3(org.name)
        doc.mini_html(f"<p><em>{org.location}</em></p>")

        for pos in org.positions.all():
            doc.spacer()
            doc.mini_html(
                f"<p><strong>{pos.title}</strong> · <em>{pos.started} - {pos.ended}</em></p>"
            )

            desc = pos.summary
            if desc:
                doc.mini_html(f"<p><em>{desc}</em></p>")

            if pos.achievements:
                achs = list(pos.iter_achievements)
                doc.ul(achs)

    if cv.educations.count():
        doc.h2("Education")
        for edu in cv.educations.all():
            deg = edu.result
            dis = edu.focus
            doc.p(
                "{}, {}{}{}".format(
                    edu.institution,
                    edu.location,
                    f", {deg}" if deg else "",
                    f", {dis}" if dis else "",
                )
            )

    doc.spacer()
    doc.hr_mini()
    doc.smaller("Last Modified: {}".format(cv.date_updated))
    doc.generate()
    return doc
