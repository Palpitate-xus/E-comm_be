import qrcode
import base64
import io
def generate_qr_code(order_details):
    # Convert order details to a string representation
    order_info = str(order_details)

    # Generate QR code image
    qr = qrcode.QRCode()
    qr.add_data(order_info)
    qr.make()
    qr_code_image = qr.make_image(fill_color="black", back_color="white")

    # Convert QR code image to base64 format
    qr_code_bytes = io.BytesIO()
    qr_code_image.save(qr_code_bytes, format='PNG')
    qr_code_base64 = base64.b64encode(qr_code_bytes.getvalue()).decode('utf-8')

    return qr_code_base64