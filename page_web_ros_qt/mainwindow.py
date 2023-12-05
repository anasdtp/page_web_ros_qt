import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from threading import Thread

class MinimalPublisher(Node):
    def __init__(self):
       super().__init__('minimal_publisher')
       self.publisher_ = self.create_publisher(String, 'topic', 10)

    def publish_string(self, msg):
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sendButton.clicked.connect(self.doSomething)
        self.i = 0
        self.node_ = MinimalPublisher() 

    def doSomething(self):
        msg = String()
        msg.data = self.ui.lineEdit_1.text()
        self.node_.publish_string(msg)

    def closeEvent(self, event):
        print("Au revoir")
        rclpy.shutdown()
        event.accept()

def run_ros_node():
   rclpy.init()
   ros_node = MinimalPublisher()
   rclpy.spin(ros_node)
   rclpy.shutdown()

def main():
    app = QApplication([])
    # run_ros_node()
    ros_thread = Thread(target=run_ros_node)
    ros_thread.start()


    window = MainWindow()

    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
