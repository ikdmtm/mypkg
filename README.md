# mypkg
rosのpackageです。
nodeを3つ使い59分59秒99まで計測できます。

node1で1秒未満、node2で秒、node3で分を計測

### 使い方

$roscore

$rosrun mypkg ros1.py
$rosrun mypkg ros2.py
$rosrun mypkg ros3.py

$rosnode list　　nodeがあるか確認
$rostopic list 　データが出力されている場所確認

$rostopic echo /ros1
$rostopic echo /ros2
$rostopic echo /ros3　　それぞれデータを表示



