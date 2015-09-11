from django.db import models

# Create your models here.
class Log(models.Model):
    value       = models.IntegerField()
    number      = models.IntegerField()
    occurrences = models.IntegerField(default=0)

    def do_calc(self, n):
        n1 = 0
        n2 = 0
        for i in xrange(1, n +1):
            n1 += i * i
            n2 += i

        self.value  = abs(n1 - (n2 * n2))
        self.number = n

