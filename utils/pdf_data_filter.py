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
            "ipcaData4Weeks": ipcaData4Weeks,
            "ipcaData1Week": ipcaData1Week,
            "ipcaDataToday": ipcaDataToday,
            "pibData4Weeks": pibData4Weeks,
            "pibData1Week": pibData1Week,
            "pibDataToday": pibDataToday,
            "cambioData4Weeks": cambioData4Weeks,
            "cambioData1Week": cambioData1Week,
            "cambioDataToday": cambioDataToday,
            "selicData4Weeks": selicData4Weeks,
            "selicData1Week": selicData1Week,
            "selicDataToday": selicDataToday,
            "igpData4Weeks": igpData4Weeks,
            "igpData1Week": igpData1Week,
            "igpDataToday": igpDataToday,
            "ipcaAdminData4Weeks": ipcaAdminData4Weeks,
            "ipcaAdminData1Week": ipcaAdminData1Week,
            "ipcaAdminDataToday": ipcaAdminDataToday,
            "contaCorrenteData4Weeks": contaCorrenteData4Weeks,
            "contaCorrenteData1Week": contaCorrenteData1Week,
            "contaCorrenteDataToday": contaCorrenteDataToday,
            "balComData4Weeks": balComData4Weeks,
            "balComData1Week": balComData1Week,
            "balComDataToday": balComDataToday,
            "investimentoData4Weeks": investimentoData4Weeks,
            "investimentoData1Week": investimentoData1Week,
            "investimentoDataToday": investimentoDataToday,
            "dividaLiquidaData4Weeks": dividaLiquidaData4Weeks,
            "dividaLiquidaData1Week": dividaLiquidaData1Week,
            "dividaLiquidaDataToday": dividaLiquidaDataToday,
            "resPrimarioData4Weeks": resPrimarioData4Weeks,
            "resPrimarioData1Week": resPrimarioData1Week,
            "resPrimarioDataToday": resPrimarioDataToday,
            "resNominalData4Weeks": resNominalData4Weeks,
            "resNominalData1Week": resNominalData1Week,
            "resNominalDataToday": resNominalDataToday
        }
