import shutil
import os 
import frontmatter

#list of frontmatter properties with folder destinations
frontmatter_to_dir = {
    'project':'1.Projects',
    'area':'2.Areas',
    'resource':'3.Resources',
}


def try_move_file(file, destination):
    print('-moving file',file,'to',destination)
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)
        shutil.move(file, destination)
    except shutil.Error as err:
        print(f'Error:{err}')
    except Exception as err:
        print('--Project not found', err)

# Read all files inside the 'inbox' directory
notes = os.listdir('!inbox')
for note in notes:
    note_path = f"!inbox/{note}"
    # read the file's frontmatter
    note_metadata = frontmatter.load(note_path)

    # check if the file has a property to categorize this note,
    # for example: project, area or resource
    for group, group_destination in frontmatter_to_dir.items():
        if group in note_metadata:
            # try moving file, it can be the case the project is for example mispelled,
            # in that case it won't do anything with the note
            try_move_file(note_path, f"{group_destination}/{note_metadata[group]}/{note}")


        