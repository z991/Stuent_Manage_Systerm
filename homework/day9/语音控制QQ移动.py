from win32com.client import constants
import os
import win32com.client
import pythoncom
import  win32com
import  win32con
import  win32gui
speaker = win32com.client.Dispatch("SAPI.SPVOICE")


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


        import math
        QQ = win32gui.FindWindow("TXGuiFoundation", "QQ")
        if  speechstr=="关闭":
            os.system("taskkill /f  /im QQ.exe")


        elif  speechstr=="往上":
            for size in range(600, 0, -1):  # 向上
                win32gui.SetWindowPos(QQ,  # 操作记事本
                                      win32con.HWND_TOPMOST,  # 最上方
                                      0,  # 位置x
                                      size,  # 置y
                                      300,  # 长度
                                      300,  # 宽度
                                      win32con.SWP_SHOWWINDOW)

        elif  speechstr=="往下":
            for  size  in  range(0,600,1):#向下
             win32gui.SetWindowPos(QQ,
                          win32con.HWND_TOPMOST, #最上方
                          800, #位置x
                          size,#位置y
                          300,#长度
                          300,#宽度
                          win32con.SWP_SHOWWINDOW)
        elif  speechstr=="往左":
            for size in range(800, 0, -1):  # 向左
                win32gui.SetWindowPos(QQ,  # 操作记事本
                                      win32con.HWND_TOPMOST,  # 最上方
                                      size,  # 位置x
                                      600,  # 位置y
                                      300,  # 长度
                                      300,  # 宽度
                                      win32con.SWP_SHOWWINDOW)
        elif  speechstr=="往右":
            for size in range(0, 800, 1):  # 向右
                win32gui.SetWindowPos(QQ,  # 操作记事本
                                      win32con.HWND_TOPMOST,  # 最上方
                                      size,  # 位置x
                                      0,  # 位置y
                                      300,  # 长度
                                      300,  # 宽度
                                      win32con.SWP_SHOWWINDOW)
        elif speechstr == "滚出来":
            QQ=win32gui.FindWindow("TXGuiFoundation","QQ")
            win32gui.ShowWindow(QQ,win32con.SW_SHOW)
            pass
        elif speechstr == "躲起来":
            QQ = win32gui.FindWindow("TXGuiFoundation", "QQ")
            win32gui.ShowWindow(QQ, win32con.SW_HIDE)
            pass
        else:
            pass

if __name__ == '__main__':

    speaker.Speak("语音识别开启")
    wordsToAdd = ["关闭",
                  "往上",
                  "往下",
                  "往左",
                  "往右",
                  "滚出来",
                  "躲起来"
                  ]
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()