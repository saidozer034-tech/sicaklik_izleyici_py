import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SicaklikDinleyici(Node):
    def __init__(self):
        super().__init__('sicaklik_dinleyici')
        self.subscription = self.create_subscription(
            Float32,
            'sicaklik_veri',
            self.listener_callback,
            10)
        self.get_logger().info('Sıcaklık Dinleyicisi Başlatıldı!')

    def listener_callback(self, msg):
        self.get_logger().info(f'Okunan Sıcaklık: {msg.data} °C')

def main(args=None):
    rclpy.init(args=args)
    node = SicaklikDinleyici()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
