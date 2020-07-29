import find_book
import ww
import xlwings as xw

app = xw.App(visible=True, add_book=False)
wb = app.books.add()
wb.save(r'D://book_imformation.xlsx')
wb.sheets['sheet1'].range('A1').options(transpose=True).value = [find_book.title,find_book.score,ww.name,ww.tran,ww.out,ww.date,ww.price]

wb.save()
wb.close()
app.quit()