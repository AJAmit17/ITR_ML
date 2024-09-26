from setuptools import setup, find_packages

setup(
    name='image_text_recognition',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'easyocr',
        'Pillow',
        'numpy',
        'opencv-python'
    ],
    entry_points={
        'console_scripts': [
            'image_text_recognition=image_text_recognition.image_text_recognition:main',
            'fine_tune=image_text_recognition.fine_tune:main'
        ],
    },
    author='',
    author_email='',
    description='A package for recognizing text in images using EasyOCR',
    license='MIT',
    keywords='image text recognition easyocr',
    url='',
)