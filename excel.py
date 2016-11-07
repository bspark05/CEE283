#-*- coding: utf-8 -*-

import xlrd
import numpy as np

def excelRead(filepath, sheetname):
    workbook = xlrd.open_workbook(filepath)
    worksheet = workbook.sheet_by_name(sheetname)
    
    num_rows = worksheet.nrows -1
    curr_row = -1
    result = []
    
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        result.append(row)
    
    return result


def excelToArray(filepath, sheetname):
    varExcel = excelRead(filepath, sheetname)
    varList = []
    # first row is a field name
    for row in varExcel[1:]:
        rowList = []
        for value in row:
            rowList.append(float(value.value))
        varList.append(rowList)
    varArray = np.array(varList)
    # transpose the array
    varArrayTras = np.transpose(varArray)
    
    return varArrayTras


