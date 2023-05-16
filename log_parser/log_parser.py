"""
    Web-application log parser
"""
import argparse
import re
import json
from os.path import isfile, join
from os import listdir

def get_duration(rec):
    return rec.get('duration')

def parse_log_file(file):
    res = {}
    with open(file) as f:
        rows = 0
        top_3 = []
        ip_list = {}
        total_stat = {}
        for line in f:
            ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            if ip_match is not None:
                ip = ip_match.group()
                method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE|PATCH)", line)
                if method is not None:
                    cdate = re.search('\[(.+?)\]', line).group()
                    referrer = re.search('\"http(.+?)\"', line)
                    if referrer is not None:
                        referrer = referrer.group()[1:-1]
                    else:
                        referrer = '-'
                    duration = int(line.split()[-1])
                    rows += 1
                    total_stat[method.group(1)] = total_stat.get(method.group(1), 0) + 1
                    ip_list[ip] = ip_list.get(ip, 0) + 1
                    cur_rec = {}
                    cur_rec['ip'] = ip
                    cur_rec['date'] = cdate
                    cur_rec['method'] = method.group(1)
                    cur_rec['url'] = referrer
                    cur_rec['duration'] = duration
                    top_3.append(cur_rec)
                    top_3.sort(key=get_duration, reverse=True)
                    top_3 = top_3[:3]
        most_ips = sorted(ip_list, key=ip_list.get, reverse=True)[:3]
        top_ips = {}
        for ip in most_ips:
            top_ips[ip] = ip_list[ip]
        res['top_ips'] = top_ips
        res['top_longest'] = top_3
        res['total_stat'] = total_stat
        res['total_requests'] = rows
    return res

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process access.log')
    # https://docs.python.org/3/library/argparse.html
    # https://docs.python.org/3/library/argparse.html#the-add-argument-method
    parser.add_argument('target', type=str, help='log file or directory with log files')
    args = parser.parse_args()
    log_files = []
    if isfile(args.target):
        log_files.append(args.target)
    else:
        log_files = [join(args.target, f) for f in listdir(args.target) if isfile(join(args.target, f))]
    for file in log_files:
        res_json = json.dumps(parse_log_file(file), indent=4)
        print(res_json)
        out_filename = file + '.json'
        with open(out_filename, "w") as f:
            f.write(res_json)
