import datetime

"""
books = [
    {
        'title': "Genesis",
        'chapters': [
            <line count>,
            <line count>
        ]
    },
    {
        'title': "Exodus",
        'chapters': [
            <line count>,
            <line count>
        ]
    }
]
"""


# Setup...

books = []

bible = open("pg10-edit.txt", "r")

between_books = True
lines_since_text = 0



# Assemble bible data
for raw_line in bible:
    line = raw_line.rstrip()
    
    if between_books:
        # Only look for ## when between books
        if line[:2] == "##":
            title = line[2:]
            books.append({'title': title, 'chapters': []})
            between_books = False
            lines_since_text = 0
    
    elif not line:
        # Line is empty
        lines_since_text = lines_since_text + 1
    
    else:
        # Line is not empty
        if lines_since_text >= 3:
            # Big gap
            between_books = True
        
        elif lines_since_text >= 1:
            # Small gap (means new verse)
            address = line.split(" ")[0].split(":")
            
            if address[0] > len(books[-1]['chapters']):
                # Begin new chapter
                books[-1]['chapters'].append([1])
            else:
                # Continuing current chapter
                books[-1]['chapters'][-1].append(1)
        
        else:
            # No gap
            books[-1]['chapters'][-1] = books[-1]['chapters'][-1] + 1

bible.close()



# Setup...

old_testament_lines = 0
new_testament_lines = 0

for index, book in enumerate(books):
    lines_in_book = 0
    for lines_in_chapter in book.chapters:
        lines_in_book = lines_in_book + lines_in_chapter
    if index < 39:
        old_testament_lines = old_testament_lines + lines_in_book
    else:
        new_testament_lines = new_testament_lines + lines_in_book
    

daily_line_target = (old_testament_lines + new_testament_lines) / 365
ot_progress = {
    "book": 0,
    "chapter": 0,
    "lines_read": 0
}
nt_progress = {
    "book": 39,
    "chapter": 0,
    "lines_read": 0
}


# Assemble reading plan
    
    

# Write out plan
plan_file = open("bible-reading-plan.txt", "w")

for day, plan in enumerate(reading_plan):
    day_one = datetime.date(2018, 1, 1)
    this_day = day_one + datetime.timedelta(days = day)
    plan_file.write(this_day.strftime("%B %d\n"))
    
    
    for book, chapters in plan.items():
        plan_file.write(books[book]['title'])
        
        for index, chapter in enumerate(chapters):
            if index == 0:
                plan_file.write(" ")
            else:
                plan_file.write(", ")
            
            plan_file.write(str(chapter + 1))
        
        plan_file.write("\n")
    
    plan_file.write("\n")
    
plan_file.close()