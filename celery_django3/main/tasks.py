from celery import shared_task
from main.models import InputImages, OutputImages
import glob
import os
import io


@shared_task
def save_image_to_model():

    results = InputImages.objects.all()
    for result in results:
        inp_image = result.input_images
        std_image = result.sandard_image
        """
        Call your image_compare function here by passing the two images of the InputImages model

        Something like this: output_image = image_compare(std_image, inp_image)

        """
        output = OutputImages.objects.create(output_image="""returned output_image by image_compare function""",input_key=result)