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
model_id = "DeepSeek-R1-0528"  # ~1.3B parameter, ringan untuk CPU
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

# Inisialisasi riwayat obrolan
chat_history = ""

print("🤖 GPT2 Chatbot - Bahasa Indonesia")
print("Ketik 'keluar' untuk mengakhiri.\n")

while True:
    user_input = input("Kamu : ")
    if user_input.lower() == "keluar":
        break

    # Tambahkan input pengguna ke konteks
    chat_history += f"Kamu: {user_input}\nBot:"

    # Generate respons
    response = pipe(chat_history, max_new_tokens=256, do_sample=False)

    # Ambil output & tambahkan ke riwayat
    generated_text = response[0]["generated_text"]
    bot_reply = generated_text[len(chat_history):].split("\n")[0]  # ambil satu baris respons

    print(f"Bot  : {bot_reply.strip()}")
    chat_history += f"{bot_reply.strip()}\n"





# Versi awal kode yang menggunakan format ChatML untuk percakapan:
# # ====== Menyiapkan percakapan (format ChatML) ======
# messages = [
#     {"role": "system", "content": "Kamu adalah asisten AI yang membantu menjawab pertanyaan."},
#     {"role": "user",   "content": "Apakah kamu bisa bahasa indonesia?"},
# ]
# print("p3")
# # ====== Melakukan inferensi (membuat balasan) ======

# print("p4")
# # ====== Menampilkan hasil ======

# # ====== Menyusun prompt bergaya "role: konten" ======
# prompt = ""
# for message in messages:                               # Iterasi tiap elemen dict pada list messages
#     role = message["role"]                             # Contoh: "system" atau "user"
#     content = message["content"]                       # Teks asli yang dikirim
#     prompt += f"{role.capitalize()}: {content}\n"      # Gabungkan ke string prompt dengan newline

# prompt += "Assistant:"                                 # Sinyal bagi model di mana jawaban harus dimulai
# print("p5")
# # ====== Melakukan inferensi dengan metode string-prompt ======
# # Perlu waktu ±2x lebih lama daripada format ChatML karena seluruh prompt diproses sebagai teks mentah.

# outputs = pipe(
#     prompt,                                            # Masukan prompt lengkap
#     max_new_tokens=400,                                # Batas maksimal token yang akan dihasilkan
#     do_sample=True                                     # Sampling acak → keluaran lebih bervariasi & kreatif
# )
# print("p6")
# # ====== Menampilkan hasil akhir ======
# print(outputs[0]["generated_text"])                    # Cetak keseluruhan teks (prompt + balasan model)

# # print("generate done in", time.time() - start, "seconds")

print("sudah selesai menjalankan coba.py")