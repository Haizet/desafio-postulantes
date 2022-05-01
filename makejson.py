from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pandas import DataFrame


def info_table_grab(url, table_name, header_finder, rows_finder):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    table = driver.find_element(By.ID, table_name)
    header = table.find_elements(By.TAG_NAME, header_finder)
    rows = table.find_elements(By.TAG_NAME, rows_finder)

    col_name = [head.text for head in header]

    cel_cont = []
    for row in rows:
        data = row.find_elements(By.TAG_NAME, "td")
        content = [info.text for info in data]
        if content:
            cel_cont.append(content)

    driver.close()

    DataFrame(data=cel_cont, columns=col_name).to_json(path_or_buf="proyect.json", orient="table", index=False)
