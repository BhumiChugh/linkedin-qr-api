from flask import Flask, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate_qr():
    data = request.get_json()
    linkedin_url = data.get("linkedin_url")

    if not linkedin_url:
        return {"error": "Missing LinkedIn URL"}, 400

    # Generate QR code image
    qr = qrcode.make(linkedin_url)

    # Save the image in memory as a PNG
    img_io = io.BytesIO()
    qr.save(img_io, format='PNG')
    img_io.seek(0)  # Move pointer to the start

    # Send the image back to Wix as a file response
    return send_file(img_io, mimetype='image/png')
