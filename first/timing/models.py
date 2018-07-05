from django.db import models


# Create your models here.
class Meeting(models.Model):
    start = models.DateTimeField(null=True, default=None, help_text='开始时间')
    end = models.DateTimeField(null=True, default=None, help_text='结束时间')
    state = models.CharField(max_length=32, default='未开始', help_text='状态')
    dif = models.DateTimeField(null=True, default=None, help_text='时间差')

    def save_me(self, request):
        start = request.POST.get('start', None)
        end = request.POST.get('end', None)

        self.start = start
        self.end = end
        # self.dif = (self.end - self.start)
        self.save()
        return self
