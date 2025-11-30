from flask import Flask, jsonify

app = Flask(__name__)

class HW:
    def __init__(self, name, secondName)->None:
        self.name = name
        self.secondName = secondName

    def toDict(self):
        return {
            "name":self.name,
            "secondName":self.secondName
        }

@app.route("/getHelloWorldStr", methods=["GET"])
def getHelloWoroldStr() -> str:
    return "Hello World"

@app.route("/getHelloWorldList", methods=["GET"])
def getHelloWoroldList() -> list[str]:
    return ["Hello", "World"]

@app.route("/getHelloWorldHash", methods=["GET"])
def getHelloWoroldHash() -> dict:
    return {
        "name": "Hello",
        "secondName": "World"
        }

@app.route("/getHelloWorldObj", methods=["GET"])
def getHelloWoroldObj() -> 'HW':
    return jsonify(HW("Hello", "World").toDict())




app.run(debug=True)