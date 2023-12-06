# page_web_ros_qt
Simple publisher ros2 avec qt

Avec la particularité de normalement communiquer avec un sub qui recopie ce qu'il reçoit sur une page web :

```
https://github.com/anasdtp/pg_web_ros
```

Faire un git clone sur le workspace de ros2.

Commande à faire :

Bien ce mettre sur le workspace de ros2 puis : 

```
git clone https://github.com/anasdtp/pg_web_ros
git clone https://github.com/anasdtp/page_web_ros_qt
```
```
colcon build
source install/setup.bash
```
```
cd src/page_web_ros_qt/launch/
ros2 launch page_web_base.xml
```

Cela devrait lancer une petite fenetre :

![image](https://github.com/anasdtp/page_web_ros_qt/assets/116441391/0e440a06-8fb7-4354-a83e-2795d479731b)

La page web est accessible en cliquant sur le lien avec l'adresse IP

Si on ecrit des trucs dans la barre et qu'on fait send, ça s'ecrit sur la page web

Ce projet servira de base pour faire un projet de controle par wifi et par ros2 de petits robots 
