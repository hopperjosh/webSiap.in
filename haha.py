import numpy as np

print("numpy berhasil diimpor:", np.__version__)
print("contoh array numpy:", np.array([1, 2, 3, 4, 5]))

a = np.array([1, 2, 3])
b = np.array([4, 5,6])
print("hasil penjumlahan a + b:", a + b)
print("hasil penjumlahan a + b:", a - b)

import torch
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))

print("hasil perkalian a * b:", a * b)
print("hasil pembagian a / b:", a / b)
print("sudah selesai menjalankan haha.py")
