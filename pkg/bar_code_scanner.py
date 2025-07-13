import cv2
from pyzbar.pyzbar import decode
import openfoodfacts

image = cv2.imread("pkg/test.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error loading image")
else:
    print("Image loaded")

scaled = cv2.resize(image, (600, int(image.shape[0] * 600 / image.shape[1])))

barcodes = decode(scaled)

for barcode in barcodes:
    barcode_data = barcode.data.decode("utf-8")
    barcode_type = barcode.type

    x, y, w, h = barcode.rect

    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    text = f"{barcode_data} ({barcode_type})"

    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 0.5, (0, 255, 0), 2)

    print(f"Detected {barcode_type}: {barcode_data}")

    api = openfoodfacts.API(user_agent="TestApp/1.0")
    result = api.product.get(barcode_data, fields=["product_name"])

    print(result)