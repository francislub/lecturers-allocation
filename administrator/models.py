from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
#from administrator.models import CustomUser, Department
class Course(models.Model):
    # Existing fields
    
    id = models.CharField(primary_key=True, max_length=100)
    coursename = models.CharField(max_length=300, null=True, blank=True)
    semester = models.CharField(max_length=255, null=True, blank=True)
    
SEMESTER_CHOICES = (
    ('F', 'First Semester'),
    ('S', 'Second Semester'),
)
Qualification_CHOICES = (
    ('D', 'Degree'),
    ('DM', 'Degree - Masters'),
    ('DMP', 'Degree - Masters - PhD'),
)
publication_CHOICES = (
    ('N', 'None '),
    ('1', '1 to 2 Papers'),
    ('3', '3 to 4 Papers'),
    ('5', '5 to 6 Papers'),
    ('7', '7 to 8 Papers'),
    ('9', '9 and above'),
)
    
class Lecturer(models.Model):
    # Existing fields
    #requester = models.ForeignKey(CustomUser, related_name='requested_requisitions', on_delete=models.CASCADE)
    requester_signature= models.ImageField(upload_to='requester_signatures/')
    
    id = models.CharField(primary_key=True, max_length=100)
    LECTERER_NAME_REGEX = r'^[A-Za-z\s]+$'  # Allows letters and spaces
    lecturername = models.CharField(max_length=200, validators=[RegexValidator(LECTERER_NAME_REGEX, 'Only letters and spaces allowed for lecturer name')], null=True, blank=True)
    qualification = models.CharField(max_length=255,choices=Qualification_CHOICES, null=True, blank=True)
    #publication = models.CharField(max_length=255 , choices=publication_CHOICES , null=True, blank=True)
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES, null=True, blank=True)
    
    
    received_by = models.CharField(max_length=100, null=True, blank=True)
    date_received = models.DateTimeField(null=True, blank=True)
    cashier_signature = models.ImageField(upload_to='cashier_signatures/', null=True, blank=True)
    receiver_signature = models.ImageField(upload_to='receiver_signatures/', null=True, blank=True)
    voucher_number = models.CharField(max_length=100, null=True, blank=True)
    #supervisor = models.ForeignKey(CustomUser, related_name='supervised_requisitions', on_delete=models.CASCADE, null=True,)
    supervisor_comment = models.TextField(blank=True)
    supervisor_approval_date = models.DateTimeField(null=True, blank=True)
    phase = models.IntegerField(default=1)  
    STATUS_CHOICES = [
        ('Pending Supervisor Approval', 'Pending Supervisor Approval'),
        ('Pending Approver Approval', 'Pending Approver Approval'),
        ('Business Approval 1', 'Business Approval 1'),
        ('Business Approval 2', 'Business Approval 2'),
        ('Business Approval 3', 'Business Approval 3'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('Cash Out', 'Cash Out'),
    ]
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending Supervisor Approval')
    
    
    @property
    def requester_signature(self):
        return f"/media/requester_signatures/{self.requester.first_name.lower()}_{self.requester.last_name.lower()}.png"

    @property
    def supervisor_signature(self):
        if self.supervisor:
            return f"/media/supervisor_signatures/{self.supervisor.first_name.lower()}_{self.supervisor.last_name.lower()}.png"
        return ""

    @property
    def approver_signature(self):
        if self.approver:
            return f"/media/approver_signatures/{self.approver.first_name.lower()}_{self.approver.last_name.lower()}.png"
        return ""

    @property
    def cashier_signature_filename(self):
        return f"/media/cashier_signatures/{self.cashier_signature.name.split('/')[-1]}"

    @property
    def receiver_signature_filename(self):
        return f"/media/receiver_signatures/{self.receiver_signature.name.split('/')[-1]}"
    
    def __str__(self):
        return f"Requisition #{self.pk}"
