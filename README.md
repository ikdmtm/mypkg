# mypkg
rosのpackageです。<br>
nodeを3つ使い59分59秒99まで計測できます。

node1で1秒未満、node2で秒、node3で分を計測

### 使い方

$roscore

$rosrun mypkg ros1.py<br>
$rosrun mypkg ros2.py<br>
$rosrun mypkg ros3.py<br>

$rosnode list　　nodeがあるか確認<br>
$rostopic list 　データが出力されている場所確認<br>

$rostopic echo /ros1<br>
$rostopic echo /ros2<br>
$rostopic echo /ros3　　それぞれデータを表示<br>



