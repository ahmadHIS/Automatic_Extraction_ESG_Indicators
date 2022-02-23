companies = ["SASB", "FBHS-ESG-Data-Sheet-FINAL", "AES_Sustainability-Report", "Apple_ESG_Report", "bgildan-esg-report",
             "Climate-Report"
    , "CORP-Report-Sustainability", "eBay-Impact-2020-Report", "ESG_Data_Center 2020-2015", "FedEx_2021_ESG_Report",
             "Fortive_ CDP Climate Change Disclosure 2021", "Fortune Brands ESG Report",
             "ft-corporate-social-responsibility-report"
    , "gap-inc-report", "gartner_csr_report", "GRI_preliminaryReport_v5", "hershey_sustainability_report",
             "purpose-report-2021"
    , "Sustainability-Report"]

import camelot


def extract(pdf_path, company):
    try:
        tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')
        tables.export(company + '.csv', f='csv', compress=True)
    except:
        print("An exception occurred")


str = ""
path = "E:\HIS\HisProject\\"

for i in companies:
    mPath = path + i + ".pdf"
    print("Printing" + mPath)
    extract(mPath, i)