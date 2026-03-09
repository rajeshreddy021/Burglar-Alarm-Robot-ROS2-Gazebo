import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class MotionDetectorAlarm(Node):
    def __init__(self):
        super().__init__('burglar_detector')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10)
        self.bridge = CvBridge()
        
        # Variables for motion detection
        self.prev_frame = None
        self.get_logger().info("Motion Detection Alarm Active. System Stationary...")

    def image_callback(self, msg):
        # 1. Convert ROS Image to OpenCV
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        # 2. Pre-process: Convert to Grayscale and Blur to reduce noise
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # 3. Initialize prev_frame if it's the first image
        if self.prev_frame is None:
            self.prev_frame = gray
            return

        # 4. Frame Differencing: Absolute difference between current and previous frame
        frame_delta = cv2.absdiff(self.prev_frame, gray)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

        # 5. Dilate the thresholded image to fill in holes
        thresh = cv2.dilate(thresh, None, iterations=2)
        
        # 6. Calculate amount of motion (sum of white pixels)
        motion_amount = np.sum(thresh > 0)
        
        # Update previous frame for next iteration
        self.prev_frame = gray

        # 7. Trigger Alarm if motion exceeds threshold
        if motion_amount > 10000:  # Adjust this sensitivity threshold
            self.get_logger().error("!!! SIREN TRIGGERED: MOTION DETECTED !!!")
            cv2.putText(frame, "INTRUDER ALERT: MOTION", (20, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            
            # Draw contours around moving objects
            contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) < 500:
                    continue
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 8. Show the security feeds
        cv2.imshow("Security Feed", frame)
        cv2.imshow("Motion Delta (Difference)", thresh)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = MotionDetectorAlarm()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()
