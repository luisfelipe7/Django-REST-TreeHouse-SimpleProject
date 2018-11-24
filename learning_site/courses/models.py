from django.db import models
# Create your models here.


class Course(models.Model):
    # This set the time automatically (DataTimeField)
    created_at = models.DateTimeField(auto_now_add=True)
    # This set the max length of the title (CharField)
    title = models.CharField(max_length=255)
    # This set the text of the descriptiob
    description = models.TextField(max_length=500)
    # URL Field
    url = models.URLField(unique=True, default='')

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    # In this way a single course can have multiple steps,but each step only have one course
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)  # or models.DO_NOTHING
    content = models.TextField(blank=True, default='')

    class Meta:
        # Order the elements by the order, example: ordering = ['field1', 'field2']
        ordering = ['order', ]

    def __str__(self):
        return self.title


class Review(models.Model):
    # A course can have multiples reviews and the review can stay in only one course
    course = models.ForeignKey(
        Course, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()
    rating = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['email', 'course']

    def __str__(self):
        return self.rating+" "+" by "+self.email+" for "+self.course
