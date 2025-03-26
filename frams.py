import cv2
import os

def extract_frames_from_videos(video_paths, output_folder, frame_rate=1):
    """
    Extract frames from multiple videos and save them in a single folder.

    Args:
        video_paths (list): List of paths to video files.
        output_folder (str): Folder to save the extracted frames.
        frame_rate (int): Number of frames to save per second of video.

    Returns:
        None
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Frame counter to ensure unique filenames
    frame_counter = 0

    # Process each video
    for video_path in video_paths:
        # Capture the video
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Error: Unable to open video {video_path}")
            continue

        # Get the frame rate of the video
        video_fps = int(cap.get(cv2.CAP_PROP_FPS))
        skip_frames = max(1, video_fps // frame_rate)

        frame_index = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Save only the frames based on the desired frame rate
            if frame_index % skip_frames == 0:
                frame_filename = os.path.join(output_folder, f"frame_{frame_counter:06d}.jpg")
                cv2.imwrite(frame_filename, frame)
                frame_counter += 1

            frame_index += 1

        cap.release()

    print(f"Frame extraction complete. Frames saved to {output_folder}")

def process_videos_in_folder(folder_path, output_folder):
    """
    Process all videos in a folder and extract frames into a single folder.

    Args:
        folder_path (str): Path to the folder containing videos.
        output_folder (str): Folder to save all extracted frames.

    Returns:
        None
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Collect all video paths in the folder
    video_paths = []
    for filename in os.listdir(folder_path):
        # Construct full file path
        video_path = os.path.join(folder_path, filename)
        
        # Check if it's a file (not a directory) and has a video extension
        if os.path.isfile(video_path) and filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            video_paths.append(video_path)
            print(f"Found video: {filename}")

    # Extract frames from all videos into the same output folder
    extract_frames_from_videos(video_paths, output_folder, frame_rate=1)

# Example usage
folder_path = "/Users/sanskritiagrawal/Downloads/threat in retail/videos"
output_folder = "extracted_frames"
process_videos_in_folder(folder_path, output_folder)