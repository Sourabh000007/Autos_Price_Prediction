from flask import Flask,jsonify,render_template,request

from project_app.utils import Autos_price

app = Flask(__name__)
app.debug=True

@app.route("/")
def hello():
    return render_template("test.html")

@app.route("/predict_price", methods = ["POST","GET"])

def get_complete_price():
    if request.method == "GET":

        symboling              = (request.args.get("symboling"))
        normalized_losses      = (request.args.get("normalized_losses"))
        fuel_type              = (request.args.get("fuel_type"))
        aspiration             = (request.args.get("aspiration"))
        num_of_doors           = (request.args.get("num_of_doors"))
        drive_wheels           = (request.args.get("drive_wheels"))
        engine_location        = (request.args.get("engine_location"))
        wheel_base             = (request.args.get("wheel_base"))
        length                 = (request.args.get("length"))
        width                  = (request.args.get("width"))
        height                 = (request.args.get("height"))
        curb_weight            = (request.args.get("curb_weight"))
        engine_type            = (request.args.get("engine_type"))
        num_of_cylinders       = (request.args.get("num_of_cylinders"))
        engine_size            = (request.args.get("engine_size"))
        bore                   = (request.args.get("bore"))
        stroke                 = (request.args.get("stroke"))
        compression_ratio      = (request.args.get("compression_ratio"))
        horsepower             = (request.args.get("horsepower"))
        peak_rpm               = (request.args.get("peak_rpm"))
        city_mpg               = (request.args.get("city_mpg"))
        highway_mpg            = (request.args.get("highway_mpg"))
        make                   = (request.args.get("make"))
        body_style             = (request.args.get("body_style"))
        fuel_system            = (request.args.get("fuel_system"))

        price = Autos_price(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,wheel_base,length,
                    width,height,curb_weight,engine_type,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,
                    peak_rpm,city_mpg,highway_mpg,make,body_style,fuel_system)
    
        price = price.get_autos_price()

        return render_template("test.html",prediction=price)

if __name__ == "__main__":
    app.run()