import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class SicaklikYayinci(Node):
    def __init__(self):
        super().__init__('sicaklik_yayinci')
        self.publisher_ = self.create_publisher(Float32, 'sicaklik_veri', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Sıcaklık Yayımcısı Başlatıldı!')

    def timer_callback(self):
        msg = Float32()
        msg.data = round(random.uniform(15.0, 35.0), 2)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Yayınlanan Sıcaklık: {msg.data} °C')

def main(args=None):
    rclpy.init(args=args)
    node = SicaklikYayinci()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
