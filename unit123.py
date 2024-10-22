# to make it main modudle if condition is used
# __name__  is std variable
import unittest
# def add(a,b):
#     return a+b
# def multiply(a,b):
#     return a*b

# class unittesting(unittest.TestCase): #unnitest ile TestCase class
#     # def test1(self): #method kodkkmbo eppzhm test enn peru kodkknm
#     #     self.assertEqual(add(2,3),5)
#     # def test2(self):
#     #     self.assertTrue("ABC".isupper())
#     # def test3(self):
#     #     self.assertFalse("ABC".isupper())
#     # def test4(self):
#     #     result = 10
#     #     self.assertGreater(result,5)
#     # def test5(self):
#     #     result = 10
#     #     self.assertGreater(5,result) #5 > 10 - false
#     # def test6(self):
#     #     result = [1,2,3,4,5]
#     #     self.assertIn(5,result)
#     #   def test7(self):
#     #     self.assertNotEqual(multiply(1,2),4)
#     #   def test8(self):
#     #     self.assertFalse('Hai'.isupper())
#     #   def test9(self):
#     #     result = [1,2,3,4,5]
#     #     self.assertNotIn(51,result)
#     #   def test10(self):
#     #     l1 = [1,2,3]
#     #     l2 = [1,2,3]
#     #     self.assertListEqual(l1,l2)
#     #   def tets_tuple(self):
#     #     l1 = (1,2,3)
#     #     l2 = (1,2,3)
#     #     self.assertTupleEqual(l1,l2)
#         # def test_dict(self):
#         #     d1 = {"a":1,"b":2,"c":3}
#         #     d2 = {"a":1,"b":2,"c":3}
#         #     self.assertDictEqual(d1,d2)
#         # def test_count(self):
#         #     self.assertCountEqual([1,2,3],[1,2,3])
#         # def test_counts(self):
#         #     self.assertCountEqual([1,2,3],[2,3,1])
#         # def test_counts1(self):
#         #     self.assertCountEqual([1,2,3],[4,6,1])
#         # def test_regex(self):
#         #     self.assertRegex("hello","^h.*$")
#         # def test_regex(self):
#         #     self.assertRegex("hello","^x.*$")
#         #   def test_six(self):
#         #     result =10
#         #     self.assertGreater(result,5)
#         #   def test_six1(self):
#         #     result = 5 
#         #     self.assertGreaterEqual(result,3)
#         #   def test_six2(self):
#         #     result = 3
#         #     self.assertLess(result,10)
#         #   def test_six6(self):
#         #     result = 3
#         #     self.assertLessEqual(result,3)
#         def test_six6(self):
#             result = 3
#             self.assertLessEqual(result,10)
      

if __name__ == "__main__": # __name__ inte value main enn aaan
    unittest.main()


# # acceptig list elements in single line of code
# list1 = list(map(int,input("List elements with space separated: ").split()))
# print(list1)