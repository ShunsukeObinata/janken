
import random
import foo

print("コンピューターとじゃんけんをしましょう！！")
# 相手の名前を受け取り変数に入れる
player_name = input("名前を入力してください：")
print(player_name + "さんこんにちは")

# 相手の出した手を変数に入れる
print("(0:グー、1:チョキ、2:パー) 何を出しますか？")
player_choice = input("数字で入力してください：")
lists = ["グー","チョキ","パー"]

#コンピューターの出す手をランダムにする
computer_foo = random.randint(0,2)

#playerの入力があっているか条件分岐しあっている場合は対戦結果を表示する
if int(player_choice) < 0 or 2<int(player_choice):
   print("正しい数字を入れてください")
else:
  player_hand = lists[int(player_choice)]
  computer_hand = lists[computer_foo]
  print("コンピューターは" + computer_hand + "を出しました")
  foo.judge(player_hand,computer_hand,player_name)

