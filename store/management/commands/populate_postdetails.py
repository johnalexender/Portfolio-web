from typing import Any
from store.models import Designpost
from django.templatetags.static import static
from django.core.management.base import BaseCommand

   
class Command(BaseCommand):
    help = "This commands inserts post details"
    
    def handle(self, *args: Any, **options: Any):
        
        
        OverviewTitle=[
            'Overview'
        ]
        OverviewPara =[
            'A worldwide travel guide application focusing on ease of navigation for travelers. It offers features like hotel search, restaurant discovery, transportation arrangements, and location sharing.',
            'A platform to connect pet owners with veterinary services, pet sitters, trainers, and adoption services.',
            'A product-specific app or interface for Sony Cameras, designed to enhance photography experiences with features like remote control, editing tools, and tutorials.',
            'A platform for gaming enthusiasts, featuring game reviews, news, online gaming communities, and live streams.',
            'A vacation planning app specializing in coastal destinations, featuring accommodations, activities, and travel guides.',
            'A customizable platform or application showcasing special features for various domains, such as e-commerce or portfolio building.'
        ]
        ApproachTitle=[
            'Approach'
        ]
        ApproachPara=[
            'Clean Design: Use intuitive layouts for seamless browsing.Interactive Maps: Highlight nearby attractions and travel routes visually.Personalization: Incorporate preferences to tailor experiences',
            'User-Centric: Design with a friendly, playful theme using icons and images of pets.Quick Navigation: Easy access to services with clear categories.Community Focus: Include forums or blogs for pet-related discussions and advice.',
            'Minimalist Interface: Highlight photography with dark mode and focus on images.Real-Time Control: Offer camera adjustments (ISO, shutter speed) through the app.Learning Hub: Tutorials and tips section for beginner photographers.',
            'Dynamic Design: Incorporate animations and bold visuals to match the gaming theme.Community Engagement: Chat rooms, leaderboards, and forums to connect gamers.Live Integration: Support live-streaming directly on the platform.',
            'Relaxing Aesthetic: Soft, beachy colors and smooth transitions to evoke a vacation vibe.Visual Content: High-resolution imagery to showcase destinations.Simple Itineraries: Allow users to build itineraries with drag-and-drop featuresOffline Access: Include offline guides for remote locations.',
            'Flexible Design: Modular UI components that adapt to user needs.Highlight Focus: Use engaging visuals to showcase individual features effectively.User Control: Empower users to personalize layouts and functionalities.'
        ]
        Details_imageurl=[
            static('assets/img/BEACH/beachetour d1.png'),
            static('assets/img/BEACH/beachetour d2.png'),
            static('assets/img/BEACH/beachetour d3.png'),
            static('assets/img/PawSquad/cover design-1.png'),
            static('assets/img/PawSquad/cover design-2.png'),
            static('assets/img/PawSquad/cover design-3.png'),
            static('assets/img/PawSquad/cover design-4.png'),
            static('assets/img/travel/travel d1.png'),
            static('assets/img/travel/travel d2.png'),
            static('assets/img/travel/travel d3.png'),
            static('assets/img/travel/travel d4.png')
        ]
        for Details_imageurl,OverviewTitle,OverviewPara,ApproachTitle,ApproachPara in zip(
              Details_imageurl,OverviewTitle,OverviewPara,ApproachTitle,ApproachPara
            ): 
            Designpost.objects.create(
                 Details_imageurl=Details_imageurl,
                 OverviewTitle=OverviewTitle,
                 OverviewPara=OverviewPara,
                 ApproachTitle=ApproachTitle,
                 ApproachPara=ApproachPara
            )

         
        self.stdout.write(self.style.SUCCESS("details inserting post details data!"))