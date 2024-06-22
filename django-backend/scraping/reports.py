import xlsxwriter
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


def dowload_excel(model_admin, request, queryset):
    model_name = model_admin.model.__name__
    response = HttpResponse(
        content_type="application/vnd.openxmlsformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = f"attachment; filename={model_name}.xlsx"
    workbook = xlsxwriter.Workbook(response)
    worksheet = workbook.add_worksheet()

    headers = [field.verbose_name for field in model_admin.model._meta.fields]
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)

    for row_num, obj in enumerate(queryset, 1):
        for col_num, field in enumerate(model_admin.model._meta.fields):
            value = str(getattr(obj, field.name))
            worksheet.write(row_num, col_num, value)

    workbook.close()
    return response


def dowload_pdf(self, request, queryset):
    model_name = self.model.__name__
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"attachment; filename={model_name}.pdf"

    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setTitle("PDF Report")

    headers = [field.verbose_name for field in self.model._meta.fields]
    data = [headers]

    for obj in queryset:
        data_row = [str(getattr(obj, field.name)) for field in self.model._meta.fields]
        data.append(data_row)

    table = Table(data)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
    )

    canvas_width = 600
    canvas_height = 600

    table.wrapOn(pdf, canvas_width, canvas_height)
    table.drawOn(pdf, 40, canvas_height - len(data))

    pdf.save()
    return response
