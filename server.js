const express = require("express");
const multer = require("multer");
const { exec } = require("child_process");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.static("public"));

const upload = multer({ dest: "uploads/" });

app.post("/upload", upload.single("file"), (req, res) => {
    const filePath = req.file.path;

    exec(`python analyzer.py ${filePath}`, (error, stdout) => {
        if (error) {
            return res.send("Error processing file");
        }
        res.send(stdout);
    });
});

app.listen(3000, () =>
    console.log("Server running at http://localhost:3000")
);
