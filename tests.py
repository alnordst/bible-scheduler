import unittest
from BibleData import BibleData
from BibleSchedule import BibleSchedule


class TestBibleData(unittest.TestCase):
    
    def test_inits_without_errors(self):
        bd = BibleData("pg10-edit.txt")
        self.assertTrue(True)
        
    def test_sixty_six_books_in_bible(self):
        bd = BibleData("pg10-edit.txt")
        self.assertEqual(len(bd.data), 66)
        
    def test_line_count_viable(self):
        bd = BibleData("pg10-edit.txt")
        self.assertTrue(bd.ot_lines > 0)
        self.assertTrue(bd.nt_lines > 0)
        self.assertEqual(bd.ot_lines + bd.nt_lines, bd.total_lines)
        
    def test_no_empty_chapters(self):
        bd = BibleData("pg10-edit.txt")
        all_chapters_are_ints = True
        no_empty_chapters = True
        
        for book in bd.data:
            for chapter in book["chapters"]:
                if not isinstance(chapter, int):
                    all_chapters_are_ints = False
                if chapter == 0:
                    no_empty_chapters = False
                    
        self.assertTrue(all_chapters_are_ints)
        self.assertTrue(no_empty_chapters)
        
        
        
class TestBibleSchedule(unittest.TestCase):
    
    def dont_test_inits_without_errors(self):
        bs = BibleSchedule("pg10-edit.txt")
        self.assertTrue(True)