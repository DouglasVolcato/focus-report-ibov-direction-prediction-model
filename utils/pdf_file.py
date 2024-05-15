import tabula
from utils.pdf_data_filter import PdfDataFilter

class PdfFile:
    def set_pdf_path(self, pdfPath) -> None:
        self.__pdfPath = pdfPath

    def get_data(self) -> list:
        data = self.__read_file()
        return self.__filter_data(data)

    def __read_file(self) -> list:
        return tabula.read_pdf(self.__pdfPath, pages = "1")
    
    def __filter_data(self, data) -> list:
        dataFilter = PdfDataFilter(data[0]['Expectativas de Mercado'])
        filteredData = dataFilter.get_data()
        return filteredData
