
import copy
import itertools

from requests import options

from oomp_populate_helper import write_extras, build_oomp_id


def main(**kwargs):
    # Define default input dict with all required fields
    default_input = {
        "taxonomy_1": "paper",
        "taxonomy_2": "sheet",
        "taxonomy_3": "",
        "taxonomy_4": "",
        "taxonomy_5": "",
        "taxonomy_6": "",
        "taxonomy_7": "",
        "taxonomy_8": "",
        # Add any additional details here
    }
     
    
    #### define extra entries
    


    options = []
    #define single parts (take the default options add one with the extra details)
    option = {}
    
    ############################# examples
        
        

    #################### for this project
    if True:        
        current_sheet = "a4"
        current_weight = "80_gsm"
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "blue_light_colour",          "taxonomy_6": "sky_blue",    "taxonomy_14": "papago","taxonomy_15": "21514"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "green_flourescent_colour",                          "taxonomy_14": "papago","taxonomy_15": "21403"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "grey_dark_colour",    "taxonomy_6": "steel_grey",    "taxonomy_14": "papago","taxonomy_15": "21220"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "orange_colour",          "taxonomy_6": "deep_tangerine",    "taxonomy_14": "papago","taxonomy_15": "21205"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "pink_pale_colour",          "taxonomy_6": "peach",    "taxonomy_14": "papago","taxonomy_15": "21401"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "pink_pale_colour",       "taxonomy_6": "wild_rose",    "taxonomy_14": "papago","taxonomy_15": "21227"})        
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "purple_light_colour",    "taxonomy_6": "lilac",               "taxonomy_14": "papago","taxonomy_15": "21202"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "yellow_light_colour",    "taxonomy_6": "canary",    "taxonomy_14": "papago","taxonomy_15": "21207"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "yellow_light_colour",    "taxonomy_6": "daffodil",    "taxonomy_14": "papago","taxonomy_15": "21228"})

        current_weight = "100_gsm"
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "white_colour"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "white_colour", "taxonomy_6": "textured", "taxonomy_7" : "watermarked"})


        current_weight = "160_gsm"
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "blue_colour",    "taxonomy_6": "kingfisher_blue",    "taxonomy_14": "colorit","taxonomy_15": "387_969"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "green_colour",    "taxonomy_6": "emerald_green",    "taxonomy_14": "colorit","taxonomy_15": "387_960"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "green_colour",    "taxonomy_6": "forest_green",    "taxonomy_14": "image_coloraction","upc": "03597320018206"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "orange_colour",    "taxonomy_6": "tangerine",    "taxonomy_14": "papago","taxonomy_15": "21264"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "purple_light_colour",    "taxonomy_6": "lilac",               "taxonomy_14": "papago","taxonomy_15": "21262"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "yellow_colour",    "taxonomy_6": "golden_yellow",    "taxonomy_14": "colorit","taxonomy_15": "387_942"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "yellow_colour",    "taxonomy_6": "intensive_yellow",    "taxonomy_14": "papago","taxonomy_15": "21275"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "white_colour", "taxonomy_6": "glossy_finish", "taxonomy_7": "single_sided_printing"})
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "white_colour", "taxonomy_6": "white_bright_160_cie", "taxonomy_14": "mondi", "taxonomy_15": "a4_26626", "upc": "9003974411965"})


        current_weight = "125_gsm"
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "white_colour", "taxonomy_6": "sublimation", "taxonomy_14": "a_sub"})

        #a3
        current_sheet = "a3"
        current_weight = "80_gsm"
        options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "white_colour"})

        current_sheet = "postcard_152_4_mm_width_101_6_mm_height"
        weights = ["230_gsm"]
        for current_weight in weights:
            options.append({"taxonomy_1": "paper", "taxonomy_2": "sheet", "taxonomy_3": current_sheet, "taxonomy_4": current_weight,       "taxonomy_5": "white_colour", "taxonomy_6": "glossy_finish", "taxonomy_7": "single_sided_printing"})

        #envelope
        if True:            
            options.append({"taxonomy_1": "paper", "taxonomy_2": "envelope", "taxonomy_3": "c4", "taxonomy_4": "",       "taxonomy_5": "brown_colour", "taxonomy_6": "kraft_brown", "taxonomy_14": "papago","taxonomy_15": "21301"})

    #define loop parts here
    if False:
        options = looping_options(default_input, options)

    #define oobb parts here
    if False:
        option = {}
        option["oobb"] = True
        option["width"] = 5
        option["height"] = 6
        option["depth"] = 21
        #name oobb_holder
        option["oobb_name"] = "holder"
        options.append(option)

    extras = []
    for option in options:
        extra = copy.deepcopy(default_input)
        extra.update(option)
        
        
        extras.append(extra)

    ######### add notes from an id string
    import working_oomp_populate_extra_detail
    working_oomp_populate_extra_detail.main(extras=extras)

    write_extras(extras, default_input)



# Call main automatically
if __name__ == "__main__":
    main()
