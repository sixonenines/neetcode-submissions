class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnMap={}
        boxMap={}
        for rowCount, row in enumerate(board):
            rowCheck=set()
            for index,element in enumerate(row):
                if element==".":
                    continue
                if element in rowCheck:
                    return False
                if index not in columnMap:
                    columnMap[index]=set()
                if element in columnMap[index]:
                    return False
                boxColumn=index//3
                boxRow=rowCount//3
                boxID=str(boxColumn)+str(boxRow)
                if boxID not in boxMap:
                    boxMap[boxID]=set()
                if element in boxMap[boxID]:
                    return False
                columnMap[index].add(element)
                rowCheck.add(element)
                boxMap[boxID].add(element)
        return True