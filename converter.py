import pandas as pd
import datetime

def parse_log_to_csv():
    with open("stats.log") as f:
        cpu_stats = []
        for line in f:
            timestamp = datetime.datetime.strptime(line[1:line.find("]")], "%Y-%m-%d %H:%M:%S")
            line = line[line.find("]")+2:]
            if line[:8] == "%Cpu(s):":
                line = line[8+1:]
                line_cpu_stats = list(map(str.strip, line.split(",")))
                line_cpu_stats = list(map(lambda x: x[:-3], line_cpu_stats))
                line_cpu_stats = list(map(float, line_cpu_stats))
                cpu_stats.append([timestamp, *line_cpu_stats])

        df = pd.DataFrame(cpu_stats, columns=["timestamp", "usage", "kernel", "nice", "idle", "io", "hardware_interrupts", "software_interrupts", "steal_time"])

    df.to_csv("stats.csv", index=False)