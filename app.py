from flask import Flask, request, send_file, jsonify
import qrcode
import io

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.get_json()

    linkedin_url = data.get('linkedin_url')
    if not linkedin_url or not linkedin_url.startswith("http"):
        return jsonify({"error": "Invalid or missing URL"}), 400

    fill_color = data.get('fill_color', 'black')
    back_color = data.get('back_color', 'white')
    box_size = int(data.get('box_size', 10))
    border = int(data.get('border', 4))

    qr = qrcode.QRCode(
        version=1,
        box_size=box_size,
        border=border
    )
    qr.add_data(linkedin_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    img_io = io.BytesIO()
    img.save(img_io, format='PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
