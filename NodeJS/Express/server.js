const express = require("express");
//const mongoose = require("mongoose");
const URLRoutes = require("./Routes/Url")

const app = express();
app.use(express.json());

app.use("/", URLRoutes);

const PORT = 3000

app.listen(PORT, ()=>{
    console.log('server no ar na port em http://localhost:'+ PORT );
})