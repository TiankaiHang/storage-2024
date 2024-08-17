import os
from glob import glob
import json

import click
from shutil import copyfile


@click.command()
@click.option("--json_path", type=str, help="Path to the json file.")
@click.option("--video_dir", type=str, help="Path to the video directory.")
def main(json_path, video_dir):
    with open(json_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            # prompts.append(json.loads(line)["prompt_en"])
            meta_info = json.loads(line)
            dimesions = meta_info["dimension"]
            prompt = meta_info["prompt_en"]

            for dim in dimesions:
                video_paths = glob(f"{video_dir}/" + prompt.replace(' ', '_') + f"-*.mp4")
                for video_path in video_paths:
                    video_dir_dim = os.path.join(video_dir, dim)
                    if not os.path.exists(video_dir_dim):
                        os.makedirs(video_dir_dim, exist_ok=True)
                    # copy video to video_dir_dim
                    copyfile(video_path, os.path.join(video_dir_dim, os.path.basename(video_path)))
        


if __name__ == "__main__":
    main()
