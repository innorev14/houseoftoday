from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Review)
def post_save(sender, **kwargs):
   pd = kwargs['instance'].product
   pd.review_count = pd.reviews.count()
   pd.star_avg = pd.reivews.aggregate(Avg('star_score'))
   pd.save()


