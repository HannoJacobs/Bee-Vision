import base64
import requests
from pathlib import Path
import cv2
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


def chatgpt_submit_base64_image(str_base64_image, str_prompt):
    str_response = ""
    try:

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }

        payload = {
            # "model": "gpt-4-turbo",
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": str_prompt + "?",
                            # . Please only reply with a YES or NO"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{str_base64_image}"
                            },
                        },
                    ],
                }
            ],
            "max_tokens": 300,
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
        )

        dict_response = response.json()

        list_choices = dict_response.get("choices", [])

        str_response = ""
        for item in list_choices:
            dict_message = item.get("message", {})
            str_content = dict_message.get("content", "")
            str_response = str_content
            if str_response != "":
                break

    except Exception:
        print("chatgpt_submit_image")

    return (str_response, str(dict_response))


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def list_images_sorted(root_dir):
    root_path = Path(root_dir)
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}
    all_images = sorted(
        [
            file
            for file in root_path.rglob("*")
            if file.suffix.lower() in image_extensions
        ],
        key=lambda x: x.name,  # Sort by filename
    )
    full_paths = [str(file) for file in all_images]
    filenames = [str(file.name) for file in all_images]
    return full_paths, filenames


if __name__ == "__main__":
    ROOT_IN = "Dataset/FULL_DATASETS/dataset_all_images_in"
    ROOT_OUT = "Dataset/FULL_DATASETS/dataset_all_images_out"
    os.makedirs(ROOT_OUT, exist_ok=True)

    prompt = """
    (It is really important that you obey my commands that restrict your output to exactly what I ask, no exceptions)

    What type of bee[s] is/are in this image, please reply with one of the selections from the list exactly as one of the choices with the name there:
    Allodapula, Apis-mellifera-scutellata, Braunsapis, Lasioglossum, Meliponula, Seladonia, Thyreus, Xylocopa
    (don't add '' chars in your reply)

    If it's not one of the choices in the list then please just say:
    '<name>'
    (where the name of the type[s] there are seperated by underscores, don't add '' chars in your reply)

    If there are more than one type of bee in the image, then reply with:
    'Multiple_<names>'
    (where the <names> of the types are there seperated by underscores, don't add '' chars in your reply)
    """

    full_paths, filenames = list_images_sorted(ROOT_IN)
    for i, full_path in enumerate(full_paths):
        resp, _ = chatgpt_submit_base64_image(encode_image(full_path), prompt)
        # resp = "Thyreus"
        # print(f"\n\nRESPONSE:\n'''\n{resp}\n'''\n")

        new_filename = f"{ROOT_OUT}/{resp}_{i}.png"
        cv2.imwrite(new_filename, cv2.imread(full_path))
        print(f"Saved: {new_filename}")
        pass
