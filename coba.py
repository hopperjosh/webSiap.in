from huggingface_hub import login

hf_token = input("masukkan hugging face token anda (hf_***): ")
login(token = hf_token)
print("Yes, login berhasil ke hugging face hub")

import torch                                # PyTorch: backend komputasi tensor
from transformers import pipeline           # Pipeline Hugging Face untuk tugas NLP siap pakai

# ====== Menentukan model ======
model_id = "meta-llama/Llama-3.2-3B-Instruct"
# ID repositori di Hugging Face Hub berisi checkpoint Llama-3.2-3B versi Instruct

# ====== Membuat pipeline generasi teks ======
pipe = pipeline(
    "text-generation",                      # Jenis tugas: membuat/melanjutkan teks
    model=model_id,                         # Nama atau path model
    torch_dtype=torch.bfloat16,             # Format bilangan bfloat16 → lebih ringan di GPU modern
    device_map="auto",                      # Otomatis menyebar layer ke GPU (atau CPU jika GPU tidak ada)
)

# ====== Menyiapkan percakapan (format ChatML) ======
messages = [
    {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
    {"role": "user",   "content": "Who are you?"},
]

# ====== Melakukan inferensi (membuat balasan) ======
outputs = pipe(
    messages,                               # Masukan model berupa daftar pesan
    max_new_tokens=256,                     # Batas panjang teks yang dihasilkan
)

# ====== Menampilkan hasil ======
print(outputs[0]["generated_text"][-1])     # Cetak karakter terakhir dari teks ter-generate

# ====== Menyusun prompt bergaya "role: konten" ======
prompt = ""
for message in messages:                               # Iterasi tiap elemen dict pada list messages
    role = message["role"]                             # Contoh: "system" atau "user"
    content = message["content"]                       # Teks asli yang dikirim
    prompt += f"{role.capitalize()}: {content}\n"      # Gabungkan ke string prompt dengan newline

prompt += "Assistant:"                                 # Sinyal bagi model di mana jawaban harus dimulai

# ====== Melakukan inferensi dengan metode string-prompt ======
# Perlu waktu ±2x lebih lama daripada format ChatML karena seluruh prompt diproses sebagai teks mentah.
outputs = pipe(
    prompt,                                            # Masukan prompt lengkap
    max_new_tokens=256,                                # Batas maksimal token yang akan dihasilkan
    do_sample=True                                     # Sampling acak → keluaran lebih bervariasi & kreatif
)

# ====== Menampilkan hasil akhir ======
print(outputs[0]["generated_text"])                    # Cetak keseluruhan teks (prompt + balasan model)


print("sudah selesai menjalankan coba.py")