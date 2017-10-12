from win32com.client import constants
import os
import win32com.client
import pythoncom
import win32api
import win32con
import time


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
        speechstr = newResult.PhraseInfo.GetText()
        if speechstr == "向前":
            win32api.keybd_event(87, 0, 0, 0)  # 键盘按下   向前（W）


        elif speechstr == "向左":
            win32api.keybd_event(65, 0, 0, 0)  # 键盘按下   向左（A）

        elif speechstr == "向右":
            win32api.keybd_event(68, 0, 0, 0)  # 键盘按下   向右（D）
            time.sleep(0.1)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开

        elif speechstr == "向后":
            win32api.keybd_event(83, 0, 0, 0)  # 键盘按下   向后（S）
            time.sleep(0.1)
            win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开

            '''elif speechstr == "太岁":
            win32api.keybd_event(65, 0, 0, 0)  # 键盘按下
            time.sleep(0.1)
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开
            win32api.keybd_event(68, 0, 0, 0)  # 键盘按下
            time.sleep(0.1)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        elif speechstr == "阎罗":
            win32api.keybd_event(68, 0, 0, 0)  # 键盘按下
            time.sleep(0.1)
            win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开
            win32api.keybd_event(65, 0, 0, 0)  # 键盘按下
            time.sleep(0.1)
            win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)  # 键盘松开
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)'''

        else:
            print("你妹的说啥，没听清楚")


if __name__ == '__main__':
    wordsToAdd = ["向前", "向后", "向左", "向右"]
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()