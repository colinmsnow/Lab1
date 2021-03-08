""" Visualize a nonogram given its numbers and solution """

"""
{
    "cols": [[3],[1,1],[1,1],[1,1],[3]],
    "rows": [[3],[1,1],[1,1],[1,1],[3]],
    "solution": []
}
"""

import nonograms
from matplotlib import pyplot
from matplotlib import colors




def view_nonogram(nonogram):


    dimensions = (len(nonogram["rows"]), len(nonogram["cols"]))
    print(dimensions)
    solution = nonogram["solution"]

    newDict = {}
    for key in solution.keys():
        newDict[key.name] = solution[key]


    allRows = []
    for i in range(dimensions[0]):
        row = []
        for j in range(dimensions[1]):
            key = "V" + str(i) + str(j)
            value = newDict[key]
            row.append(value)
        allRows.append(row)

    colormap = colors.ListedColormap(["white","black"])
            
    pyplot.figure(figsize=(dimensions[0], dimensions[1]))
    pyplot.imshow(allRows,
             cmap=colormap)
    pyplot.show()


sample_nonogram = {
    "cols": [[3],[1,1],[1,1],[1,1],[3]],
    "rows": [[3],[1,1],[1,1],[1,1],[3]],
    "solution": []
}

solved_nonogram = nonograms.solve_nonogram(sample_nonogram)
print(solved_nonogram)
print(view_nonogram(solved_nonogram))