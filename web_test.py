from flask import Flask, render_template, request, redirect
from aircrafts.r44 import R44

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('main.html')


@app.route('/r44', methods=['POST', 'GET'])
def r44():
    if request.method == "POST":
        aircraft = R44()
        for key, value in request.form.items():
            print(key, value)
            try:
                value = float(value)
                aircraft.set_value(key, value)
            except ValueError:
                if value == "on":
                    aircraft.set_include(key, True)
                else:
                    raise ValueError("Incorrect value {value} passed".format(value=value))
        print(aircraft)
        aircraft.calculate_com()
        print("lat arm ", aircraft._lateral_arm)
        print("Lon arm ", aircraft._longitudinal_arm)
        print("Lon mom ", aircraft._longitudinal_moment)
        print("Lat mom ", aircraft._lateral_moment)
        print("Weight ", aircraft._weight)
        return aircraft.get_com_info()

    else:
        aircraft = R44()
        moments = aircraft.get_moments()
        empty = moments['empty']
        del moments['empty']
        names = [x.get_name() for x in moments.values()]
        bool_list = [x.get_bool_include() for x in moments.values()]
        ids = list(moments.keys())
        weights = [x.get_weight() for x in moments.values()]
        return render_template("r44_input.html", lst=zip(names, bool_list, ids, weights), empty_name=empty.get_name(),
                               empty_weight=empty.get_weight())
