class Solution:
    def getTotalIsles(self, grid):
        if not grid:
            return 0

        # Dimensions 
        rows, cols = len(grid), len(grid[0])
        islands_count = 0  # Initialize the count

        # Function to perform DFS 
        def DFS(r, c):
           
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            # Mark the current landmass 
            grid[r][c] = 'W'
            # Explore all four directionSS
            DFS(r + 1, c)  
            DFS(r - 1, c)  
            DFS(r, c + 1)  
            DFS(r, c - 1)  

        # Loop 
        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j] == 'L':
                    islands_count += 1  # Increment  count
                    DFS(i, j)  # Start DFS 

        return islands_count  # Return the total number of islands

# Unit test class
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        result = self.solution.getTotalIsles([
            ["L","L","L","L","W"],
            ["L","L","W","L","W"],
            ["L","L","W","W","W"],
            ["W","W","W","W","W"]
        ])
        self.assertEqual(result, 1)

    def test_case2(self):
        result = self.solution.getTotalIsles([
            ["L","L","W","W","W"],
            ["L","L","W","W","W"],
            ["W","W","L","W","W"],
            ["W","W","W","L","L"]
        ])
        self.assertEqual(result, 3)

    def test_case3(self):
        result = self.solution.getTotalIsles([
            ["W", "W", "W", "W"],
            ["W", "L", "L", "W"],
            ["W", "L", "L", "W"],
            ["W", "W", "W", "W"]
        ])
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
