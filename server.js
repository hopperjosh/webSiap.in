require("dotenv").config(); // load .env


const express = require("express");
const { createClient } = require("@supabase/supabase-js");
const path = require("path");

const app = express();
const PORT = 3000;
app.use(express.json());

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY // ambil dari .env
);

// middleware
app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

// contoh GET data dari tabel "siapinUsers"
app.get("/api/user", async (req, res) => {
  const { data, error } = await supabase
    .from("siapinUsers")
    .select("*");

  if (error) return res.status(500).json({ error: error.message });
  res.json(data);
});

// contoh INSERT data ke tabel "murid"
// app.post("/api/murid", async (req, res) => {
//   const { nama, kelas } = req.body;
//   const { data, error } = await supabase
//     .from("murid")
//     .insert([{ nama, kelas }]);

//   if (error) return res.status(500).json({ error: error.message });
//   res.json(data);
// });

// INSERT data ke tabel "cvUsers"
app.post("/api/cv", async (req, res) => {
  const { pengalaman, prestasi, keahlian } = req.body;

  const { data, error } = await supabase
    .from("cvUsers") // pastikan tabel ini ada di Supabase
    .insert([{ pengalaman, prestasi, keahlian }]);

  if (error) return res.status(500).json({ error: error.message });
  res.json({ message: "CV berhasil disimpan", data });
});

app.listen(PORT, () => {
  console.log(`Server berjalan di http://localhost:${PORT}`);
});
