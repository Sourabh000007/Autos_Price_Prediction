import numpy as np
import pandas as pd
import json
import pickle
import warnings
warnings.filterwarnings("ignore")
import config

class Autos_price():

    def __init__(self,symboling,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,wheel_base,length,
                 width,height,curb_weight,engine_type,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,
                 peak_rpm,city_mpg,highway_mpg,make,body_style,fuel_system):
        
        self.symboling              = symboling
        self.normalized_losses      = normalized_losses
        self.fuel_type              = fuel_type
        self.aspiration             = aspiration
        self.num_of_doors           = num_of_doors
        self.drive_wheels           = drive_wheels
        self.engine_location        = engine_location
        self.wheel_base             = wheel_base
        self.length                 = length
        self.width                  = width
        self.height                 = height
        self.curb_weight            = curb_weight
        self.engine_type            = engine_type
        self.num_of_cylinders       = num_of_cylinders
        self.engine_size            = engine_size
        self.bore                   = bore
        self.stroke                 = stroke
        self.compression_ratio      = compression_ratio
        self.horsepower             = horsepower
        self.peak_rpm               = peak_rpm
        self.city_mpg               = city_mpg
        self.highway_mpg            = highway_mpg
        self.make                   = "make_" + make
        self.body_style             = "body-style_" + body_style
        self.fuel_system            = "fuel-system_" + fuel_system

    
    def load_models(self):

        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.load_model = pickle.load(f)
        with open(config.JSON_FILE_PATH,"r") as f:
            self.load_json = json.load(f)

    def get_autos_price(self):

        self.load_models()

        make_index = list(self.load_json["columns"]).index(self.make)

        body_style_index = list(self.load_json["columns"]).index(self.body_style)

        fuel_system_index = list(self.load_json["columns"]).index(self.fuel_system)

        test_array = np.zeros(len(self.load_json["columns"]))

        test_array[0] = self.symboling
        test_array[1] = self.normalized_losses
        test_array[2] = self.load_json['fuel_type'][self.fuel_type]
        test_array[3] = self.load_json['aspiration'][self.aspiration]
        test_array[4] = self.load_json['num_of_doors'][self.num_of_doors]
        test_array[5] = self.load_json['drive_wheels'][self.drive_wheels]
        test_array[6] = self.load_json['engine_location'][self.engine_location]
        test_array[7] = self.wheel_base
        test_array[8] = self.length
        test_array[9] = self.width
        test_array[10] = self.height
        test_array[11] = self.curb_weight
        test_array[12] = self.load_json['engine_type'][self.engine_type]
        test_array[13] = self.load_json['num_of_cylinders'][self.num_of_cylinders]
        test_array[14] = self.engine_size
        test_array[15] = self.bore
        test_array[16] = self.stroke
        test_array[17] = self.compression_ratio
        test_array[18] = self.horsepower
        test_array[19] = self.peak_rpm
        test_array[20] = self.city_mpg
        test_array[21] = self.highway_mpg
        test_array[make_index] = 1
        test_array[body_style_index] = 1
        test_array[fuel_system_index] = 1

        price = round(self.load_model.predict([test_array])[0],2)

        return price
    
if __name__== "__main__":

    symboling              = 3
    normalized_losses      = 122
    fuel_type              = "gas"
    aspiration             = "std"
    num_of_doors           = "four"
    drive_wheels           = "fwd"
    engine_location        = "front"
    wheel_base             = 88.60
    length                 = 168.80
    width                  = 64.10
    height                 = 48.80
    curb_weight            = 2548.00
    engine_type            = "ohc"
    num_of_cylinders       = "four"
    engine_size            = 130
    bore                   = 3.47
    stroke                 = 2.68
    compression_ratio      = 9.00
    horsepower             = 111
    peak_rpm               = 5000
    city_mpg               = 21
    highway_mpg            = 27
    make                   = "mazda"
    make                   = "make_" + make
    body_style             = "hardtop"
    body_style             = "body-style_" + body_style
    fuel_system            = "mpfi"
    fuel_system            = "fuel-system_" + fuel_system

    price = Autos_price(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,wheel_base,length,
                 width,height,curb_weight,engine_type,num_of_cylinders,engine_size,bore,stroke,compression_ratio,horsepower,
                 peak_rpm,city_mpg,highway_mpg,make,body_style,fuel_system)
    
    price = Autos_price.get_autos_price
    print(price)

