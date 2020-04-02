# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import os
from ..settings import PDF_PATH, CSV_PATH
# import camelot
# import pandas
# from datetime import datetime

class GobmxSpider(scrapy.Spider):
    name = 'gobmx'
    start_urls = ['https://www.gob.mx/salud/documentos/coronavirus-covid-19-comunicado-tecnico-diario-238449']

    def parse(self, response):
        for href in response.css("div.table-responsive li a::attr(href)").extract():
            if "Tabla_casos" in href and "pdf" in href:
                yield Request(
                    url=response.urljoin(href),
                    callback=self.save_pdf
                )

    def save_pdf(self, response):
        filename = response.url.split('/')[-1]
        self.logger.info('Saving PDF %s', filename)
        file_full_path = os.path.join(PDF_PATH, filename)
        with open(file_full_path, 'wb') as f:
            f.write(response.body)
        
        # tables = camelot.read_pdf(file_full_path, pages="1-end")
        # dataframes = []
        # for table in tables:
        #     dataframes.append(table.df)
        # entire_table = pandas.concat(dataframes)

        # csv_name = self.name
        # if "casos_positivos" in filename:
        #     csv_name = "casos_positivos"
        # elif "casos_sospechosos" in filename:
        #     csv_name = "casos_sospechosos"
        # csv_name = csv_name+"_data_"+datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".csv"

        # entire_table.to_csv(os.path.join(CSV_PATH, csv_name))