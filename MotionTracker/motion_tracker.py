#!/usr/bin/python2
import time, cv2

class MotionTracker:

	def __init__(self):
		self.CAM_ID = 0
		self.CAM = None
		self.THRESH_MIN = 100
		self.THRESH_MAX = 255

	def set_cam(self, cam_id):
		self.CAM_ID = cam_id

	def init_cam(self):
		self.CAM = cv2.VideoCapture(self.CAM_ID)

	def display_cam(self):
		while True:
			
			image = self._diff_image(.05)

			cv2.imshow("Test output", image)
	
			key = cv2.waitKey(1) & 0xFF
			if key == 27:
				break;

		cv2.destroyAllWindows()

	def release_cam(self):
		self.CAM.release()

	#Clear camera buffer
	def _flush_cam(self):
		self.CAM.release()
		self.init_cam()
		
		for i in range(0, 100):
			self.CAM.read()

	def _threshold_img(self, image):
		
		thresh_image = cv2.threshold(image, self.THRESH_MIN, self.THRESH_MAX, cv2.THRESH_BINARY)
		return thresh_image

	def _diff_image(self, sleep_interval):

		#Get first frame
		(retval_one, image_one) = self.CAM.read()

		#Sleep for specified interval in seconds
		time.sleep(sleep_interval)
		
		#self._flush_cam();
		
		#Get second frame
		(retval_two, image_two) = self.CAM.read()

		#Convert images to grayscale
		image_one_gray = cv2.cvtColor(image_one, cv2.COLOR_BGR2GRAY)
		image_two_gray = cv2.cvtColor(image_two, cv2.COLOR_BGR2GRAY)

		gray_diff = cv2.absdiff(image_one_gray, image_two_gray)

		return gray_diff
def main():
	motion_tracker = MotionTracker()

	motion_tracker.init_cam()
	motion_tracker.display_cam()
	motion_tracker.release_cam()

if __name__ == "__main__":
	main()
