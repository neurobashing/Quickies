#!/usr/bin/env python

from numpy import array,append
import subprocess

def print_html_descriptions(tasks):
    for t in tasks:
        if 'depends' not in t:
            if 'tags' not in t:
                print("    <li>%s</li>" % t['description'])
            else:
                print("    <li>%s (%s)</li>" % (t['description'], t['tags']))

def main(tasklines):
    tasks = array([])
    lines = tasklines.splitlines()
    for line in lines:
        # pack columns into array
        lin = eval(line)
        tasks = append(tasks, lin)

    print("  <ol>")
    print_html_descriptions(tasks)
    print("  </ol>")

if __name__ == '__main__':
    lines = subprocess.check_output(["task", "_query", "status:pending"])
    main(lines)
