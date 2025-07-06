from datetime import datetime
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, NumberObject, TextStringObject
import io

class RTAService:
    def __init__(self, template_path='app/assets/rta_template.pdf', font_path='arial.ttf', font_size=16):
        self.template_path = template_path
        self.font_path = font_path
        self.font_size = font_size


    def _parse_address(self, address, expected_parts=5):
        # Divide endereço em partes (rua, apt, cidade, estado, cep)
        parts = [p.strip() for p in str(address).split(",")]
        return [(parts[i] if len(parts) > i else "") for i in range(expected_parts)]

    def _color_checkbox(self, form, color):
        # Marca a cor correta no PDF
        return NameObject("/On") if getattr(form, "color", None) and form.color.data == color else NameObject("/Off")

    def preencher_rta(self, form):
        reader = PdfReader(self.template_path)
        writer = PdfWriter()
        writer.append(reader)

        # Endereço do vendedor
        seller_rua, seller_apt, seller_cidade, seller_estado, seller_cep = self._parse_address(
            getattr(form, "seller_address", None) and form.seller_address.data or "",
            expected_parts=5
        )
        # Endereço do proprietário
        endereco_rua, endereco_apt, endereco_cidade, endereco_estado, endereco_cep = self._parse_address(
            getattr(form, "owner_residential_address", None) and form.owner_residential_address.data or ""
        )

        # Campos do PDF
        campos = {
            # Seller Info
            "(L1) Seller name (Please print)": str(getattr(form, "seller_name", None) and form.seller_name.data or ""),
            "(L2) (Seller) Address": seller_rua,
            "(L2) (Seller) Apt": seller_apt,
            "(L2) (Seller) City": seller_cidade,
            "(L2) (Seller) State": seller_estado,
            "(L2) (Seller) Zip Code": seller_cep,
            # Sale Info
            "(I3) Gross Sale Price (Proof Required)": str(getattr(form, "gross_sale_price", None) and form.gross_sale_price.data or ""),
            # Purchase Info
            "(J1) Purchase Date": form.purchase_date.data.strftime('%m/%d/%Y') if getattr(form, "purchase_date", None) and form.purchase_date.data else "",
            # Insurance Info
            "(K3) Effective Date of Insurance": form.insurance_effective_date.data.strftime('%m/%d/%Y') if getattr(form, "insurance_effective_date", None) and form.insurance_effective_date.data else "",
            "(K5) Policy Change Date": form.insurance_policy_change_date.data.strftime('%m/%d/%Y') if getattr(form, "insurance_policy_change_date", None) and form.insurance_policy_change_date.data else "",
            # Owner 1 Information
            "(D2) (First Owner's) Name (Last, First, Middle)": str(getattr(form, "owner_name", None) and form.owner_name.data or ""),
            "(D3) (Owner 1) Date of Birth (MM/DD/YYYY)": form.owner_dob.data.strftime('%m/%d/%Y') if getattr(form, "owner_dob", None) and form.owner_dob.data else "",
            "(D4) (Owner 1) License Number/ ID (Identification) Number / SSN (Social Security Number)": str(getattr(form, "owner_license", None) and form.owner_license.data or ""),
            "(D5) (Owner 1) Residential Address": endereco_rua,
            "(D5) (Owner 1) Apt (Apartment) Number": endereco_apt,
            "(D5) (Owner 1) City": endereco_cidade,
            "(D5) (Owner 1) State": endereco_estado,
            "(D5) (Owner 1) Zip Code": endereco_cep,
            "(D6) (Owner 1) State/Country of License/ID (Identification)": str(getattr(form, "owner_license_issued_state", None) and form.owner_license_issued_state.data or ""),
            # Garaging Address (G1) - igual ao endereço residencial
            "(G1) (Garaging) Address": endereco_rua,
            "(G1) Apt.#": endereco_apt,
            "(G1) (Garaging Address) City": endereco_cidade,
            "(G1) (Garaging Address) State": endereco_estado,
            "(G1) (Garaging Address) Zip Code": endereco_cep,
            # VIN
            "(B1) Vehicle Identification Number (VIN)": str(getattr(form, "vin", None) and form.vin.data or ""),
            # Body Style
            "(B2) Body Style": str(getattr(form, "body_style", None) and form.body_style.data or ""),
            # Cores (checkboxes)
            "(B4) Black": self._color_checkbox(form, "Black"),
            "(B4 ) White": self._color_checkbox(form, "White"),
            "(B4) Brown": self._color_checkbox(form, "Brown"),
            "(B4) Blue": self._color_checkbox(form, "Blue"),
            "(B4) Yellow": self._color_checkbox(form, "Yellow"),
            "(B4) Gray": self._color_checkbox(form, "Gray"),
            "(B4 ) Purple": self._color_checkbox(form, "Purple"),
            "(B4) Green": self._color_checkbox(form, "Green"),
            "(B4) Orange": self._color_checkbox(form, "Orange"),
            "(B4) Red": self._color_checkbox(form, "Red"),
            "(B4) Silver": self._color_checkbox(form, "Silver"),
            "(B4) Gold": self._color_checkbox(form, "Gold"),
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

        # Preenche os campos do PDF
        for page in writer.pages:
            if "/Annots" in page:
                for annot in page["/Annots"]:
                    obj = annot.get_object()
                    field_name = obj.get("/T")
                    if field_name and field_name in campos:
                        value = campos[field_name]
                        obj.update({NameObject("/Ff"): NumberObject(0)})
                        field_type = obj.get("/FT")
                        if field_type == "/Btn":
                            obj.update({NameObject("/V"): value, NameObject("/AS"): value})
                        elif field_type == "/Tx":
                            obj.update({NameObject("/V"): TextStringObject(str(value))})
        writer.set_need_appearances_writer(True)

        pdf_io = io.BytesIO()
        writer.write(pdf_io)
        pdf_io.seek(0)
        return pdf_io
