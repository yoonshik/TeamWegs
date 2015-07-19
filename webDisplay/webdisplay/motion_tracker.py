#!/usr/bin/python2
import time, cv2, requests

class WebLink:

	def __init__(self):

		#HTTP Server to POST to 
		self.TARGET_URL = "http://localhost:6543/motion_detected"

	def rest_alert(self):
		try:
			req = requests.post(self.TARGET_URL)
		except:
			print("HTTP POST Failed")

class CamStreamer:

	def __init__(self):

		self.CAM_ID = 0
		self.CAM = None
		
		self.LAST_IMAGE = 0

	def set_cam(self, cam_id):

		self.CAM_ID = cam_id

	def init_cam(self):

		self.CAM = cv2.VideoCapture(self.CAM_ID)

	def release_cam(self):

		self.CAM.release()
	
	def read_frame(self):

		(status, self.LAST_IMAGE) = self.CAM.read()
		return self.LAST_IMAGE

	def peek_frame(self):

		return self.LAST_IMAGE

	#Save cached frame to a file
	def save_peek(self, path):

		return cv2.imwrite(path, self.LAST_IMAGE)

class MotionTracker:

	def __init__(self, cam_stream, web_link):

		self.CAM_STREAM = cam_stream
		self.WEB_LINK = web_link
		self.THRESH_MIN = 100
		self.THRESH_MAX = 255
		self.WAIT_INTERVAL = .005
		self.NUM_DIFF_THRESHOLD = 80

		self.NEW_MOTION_WAIT_SECS = 3
		self.LAST_MOTION_TIME = 0

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

		#Get indices of non-zero pixels
		(non_z_row, non_z_col) = image.nonzero()

		num_different_pixels = len(non_z_row)

		return (self.NUM_DIFF_THRESHOLD < num_different_pixels)

	def run(self, show_frame):

		while True:
			gray_diff = self._diff_image(self.WAIT_INTERVAL)
			thresh_img = self._threshold_img(gray_diff)
	
			is_motion = self._get_motion_in_diffed(thresh_img)

			if show_frame:
				if not self._display_img(thresh_img):
					break

			#Always save image
			self.CAM_STREAM.save_peek("./webDisplay/webdisplay/static/captured_images/feed.jpg")

			#Ignore for time lock-out
			if (time.time() - self.LAST_MOTION_TIME < self.NEW_MOTION_WAIT_SECS):
				continue 

	
			#Motion detected
			if is_motion:

				#Update metadata
				self.LAST_MOTION_TIME = time.time()	

				#Save file
				self.CAM_STREAM.save_peek("./webDisplay/webdisplay/static/captured_images/motion.jpg")

				#Send POST
				self.WEB_LINK.rest_alert()

				print("MOTION")

def main():
	
	cam_stream = CamStreamer()
	web_link = WebLink()
	motion_tracker = MotionTracker(cam_stream, web_link)

	cam_stream.init_cam()
	motion_tracker.run(False)
	cam_stream.release_cam()

if __name__ == "__main__":
	main()
