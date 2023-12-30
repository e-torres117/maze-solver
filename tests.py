import unittest
from maze import Maze

class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_reset_visited_cells(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in m1._cells:
            for j in i:
                self.assertEqual(
                    cell._visited,
                    False
                ) 




if __name__ == "__main__":
    unittest.main()