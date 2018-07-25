Mat hsv = new Mat();
Imgproc.cvtColor(rgba, hsv, Imgproc.COLOR_RGBA2HSV);

Mat mask = new Mat();
Core.inRange(hsv,  new Scalar(10,100,100), new Scalar(30,255,255), mask);

rgba.setTo(new Scalar(255,255,0, 100), mask);
