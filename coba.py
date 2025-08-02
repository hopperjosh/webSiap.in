from huggingface_hub import login

hf_token = input("masukkan hugging face token anda (hf_***): ")
login(token = hf_token)
print("Yes, login berhasil ke hugging face hub")

import time
start = time.time()

import torch                                # PyTorch: backend komputasi tensor
from transformers import pipeline           # Pipeline Hugging Face untuk tugas NLP siap pakai

print ("program sedang berjalan")
# ====== Menentukan model ======
model_id = "tiiuae/falcon-rw-1b"  # ~1.3B parameter, ringan untuk CPU
# ID repositori di Hugging Face Hub berisi checkpoint Llama-3.2-3B versi Instruct
print("p1")
# ====== Membuat pipeline generasi teks ======
pipe = pipeline(
    "text-generation",                      # Jenis tugas: membuat/melanjutkan teks
    model=model_id,                         # Nama atau path model
    torch_dtype=torch.bfloat16,             # Format bilangan bfloat16 → lebih ringan di GPU modern
    device_map="auto",                      # Otomatis menyebar layer ke GPU (atau CPU jika GPU tidak ada)
)
print("p2")
# ====== Menyiapkan percakapan (format ChatML) ======
messages = [
    {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
    {"role": "user",   "content": "Who are you?"},
]
print("p3")
# ====== Melakukan inferensi (membuat balasan) ======

print("p4")
# ====== Menampilkan hasil ======

# ====== Menyusun prompt bergaya "role: konten" ======
prompt = ""
for message in messages:                               # Iterasi tiap elemen dict pada list messages
    role = message["role"]                             # Contoh: "system" atau "user"
    content = message["content"]                       # Teks asli yang dikirim
    prompt += f"{role.capitalize()}: {content}\n"      # Gabungkan ke string prompt dengan newline

prompt += "Assistant:"                                 # Sinyal bagi model di mana jawaban harus dimulai
print("p5")
# ====== Melakukan inferensi dengan metode string-prompt ======
# Perlu waktu ±2x lebih lama daripada format ChatML karena seluruh prompt diproses sebagai teks mentah.

outputs = pipe(
    prompt,                                            # Masukan prompt lengkap
    max_new_tokens=256,                                # Batas maksimal token yang akan dihasilkan
    do_sample=True                                     # Sampling acak → keluaran lebih bervariasi & kreatif
)
print("p6")
# ====== Menampilkan hasil akhir ======
print(outputs[0]["generated_text"])                    # Cetak keseluruhan teks (prompt + balasan model)
print("generate done in", time.time() - start, "seconds")


print("sudah selesai menjalankan coba.py")