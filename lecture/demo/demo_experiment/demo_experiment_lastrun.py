#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.3),
    on October 23, 2024, at 13:56
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.3'
expName = 'demo_experiment'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'age': '18',
    'gender': ['male', 'female', 'non-binary', 'not listed / prefer not to say'],
    'dominant hand': ['right','left'],
    'first language': ['german', 'other'],
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1920, 1200]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\Jack\\Documents\\Misc Repositories\\expra-wise24\\lecture\\demo\\demo_experiment\\demo_experiment_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('intro_resp') is None:
        # initialise intro_resp
        intro_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='intro_resp',
        )
    if deviceManager.getDevice('feedback_prep_key_resp') is None:
        # initialise feedback_prep_key_resp
        feedback_prep_key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='feedback_prep_key_resp',
        )
    if deviceManager.getDevice('stim_resp') is None:
        # initialise stim_resp
        stim_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='stim_resp',
        )
    if deviceManager.getDevice('proper_trials_prep_resp') is None:
        # initialise proper_trials_prep_resp
        proper_trials_prep_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='proper_trials_prep_resp',
        )
    if deviceManager.getDevice('end_resp') is None:
        # initialise end_resp
        end_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='end_resp',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "intro" ---
    intro_welcome = visual.TextStim(win=win, name='intro_welcome',
        text='Welcome to the Demo Experiment!\n\nIn this experiment, you will be asked to identify words.\n\nFor each line of text that you see, press:\n- Right Alt Key if you see a real word\n- Left Alt Key if you do not see a real word\n\nWhen you are ready, press SPACE (Leertaste) to begin...',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    intro_resp = keyboard.Keyboard(deviceName='intro_resp')
    
    # --- Initialize components for Routine "feedback_prep" ---
    feedback_prep_text = visual.TextStim(win=win, name='feedback_prep_text',
        text='The first 10 trials will be practice trials, during which you will receive feedback.\n\nRemember:\n\nIf a Word: press Right Alt\nIf not a Word: press Left Alt\n\nPress SPACE to begin the practice trials...',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    feedback_prep_key_resp = keyboard.Keyboard(deviceName='feedback_prep_key_resp')
    
    # --- Initialize components for Routine "trial" ---
    fix = visual.TextStim(win=win, name='fix',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    stimulus = visual.TextStim(win=win, name='stimulus',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    stim_resp = keyboard.Keyboard(deviceName='stim_resp')
    
    # --- Initialize components for Routine "feedback" ---
    
    # --- Initialize components for Routine "proper_trials_prep" ---
    proper_trials_prep_text = visual.TextStim(win=win, name='proper_trials_prep_text',
        text='From now on, you will not get any feedback on your responses.\n\nGood luck!\n\nHere is a reminder of the task instructions:\nIf a Word: press Right Alt\nIf not a Word: press Left Alt\n\nPress SPACE to begin...',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    proper_trials_prep_resp = keyboard.Keyboard(deviceName='proper_trials_prep_resp')
    
    # --- Initialize components for Routine "trial" ---
    fix = visual.TextStim(win=win, name='fix',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    stimulus = visual.TextStim(win=win, name='stimulus',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    stim_resp = keyboard.Keyboard(deviceName='stim_resp')
    
    # --- Initialize components for Routine "store_resp_and_break" ---
    # Run 'Begin Experiment' code from break_code
    break_every = 50
    rt_list = []
    acc_list = []
    
    
    # --- Initialize components for Routine "end" ---
    end_text = visual.TextStim(win=win, name='end_text',
        text='Thank you for taking part!\n\nNow please follow the instructions on the\nExPra website to upload your data.\n\nWhen you are ready, please press SPACE to exit...',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    end_resp = keyboard.Keyboard(deviceName='end_resp')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "intro" ---
    # create an object to store info about Routine intro
    intro = data.Routine(
        name='intro',
        components=[intro_welcome, intro_resp],
    )
    intro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for intro_resp
    intro_resp.keys = []
    intro_resp.rt = []
    _intro_resp_allKeys = []
    # store start times for intro
    intro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    intro.tStart = globalClock.getTime(format='float')
    intro.status = STARTED
    thisExp.addData('intro.started', intro.tStart)
    intro.maxDuration = None
    # keep track of which components have finished
    introComponents = intro.components
    for thisComponent in intro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "intro" ---
    intro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intro_welcome* updates
        
        # if intro_welcome is starting this frame...
        if intro_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro_welcome.frameNStart = frameN  # exact frame index
            intro_welcome.tStart = t  # local t and not account for scr refresh
            intro_welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro_welcome, 'tStartRefresh')  # time at next scr refresh
            # update status
            intro_welcome.status = STARTED
            intro_welcome.setAutoDraw(True)
        
        # if intro_welcome is active this frame...
        if intro_welcome.status == STARTED:
            # update params
            pass
        
        # *intro_resp* updates
        waitOnFlip = False
        
        # if intro_resp is starting this frame...
        if intro_resp.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            intro_resp.frameNStart = frameN  # exact frame index
            intro_resp.tStart = t  # local t and not account for scr refresh
            intro_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'intro_resp.started')
            # update status
            intro_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(intro_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(intro_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if intro_resp.status == STARTED and not waitOnFlip:
            theseKeys = intro_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _intro_resp_allKeys.extend(theseKeys)
            if len(_intro_resp_allKeys):
                intro_resp.keys = _intro_resp_allKeys[-1].name  # just the last key pressed
                intro_resp.rt = _intro_resp_allKeys[-1].rt
                intro_resp.duration = _intro_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            intro.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "intro" ---
    for thisComponent in intro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for intro
    intro.tStop = globalClock.getTime(format='float')
    intro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('intro.stopped', intro.tStop)
    thisExp.nextEntry()
    # the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback_prep" ---
    # create an object to store info about Routine feedback_prep
    feedback_prep = data.Routine(
        name='feedback_prep',
        components=[feedback_prep_text, feedback_prep_key_resp],
    )
    feedback_prep.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for feedback_prep_key_resp
    feedback_prep_key_resp.keys = []
    feedback_prep_key_resp.rt = []
    _feedback_prep_key_resp_allKeys = []
    # store start times for feedback_prep
    feedback_prep.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    feedback_prep.tStart = globalClock.getTime(format='float')
    feedback_prep.status = STARTED
    thisExp.addData('feedback_prep.started', feedback_prep.tStart)
    feedback_prep.maxDuration = None
    # keep track of which components have finished
    feedback_prepComponents = feedback_prep.components
    for thisComponent in feedback_prep.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback_prep" ---
    feedback_prep.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_prep_text* updates
        
        # if feedback_prep_text is starting this frame...
        if feedback_prep_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_prep_text.frameNStart = frameN  # exact frame index
            feedback_prep_text.tStart = t  # local t and not account for scr refresh
            feedback_prep_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_prep_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_prep_text.started')
            # update status
            feedback_prep_text.status = STARTED
            feedback_prep_text.setAutoDraw(True)
        
        # if feedback_prep_text is active this frame...
        if feedback_prep_text.status == STARTED:
            # update params
            pass
        
        # *feedback_prep_key_resp* updates
        waitOnFlip = False
        
        # if feedback_prep_key_resp is starting this frame...
        if feedback_prep_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_prep_key_resp.frameNStart = frameN  # exact frame index
            feedback_prep_key_resp.tStart = t  # local t and not account for scr refresh
            feedback_prep_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_prep_key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_prep_key_resp.started')
            # update status
            feedback_prep_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(feedback_prep_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(feedback_prep_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if feedback_prep_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = feedback_prep_key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _feedback_prep_key_resp_allKeys.extend(theseKeys)
            if len(_feedback_prep_key_resp_allKeys):
                feedback_prep_key_resp.keys = _feedback_prep_key_resp_allKeys[-1].name  # just the last key pressed
                feedback_prep_key_resp.rt = _feedback_prep_key_resp_allKeys[-1].rt
                feedback_prep_key_resp.duration = _feedback_prep_key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            feedback_prep.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedback_prep.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback_prep" ---
    for thisComponent in feedback_prep.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for feedback_prep
    feedback_prep.tStop = globalClock.getTime(format='float')
    feedback_prep.tStopRefresh = tThisFlipGlobal
    thisExp.addData('feedback_prep.stopped', feedback_prep.tStop)
    thisExp.nextEntry()
    # the Routine "feedback_prep" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_trials = data.TrialHandler2(
        name='practice_trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('stimuli/practice_stim_long.csv'), 
        seed=None, 
    )
    thisExp.addLoop(practice_trials)  # add the loop to the experiment
    thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            globals()[paramName] = thisPractice_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPractice_trial in practice_trials:
        currentLoop = practice_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
        if thisPractice_trial != None:
            for paramName in thisPractice_trial:
                globals()[paramName] = thisPractice_trial[paramName]
        
        # --- Prepare to start Routine "trial" ---
        # create an object to store info about Routine trial
        trial = data.Routine(
            name='trial',
            components=[fix, stimulus, stim_resp],
        )
        trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        stimulus.setText(text)
        # create starting attributes for stim_resp
        stim_resp.keys = []
        stim_resp.rt = []
        _stim_resp_allKeys = []
        # store start times for trial
        trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial.tStart = globalClock.getTime(format='float')
        trial.status = STARTED
        thisExp.addData('trial.started', trial.tStart)
        trial.maxDuration = None
        # keep track of which components have finished
        trialComponents = trial.components
        for thisComponent in trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        # if trial has changed, end Routine now
        if isinstance(practice_trials, data.TrialHandler2) and thisPractice_trial.thisN != practice_trials.thisTrial.thisN:
            continueRoutine = False
        trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix* updates
            
            # if fix is starting this frame...
            if fix.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                fix.frameNStart = frameN  # exact frame index
                fix.tStart = t  # local t and not account for scr refresh
                fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix.started')
                # update status
                fix.status = STARTED
                fix.setAutoDraw(True)
            
            # if fix is active this frame...
            if fix.status == STARTED:
                # update params
                pass
            
            # if fix is stopping this frame...
            if fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix.tStop = t  # not accounting for scr refresh
                    fix.tStopRefresh = tThisFlipGlobal  # on global time
                    fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix.stopped')
                    # update status
                    fix.status = FINISHED
                    fix.setAutoDraw(False)
            
            # *stimulus* updates
            
            # if stimulus is starting this frame...
            if stimulus.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                stimulus.frameNStart = frameN  # exact frame index
                stimulus.tStart = t  # local t and not account for scr refresh
                stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus.started')
                # update status
                stimulus.status = STARTED
                stimulus.setAutoDraw(True)
            
            # if stimulus is active this frame...
            if stimulus.status == STARTED:
                # update params
                pass
            
            # *stim_resp* updates
            waitOnFlip = False
            
            # if stim_resp is starting this frame...
            if stim_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                stim_resp.frameNStart = frameN  # exact frame index
                stim_resp.tStart = t  # local t and not account for scr refresh
                stim_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim_resp.started')
                # update status
                stim_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(stim_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(stim_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if stim_resp.status == STARTED and not waitOnFlip:
                theseKeys = stim_resp.getKeys(keyList=['lalt', 'ralt'], ignoreKeys=["escape"], waitRelease=False)
                _stim_resp_allKeys.extend(theseKeys)
                if len(_stim_resp_allKeys):
                    stim_resp.keys = _stim_resp_allKeys[0].name  # just the first key pressed
                    stim_resp.rt = _stim_resp_allKeys[0].rt
                    stim_resp.duration = _stim_resp_allKeys[0].duration
                    # was this correct?
                    if (stim_resp.keys == str(corr_ans)) or (stim_resp.keys == corr_ans):
                        stim_resp.corr = 1
                    else:
                        stim_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial
        trial.tStop = globalClock.getTime(format='float')
        trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial.stopped', trial.tStop)
        # check responses
        if stim_resp.keys in ['', [], None]:  # No response was made
            stim_resp.keys = None
            # was no response the correct answer?!
            if str(corr_ans).lower() == 'none':
               stim_resp.corr = 1;  # correct non-response
            else:
               stim_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for practice_trials (TrialHandler)
        practice_trials.addData('stim_resp.keys',stim_resp.keys)
        practice_trials.addData('stim_resp.corr', stim_resp.corr)
        if stim_resp.keys != None:  # we had a response
            practice_trials.addData('stim_resp.rt', stim_resp.rt)
            practice_trials.addData('stim_resp.duration', stim_resp.duration)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        # create an object to store info about Routine feedback
        feedback = data.Routine(
            name='feedback',
            components=[],
        )
        feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        if stim_resp.corr==1:
            feedback_text = visual.TextStim(win=win, height=0.05, units='height', text=f'Correct!', color='chartreuse')
        else:
            feedback_text = visual.TextStim(win=win, height=0.05, units='height', text=f'Incorrect!', color='red')
        
        win.flip()
        feedback_text.draw()
        win.flip()
        core.wait(0.5)
        
        # store start times for feedback
        feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback.tStart = globalClock.getTime(format='float')
        feedback.status = STARTED
        thisExp.addData('feedback.started', feedback.tStart)
        feedback.maxDuration = None
        # keep track of which components have finished
        feedbackComponents = feedback.components
        for thisComponent in feedback.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback" ---
        # if trial has changed, end Routine now
        if isinstance(practice_trials, data.TrialHandler2) and thisPractice_trial.thisN != practice_trials.thisTrial.thisN:
            continueRoutine = False
        feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback
        feedback.tStop = globalClock.getTime(format='float')
        feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback.stopped', feedback.tStop)
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practice_trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "proper_trials_prep" ---
    # create an object to store info about Routine proper_trials_prep
    proper_trials_prep = data.Routine(
        name='proper_trials_prep',
        components=[proper_trials_prep_text, proper_trials_prep_resp],
    )
    proper_trials_prep.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for proper_trials_prep_resp
    proper_trials_prep_resp.keys = []
    proper_trials_prep_resp.rt = []
    _proper_trials_prep_resp_allKeys = []
    # store start times for proper_trials_prep
    proper_trials_prep.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    proper_trials_prep.tStart = globalClock.getTime(format='float')
    proper_trials_prep.status = STARTED
    thisExp.addData('proper_trials_prep.started', proper_trials_prep.tStart)
    proper_trials_prep.maxDuration = None
    # keep track of which components have finished
    proper_trials_prepComponents = proper_trials_prep.components
    for thisComponent in proper_trials_prep.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "proper_trials_prep" ---
    proper_trials_prep.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *proper_trials_prep_text* updates
        
        # if proper_trials_prep_text is starting this frame...
        if proper_trials_prep_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            proper_trials_prep_text.frameNStart = frameN  # exact frame index
            proper_trials_prep_text.tStart = t  # local t and not account for scr refresh
            proper_trials_prep_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(proper_trials_prep_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'proper_trials_prep_text.started')
            # update status
            proper_trials_prep_text.status = STARTED
            proper_trials_prep_text.setAutoDraw(True)
        
        # if proper_trials_prep_text is active this frame...
        if proper_trials_prep_text.status == STARTED:
            # update params
            pass
        
        # *proper_trials_prep_resp* updates
        waitOnFlip = False
        
        # if proper_trials_prep_resp is starting this frame...
        if proper_trials_prep_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            proper_trials_prep_resp.frameNStart = frameN  # exact frame index
            proper_trials_prep_resp.tStart = t  # local t and not account for scr refresh
            proper_trials_prep_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(proper_trials_prep_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'proper_trials_prep_resp.started')
            # update status
            proper_trials_prep_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(proper_trials_prep_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(proper_trials_prep_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if proper_trials_prep_resp.status == STARTED and not waitOnFlip:
            theseKeys = proper_trials_prep_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _proper_trials_prep_resp_allKeys.extend(theseKeys)
            if len(_proper_trials_prep_resp_allKeys):
                proper_trials_prep_resp.keys = _proper_trials_prep_resp_allKeys[-1].name  # just the last key pressed
                proper_trials_prep_resp.rt = _proper_trials_prep_resp_allKeys[-1].rt
                proper_trials_prep_resp.duration = _proper_trials_prep_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            proper_trials_prep.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in proper_trials_prep.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "proper_trials_prep" ---
    for thisComponent in proper_trials_prep.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for proper_trials_prep
    proper_trials_prep.tStop = globalClock.getTime(format='float')
    proper_trials_prep.tStopRefresh = tThisFlipGlobal
    thisExp.addData('proper_trials_prep.stopped', proper_trials_prep.tStop)
    thisExp.nextEntry()
    # the Routine "proper_trials_prep" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('stimuli/stim_long.csv'), 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "trial" ---
        # create an object to store info about Routine trial
        trial = data.Routine(
            name='trial',
            components=[fix, stimulus, stim_resp],
        )
        trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        stimulus.setText(text)
        # create starting attributes for stim_resp
        stim_resp.keys = []
        stim_resp.rt = []
        _stim_resp_allKeys = []
        # store start times for trial
        trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial.tStart = globalClock.getTime(format='float')
        trial.status = STARTED
        thisExp.addData('trial.started', trial.tStart)
        trial.maxDuration = None
        # keep track of which components have finished
        trialComponents = trial.components
        for thisComponent in trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix* updates
            
            # if fix is starting this frame...
            if fix.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                fix.frameNStart = frameN  # exact frame index
                fix.tStart = t  # local t and not account for scr refresh
                fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix.started')
                # update status
                fix.status = STARTED
                fix.setAutoDraw(True)
            
            # if fix is active this frame...
            if fix.status == STARTED:
                # update params
                pass
            
            # if fix is stopping this frame...
            if fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix.tStop = t  # not accounting for scr refresh
                    fix.tStopRefresh = tThisFlipGlobal  # on global time
                    fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix.stopped')
                    # update status
                    fix.status = FINISHED
                    fix.setAutoDraw(False)
            
            # *stimulus* updates
            
            # if stimulus is starting this frame...
            if stimulus.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                stimulus.frameNStart = frameN  # exact frame index
                stimulus.tStart = t  # local t and not account for scr refresh
                stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus.started')
                # update status
                stimulus.status = STARTED
                stimulus.setAutoDraw(True)
            
            # if stimulus is active this frame...
            if stimulus.status == STARTED:
                # update params
                pass
            
            # *stim_resp* updates
            waitOnFlip = False
            
            # if stim_resp is starting this frame...
            if stim_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                stim_resp.frameNStart = frameN  # exact frame index
                stim_resp.tStart = t  # local t and not account for scr refresh
                stim_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim_resp.started')
                # update status
                stim_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(stim_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(stim_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if stim_resp.status == STARTED and not waitOnFlip:
                theseKeys = stim_resp.getKeys(keyList=['lalt', 'ralt'], ignoreKeys=["escape"], waitRelease=False)
                _stim_resp_allKeys.extend(theseKeys)
                if len(_stim_resp_allKeys):
                    stim_resp.keys = _stim_resp_allKeys[0].name  # just the first key pressed
                    stim_resp.rt = _stim_resp_allKeys[0].rt
                    stim_resp.duration = _stim_resp_allKeys[0].duration
                    # was this correct?
                    if (stim_resp.keys == str(corr_ans)) or (stim_resp.keys == corr_ans):
                        stim_resp.corr = 1
                    else:
                        stim_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial
        trial.tStop = globalClock.getTime(format='float')
        trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial.stopped', trial.tStop)
        # check responses
        if stim_resp.keys in ['', [], None]:  # No response was made
            stim_resp.keys = None
            # was no response the correct answer?!
            if str(corr_ans).lower() == 'none':
               stim_resp.corr = 1;  # correct non-response
            else:
               stim_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('stim_resp.keys',stim_resp.keys)
        trials.addData('stim_resp.corr', stim_resp.corr)
        if stim_resp.keys != None:  # we had a response
            trials.addData('stim_resp.rt', stim_resp.rt)
            trials.addData('stim_resp.duration', stim_resp.duration)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "store_resp_and_break" ---
        # create an object to store info about Routine store_resp_and_break
        store_resp_and_break = data.Routine(
            name='store_resp_and_break',
            components=[],
        )
        store_resp_and_break.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from break_code
        rt_list.append(stim_resp.rt)
        acc_list.append(stim_resp.corr)
        
        if trials.thisN % break_every == 0 and trials.thisN < len(trials.trialList) and trials.thisN > 0:
            print('STARTING BREAK')
            break_progress = f'You have completed {trials.thisN} / {len(trials.trialList)} trials - great job!'
            #median_rt = int(np.round(np.median(rt_list)*1000))
            #perc_corr = int(np.round(np.mean(acc_list)*100))
            #performance_summ = f'Your median response time in the last {break_every} trials: {median_rt} ms\nYour accuracy in the last {break_every} trials: {perc_corr}%'
            performance_summ = ''
            break_text = visual.TextStim(win=win, height=0.05, units='height', text=f'{break_progress}\n\n{performance_summ}\n\nPlease take a short break...\n\nWhen you are ready to continue, press SPACE')
            win.flip()
            break_text.draw()
            win.flip()
            core.wait(2)
            event.waitKeys(keyList=['space'])
            rt_list = []
            acc_list = []
            print('BREAK ENDED')
        # store start times for store_resp_and_break
        store_resp_and_break.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        store_resp_and_break.tStart = globalClock.getTime(format='float')
        store_resp_and_break.status = STARTED
        thisExp.addData('store_resp_and_break.started', store_resp_and_break.tStart)
        store_resp_and_break.maxDuration = None
        # keep track of which components have finished
        store_resp_and_breakComponents = store_resp_and_break.components
        for thisComponent in store_resp_and_break.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "store_resp_and_break" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        store_resp_and_break.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                store_resp_and_break.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in store_resp_and_break.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "store_resp_and_break" ---
        for thisComponent in store_resp_and_break.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for store_resp_and_break
        store_resp_and_break.tStop = globalClock.getTime(format='float')
        store_resp_and_break.tStopRefresh = tThisFlipGlobal
        thisExp.addData('store_resp_and_break.stopped', store_resp_and_break.tStop)
        # the Routine "store_resp_and_break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end" ---
    # create an object to store info about Routine end
    end = data.Routine(
        name='end',
        components=[end_text, end_resp],
    )
    end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for end_resp
    end_resp.keys = []
    end_resp.rt = []
    _end_resp_allKeys = []
    # store start times for end
    end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end.tStart = globalClock.getTime(format='float')
    end.status = STARTED
    thisExp.addData('end.started', end.tStart)
    end.maxDuration = None
    # keep track of which components have finished
    endComponents = end.components
    for thisComponent in end.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_text* updates
        
        # if end_text is starting this frame...
        if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_text.frameNStart = frameN  # exact frame index
            end_text.tStart = t  # local t and not account for scr refresh
            end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            end_text.status = STARTED
            end_text.setAutoDraw(True)
        
        # if end_text is active this frame...
        if end_text.status == STARTED:
            # update params
            pass
        
        # *end_resp* updates
        
        # if end_resp is starting this frame...
        if end_resp.status == NOT_STARTED and t >= 2-frameTolerance:
            # keep track of start time/frame for later
            end_resp.frameNStart = frameN  # exact frame index
            end_resp.tStart = t  # local t and not account for scr refresh
            end_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            end_resp.status = STARTED
            # keyboard checking is just starting
            end_resp.clock.reset()  # now t=0
            end_resp.clearEvents(eventType='keyboard')
        if end_resp.status == STARTED:
            theseKeys = end_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _end_resp_allKeys.extend(theseKeys)
            if len(_end_resp_allKeys):
                end_resp.keys = _end_resp_allKeys[-1].name  # just the last key pressed
                end_resp.rt = _end_resp_allKeys[-1].rt
                end_resp.duration = _end_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in end.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end
    end.tStop = globalClock.getTime(format='float')
    end.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end.stopped', end.tStop)
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
