#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), July 12, 2016, at 12:26
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding
#----

from psychopy import logging, core, visual

"""PsychoPy's log module is mostly a simple wrapper of the python logging module. 
It allows messages to be sent from any location (any library or your script) and 
written to files according to the importance level of the message and the minimum level
that the log file (or console) is set to receive. You can have multiple log files each receiving 
different levels of input.

The importance levels are;
    40:ERROR
    35:DATA
    30:WARNING
    25:DATA
    22: EXP
    20:INFO
    10:DEBUG
So setting to DEBUG level will include all possible messages, setting to ERROR will include only the absolutely essential messages.

"""

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'SoundTaskSimple'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.ERROR)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1680, 1050), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started

# try trigger here
calib_seq = [201, 251, 101, 151, 51, 1]
t_trig_st = globalClock.getTime()
for value in reversed(calib_seq):
    circle = visual.Circle(win, units='height', radius=0.05,
                           fillColorSpace='rgb255',
                           lineColorSpace='rgb255',
                           fillColor=(0, 0, 0), pos=(0.84, 0.44),
                           lineColor=(0, 0, 0))
    value = np.binary_repr(value)
    # zero pad to 8 bits and add stop and start bits
    value = '1' + (8 - len(value)) * '0' + value + '1'
    # draw bits
    for bit in value:
        if bit == '1':
            circle.fillColor = (255, 255, 255)
            circle.draw()
        if bit == '0':
            circle.fillColor = (0, 0, 0)
            circle.draw()
        win.flip(clearBuffer=False)
    # clear circle on both buffers
    circle.fillColor = (0, 0, 0)
    circle.draw()
    win.flip(clearBuffer=False)
    circle.draw()
t_trig_end = globalClock.getTime()
core.wait(1.0)
# end of trigger






# Initialize components for Routine "Image"
ImageClock = core.Clock()
image = visual.ImageStim(win=win, name='image',
    image=u'R.png', mask=None,
    ori=0, pos=[0, 0], size=[1.2, 1.2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "image_instr2"
image_instr2Clock = core.Clock()
image_2 = visual.ImageStim(win=win, name='image_2',
    image=u'R2.6.png', mask=None,
    ori=0, pos=[0, 0], size=[1.2, 1.2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "alignment"
alignmentClock = core.Clock()
sound_3 = sound.Sound(u'A', secs=-1)
sound_3.setVolume(1)

# Initialize components for Routine "wait"
waitClock = core.Clock()
sound_4 = sound.Sound(u'A', secs=-1)
sound_4.setVolume(0)

# Initialize components for Routine "Familiarization"
FamiliarizationClock = core.Clock()
sound_5 = sound.Sound('A', secs=-1)
sound_5.setVolume(1)
sound_6 = sound.Sound('A', secs=-1)
sound_6.setVolume(1)
image_6 = visual.ImageStim(win=win, name='image_6',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1.2, 1.2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "image_end1"
image_end1Clock = core.Clock()
image_3 = visual.ImageStim(win=win, name='image_3',
    image=u'R3.png', mask=None,
    ori=0, pos=[0, 0], size=[1.2, 1.2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "sound_task"
sound_taskClock = core.Clock()
sound_1 = sound.Sound('A', secs=-1)
sound_1.setVolume(1)
sound_2 = sound.Sound('A', secs=-1)
sound_2.setVolume(1)
image_5 = visual.ImageStim(win=win, name='image_5',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1.2, 1.2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "image_end_all"
image_end_allClock = core.Clock()
image_4 = visual.ImageStim(win=win, name='image_4',
    image=u'R4.png', mask=None,
    ori=0, pos=[0, 0], size=[1.2, 1.2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
# globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine #------Prepare to start Routine "Image"-------
t = 0
ImageClock.reset()  # clock 
frameN = -1

# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_10.status = NOT_STARTED
# keep track of which components have finished
ImageComponents = []
ImageComponents.append(image)
ImageComponents.append(key_resp_10)
for thisComponent in ImageComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Image"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = ImageClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if t >= 0.0 and image.status == NOT_STARTED:
        # keep track of start time/frame for later
        image.tStart = t  # underestimates by a little under one frame
        image.frameNStart = frameN  # exact frame index
        image.setAutoDraw(True)
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t  # underestimates by a little under one frame
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ImageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Image"-------
for thisComponent in ImageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        win.flip()
        win.flip()
# the Routine "Image" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "image_instr2"-------
t = 0
image_instr2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_11.status = NOT_STARTED
# keep track of which components have finished
image_instr2Components = []
image_instr2Components.append(image_2)
image_instr2Components.append(key_resp_11)
for thisComponent in image_instr2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "image_instr2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = image_instr2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if t >= 0.0 and image_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_2.tStart = t  # underestimates by a little under one frame
        image_2.frameNStart = frameN  # exact frame index
        image_2.setAutoDraw(True)
    
    # *key_resp_11* updates
    if t >= 0.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t  # underestimates by a little under one frame
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in image_instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "image_instr2"-------
for thisComponent in image_instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "image_instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "alignment"-------
t = 0
alignmentClock.reset()  # clock 
frameN = -1
routineTimer.add(0.200000)
# update component parameters for each repeat
# keep track of which components have finished
alignmentComponents = []
alignmentComponents.append(sound_3)
for thisComponent in alignmentComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "alignment"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = alignmentClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_3
    if t >= 0.0 and sound_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_3.tStart = t  # underestimates by a little under one frame
        t0 = globalClock.getTime()
        sound_3.frameNStart = frameN  # exact frame index
        sound_3.play()  # start the sound (it finishes automatically)
    if sound_3.status == STARTED and t >= (0.0 + (0.2-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_3.stop()  # stop the sound (if longer than duration)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in alignmentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "alignment"-------
for thisComponent in alignmentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_3.stop() #ensure sound has stopped at end of routine

#------Prepare to start Routine "wait"-------
t = 0
waitClock.reset()  # clock 
frameN = -1
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
waitComponents = []
waitComponents.append(sound_4)
for thisComponent in waitComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "wait"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = waitClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_4
    if t >= 0.0 and sound_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_4.tStart = t  # underestimates by a little under one frame
        sound_4.frameNStart = frameN  # exact frame index
        sound_4.play()  # start the sound (it finishes automatically)
    if sound_4.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        sound_4.stop()  # stop the sound (if longer than duration)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "wait"-------
for thisComponent in waitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_4.stop() #ensure sound has stopped at end of routine

# set up handler to look after randomisation of conditions etc
fam_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'Conditions_Familiariz_images.xlsx'),
    seed=None, name='fam_trials')
thisExp.addLoop(fam_trials)  # add the loop to the experiment
thisFam_trial = fam_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisFam_trial.rgb)
if thisFam_trial != None:
    for paramName in thisFam_trial.keys():
        exec(paramName + '= thisFam_trial.' + paramName)

for thisFam_trial in fam_trials:
    currentLoop = fam_trials
    # abbreviate parameter names if possible (e.g. rgb = thisFam_trial.rgb)
    if thisFam_trial != None:
        for paramName in thisFam_trial.keys():
            exec(paramName + '= thisFam_trial.' + paramName)
    
    #------Prepare to start Routine "Familiarization"-------
    t = 0
    FamiliarizationClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    sound_5.setSound(Sound_N, secs=-1)
    sound_6.setSound(Sound_W, secs=-1)
    image_6.setImage(question)
    key_resp_14 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_14.status = NOT_STARTED
    # keep track of which components have finished
    FamiliarizationComponents = []
    FamiliarizationComponents.append(sound_5)
    FamiliarizationComponents.append(sound_6)
    FamiliarizationComponents.append(image_6)
    FamiliarizationComponents.append(key_resp_14)
    for thisComponent in FamiliarizationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # try trigger here
    t_trig_st1 = globalClock.getTime()
    value = np.binary_repr(1)
    # zero pad to 8 bits and add stop and start bits
    value = '1' + (8 - len(value)) * '0' + value + '1'
    # draw bits
    for bit in value:
        if bit == '1':
            circle.fillColor = (255, 255, 255)
            circle.draw()
        if bit == '0':
            circle.fillColor = (0, 0, 0)
            circle.draw()
        win.flip(clearBuffer=False)
    # clear circle on both buffers
    circle.fillColor = (0, 0, 0)
    circle.draw()
    win.flip(clearBuffer=False)
    circle.draw()
    t_trig_end1 = globalClock.getTime()
    # end of trigger
    
    #-------Start Routine "Familiarization"-------
    continueRoutine = True
    while continueRoutine: 
        # get current time
        t = FamiliarizationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_5
        if t >= 0.5 and sound_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_5.tStart = t  # underestimates by a little under one frame
            t1 = globalClock.getTime()
            sound_5.frameNStart = frameN  # exact frame index
            sound_5.play()  # start the sound (it finishes automatically)
        # start/stop sound_6
        if t >= sound_5.getDuration() + 1 and sound_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_6.tStart = t  # underestimates by a little under one frame
            t2 = globalClock.getTime()
            sound_6.frameNStart = frameN  # exact frame index
            sound_6.play()  # start the sound (it finishes automatically)
        
        # *image_6* updates
        if t >= sound_5.getDuration() + 1 + sound_6.getDuration() and image_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            print 'if condition passed'
            image_6.tStart = t  # underestimates by a little under one frame
            image_6.frameNStart = frameN  # exact frame index
            image_6.setAutoDraw(True)
            print 'image 6 should be queued'
        
        # *key_resp_14* updates
        if sound_5.getDuration() + 1 + sound_6.getDuration() and key_resp_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_14.tStart = t  # underestimates by a little under one frame
            t3 = globalClock.getTime()
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_14.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_14.keys.extend(theseKeys)  # storing all keys
                key_resp_14.rt.append(key_resp_14.clock.getTime())
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FamiliarizationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Familiarization"-------
    for thisComponent in FamiliarizationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_5.stop() #ensure sound has stopped at end of routine
    sound_6.stop() #ensure sound has stopped at end of routine
    # check responses
    if key_resp_14.keys in ['', [], None]:  # No response was made
       key_resp_14.keys=None
    # store data for fam_trials (TrialHandler)
       fam_trials.addData('key_resp_14.keys',key_resp_14.keys)
    if key_resp_14.keys != None:  # we had a response
        dur1 = sound_5.getDuration()
        dur2 = sound_6.getDuration()
        fam_trials.addData('sound1_dur', dur1) # click.tStart
        fam_trials.addData('sound2_dur', dur2) # sound_1.tStart
        fam_trials.addData('Trig.tstart_session', t_trig_st) # trigger start
        fam_trials.addData('Trig.tend_session', t_trig_end) # trigger stop
        fam_trials.addData('Click.tStart', t0) # sound_1.tStart
        fam_trials.addData('Trig.tstart_trial', t_trig_st1) # trigger start
        fam_trials.addData('Trig.tend_trial', t_trig_end1) # trigger stop
        fam_trials.addData('sound_1.tStart', t1) # sound_1.tStart
        fam_trials.addData('sound_2.tStart', t2) # sound_2.tStart
        fam_trials.addData('response.tStart', t3) # response.tStart
        fam_trials.addData('response.rt', key_resp_14.rt)
        fam_trials.addData('task.id', 0)
# the Routine "Familiarization" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'fam_trials'


#------Prepare to start Routine "image_end1"-------
t = 0
image_end1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_12 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_12.status = NOT_STARTED
# keep track of which components have finished
image_end1Components = []
image_end1Components.append(image_3)
image_end1Components.append(key_resp_12)
for thisComponent in image_end1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "image_end1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = image_end1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if t >= 0.0 and image_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_3.tStart = t  # underestimates by a little under one frame
        image_3.frameNStart = frameN  # exact frame index
        image_3.setAutoDraw(True)
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t  # underestimates by a little under one frame
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in image_end1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "image_end1"-------
for thisComponent in image_end1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "image_end1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_b2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'Conditions_NumWord_all_images.csv'),
    seed=None, name='trials_b2')
thisExp.addLoop(trials_b2)  # add the loop to the experiment
thisTrials_b2 = trials_b2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrials_b2.rgb)
if thisTrials_b2 != None:
    for paramName in thisTrials_b2.keys():
        exec(paramName + '= thisTrials_b2.' + paramName)

for thisTrials_b2 in trials_b2:
    currentLoop = trials_b2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_b2.rgb)
    if thisTrials_b2 != None:
        for paramName in thisTrials_b2.keys():
            exec(paramName + '= thisTrials_b2.' + paramName)
    
    #------Prepare to start Routine "sound_task"-------
    t = 0
    sound_taskClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    sound_1.setSound(Sound_N, secs=-1)
    sound_2.setSound(Sound_W, secs=-1)
    image_5.setImage(question)
    key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_5.status = NOT_STARTED
    # keep track of which components have finished
    sound_taskComponents = []
    sound_taskComponents.append(sound_1)
    sound_taskComponents.append(sound_2)
    sound_taskComponents.append(image_5)
    sound_taskComponents.append(key_resp_5)
    for thisComponent in sound_taskComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # try trigger here
    t_trig_st1 = globalClock.getTime()
    value = np.binary_repr(1)
    # zero pad to 8 bits and add stop and start bits
    value = '1' + (8 - len(value)) * '0' + value + '1'
    # draw bits
    for bit in value:
        if bit == '1':
            circle.fillColor = (255, 255, 255)
            circle.draw()
        if bit == '0':
            circle.fillColor = (0, 0, 0)
            circle.draw()
        win.flip(clearBuffer=False)
    # clear circle on both buffers
    circle.fillColor = (0, 0, 0)
    circle.draw()
    win.flip(clearBuffer=False)
    circle.draw()
    t_trig_end1 = globalClock.getTime()
    # end of trigger
    
    
    #-------Start Routine "sound_task"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = sound_taskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if t >= 0.5 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            t11 = globalClock.getTime()
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        # start/stop sound_2
        if t >= sound_1.getDuration() + 1 and sound_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_2.tStart = t  # underestimates by a little under one frame
            t22 = globalClock.getTime()
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.play()  # start the sound (it finishes automatically)
        
        # *image_5* updates
        if t >= sound_1.getDuration() + 1 + sound_2.getDuration() and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t  # underestimates by a little under one frame
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        
        # *key_resp_5* updates
        if t >= sound_1.getDuration() + 1 + sound_2.getDuration()  and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t  # underestimates by a little under one frame
            t33 = globalClock.getTime()
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_5.keys.extend(theseKeys)  # storing all keys
                key_resp_5.rt.append(key_resp_5.clock.getTime())
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sound_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "sound_task"-------
    for thisComponent in sound_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop() #ensure sound has stopped at end of routine
    sound_2.stop() #ensure sound has stopped at end of routine
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
       key_resp_5.keys=None
    # store data for trials_b2 (TrialHandler)
       trials_b2.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        dur11 = sound_1.getDuration()
        dur22 = sound_2.getDuration()
        trials_b2.addData('sound1_dur', dur11) # click.tStart
        trials_b2.addData('sound2_dur', dur22) # sound_1.tStart
        trials_b2.addData('Click.tStart', t0) # click.tStart
        trials_b2.addData('Trig.tstart_trial', t_trig_st1) # trigger start
        trials_b2.addData('Trig.tend_trial', t_trig_end1) # trigger stop
        trials_b2.addData('sound_1.tStart', t11) # sound_1.tStart
        trials_b2.addData('sound_2.tStart', t22) # sound_2.tStart
        trials_b2.addData('response.tStart', t33) # response.tStart
        trials_b2.addData('response.rt', key_resp_5.rt)
        trials_b2.addData('task.id', 1)
    # the Routine "sound_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_b2'


#------Prepare to start Routine "image_end_all"-------
t = 0
image_end_allClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_13 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_13.status = NOT_STARTED
# keep track of which components have finished
image_end_allComponents = []
image_end_allComponents.append(image_4)
image_end_allComponents.append(key_resp_13)
for thisComponent in image_end_allComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "image_end_all"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = image_end_allClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if t >= 0.0 and image_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_4.tStart = t  # underestimates by a little under one frame
        image_4.frameNStart = frameN  # exact frame index
        image_4.setAutoDraw(True)
    
    # *key_resp_13* updates
    if t >= 0.0 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t  # underestimates by a little under one frame
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in image_end_allComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "image_end_all"-------
for thisComponent in image_end_allComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "image_end_all" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
