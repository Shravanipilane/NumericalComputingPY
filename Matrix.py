class Matrix:
   
    def __init__(self, data):
        # data = list of lists, e.g. [[1, 2], [3, 4]]
        self.data = data                        #the data belongs to the particular object
        self.rows = len(data)                             
        self.cols = len(data[0]) if data else 0      #if data exits(data[1] find the number of colunms.otherwise return 0)

    def __str__(self):                                    
        lines = []
        for row in self.data:
            lines.append("  ".join(str(val) for val in row))
        return "\n".join(lines)

    def add_row(self, row):
        self.data.append(row)
        self.rows += 1 