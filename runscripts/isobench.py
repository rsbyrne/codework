import sys
workPath = '/home/jovyan/workspace'
if not workPath in sys.path:
    sys.path.append(workPath)

import planetengine
outDir = planetengine.paths.defaultPath

projName = 'arrbench'
projBranch = ''
outputPath = os.path.join(outDir, projName, projBranch)

import planetengine
import modelscripts

chunks = int(sys.argv[1])
chunkno = int(sys.argv[2])
iterno = int(sys.argv[3])

suitelist = planetengine.utilities.suite_list({
    'f': [0.2, 0.4, 0.6, 0.8, 1.],
    'eta': [1., 10., 100., 1000., 10000.],
    'Ra': [1e3, 1e4, 1e5, 1e6, 1e7],
    }, shuffle = True, chunks = chunks)

localJob = suitelist[chunkno][iterno]

planetengine.log(
    "Starting chunk no# " + str(chunkno) + ", iter no# " + str(iterno),
    'logs'
    )

for index, job in enumerate(localJobs):

    model = planetengine.frame.make_frame(
        modelscripts.isovisc.build(**job, res = 64),
        {'temperatureField': planetengine.initials.sinusoidal.IC(freq = 1.)},
        outputPath
        )

    conditions = {
        'stopCondition': lambda: model.modeltime() > 0.3,
        'checkpointCondition': lambda: any([
            model.status == 'pre-traverse',
            model.step() % 1000 == 0,
            model.status == 'post-traverse',
            ]),
        }

    model.traverse(**conditions)

planetengine.log(
    "Finishing chunk no# " + str(chunkno) + ", iter no# " + str(iterno),
    'logs'
    )
