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
    data = cv.data
    doc = PDFDocumentCV(stream)
    doc.init_report()
    doc.h1(data["name"])
    doc.hr_mini()

    urls = " · ".join(data["urls"])
    doc.p(
        "{email} · {tel}\n{urls}".format(
            email=data["email"], tel=data["tel"], urls=urls
        )
    )

    doc.h2("Summary")
    doc.p(data["summary"])

    doc.h2("Skills")
    doc.table([(sk["key"], sk["value"]) for sk in data["skills"]], [inch, inch * 5.5])

    doc.h2("Work Experience")
    for i, exp in enumerate(data["experience"]):
        if i:
            doc.spacer()

        doc.h3(exp["org"])
        doc.p("{}".format(exp["location"]))

        for i, pos in enumerate(exp["positions"]):
            doc.p(
                "{} · {} - {}".format(
                    pos["title"], pos["period"]["from"], pos["period"]["to"]
                )
            )

            desc = pos.get("description")
            if desc:
                doc.p(desc)

            achs = pos.get("achievements", [])
            if achs:
                doc.ul(achs)

    if data["education"]:
        doc.h2("Education")
        for i, edu in enumerate(data["education"]):
            deg = edu.get("degree", "")
            dis = edu.get("descipline", "")
            doc.p(
                "{}, {}{}{}".format(
                    edu["entity"],
                    edu["location"],
                    ", {}".format(deg) if deg else "",
                    ", {}".format(dis) if dis else "",
                )
            )

    doc.spacer()
    doc.hr_mini()
    doc.smaller("Last Modified: {}".format(cv.date_updated))
    doc.generate()
    return doc
