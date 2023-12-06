from setuptools import find_packages, setup

package_name = 'page_web_ros_qt'

setup(
    name=package_name,
    version='1.0',
    packages=find_packages(exclude=['test']),
    install_requires=[
        'qtbase5-dev',
        'qt5-qmake',
        'libqt5-core',
        'rclpy',
        'std_msgs',
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    zip_safe=True,
    maintainer='anas',
    maintainer_email='mohamed-anas.daggag@universite-paris-saclay.fr',
    description='ROS 2 Python package for pubsub functionality',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           'qt_page_web_talker = page_web_ros_qt.mainwindow:main',
        ],
    },
)
