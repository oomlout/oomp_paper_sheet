import oomp
import copy
import oomlout_roboclick
import oomp_helper

def main(**kwargs):
    load_parts(**kwargs)

def load_parts(**kwargs):
    make_files = kwargs.get("make_files", True)
    #print "loading parts" plus the module name get the module name from the filename using __name__
    print(f"  loading parts {__name__}")
    create_generic(**kwargs)

def create_generic(**kwargs):
    print(f"  loading parts from part_source")
    things = {}    
    
    #load parts from parts_source directory
    directory_source = "parts_source"
    import os
    if not os.path.exists(directory_source):
        print(f"      directory {directory_source} does not exist, creating it")
        #create it
        os.makedirs(directory_source)
    directories = os.listdir(directory_source)
    for directory  in directories:
        directory_full = f"{directory_source}/{directory}"
        filenames = os.listdir(f"{directory_full}")
        for filename in filenames:
            import yaml
            #go through directories and load working.yaml files
            # only load .yaml files
            if "working.yaml" in filename:
                file_path = os.path.join(directory_full, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = yaml.safe_load(file)
                    thing_details = {}
                    for deet in data:
                        thing_details[deet] = data[deet]
                    things[directory] = thing_details
    
    
    parts = []

    for thing in things:
        current = things[thing]                
        #name stuff        
        part = copy.deepcopy(current)
        
        part["name"] = thing
        part["name_space"] = thing.replace("_", " ")
        part["name_proper"] = part["name_space"].title()
        part["name_upper"] = part["name_space"].upper()
        
        folder = oomlout_roboclick.get_directory(part)   
        part["directory"] = folder  
        url_chat = oomlout_roboclick.get_url(part)   
        part["url_chat"] = url_chat
        files_to_trace = []
        count = 0

        #mode_ai_wait = "fast"
        mode_ai_wait = "slow"


        #icon
        if True:
            count += 1            
            action_type = "ai" # "corel"
            
            #action_name = f"create_icon"
            action_name = f"step_{count}_create_icon"
            
            file_test = f"initial_generated_icon.png" 
            #file_test = "tag" #(creates a tag at the end)

            actions = []
            
            #### action 1
            action = {}
            action["command"] = "ai_skill_image_laser_cut_logo_full"            
            action["file_destination"] = file_test
            #action["file_destination"] = f"intial_generated_icon.png"
            detail = f'{part.get("name_space", "")} make sure to include an item that is identified by the colour included so you know even though the image is black and white'
            image_detail = f"an image of {detail}"
            action["image_detail"] = image_detail
            #mode_ai_wait fast
            action["mode_ai_wait"] = mode_ai_wait
            actions.append(copy.deepcopy(action))

            oomlout_roboclick.add_action(part=part, action_type=action_type, action_name=action_name, actions=actions, file_test=file_test)

            #image chibi
        test_image_chibi = True
        if test_image_chibi:
            content_string = part.get("content_string", "")    
            count += 1
            chibi_detail = "make it cute"
            oomp_helper.add_image_chibi(part=part, count=count, mode_ai_wait=mode_ai_wait, chibi_detail=chibi_detail)       

        #jinja_template replace
        if True:
            templates = []
            templates.append({"template_folder": "default"})
            templates.append({"template_folder": "source_file\\template_jinja\\oomp_paper_sheet\\template_jinja_paper_ream_oomlout_297_mm_210_mm", "output_filename": "paper_ream_oomp.svg"})
            convert_to_pdf = False
            convert_to_png = False
            count = oomp_helper.add_jinja_template(part=part, templates=templates, mode_ai_wait=mode_ai_wait, count=count, convert_to_pdf=convert_to_pdf, convert_to_png=convert_to_png)
        

        #folder_project = "helen_personal_chart_bribe_bank"

        #prompt bubble letter        
        if False:
            # prompt change
            prompts = []
            prompts.append({"folder_name" : f"roboclick\\{folder_project}\\prompt_three_dimension_letter_two_line_1", "delay" : "60"})
            #prompts.append({"file_name" : "roboclick\\prompt_bubble_letter_1\\working_2.md", "delay" : "60"})
            words = part.get("words", [])
            word_count = len(words)
            for i in range(word_count):            
                word = words[i]
                prompts.append({"text" : f'Awesome fill in the json template with "{word}"'})
                file_name = f"initial_generated_{i+1}.png"
                prompts.append({"file_name_image" : file_name, "text" : f"Generate the image take all the time you need", "delay" : "60"})
                files_to_trace.append(file_name)
            part2 = copy.deepcopy(part)
            count = oomlout_roboclick.ai_query_from_prompts(part, part2, prompts, mode_ai_wait, count)       

        #prompt image theme
        if False:
            # prompt change
            prompts = []
            prompts.append({"folder_name" : f"roboclick\\{folder_project}\\prompt_image_main_1", "delay" : "60"})                        
            file_name = f"image_main_1.png"
            prompts.append({"file_name_image" : file_name, "text" : f"Generate the image take all the time you need", "delay" : "60"})
            files_to_trace.append(file_name)
            part2 = copy.deepcopy(part)
            count = oomlout_roboclick.ai_query_from_prompts(part, part2, prompts, mode_ai_wait, count)       
        #value
        if False:
            # prompt change
            for i in range(1, 4):
                value = part.get(f"value_{i}", "")
                if value != "":
                    prompts = []
                    prompts.append({"folder_name" : f"roboclick\\{folder_project}\\prompt_image_main_{i}", "delay" : "60"})                        
                    file_name = f"image_value_{i}.png"
                    prompts.append({"file_name_image" : file_name, "text" : f"Generate the image take all the time you need", "delay" : "60"})
                    files_to_trace.append(file_name)
                    part2 = copy.deepcopy(part)                    
                    count = oomlout_roboclick.ai_query_from_prompts(part, part2, prompts, mode_ai_wait, count)
            

        #cover_background
        #prompt image
        if False:
            # prompt change
            prompts = []
            prompts.append({"folder_name" : f"roboclick\\{folder_project}\\prompt_image_background_1", "delay" : "60"})                        
            file_name = f"image_cover_background.png"
            prompts.append({"file_name_image" : file_name, "text" : f"Generate the image take all the time you need", "delay" : "60"})
            files_to_trace.append(file_name)
            new_theme = f'A Bribe Bank with these rewards: {part.get("value_1", "")}, {part.get("value_2", "")}, and {part.get("value_3", "")}'
            part["background_theme"] = new_theme
            part2 = copy.deepcopy(part)
            count = oomlout_roboclick.ai_query_from_prompts(part, part2, prompts, mode_ai_wait, count)       
       
        #internal border
        #prompt image
        if False:
            # prompt change
            prompts = []
            prompts.append({"folder_name" : f"roboclick\\{folder_project}\\prompt_inside_border_1", "delay" : "60"})                        
            file_name = f"image_inside_border.png"
            prompts.append({"file_name_image" : file_name, "text" : f"Generate the image take all the time you need", "delay" : "60"})
            files_to_trace.append(file_name)
            part2 = copy.deepcopy(part)
            count = oomlout_roboclick.ai_query_from_prompts(part, part2, prompts, mode_ai_wait, count)       

        #logo back
        #prompt image
        if False:
            # prompt change
            prompts = []
            prompts.append({"folder_name" : f"roboclick\\{folder_project}\\prompt_logo_back_1", "delay" : "60"})                        
            file_name = f"image_logo_back.png"
            prompts.append({"file_name_image" : file_name, "text" : f"Generate the image take all the time you need", "delay" : "60"})
            files_to_trace.append(file_name)
            part2 = copy.deepcopy(part)
            count = oomlout_roboclick.ai_query_from_prompts(part, part2, prompts, mode_ai_wait, count)       

         


        #trace
        if False:  
            for file_to_trace in files_to_trace:
                folder_name = "roboclick\\action_corel_trace_1" 
                part2 = copy.deepcopy(part)
                part2["file_source"] = file_to_trace
                part2["folder_name"] = folder_name
                if "inside_border" in file_to_trace or "logo_back" in file_to_trace:
                    part2["number_of_colors"] = 2
                if "cover_background" not in file_to_trace:
                    part2["remove_background_color_from_entire_image"] = True                
                part2["mode_ai_wait"] = mode_ai_wait
                part2["file_test"] = "tag"
                count = oomlout_roboclick.ai_action_from_folder(part=part, part2=part2)

        #make_card
        if False:
            folder_name = f"roboclick\\{folder_project}\\action_corel_card_make"
            part2 = copy.deepcopy(part)
            part2["folder_name"] = folder_name
            count = oomlout_roboclick.ai_action_from_folder(part=part, part2=part2)

        #research
        if False:
            folder_name = f"roboclick\\{folder_project}\\research_day_of_the_year"
            prompts = []
            prompts.append({"folder_name" : folder_name, "delay" : "120"})
            file_destination_yaml = "research.yaml"
            action_name = f"research_day_of_the_year"
            part2 = copy.deepcopy(part)
            part2["new_item_name"] = "date_type"
            part2["remove_top_level"] = "data"
            #part2["file_tag"] = file_destination_yaml ## "tag" defaults to creating a tag file after completion
            count = oomlout_roboclick.ai_query_from_prompts(part=part, part2=part2, prompts=prompts, mode_ai_wait=mode_ai_wait, count=count, file_destination_yaml=file_destination_yaml, action_name=action_name)


        parts.append(part)
    



    oomp.add_parts(parts, **kwargs)

    #dd file copy
    for part in parts:
        file_copies = part.get("file_copy", [])
        if file_copies != []:
            for file_copy in file_copies:
                directory = part.get("directory", "")
                if directory != "":
                    file_source = f'{file_copy["file_source"]}'
                    file_destination = f'{directory}\\{file_copy["file_destination"]}'
                    import shutil
                    print(f"      copying {file_source} to {file_destination}")
                    try:
                        shutil.copyfile(file_source, file_destination)
                    except Exception as e:
                        print(f"      error copying file: {e}") 

    import time
    time.sleep(2)



if __name__ == "__main__":
    # run the function
    load_parts()    
    