var minPathSum = function (grid) {
    let h1 = 0, v1 = 0, minSum = 0;
    const lenH = grid[0].length, lenV = grid.length;
    sumPath(v1, h1, 0);

    function sumPath(v, h, sum = 0) {
        console.log(v, h)
        sum += grid[v][h];
        if (h === lenH - 1 && v === lenV - 1) {
            console.log(sum);
            minSum = !minSum ? sum : Math.min(minSum, sum);
            return;
        };

        if (h < lenH - 1) sumPath(v, h + 1, sum);
        console.log('next', v, h, sum)
        if (v < lenV - 1) sumPath(v + 1, h, sum);

    }
    return minSum;
};
var grid = [[1, 3, 5], [1, 5, 1], [4, 2, 1]];
console.log(minPathSum(grid));