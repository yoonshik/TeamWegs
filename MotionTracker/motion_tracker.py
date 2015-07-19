#!/usr/bin/python2
import cv2
class MotionTracker:
	def __init__(self):
		self.CAM_ID = 0
		self.CAM = None
	def set_cam(self, cam_id):
		self.CAM_ID = cam_id
	def init_cam(self):
		self.CAM = cv2.VideoCapture(self.CAM_ID)
	def display_cam(self):
		while True:
			(retval, image) = self.CAM.read()
			
			cv2.imshow("Test output", image)
	
			key = cv2.waitKey(1) & 0xFF
			if key == 27:
				break;

		cv2.destroyAllWindows()
def main():
	motion_tracker = MotionTracker()

	motion_tracker.init_cam()
	motion_tracker.display_cam()

if __name__ == "__main__":
	main()
