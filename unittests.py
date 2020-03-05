import unittest, autodate, openpyxl, datetime

class TestAutoDate(unittest.TestCase):
    
    def setUp(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.cell_a1 = self.ws["a1"]
        self.cell_a2 = self.ws["a2"]
        self.cell_b1 = self.ws["b1"]
        self.cell_b1.value = datetime.datetime(2020,1,1)
        self.cell_b2 = self.ws["b2"]
        self.cell_b2.value = datetime.datetime(2020,1,2)
        self.timedelta = 1
    
    def test_see_if_date_has_passed(self):
        self.assertEqual(autodate.see_if_date_has_passed(datetime.datetime(2000,1,1)), True)
        self.assertFalse(autodate.see_if_date_has_passed(datetime.datetime.today() + datetime.timedelta(days=1)))
        self.assertTrue(autodate.see_if_date_has_passed(datetime.datetime.today()))
        
    def test_update_date(self):
        self.assertEqual(autodate.update_date(self.cell_b1, 1), self.cell_b2.value)

    def test_check_cell_range(self):
        autodate.check_cell_range(self.ws, "b1", "b2", self.timedelta)
        self.assertEqual((self.cell_b1.value, self.cell_b2.value), (datetime.datetime(2020,1,2), datetime.datetime(2020,1,3)))
        
if __name__ == "main":
    unittest.main()