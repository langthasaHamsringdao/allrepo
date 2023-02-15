from gsheets import Sheets

sheets = Sheets.from_files('../creds/client_secrets.json', '../creds/storage.json')

sheet = sheets['15i5MitYudlbevoJDNBbm-fRIQ_dTiCsHUguJ0RKNkDs']

conf_sheet = sheet.find('conf_sheet')


def process(sheet, worksheet_name, process_query, columns, run_flag=0, token=True):
    global lst
    lst = process_query.strip()
    if run_flag:
        print(sheet)
        print(worksheet_name)
        print(process_query)
        print(columns)
        print('==>' * 10)


for row in range(1, conf_sheet.nrows):
    sheet = conf_sheet.at(row, 0)
    worksheet_name = conf_sheet.at(row, 1)
    process_query = conf_sheet.at(row, 2)
    columns = conf_sheet.at(row, 3)
    run_flag = conf_sheet.at(row, 4)

    process(sheet, worksheet_name, process_query, columns, run_flag)