#!/usr/bin/python2
import time, cv2

class CamStreamer:

	def __init__(self):
		self.CAM_ID = 0
		self.CAM = None

	def set_cam(self, cam_id):
		self.CAM_ID = cam_id

	def init_cam(self):
		self.CAM = cv2.VideoCapture(self.CAM_ID)

	def release_cam(self):
		self.CAM.release()
	
	def read_frame(self):
		(status, image) = self.CAM.read()
		return image

class MotionTracker:

	def __init__(self, cam_stream):
		self.CAM_STREAM = cam_stream
		self.THRESH_MIN = 100
		self.THRESH_MAX = 255
		self.WAIT_INTERVAL = .005
		self.NUM_DIFF_THRESHOLD = 80

	def _display_img(self, image):
		cv2.imshow("Test output", image)
	
		key = cv2.waitKey(1) & 0xFF
		if key == 27:
			cv2.destroyAllWindows()
			return False
		return True

	def _threshold_img(self, image):
		
		(retval, thresh_image) = cv2.threshold(image, self.THRESH_MIN, self.THRESH_MAX, cv2.THRESH_BINARY)
		return thresh_image

	def _diff_image(self, sleep_interval):

		#Get first frame
		image_one = self.CAM_STREAM.read_frame()

		#Sleep for specified interval in seconds
		time.sleep(sleep_interval)
		
		#self._flush_cam();
		
		#Get second frame
		image_two = self.CAM_STREAM.read_frame()

		#Convert images to grayscale
		image_one_gray = cv2.cvtColor(image_one, cv2.COLOR_BGR2GRAY)
		image_two_gray = cv2.cvtColor(image_two, cv2.COLOR_BGR2GRAY)

		gray_diff = cv2.absdiff(image_one_gray, image_two_gray)

		return gray_diff

	def _get_motion_in_diffed(self, image):
		
		(rows, cols) = image.shape

		(non_z_row, non_z_col) = image.nonzero()

		num_different_pixels = len(non_z_row)

		return (self.NUM_DIFF_THRESHOLD < num_different_pixels)

	def run(self, show):

		while True:
			gray_diff = self._diff_image(self.WAIT_INTERVAL)
			thresh_img = self._threshold_img(gray_diff)
	
			is_motion = self._get_motion_in_diffed(thresh_img)

			if show:
				if not self._display_img(thresh_img):
					break

			print(is_motion)

def main():
	
	cam_stream = CamStreamer()
	motion_tracker = MotionTracker(cam_stream)

	cam_stream.init_cam()
	motion_tracker.run(True)
	motion_tracker.release_cam()

if __name__ == "__main__":
	main()
