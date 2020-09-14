#じゃんけんの勝ち負けを判定
def judge(p_hand,c_hand,name1):
  if p_hand == c_hand :
    return print("引き分けです")
  elif p_hand==2 and c_hand==0:
    return print(name1 + "さんの勝ちです")
  elif p_hand==1 and c_hand==2:
    return print(name1 + "さんの勝ちです")
  elif p_hand==2 and c_hand==0:
    return print(name1 + "さんの勝ちです")
  else:
    return print(name1 + "さんの負けです")

