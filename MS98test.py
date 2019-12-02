import os

import planetengine

frameID = 'MS98test'
outputPath = 'out/test'

#if planetengine.mpi.rank == 0:
#    os.makedirs(outputPath)

system = planetengine.systems.MS98.build(
    res = 32,
    dither = 6
    )
observer = planetengine.observers.observeMS98.build(
    system,
    buoyancyKey = 'temperature'
    )

system.anchor(frameID, outputPath)
system.coanchor(observer)

#system.store()
#observer.store()
#for i in range(1000):
#    system.iterate()
#    if not i % 3:
#        observer.store()
#    if not i % 13:
#        system.store()
#    if not i % 100:
#        system.save()
#        observer.save()

with observer.file() as file:
    imgArrs = file[observer.hashID]['raster']
    for index, imgArr in enumerate(imgArrs):
        split_imgArr = planetengine.visualisation.raster.split_imgArr(imgArr)
        img = planetengine.visualisation.raster.rasterise(*split_imgArr)
        saveName = os.path.join(outputPath, str(index).zfill(3) + '.png')
        if planetengine.mpi.rank == 0:
            img.save(saveName)
