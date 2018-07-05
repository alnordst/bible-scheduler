class BibleData:
    OT_BOOK_COUNT = 39
    
    def __init__(self, bible_path):
        self.data = []
        
        bible = open(bible_path, "r")
        
        between_books = True
        lines_since_text = 0
        
        for raw_line in bible:
            line = raw_line.rstrip()
            
            if between_books:
                # Only look for ## when between books
                if line[:2] == "##":
                    title = line[2:]
                    self.data.append({'title': title, 'chapters': []})
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
                    try:
                        ch_address = int(line.split(":")[0])
                        
                        if ch_address > len(self.data[-1]['chapters']):
                            # Begin new chapter
                            self.data[-1]['chapters'].append(1)
                        else:
                            # Continuing current chapter
                            self.data[-1]['chapters'][-1] = self.data[-1]['chapters'][-1] + 1
                    except ValueError:
                        self.data[-1]['chapters'][-1] = self.data[-1]['chapters'][-1] + 1

                else:
                    # No gap
                    self.data[-1]['chapters'][-1] = self.data[-1]['chapters'][-1] + 1
        
                lines_since_text = 0
        
        bible.close()
        
        self.calculate_lines()
        
    
    def calculate_lines(self):    
        ot_lines = 0
        nt_lines = 0
        
        for book_num, book_data in enumerate(self.data):
            lines_in_book = 0
            for lines_in_chapter in book_data['chapters']:
                lines_in_book = lines_in_book + lines_in_chapter
            if book_num < self.OT_BOOK_COUNT:
                ot_lines = ot_lines + lines_in_book
            else:
                nt_lines = nt_lines + lines_in_book
                
        self.ot_lines = ot_lines
        self.nt_lines = nt_lines
        self.total_lines = ot_lines + nt_lines