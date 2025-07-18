#!/usr/bin/python3

class SafeDict(dict):
    def __missing__(self, key):
        return "N/A"

def generate_invitations(template, attendees):
    if not isinstance(template, str)or not template:
        print('Template is empty or not a string')
        return

    if not isinstance(attendees, list) or not attendees:
        print('Attendees list is empty or invalid')
        return

    for i, attendee in enumerate(attendees, start=1):

        for key in attendee:
            if attendee[key] is None:
                attendee[key] = "N/A"

        filled_template = template.format_map(SafeDict(attendee))

        filename = f"output_{i}.txt"

        with open(filename, "w") as file:
            file.write(filled_template)
