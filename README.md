# Klasifikasi Angka Tangan (0–9) dengan TensorFlow

Proyek ini merupakan model klasifikasi gambar digit (0 hingga 9) menggunakan TensorFlow dan Keras. Model terbaik diekspor ke berbagai format: SavedModel, TensorFlow Lite, dan TensorFlow.js.


## Format Model

- **SavedModel**: Untuk penggunaan dengan TensorFlow.
- **TFLite**: Untuk integrasi ke mobile (Android/iOS).
- **TensorFlow.js**: Untuk digunakan di web browser.

## Cara Konversi

Jalankan skrip berikut setelah pelatihan:

```python
best_model.export("saved_model")

# Konversi ke TFLite
converter = tf.lite.TFLiteConverter.from_saved_model("saved_model")
tflite_model = converter.convert()
with open("tflite/model.tflite", "wb") as f:
    f.write(tflite_model)

# Buat label.txt
with open("tflite/label.txt", "w") as f:
    for i in range(10):
        f.write(f"{i}\n")

# Konversi ke TF.js
!tensorflowjs_converter --input_format=tf_saved_model saved_model tfjs_model
