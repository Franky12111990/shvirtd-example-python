def insert_proxy(config_file_path, proxy_file_path):
    with open(proxy_file_path, 'r') as f:
        proxy_data = f.readlines()[3:-7]  # Начинаем считывать с 4 строки, исключаем последние 7 строк

    with open(config_file_path, 'r') as f:
        config_data = f.readlines()

    insert_index = None
    for i, line in enumerate(config_data):
        if 'services:' in line:
            insert_index = i + 1
            break

    if insert_index is not None:
        # Вставляем содержимое proxy_data в config_data
        config_data = config_data[:insert_index] + proxy_data + config_data[insert_index:]

    with open(config_file_path, 'w') as f:
        f.writelines(config_data)

if __name__ == '__main__':
    config_file_path = 'compose.yaml'
    proxy_file_path = 'proxy.yaml'
    insert_proxy(config_file_path, proxy_file_path)

