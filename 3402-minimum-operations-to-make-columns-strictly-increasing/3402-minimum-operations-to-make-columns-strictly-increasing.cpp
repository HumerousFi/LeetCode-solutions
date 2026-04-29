class Solution {
public:
    int minimumOperations(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int ops = 0;

        for (int j = 0; j < n; j++) {
            int prev = grid[0][j];
            for (int i = 1; i < m; i++) {
                if (grid[i][j] <= prev) {
                    int need = prev + 1;
                    ops += (need - grid[i][j]);
                    prev = need;
                } else {
                    prev = grid[i][j];
                }
            }
        }

        return ops;
    }
};