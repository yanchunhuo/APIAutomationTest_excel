#!/usr/bin/python
#-*- coding:utf-8 -*-
import xlrd
import xlwt
import xlutils.copy
import sys

class ExcelTool():
    def __init__(self):
        pass

    '''
    @param:excelFilePath excel文件路径
    @param:sheetNum 读取第几个sheet，从0开始
    @return: 返回一个字典数组，第一行作为字典的属性，第二行开始每一行代表一个字典
    '''
    def readAsDictArray(self,excelFilePath,sheetNum):
        resultList=[]
        with xlrd.open_workbook(excelFilePath) as workbook:
            sheet=workbook.sheets()[sheetNum]
            rows_num=sheet.nrows
            cols_num=sheet.ncols
            print '共有',rows_num,'行,',cols_num,'列'
            firt_row=[]
            for curt_col in range(cols_num):
                tmp_firt_cell=sheet.cell_value(0,curt_col)
                if(sheet.cell_type(0,curt_col)==2):
                    if(tmp_firt_cell==int(tmp_firt_cell)):
                        tmp_firt_cell=int(tmp_firt_cell)
                firt_row.append(tmp_firt_cell)
            for curt_row in range(1,rows_num):
                tmp_row=[]
                for curt_col in range(cols_num):
                    tmp_cell=sheet.cell_value(curt_row,curt_col)
                    #如果数据类型是数字
                    if(sheet.cell_type(curt_row,curt_col)==2):
                        if(tmp_cell==int(tmp_cell)):
                            tmp_cell=int(tmp_cell)
                    tmp_row.append(tmp_cell)        
                resultList.append(dict(zip(firt_row,tmp_row)))
        return resultList

    '''
    @param:excelFilePath excel文件路径
    @param:sheetNum 读取第几个sheet，从0开始
    @return: 返回一个数组，每一行是数组的元素
    '''
    def readAsArray(self,excelFilePath,sheetNum):
        resultList=[]
        with xlrd.open_workbook(excelFilePath) as workbook:
            sheet=workbook.sheets()[sheetNum]
            rows_num=sheet.nrows
            cols_num=sheet.ncols
            print '共有',rows_num,'行,',cols_num,'列'
            for curt_row in range(rows_num):
                tmp_row=[]
                for curt_col in range(cols_num):
                    tmp_cell=sheet.cell_value(curt_row,curt_col)
                    #如果数据类型是数字
                    if(sheet.cell_type(curt_row,curt_col)==2):
                        if(tmp_cell==int(tmp_cell)):
                            tmp_cell=int(tmp_cell)
                    tmp_row.append(tmp_cell)        
                resultList.append(tmp_row)
        return resultList
    
    '''
    @param: excelFilePath 文件保存的路径
    @param: sheetName sheet的名字
    @param: data[[]] 外层每个元素代表一行，理财数组每个元素代表单元格数据
    '''
    def createWithArray(self,excelFilePath,sheetName,data=[[]]):
        wb=xlwt.Workbook() 
        sheet=wb.add_sheet(sheetName,True)
        for curt_row in range(len(data)):
            for curt_col in range(len(data[curt_row])):
                sheet.write(curt_row,curt_col,data[curt_row][curt_col])
        wb.save(excelFilePath)

    '''
    @param: excelFilePath 需要修改的excel路径
    @param: sheetNum 修改第几个sheet，从0开始
    @param: row_num 修改第几行
    @param: col_num 修改第几列
    @param: cell_value 修改的值
    '''
    def modifyCell(sefl,excelFilePath,sheetNum,row_num,col_num,cell_value):
        with xlrd.open_workbook(excelFilePath) as workbook:
            wb=xlutils.copy.copy(workbook)
            sheet=wb.get_sheet(sheetNum)
            sheet.write(row_num,col_num,cell_value)
            wb.save(excelFilePath)

    '''
    @param: excelFilePath 需要修改的excel路径
    @param: sheetName 新增sheet的名字
    @param: data[[]] 外层每个元素代表一行，理财数组每个元素代表单元格数据
    '''
    def addSheetAndValue(sefl,excelFilePath,sheetName,data=[[]]):
        with xlrd.open_workbook(excelFilePath) as workbook:
            wb=xlutils.copy.copy(workbook)
            sheet=wb.add_sheet(sheetName,True)
            for curt_row in range(len(data)):
                for curt_col in range(len(data[curt_row])):
                    sheet.write(curt_row,curt_col,data[curt_row][curt_col])
            wb.save(excelFilePath)

if __name__=='__main__':
    curt_path=sys.path[0]
    print curt_path
    excelTool=ExcelTool()

    a=[[1,2,3,4,5],[5,4,3,2,1],['a','b','c','d','e','f'],[1.099,2.3,2,0]]
    excelTool.addSheetAndValue(curt_path+'/a.xlsx','bb',a)




