import pandas as pd


def get_new_file(path_file, name_out_file, index_col_raz):
    """
    Метод для преобразования таблиц
    :param path_file: путь до файла
    :param name_out_file: название выходного файла
    :param index_col_raz: индекс столбца с размерами (счёт начинается с 1)
    :return: файл с таблицей в новом виде
    """
    exsel_table = pd.read_excel(path_file) # получение исходного файла
    headers = ['name', 'razmer', 'price'] # заголовки выходного файла
    data = {header:list() for header in headers}
    razmer = exsel_table.columns[index_col_raz-1] # название столбца с размерами
    columns_names = exsel_table.columns # название столбцов старой таблицы
    for i in range(0, len(columns_names)): # обход циклом названия столбцов
        name = columns_names[i]
        if name == razmer:
            continue
        df_new = exsel_table[[razmer, name]]
        for i, row in df_new.iterrows(): # обход циклом строк каждого столбца и заполнения новой таблицы
            data['name'].append(name)
            data['razmer'].append(row[razmer])
            data['price'].append(row[name])
    out_df = pd.DataFrame(data) # создание таблицы
    out_df.to_excel(name_out_file, index=None, header=headers) # сохранение в эксель


if __name__=="__main__":
    path_in_file = 'test.xlsx'
    path_in_new_file = path_in_file.replace('.xlsx','')
    get_new_file(path_in_file, path_in_new_file + '_NEW.xlsx', 1)
