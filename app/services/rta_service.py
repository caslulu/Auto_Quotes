from datetime import datetime
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, NumberObject, TextStringObject
import io

class RTAService:
    def __init__(self, template_path='app/static/rta_template.pdf', font_path='arial.ttf', font_size=16):
        self.template_path = template_path
        self.font_path = font_path
        self.font_size = font_size

    def preencher_rta(self, form):
        reader = PdfReader(self.template_path)
        writer = PdfWriter()
        writer.append(reader)
        
        # Campos a serem preenchidos
        campos = {
            # VIN
            "(B1) Vehicle Identification Number (VIN)": str(getattr(form, "vin", None) and form.vin.data or ""),
            # Body Style
            "(B2) Body Style": str(getattr(form, "body_style", None) and form.body_style.data or ""),
            # Cores
            "(B4) Black": NameObject("/On") if getattr(form, "color", None) and form.color.data == "Black" else NameObject("/Off"),
            "(B4 ) White": NameObject("/On") if getattr(form, "color", None) and form.color.data == "White" else NameObject("/Off"),
            "(B4) Brown": NameObject("/On") if getattr(form, "color", None) and form.color.data == "Brown" else NameObject("/Off"),
            "(B4) Blue": NameObject("/On") if getattr(form, "color", None) and form.color.data == "Blue" else NameObject("/Off"),
            "(B4) Yellow": NameObject("/On") if getattr(form, "color", None) and form.color.data == "Yellow" else NameObject("/Off"),
            "(B4) Gray": NameObject("/On") if getattr(form, "color", None) and form.color.data == "Gray" else NameObject("/Off"),
            "(B4 ) Purple": NameObject("/On") if getattr(form, "color", None) and form.color.data == "Purple" else NameObject("/Off"),
            "(B4) Green": NameObject("/On") if getattr(form, "color", None) and form.color.data == "Green" else NameObject("/Off"),
            "(B4) Orange": NameObject("/On") if getattr(form, "color", None) and form.color.data == "Orange" else NameObject("/Off"),
            "(B4) Red": NameObject("/On") if getattr(form, "color", None) and form.color.data == "Red" else NameObject("/Off"),
            "(B4) Silver": NameObject("/On") if getattr(form, "color", None) and form.color.data == "Silver" else NameObject("/Off"),
            "(B4) Gold": NameObject("/On") if getattr(form, "color", None) and form.color.data == "Gold" else NameObject("/Off"),
            # Odometer
            "(B9) Odometer (Miles)": str(form.odometer.data) if getattr(form, "odometer", None) and form.odometer.data not in (None, "") else "",
            # Year
            "(B5) Vehicle Year": str(getattr(form, "year", None) and form.year.data or ""),
            # Make
            "(B5) (Vehicle) Make": str(getattr(form, "make", None) and form.make.data or ""),
            # Model
            "(B5) (Vehicle) Model": str(getattr(form, "model", None) and form.model.data or ""),
            # Cylinder, Passengers, Doors
            "(B7) Number of cylinders": str(getattr(form, "cylinders", None) and form.cylinders.data or ""),
            "(B7) Number of passengers": str(getattr(form, "passengers", None) and form.passengers.data or ""),
            "(B7) Number of doors": str(getattr(form, "doors", None) and form.doors.data or ""),
            # Previous Title Info
            "(C3) Previous title number": str(getattr(form, "previous_title_number", None) and form.previous_title_number.data or ""),
            "(C3) Previous title state": str(getattr(form, "previous_title_state", None) and form.previous_title_state.data or ""),
            "(C3) Previous title country": str(getattr(form, "previous_title_country", None) and form.previous_title_country.data or ""),
        }

        # Abordagem manual e direta para garantir o preenchimento
        for page in writer.pages:
            if "/Annots" in page:
                for annot in page["/Annots"]:
                    obj = annot.get_object()
                    field_name = obj.get("/T")

                    if field_name and field_name in campos:
                        value = campos[field_name]
                        
                        obj.update({
                            NameObject("/Ff"): NumberObject(0)
                        })

                        if obj.get("/FT") == "/Btn":
                            obj.update({
                                NameObject("/V"): value,
                                NameObject("/AS"): value,
                            })
                        elif obj.get("/FT") == "/Tx":
                            obj.update({
                                NameObject("/V"): TextStringObject(str(value))
                            })
        writer.set_need_appearances_writer(True)

        pdf_io = io.BytesIO()
        writer.write(pdf_io)
        pdf_io.seek(0)
        return pdf_io
