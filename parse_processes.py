"""
homework for OS
"""

import sys
from datetime import datetime
import shutil
from subprocess import run, PIPE

def parse_processes():
    res = run(['ps', 'aux'], stdout=PIPE)
    procs = res.stdout.decode().split('\n')
    titles = procs[0].split()
    agg_res = {}
    total_used_memory = 0
    total_used_cpu = 0
    max_memory = -1
    max_cpu = -1
    max_memory_process = ''
    max_cpu_process = ''

    for process in procs[1:-1]:
        columns = process.split()
        p_user = columns[titles.index('USER')]
        p_cpu = float(columns[titles.index('%CPU')])
        p_memory = float(columns[titles.index('%MEM')])
        p_command =  columns[titles.index('COMMAND')][:20]
        agg_res[p_user] = agg_res.get(p_user, 0) + 1
        total_used_memory += p_memory
        total_used_cpu += p_cpu
        if p_memory > max_memory:
            max_memory = p_memory
            max_memory_process = p_command
        if p_cpu > max_cpu:
            max_cpu = p_cpu
            max_cpu_process = p_command

    filename = datetime.now().strftime("%d-%m-%Y-%H:%M-scan.txt")
    with open(filename, "w") as f:
        f.write('Отчёт о состоянии системы: \n')
        f.write(f'Пользователи системы:  {", ".join(agg_res.keys())}\n')
        f.write(f'Процессов запущено: {sum(agg_res.values())}\n')
        f.write('Пользовательских процессов:\n')
        for key, value in agg_res.items():
            f.write(f'    {key}: {value}\n')
        f.write(f'Всего памяти используется: {round(total_used_memory, 1)}%\n')
        f.write(f'Всего CPU используется: {round(total_used_cpu, 1)}%\n')
        f.write(f'Больше всего памяти использует: {max_memory}% - {max_memory_process}\n' )
        f.write(f'Больше всего CPU использует: {max_cpu}% - {max_cpu_process}\n' )

    with open(filename, "r") as f:
        shutil.copyfileobj(f, sys.stdout)


parse_processes()
