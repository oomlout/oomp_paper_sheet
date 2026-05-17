import working_oomp_populate

def main(**kwargs):
    extras = kwargs.get("extras", [])
    extras_dict = {}
    for extra in extras:
        oomp_id =  working_oomp_populate.build_oomp_id(extra)
        extras_dict[oomp_id] = extra

    resistor_colors = ["brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white", "black"]
    band_1_values = [
        "a4",
        "a3",
        "postcard_152_4_mm_width_101_6_mm_height",
    ]
    band_2_values = [
        "80_gsm",
        "100_gsm",
        "160_gsm",
        "230_gsm",
    ]
    band_3_values = [
        "blue_colour",
        "blue_light_colour",
        "green_colour",
        "green_flourescent",
        "green_flourescent_colour",
        "grey_dark_colour",
        "orange_colour",
        "pink_pale_colour",
        "purple_light_colour",
        "white_colour",
        "yellow_colour",
        "yellow_light_colour",
    ]

    band_1_color_map = {}
    for index, band_1_value in enumerate(band_1_values):
        color_index = min(index, len(resistor_colors) - 1)
        band_1_color_map[band_1_value] = resistor_colors[color_index]

    band_2_color_map = {}
    for index, band_2_value in enumerate(band_2_values):
        color_index = min(index, len(resistor_colors) - 1)
        band_2_color_map[band_2_value] = resistor_colors[color_index]

    band_3_color_map = {}
    for index, band_3_value in enumerate(band_3_values):
        color_index = min(index, len(resistor_colors) - 1)
        band_3_color_map[band_3_value] = resistor_colors[color_index]

    ###### add colour bands to tray
    for extra in extras_dict.values():
        band_1 = extra.get("taxonomy_3", "")
        band_2 = extra.get("taxonomy_4", "")
        band_3 = extra.get("taxonomy_5", "")

        if band_1 == "" or band_2 == "" or band_3 == "":
            continue

        band_1_string = band_1.replace("_", " ")
        band_2_string = band_2.replace("_", " ")
        band_3_string = band_3.replace("_", " ")
        band_1_color = band_1_color_map[band_1]
        band_2_color = band_2_color_map[band_2]
        band_3_color = band_3_color_map[band_3]

        extra["color_band_project_bolt_1"] = band_3_color
        extra["color_band_project_bolt_1_string"] = band_3_string
        extra["color_band_taxonomy_5"] = band_3_color
        extra["color_band_project_bolt_2"] = band_2_color
        extra["color_band_project_bolt_2_string"] = band_2_string
        extra["color_band_taxonomy_4"] = band_2_color
        extra["color_band_project_bolt_3"] = band_1_color
        extra["color_band_project_bolt_3_string"] = band_1_string
        extra["color_band_taxonomy_3"] = band_1_color
        extra["color_band_string_project_bolt"] = f"colour_band_{band_1_color}_{band_2_color}_{band_3_color}"
        extra["color_band_string_project_bolt_string"] = f"colour_band_{band_1_string}_{band_2_string}_{band_3_string}"
                
        
    