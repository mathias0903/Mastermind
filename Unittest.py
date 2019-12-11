import unittest as ut
import datalag as dl
import logiklag as ll

class Testfunctions(ut.testcase):

    def test_notspecifiedinit(self):
        testdatalag = dl.datalag()
        self.assertEqual(testdatalag.brikker , 4)
        self.assertEqual(testdatalag.muligheder , 6)
        self.assertEqual(testdatalag.maks , 10)
        self.assertTrue(isinstance(testdatalag.solution, tuple))
        self.assertEqual(len(testdatalag.solution), testdatalag.brikker)

    def test_specifiedinit(self):
        testdatalag = dl.datalag(brikker=6, muligheder=8, maks=12, solution=4,6,1,2,3,8)
        self.assertEqual(testdatalag.brikker , 6)
        self.assertEqual(testdatalag.muligheder , 8)
        self.assertEqual(testdatalag.maks , 12)
        self.assertTrue(isinstance(testdatalag.solution, tuple))
        self.assertEqual(len(testdatalag.solution), testdatalag.brikker)
        self.assertEqual(testdatalag.solution, [4,6,1,2,3,8])

    def test_get(self):
        testdatalag = dl.datalag(brikker=6, muligheder=8, maks=12, solution=4,6,1,2,3,7)
        self.assertEqual(dl.getbrikker(), 6)
        self.assertEqual(dl.getmuligheder(), 8)
        self.assertEqual(dl.getmaks(), 12)
        self.assertEqual(dl.getsolution(), [4,6,1,2,3,7])

    def test_set(self):
        testdatalag = dl.datalag(brikker=6, muligheder=8, maks=12, solution=4,6,1,2,3,7)
        dl.setbrikker(2)
        self.assertEqual(dl.getbrikker(), 2)
        dl.setmuligheder(69)
        self.assertEqual(dl.getmuligheder(), 69)
        dl.setmaks(42)
        self.assertEqual(dl.getmaks(), 42)
        dl.setsolution(4,6)
        self.assertEqual(dl.getsolution(), [4,6])
        with self.assertRaises(TypeError):
            dl.setbrikker("Epstein didn't kill himself")
        with self.assertRaises(TypeError):
            dl.setmuligheder(4.0)
        with self.assertRaises(TypeError):
            dl.setmaks("EXDEE IM PICKLE WICK JOHN WICK FORTNITE UWU JOHN FORTNITE PICKLE WICK UWU")