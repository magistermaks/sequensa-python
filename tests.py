
import unittest
import sequensa as sq


class MyTestCase(unittest.TestCase):

    def test_basic_return(self):
        compiler = sq.Compiler()
        executor = sq.Executor()

        program = compiler.build(b"#exit << 123")

        if program is not None:
            executor.execute(program)
            res = executor.results()
            gen = res.get(0)
            self.assertEqual(gen.get_long(), 123)
        else:
            self.fail("Failed to compile!")


if __name__ == '__main__':
    unittest.main()
