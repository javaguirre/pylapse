import os
import Image
import select
import v4l2capture
import time


def capture(directory, video_device='/dev/video0',
            resolution=[1280, 1024], image_ext='png',
            buffers=1):

    video = v4l2capture.Video_device(video_device)
# Suggest an image size to the device. The device may choose and
# return another size if it doesn't support the suggested one.
    size_x, size_y = video.set_format(*resolution)
# Create a buffer to store image data in. This must be done before
# calling 'start' if v4l2capture is compiled with libv4l2. Otherwise
# raises IOError.
    video.create_buffers(buffers)
# Send the buffer to the device. Some devices require this to be done
# before calling 'start'.
    video.queue_all_buffers()
# Start the device. This lights the LED if it's a camera that has one.
    video.start()
# Wait for the device to fill the buffer.
    select.select((video,), (), ())

    image_data = video.read()
    image_name = "%s.%s" % (str(time.time()).split('.')[0], image_ext)
    full_path = os.path.join(directory, image_name)
    video.close()
    image = Image.fromstring("RGB", (size_x, size_y), image_data)
    image.save(full_path)
