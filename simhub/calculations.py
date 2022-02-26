import math

def f1(last_vals, current_vals, next_vals):
    next_vals["yd"] = current_vals["y"] + current_vals["rr"] * last_vals["v"] - current_vals["t"]
    next_vals["alpha1"] = current_vals["alpha10"] - current_vals["iota"] * current_vals["rr"]
    next_vals["v"] = last_vals["v"] + current_vals["alpha2"] * (current_vals["vstar"] - last_vals["v"])
    next_vals["vstar"] = current_vals["alpha3"] * current_vals["yd"]
    next_vals["alpha3"] = (1 - current_vals["alpha1"])/current_vals["alpha2"]
    next_vals["px"] = current_vals["yd"] - current_vals["v"] + last_vals["v"]
    next_vals["T"] = current_vals["theta"] * (current_vals["Y"] + current_vals["r"] * last_vals["V"])
    next_vals["Y"] = current_vals["y"] * current_vals["p"]
    next_vals["V"] = current_vals["v"] * current_vals["p"]
    next_vals["rr"] = (1 + current_vals["r"])/(1 + current_vals["pi"]) - 1
    next_vals["pi"] = current_vals["pi"]
    next_vals["y"] = last_vals["y"] * (1 + current_vals["gr"])
    next_vals["t"] = current_vals["T"]/current_vals["p"]
    next_vals["gT"] = current_vals["g"] + current_vals["rr"] * last_vals["GD"]/last_vals["p"]
    next_vals["deltagd"] = current_vals["gT"] - current_vals["t"]
    next_vals["GT"] = current_vals["G"] + current_vals["r"] * last_vals["GD"]
    next_vals["G"] = current_vals["g"] * current_vals["p"]
    next_vals["DEF"] = current_vals["GT"] - current_vals["T"]
    next_vals["GD"] = last_vals["GD"] + current_vals["DEF"]
    next_vals["g"] = current_vals["y"] - current_vals["px"]
    next_vals["p"] = last_vals["p"] * (1 + current_vals["pi"])

    errorsquare = 0

    for key in current_vals:
        errorsquare += (next_vals[key] - current_vals[key])**2
        current_vals[key] = next_vals[key]
    
    return math.sqrt(errorsquare)

def solver1Function(last_vals, current_vals, next_vals):
    iterations = 0
    error = 1
    
    while iterations < 100 and error > 0.00000001:
        error = f1(last_vals, current_vals, next_vals)
        iterations += 1

    return next_vals