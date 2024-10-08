# from PIL import Image, ImageDraw, ImageFont
# import os
# import random

# def create_image_with_text(text, filename, directory, font_size=20, image_size=(200, 50)):
#     img = Image.new('RGB', image_size, color='white')
#     d = ImageDraw.Draw(img)
#     try:
#         font = ImageFont.truetype("arial.ttf", font_size)
#     except IOError:
#         font = ImageFont.load_default()
    
#     bbox = font.getbbox(text)
#     text_width = bbox[2] - bbox[0]
#     text_height = bbox[3] - bbox[1]
    
#     position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
    
#     d.text(position, text, fill='black', font=font)
    
#     if not os.path.exists(directory):
#         os.makedirs(directory)
    
#     img.save(os.path.join(directory, filename))

# def generate_sample_images():
#     sample_texts = [
#         "Hello World", "OpenAI GPT", "Machine Learning", "Python Code", "Deep Learning",
#         "Artificial Intelligence", "Neural Networks", "Data Science", "Computer Vision",
#         "Natural Language Processing", "Reinforcement Learning", "Big Data Analytics",
#         "Internet of Things", "Cloud Computing", "Blockchain Technology", "Cybersecurity",
#         "Quantum Computing", "Augmented Reality", "Virtual Reality", "Robotics",
#         "78560","7856@#%"
#     ]

#     train_dir = "train_images"
#     for i in range(100):
#         text = random.choice(sample_texts)
#         font_size = random.randint(16, 24)
#         image_size = (random.randint(180, 220), random.randint(40, 60))
#         create_image_with_text(text, f"train{i+1}.jpg", train_dir, font_size, image_size)
    
#     test_dir = "test_images"
#     for i in range(20):
#         text = random.choice(sample_texts)
#         font_size = random.randint(16, 24)
#         image_size = (random.randint(180, 220), random.randint(40, 60))
#         create_image_with_text(text, f"test{i+1}.jpg", test_dir, font_size, image_size)

#     print("Sample images generated successfully.")

# if __name__ == "__main__":
#     generate_sample_images()

from PIL import Image, ImageDraw, ImageFont
import os

def generate_test_images(output_dir, texts, image_size=(300, 100), font_size=36):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, text in enumerate(texts):
        image = Image.new('RGB', image_size, color='white')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", font_size)
        text_width, text_height = draw.textsize(text, font=font)
        position = ((image_size[0]-text_width)/2, (image_size[1]-text_height)/2)
        draw.text(position, text, fill='black', font=font)
        image.save(os.path.join(output_dir, f'test{i+1}.jpg'))