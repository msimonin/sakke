"""qs: utilitaire de statistiques de devoirs

usage: qs <exercice:bareme> ...

Options:
  -h --help      Show this help message.
  exercice:bareme path the the exercice/bareme separated by :
"""
import csv
import sys
# import statistics (requires >= 3.4)
import numpy
import os
import json
from docopt import docopt
from jinja2 import Environment, FileSystemLoader

NOTE=20
QS_PATH = os.path.dirname(os.path.realpath(__file__))
TEMPLATES_DIR = os.path.join(QS_PATH, 'templates')

def clean(l):
    def el_clean(e):
        # replace hypothetic ',' by ','
        # e.g export from calc with french number formatting
        ec = e.replace(',', '.')
        return float(ec)

    return list(map(el_clean, l))

def main(exercices_baremes):
    if len(exercices_baremes) < 1:
        sys.exit(0)

    files = {}
    for exercice_bareme in exercices_baremes:
        exo, bareme = exercice_bareme.split(':')
        files[exo] = bareme
# grouping by student
    students = {}
# students = {
#   s1 : {
#      note: # note
#      sum: # sum
#      exercice1 : {
#         raw : [] # raw results
#         sum :    # the sum according the 
#         
#      }
#      exercice2 : [],
#   } 
# }
    bar = {}
# bareme = {
#     'title': [] # titles of the questions
#     'points': [] # corresponding points
# }
#
#
    general = {
        'total': 0}
    for exo, bareme in files.items():
        with open(bareme) as baremefile:
            # bareme should only contains two lines
            reader = list(csv.reader(baremefile, delimiter=','))
            bar.setdefault(exo, {})
            bar[exo]['title'] = reader[0]
            bar[exo]['points'] = clean(reader[1])
            bar[exo]['total'] = sum(bar[exo]['points'])
            # filling the general
            general['total'] = general['total'] + bar[exo]['total']
            # max_questions
            general.setdefault('max_questions', len(reader[0]))
            if general['max_questions'] < len(reader[0]):
                general['max_questions'] = len(reader[0])
        with open(exo) as exofile:
            reader = csv.reader(exofile, delimiter=',')
            exoname = os.path.basename(exo).split('.')[0].replace('_', '-')
            for row in reader:
                name = ' '.join(row[0:2]).decode('UTF-8')
                students.setdefault(name, {})
                students[name].setdefault('exercices', {})
                students[name]['name'] = name
                raw = clean(row[2:])
                corrected = raw[0:]
                # set raw results
                students[name]['exercices'].setdefault(exoname, {})
                students[name]['exercices'][exoname].setdefault('raw', raw)
                # compute corrected result 
                for i in range(len(bar[exo]['title'])):
                    corrected[i] = raw[i] * bar[exo]['points'][i] / 4
                students[name]['exercices'][exoname].setdefault('corrected', corrected)
                # compute the sum
                s = sum(corrected)    
                students[name]['exercices'][exoname].setdefault('sum', s)
                # compute the note
                note = s/bar[exo]['total'] * NOTE
                students[name]['exercices'][exoname].setdefault('note', note)
                # repeating the bareme
                students[name]['exercices'][exoname].setdefault('bar', bar[exo])
                # filling student general  
                students[name].setdefault('sum', 0)
                students[name]['sum'] = s + students[name]['sum']
                students[name].setdefault('note', 0)
                students[name]['note'] = round(students[name]['sum']/general['total']*NOTE, 1)
                students[name]['total'] = general['total']
    
    general['raw'] = numpy.array(list(map(lambda e: e['note'], students.values())))
    general['avg'] = round(numpy.mean(general['raw']), 1)
    general['std'] = round(numpy.std(general['raw']), 1)

    env = Environment(loader=FileSystemLoader(searchpath=TEMPLATES_DIR))
    template = env.get_template('stats.tex.j2')
    rendered_text = template.render(students=students.values(), general=general, bar=bar)

    with open('out.tex', 'w') as f:
        f.write(rendered_text.encode('UTF-8'))

    
if __name__ == '__main__':
    arguments = docopt(__doc__, version=0.1)
    main(arguments['<exercice:bareme>'])
