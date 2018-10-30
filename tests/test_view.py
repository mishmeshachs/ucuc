import unittest
from .. view import add_new_zone, add_new_area


class Test_View(unittest.TestCase)
def setUp(self):
    self.area_name ="Mukono"
    self.codenates ="0.43673,0.653021"
    self.zone_id = "zone1"
    self.all_zones =[{"zone_id","zone1","new_area","Mukono","0.43673,0.653021","messages","New items availabe"}]

    def test_new_area(self):
        new_area = area_and_codenates(self.area_name,codenates)
        self.assertEqual(self.area_and_codenates,new_area)

    def test_submit(self):
        resp = add_new_area(self.area_and_codenates,message)
        self.assertEqual(resp,True)