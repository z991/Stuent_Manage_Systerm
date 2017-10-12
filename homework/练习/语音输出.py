import win32com.client
speaker=win32com.client.Dispatch("SAPI.SPVOICE")
while True:
  speaker.Speak("正宗好凉茶正宗好声音欢迎收看由凉茶领导品牌加多宝为您冠名的加多宝凉茶"
              "中国好声音喝启力添动力娃哈哈启力精神保健品为中国好声音加油")



