from typing import Any
from store.models import Design_post
from django.templatetags.static import static
from django.core.management.base import BaseCommand

   
class Command(BaseCommand):
    help = "This commands inserts post data"
    
    def handle(self, *args: Any, **options: Any):
        
        design_title =[
           'Footprint',
           'Pawsquad',
           'Sony Camera',
           'Gaming Web',
           'Beach & Coastal Escapes',
           'feature'
        ]
        design_catagories=[
            'Mobile App Design',
            'Website Design',
            'App desk',
            'Braiding'
        ]
        Post_imageurl=[
              static('assets/img/footprint.png'),
              static('assets/img/paw.png'),
              static('assets/img/camera.png'),
              static('assets/img/game.png'),
              static('assets/img/beaches.png'),
              static('assets/img/feature.png'),
        ]
        

        for design_title,design_catagories,Post_imageurl in zip(
            design_title,design_catagories,Post_imageurl):
            Design_post.objects.create(
                Post_imageurl=Post_imageurl,
                design_title=design_title,
                design_catagories=design_catagories
                )
         
        self.stdout.write(self.style.SUCCESS("d inserting data!"))