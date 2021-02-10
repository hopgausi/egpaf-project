from django.db import models
import datetime

class Patient(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    district = models.CharField(max_length=150)
    village = models.CharField(max_length=250)

    OCCUPATION_CHOICES = (
        ('Teacher', 'Teacher'),
        ('Nurse', 'Nurse'),
        ('Farmer', 'Farmer'),
        ('House Wife', 'House Wife'),
        ('Technician', 'Technician'),
        ('Student', 'Student'),

    )
    occupation = models.CharField(max_length=100, choices=OCCUPATION_CHOICES)

    class Meta:
        ordering = ['last_name']

    
    def save(self, *args, **kwargs): 
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        self.district = self.district.title()
        self.village = self.village.title()
        super(Patient, self).save(*args, **kwargs)


    def __str__(self):
        return self.first_name


class Assessment(models.Model):
    ICD10CM_CODES = (
        ('A00-B99', ' Certain infectious and parasitic diseases'),
        ('C00-D49',  'Neoplasms'),
        ('D50-D89',  'Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism'),
        ('E00-E89',  'Endocrine, nutritional and metabolic diseases'),
        ('F01-F99', 'Mental, Behavioral and Neurodevelopmental disorders'),
        ('G00-G99', 'Diseases of the nervous system'),
        ('H00-H59',  'Diseases of the eye and adnexa'),
        ('H60-H95', 'Diseases of the ear and mastoid process'),
        ('I00-I99', 'Diseases of the circulatory system'),
        ('J00-J99', 'Diseases of the respiratory system'),
        ('K00-K95', 'Diseases of the digestive system'),
        ('L00-L99', 'Diseases of the skin and subcutaneous tissue'),
        ('M00-M99', 'Diseases of the musculoskeletal system and connective tissue'),
        ('N00-N99', 'Diseases of the genitourinary system'),
        ('O00-O9A', 'Pregnancy, childbirth and the puerperium'),
        ('P00-P96', 'Certain conditions originating in the perinatal period'),
        ('Q00-Q99', 'Congenital malformations, deformations and chromosomal abnormalities'),
        ('R00-R99', 'Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified'),
        ('S00-T88', 'Injury, poisoning and certain other consequences of external causes'),
        ('U00-U85',  'Codes for special purposes'),
        ('V00-Y99', 'External causes of morbidity'),
        ('Z00-Z99', 'Factors influencing health status and contact with health services'),
    )
    visit_date = models.DateField(auto_now=False, auto_now_add=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    diagnosis = models.CharField(max_length=15, choices=ICD10CM_CODES)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-visit_date']

    def save(self, *args, **kwargs): 
        self.height = self.height / 100
        super(Assessment, self).save(*args, **kwargs) 

    def __str__(self):
        return self.diagnosis
    


