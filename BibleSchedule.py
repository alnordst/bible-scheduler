from BibleData import BibleData

class BibleSchedule:
    DAYS_IN_YEAR = 365
    
    def __init__(self, bible_path):
        self.bd = BibleData(bible_path)
        self.plan = self._build_plan()
        
    def _build_plan(self):
        daily_line_target = (self.bd.ot_lines + self.bd.nt_lines) / self.DAYS_IN_YEAR
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
        
        reading_plan = []
        
        for day in range(365):
            todays_plan = {}
            MAX_CHAPTERS_IN_DAY = 6
            chapters_today = 0
            while chapters_today < MAX_CHAPTERS_IN_DAY:
                ot_percent_completion = ot_progress['lines_read'] / self.bd.ot_lines
                nt_percent_completion = nt_progress['lines_read'] / self.bd.nt_lines
                progress = None
                
                if ot_percent_completion <= nt_percent_completion and ot_percent_completion < 1:
                    progress = ot_progress
                elif nt_percent_completion < 1:
                    progress = nt_progress
                else:
                    break
                
                current_lines = ot_progress['lines_read'] + nt_progress['lines_read']
                expected_lines = daily_line_target * day
                planned_lines = self.bd.data[progress['book']]['chapters'][progress['chapter']]
                
                if not todays_plan or current_lines + planned_lines / 2 <= expected_lines:
                    # Update plan
                    if progress['book'] in todays_plan:
                        todays_plan[progress['book']].append(progress['chapter'])
                    else:
                        todays_plan[progress['book']] = [progress['chapter']]
                    
                    # Update progress
                    if len(self.bd.data[progress['book']]['chapters']) > progress['chapter'] + 1:
                        progress['chapter'] = progress['chapter'] + 1
                    else:
                        progress['book'] = progress['book'] + 1
                        progress['chapter'] = 0
                        
                chapters_today = chapters_today + 1
                        
            reading_plan.append(sorted(todays_plan))
            
        return reading_plan