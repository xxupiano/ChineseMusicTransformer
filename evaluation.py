from music21 import *
import numpy as np

# the average number of used pitch classes per bar
def ANPC_bar(filename):
    midiParse = converter.parse(filename)
    midiParse.makeMeasures(inPlace=True)
    mses = midiParse.recurse().getElementsByClass(stream.Measure)
    npcbar = []
    for ms in mses:
        eles = ms.recurse().getElementsByClass([note.Note, chord.Chord])
        pitchSet = set()
        for el in eles:
            if type(el)==note.Note:
                pitchSet.add(el.pitch.name)
            else:
                pits = el.pitches
                for p in pits:
                    pitchSet.add(p.name)
        npcbar.append(len(pitchSet))
    return np.mean(npcbar)

# the number of used pitch classes
def NPC(filename):
    midiParse = converter.parse(filename)
    noteAndChord = midiParse.recurse().getElementsByClass([note.Note, chord.Chord])
    pitchSet = set()
    for el in noteAndChord:
        if type(el)==note.Note:
            pitchSet.add(el.pitch.name)
        else:
            pits = el.pitches
            for p in pits:
                pitchSet.add(p.name)
    return len(pitchSet)

# the number of pitches
def NP(filename):
    midiParse = converter.parse(filename)
    noteAndChord = midiParse.recurse().getElementsByClass([note.Note, chord.Chord])
    pitchesList = []
    for el in noteAndChord:
        if type(el)==note.Note:
            pitchesList.append(el.pitch.midi)
        else:
            pits = el.pitches
            for p in pits:
                pitchesList.append(p.midi)
    return len(pitchesList)

# the pitch range from the highest pitch to lowest one
def PR(filename):
    midiParse = converter.parse(filename)
    noteAndChord = midiParse.recurse().getElementsByClass([note.Note, chord.Chord])
    pitchesList = []
    for el in noteAndChord:
        if type(el)==note.Note:
            pitchesList.append(el.pitch.midi)
        else:
            pits = el.pitches
            for p in pits:
                pitchesList.append(p.midi)
    pitchesList.sort()
    return (pitchesList[-1]-pitchesList[0])

# the ration of 'qualified' notes (longer than the 32th note)
def QN(filename):
    midiParse = converter.parse(filename)
    noteAndChord = midiParse.recurse().getElementsByClass([note.Note, chord.Chord])
    qulinotes = []
    for el in noteAndChord:
        if el.duration.quarterLength>0.166666666:
            qulinotes.append(el)
    return len(qulinotes)*1.0/len(noteAndChord)

# the number of notes and chords
def NC(filename):
    midiParse = converter.parse(filename)
    noteAndChord = midiParse.recurse().getElementsByClass([note.Note, chord.Chord])
    return len(noteAndChord)

# the average inter-onset-interval
def AIOI(filename):
    midiParse = converter.parse(filename)
    voices = midiParse.recurse().getElementsByClass(stream.Voice)
    intervals = []
    if len(voices)!=0:
        for v in voices:
            noteAndChord = v.getElementsByClass([note.Note, chord.Chord])
            for i in range(0,len(noteAndChord)-1):
                intervals.append(noteAndChord[i+1].offset - noteAndChord[i].offset)
    else:
        noteAndChord = midiParse.recurse().getElementsByClass([note.Note, chord.Chord])
        for i in range(0,len(noteAndChord)-1):
            intervals.append(noteAndChord[i+1].offset - noteAndChord[i].offset)
    return np.mean(intervals)

# the number of different tempos
def NT(filename):
    midiParse = converter.parse(filename)
    tempos = midiParse.recurse().getElementsByClass(tempo.MetronomeMark)
    temponum = set()
    for t in tempos:
        temponum.add(t)
    return len(temponum)

# evaluate a MIDI file
def evaluation(filename):
    res = {}
    res['anpc_bar'] = ANPC_bar(filename)
    res['npc'] = NPC(filename)
    res['np'] = NP(filename)
    res['pr'] = PR(filename)
    res['qn'] = QN(filename)
    res['nc'] = NC(filename)
    res['aioi'] = AIOI(filename)
    res['nt'] = NT(filename)
    return res
