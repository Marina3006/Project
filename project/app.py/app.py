import os

base_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(base_dir, 'output_file.txt')

def get_summary_rss(ps_output_file_path: str) -> str:
    with open(ps_output_file_path, 'r') as file:
        lines = file.readlines()[1:]
    summ_memory = 0
    for line in lines:
        columns = line.split()
        summ_memory += int(columns[5])

    thousand = 1024
    label = 0
    labels = {0: 'kilo', 1: 'mega', 2: 'giga', 3: 'tera'}

    while summ_memory > thousand:
        summ_memory /= thousand
        label += 1
    return f'Memory used {round(summ_memory,3)} {labels[label]}byte'

if __name__ == '__main__':
    path: str = output_file
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
