import unittest

def solution(N):
  return binaryGap(N)

def binaryGap(n):
  state = 0
  gap = 0
  max = 0

  while (n != 0):
    # process most significant bits first (no impact on the solution)
    bit = n%2 
    n = n//2

    if (bit == 0):
      gap = gap+1

    # The state machine:
    # "a" stands for "activate record"
    # "d" stands for "deactivate record"
    # |   bit    |
    # d -- 0 --> d
    # d -- 1 --> a
    # a -- 1 --> a
    # a -- 0 --> a
    # "+" stands for "increment gap"
    # 101 => a+d
    # 10101 => a+a+d
    # 11 => aa
    if (bit == 1):
      if (state == 1):
        if (gap > max):
          max = gap
      if (state == 0):
        state = 1
      gap = 0

  return max

class TestBinaryGap(unittest.TestCase):
  def test_0(self):
    # 00
    self.assertEqual(binaryGap(0), 0)

  def test_1(self):
    # 01
    self.assertEqual(binaryGap(1), 0)

  def test_2(self):
    # 10
    self.assertEqual(binaryGap(2), 0)

  def test_3(self):
    # 11
    self.assertEqual(binaryGap(3), 0)

  def test_4(self):
    # 100
    self.assertEqual(binaryGap(4), 0)

  def test_5(self):
    # 101
    self.assertEqual(binaryGap(5), 1)

  def test_6(self):
    # 110
    self.assertEqual(binaryGap(6), 0)

  def test_9(self):
    # 1001
    self.assertEqual(binaryGap(9), 2)

  def test_328(self):
    # 101001000
    self.assertEqual(binaryGap(328), 2)

  def test_1041(self):
    # 10000010001
    self.assertEqual(binaryGap(1041), 5)

