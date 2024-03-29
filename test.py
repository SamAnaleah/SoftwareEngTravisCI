import unittest
import calculator

class Tests(unittest.TestCase):
  def test_add(self):
    self.assertEqual(calculator.add(2,3),5)
  def test_sub(self):
    self.assertEqual(calculator.sub(2,3),-1)
  def test_multi(self):
    self.assertEqual(calculator.mult(2,3),6)
  def test_div(self):
    self.assertEqual(calculator.div(6,3),2)

if__name__=='__main__':
  unittest.main()
