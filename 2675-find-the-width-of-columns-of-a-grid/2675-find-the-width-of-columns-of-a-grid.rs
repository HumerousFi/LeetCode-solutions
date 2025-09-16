impl Solution {
    pub fn find_column_width(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let n:usize = grid[0].len();
        let mut ans = vec![0; n];
        for r in grid {
            for j in 0..n {
                ans[j] = ans[j].max(r[j].to_string().len() as i32);
            }
        }
        ans
    }
}