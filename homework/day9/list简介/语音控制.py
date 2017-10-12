from win32com.client import constants
import os
import win32com.client
import pythoncom
class SpeechRecognition:
    def __init__(self, wordsToAdd):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
        self.listener = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
        self.context = self.listener.CreateRecoContext()
        self.grammar = self.context.CreateGrammar()
        self.grammar.DictationSetState(0)
        self.wordsRule = self.grammar.Rules.Add("wordsRule", constants.SRATopLevel + constants.SRADynamic, 0)
        self.wordsRule.Clear()
        [self.wordsRule.InitialState.AddWordTransition(None, word) for word in wordsToAdd]
        self.grammar.Rules.Commit()
        self.grammar.CmdSetRuleState("wordsRule", 1)
        self.grammar.Rules.Commit()
        self.eventHandler = ContextEvents(self.context)
        self.say("Started successfully")
    def say(self, phrase):
        self.speaker.Speak(phrase)
class ContextEvents(win32com.client.getevents("SAPI.SpSharedRecoContext")):
    def OnRecognition(self, StreamNumber, StreamPosition, RecognitionType, Result):
        newResult = win32com.client.Dispatch(Result)
        print("小伙子你在说 ", newResult.PhraseInfo.GetText())
        speechstr=newResult.PhraseInfo.GetText()
        if   speechstr=="关机":
             os.system("shutdown -s -t 300")
        elif speechstr=="取消关机":
             os .system("shutdown -a")
        elif speechstr=="记事本":
             os.system("notepad")
        elif speechstr=="写字板":
             os.system("write")
        elif speechstr=="画图板":
             os.system("mspaint")
        elif speechstr=="关闭记事本":
             os.system("taskkill  /f   /im   notepad.exe")
        else:
            print("我没听懂")


if __name__ == '__main__':
    wordsToAdd = ["关机", "取消关机", "记事本", "画图板","写字板","设置",]
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()