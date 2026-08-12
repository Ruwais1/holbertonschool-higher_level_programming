import os

def generate_invitations(template, attendees):
    """
    Generates invitations for a list of attendees based on a given template.

    Args:
        template (str): The invitation template containing placeholders.
        attendees (list): A list of attendee dictionaries.
    """
    if not isinstance(template, str):
        print("Error: template must be a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    # Handle Empty section
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process Each Attendee
    placeholders = ["name", "event_title", "event_date", "event_location"]
    
    for idx, attendee in enumerate(attendees, start=1):
        content = template
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            
            content = content.replace(f"{{{placeholder}}}", str(value))
        
        # 4 Generate Output Files
        output_filename = f"output_{idx}.txt"
        
        if os.path.exists(output_filename):
            pass

        try:
            with open(output_filename, "w") as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")
