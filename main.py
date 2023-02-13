from flask import Flask, render_template, request
import zeep
wsdl_url = "https://33wsp.post.gov.tw/LZWZIP/TZIP33.asmx?WSDL"
client = zeep.Client(wsdl=wsdl_url)
result = client.service


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST", "GET"])
def receive_data():
    address_name = request.form["address_input"]
    # zeep method
    zip_formal = result.GetZipCode(address_name)
    zip_code = zip_formal["GetZipCodeResult"]
    zip_address = zip_formal["address"]
    # return f"<h3 id='content'>地址: {zip_formal_address}</h3>"
    return render_template("result.html", address_name=address_name, zip_code=zip_code, zip_address=zip_address)


if __name__ == "__main__":
    app.run(debug=True)