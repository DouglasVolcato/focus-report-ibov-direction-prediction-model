class PdfDataFilter:
    def __init__(self, data) -> None:
        self.__data = data

    def get_data(self) -> list:
        splitIpcaData = list(self.__data[5].split())
        ipcaData4Weeks = splitIpcaData[0];
        ipcaData1Week = splitIpcaData[1];
        ipcaDataToday = splitIpcaData[2];

        splitPibData = list(self.__data[6].split())
        pibData4Weeks = splitPibData[0];
        pibData1Week = splitPibData[1];
        pibDataToday = splitPibData[2];

        splitCambioData = list(self.__data[7].split())
        cambioData4Weeks = splitCambioData[0];
        cambioData1Week = splitCambioData[1];
        cambioDataToday = splitCambioData[2];

        splitSelicData = list(self.__data[8].split())
        selicData4Weeks = splitSelicData[0];
        selicData1Week = splitSelicData[1];
        selicDataToday = splitSelicData[2];

        splitIgpMData = list(self.__data[9].split())
        igpData4Weeks = splitIgpMData[0];
        igpData1Week = splitIgpMData[1];
        igpDataToday = splitIgpMData[2];

        splitIpcaAdminData = list(self.__data[10].split())
        ipcaAdminData4Weeks = splitIpcaAdminData[0];
        ipcaAdminData1Week = splitIpcaAdminData[1];
        ipcaAdminDataToday = splitIpcaAdminData[2];

        splitContaCorrenteData = list(self.__data[11].split())
        contaCorrenteData4Weeks = splitContaCorrenteData[0];
        contaCorrenteData1Week = splitContaCorrenteData[1];
        contaCorrenteDataToday = splitContaCorrenteData[2];

        splitBalComData = list(self.__data[12].split())
        balComData4Weeks = splitBalComData[0];
        balComData1Week = splitBalComData[1];
        balComDataToday = splitBalComData[2];

        splitInvestimentoData = list(self.__data[13].split())
        investimentoData4Weeks = splitInvestimentoData[0];
        investimentoData1Week = splitInvestimentoData[1];
        investimentoDataToday = splitInvestimentoData[2];

        splitDividaLiquidaData = list(self.__data[14].split())
        dividaLiquidaData4Weeks = splitDividaLiquidaData[0];
        dividaLiquidaData1Week = splitDividaLiquidaData[1];
        dividaLiquidaDataToday = splitDividaLiquidaData[2];

        splitResPrimarioData = list(self.__data[15].split())
        resPrimarioData4Weeks = splitResPrimarioData[0];
        resPrimarioData1Week = splitResPrimarioData[1];
        resPrimarioDataToday = splitResPrimarioData[2];

        splitResNominalData = list(self.__data[16].split())
        resNominalData4Weeks = splitResNominalData[0];
        resNominalData1Week = splitResNominalData[1];
        resNominalDataToday = splitResNominalData[2];

        return {
            "ipcaData4Weeks": self.__convert_to_float(ipcaData4Weeks),
            "ipcaData1Week": self.__convert_to_float(ipcaData1Week),
            "ipcaDataToday": self.__convert_to_float(ipcaDataToday),
            "pibData4Weeks": self.__convert_to_float(pibData4Weeks),
            "pibData1Week": self.__convert_to_float(pibData1Week),
            "pibDataToday": self.__convert_to_float(pibDataToday),
            "cambioData4Weeks": self.__convert_to_float(cambioData4Weeks),
            "cambioData1Week": self.__convert_to_float(cambioData1Week),
            "cambioDataToday": self.__convert_to_float(cambioDataToday),
            "selicData4Weeks": self.__convert_to_float(selicData4Weeks),
            "selicData1Week": self.__convert_to_float(selicData1Week),
            "selicDataToday": self.__convert_to_float(selicDataToday),
            "igpData4Weeks": self.__convert_to_float(igpData4Weeks),
            "igpData1Week": self.__convert_to_float(igpData1Week),
            "igpDataToday": self.__convert_to_float(igpDataToday),
            "ipcaAdminData4Weeks": self.__convert_to_float(ipcaAdminData4Weeks),
            "ipcaAdminData1Week": self.__convert_to_float(ipcaAdminData1Week),
            "ipcaAdminDataToday": self.__convert_to_float(ipcaAdminDataToday),
            "contaCorrenteData4Weeks": self.__convert_to_float(contaCorrenteData4Weeks),
            "contaCorrenteData1Week": self.__convert_to_float(contaCorrenteData1Week),
            "contaCorrenteDataToday": self.__convert_to_float(contaCorrenteDataToday),
            "balComData4Weeks": self.__convert_to_float(balComData4Weeks),
            "balComData1Week": self.__convert_to_float(balComData1Week),
            "balComDataToday": self.__convert_to_float(balComDataToday),
            "investimentoData4Weeks": self.__convert_to_float(investimentoData4Weeks),
            "investimentoData1Week": self.__convert_to_float(investimentoData1Week),
            "investimentoDataToday": self.__convert_to_float(investimentoDataToday),
            "dividaLiquidaData4Weeks": self.__convert_to_float(dividaLiquidaData4Weeks),
            "dividaLiquidaData1Week": self.__convert_to_float(dividaLiquidaData1Week),
            "dividaLiquidaDataToday": self.__convert_to_float(dividaLiquidaDataToday),
            "resPrimarioData4Weeks": self.__convert_to_float(resPrimarioData4Weeks),
            "resPrimarioData1Week": self.__convert_to_float(resPrimarioData1Week),
            "resPrimarioDataToday": self.__convert_to_float(resPrimarioDataToday),
            "resNominalData4Weeks": self.__convert_to_float(resNominalData4Weeks),
            "resNominalData1Week": self.__convert_to_float(resNominalData1Week),
            "resNominalDataToday": self.__convert_to_float(resNominalDataToday)
        }
    
    def __convert_to_float(self, num):
        return float(num.replace(",", "."))
