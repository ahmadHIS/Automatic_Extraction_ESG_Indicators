import io
import os

import spacy
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from spacy.matcher import Matcher, PhraseMatcher

nlp = spacy.load("en_core_web_sm")


def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()
            yield text

            # close open handles
            converter.close()
            fake_file_handle.close()




if __name__ == '__main__':
    companies = ["FBHS-ESG-Data-Sheet-FINAL", "ESG_Data_Center 2020-2015", "Texas Instruments summary",
             "Jacobs Engineering summary", "AWK",

             "ldan-esg-report", "BMY-2020-ESG-Report", "FedEx_2021_ESG_Report",
             "Freeport", "GenuineParts",
             "HollyCorp Summary Report"
    , "PCA_2020_Responsibility_Report summary", "BD_Sustainability-report-2020_EN",
             "GRI_preliminaryReport_v5", "hershey_sustainability_report",
             "western-digital-2020-sustainability-report"
    , "Boston_scientific_performance_report"]

    nlpRawtext=""
    str=""
    path = "E:\HIS\HisProject\AllPdfs\\"

    for i in companies:
        mPath= path+i+".pdf"
        print(mPath)
        for page in extract_text_by_page(mPath):
            str =str +page

        nlpRawtext=str
        print(str)
        print("######################### Doc finish #########################")
        print("######################### Nlp is starting #########################")

        nlp.max_length
        doc = nlp(nlpRawtext)

        matcher = PhraseMatcher(nlp.vocab)
        keywords = ["co2","CO2","scope 1"]
        # Only run nlp.make_doc to speed things up
        patterns = [nlp.make_doc(text) for text in keywords]
        matcher.add("TerminologyList", patterns)

        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            token=span.text

            print(span.sent)
            print("\n")
        print("######################### Nlp is finish #########################")

