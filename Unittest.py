import unittest as ut
import datalag as dl
import logiklag as ll

class Testfunctions(ut.testcase):

    def test_notspecifiedinit(self):
        testdatalag = dl.Datalag()
        self.assertEqual(testdatalag.brikker, 4)
        self.assertEqual(testdatalag.muligheder, 6)
        self.assertEqual(testdatalag.maks, 10)
        self.assertTrue(isinstance(testdatalag.solution, tuple))
        self.assertEqual(len(testdatalag.solution), testdatalag.brikker)

    def test_specifiedinit(self):
        testdatalag = dl.Datalag(brikker=6, muligheder=8, maks=12, solution=(4,6,1,2,3,8))
        self.assertEqual(testdatalag.brikker , 6)
        self.assertEqual(testdatalag.muligheder , 8)
        self.assertEqual(testdatalag.maks , 12)
        self.assertTrue(isinstance(testdatalag.solution, tuple))
        self.assertEqual(len(testdatalag.solution), testdatalag.brikker)
        self.assertEqual(testdatalag.solution, (4,6,1,2,3,8))

    def test_get(self):
        testdatalag = dl.Datalag(brikker=6, muligheder=8, maks=12, solution=(4,6,1,2,3,7))
        self.assertEqual(testdatalag.brikker=6)
        self.assertEqual(testdatalag.muligheder=8)
        self.assertEqual(testdatalag.maks=12)
        self.assertEqual(testdatalag.solution=(4,6,1,2,3,7))

    def test_set(self):
        testdatalag = dl.Datalag(brikker=6, muligheder=8, maks=12, solution=(4,6,1,2,3,7))
        testdatalag.brikker=2
        self.assertEqual(testdatalag.brikker, 2)
        testdatalag.muligheder=69
        self.assertEqual(testdatalag.muligheder=69)
        testdatalag.maks=42
        self.assertEqual(testdatalag.maks=42)
        testdatalag.solution=(4,6)
        self.assertEqual(testdatalag.solution=(4,6)
        with self.assertRaises(TypeError):
            testdatalag.brikker="Epstein didn't kill himself"
        with self.assertRaises(TypeError):
            testdatalag.muligheder=4.0
        with self.assertRaises(TypeError):
            testdatalag.maks="EXDEE IM PICKLE WICK JOHN WICK FORTNITE UWU JOHN FORTNITE PICKLE WICK UWU"