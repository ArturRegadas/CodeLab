const express = require("express");
const router = express.Router();

router.get("/getHelloWorld", async(req, ans) => {
    return ans.status(200).send("HelloWorld")
})

module.exports = router;