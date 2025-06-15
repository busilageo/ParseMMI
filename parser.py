import sys
import os
import ffmpeg

# Returns stream downscaled to desired res
def parse_video(file_path, width, height):

    original_width, original_height = get_video_resolution(file_path)

    scale_factor = min(width / original_width, height / original_height, 1) # last value is here so we never upscale
    width = int(original_width * scale_factor)
    height = int(original_height * scale_factor)

    input_stream = ffmpeg.input(file_path)
    video = input_stream.video.filter("scale", width, height)
    
    return video


def get_video_resolution(file_path):

    probe = ffmpeg.probe(file_path)
    video_stream = [stream for stream in probe['streams'] if stream['codec_type'] == 'video'][0]

    if not video_stream:
        raise Exception("No video stream found")
    
    width = int(video_stream['width'])
    height = int(video_stream['height'])

    return width, height

if __name__ == "__main__":

    media_path = sys.argv[1]
    destination_path = sys.argv[2]
    width = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] else 720
    height = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] else 576

    os.makedirs(destination_path, exist_ok=True)
    print(media_path)

    for filename in os.listdir(media_path):

        file_path = os.path.join(media_path, filename)
        output_path = os.path.join(destination_path, filename)
        if not os.path.isfile(file_path) or not filename.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):
            continue

        print(f"Processing: {filename}")
        if os.path.exists(output_path):
            answer = input(f"{filename} already exists at {destination_path}.\nOverwrite? (y/n): ")
            if answer.lower() != 'y':
                print("Skipping file.")
                continue
        video = parse_video(file_path, width, height)
        ffmpeg.output(video, output_path).run(quiet=True, overwrite_output=True)
