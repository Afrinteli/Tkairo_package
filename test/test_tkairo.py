# test_tkairo.py

import unittest

from tkinter import Tk   

class WidgetTests(unittest.TestCase):

      

    def setUp(self):

        self.root = Tk()

        

    def test_button(self): 

        btn = button(self.root, "Test")

        self.assertEqual(btn["text"], "Test")

   

    def test_entry(self):

        ent = entry(self.root)

        self.assertIsInstance(ent, Entry)

        

  

class WindowTests(unittest.TestCase): 

        

    def test_center(self):

       center(self.root)  

       self.assertIn("+", self.root.geometry())

   

   

class LayoutTests(unittest.TestCase):

        

    def test_pack(self):

       frm = pack_start(Frame(self.root))

       self.assertIsNotNone(frm) 

if __name__ == "__main__":        

    unittest.main()
