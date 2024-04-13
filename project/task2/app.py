import sys

def get_mean_size(ls_output: list) -> float:
    summ_file = 0
    count = 0
    for line in ls_output:
        count += 1
        summ_file += int(line.split()[4])
    return summ_file / count

if __name__ == '__main__':
    data = sys.stdin.readlines()[1:]
    if not data:
        print('Этот каталог пуст или к нему нет доступа.')
    else:
        mean_size: float = get_mean_size(data)
        print(f'Средний размер файлов в данной директории: {mean_size} байт.')
