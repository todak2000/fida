from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
# USER
class User(models.Model):
    class Meta:
        db_table = "Fida_user_table"
    # personal details
    user_id = models.CharField(max_length=500,unique=True)
    firstname = models.CharField(max_length=30,verbose_name="Firstname",blank=True)
    lastname = models.CharField(max_length=30,verbose_name="Lastname",blank=True)
    user_phone = models.TextField(max_length=15, unique=True, null=True, verbose_name="Telephone number")
    email = models.EmailField(max_length=90, unique=True,verbose_name="Email")
    user_password = models.TextField(max_length=200,verbose_name="Password")
    user_address = models.TextField(max_length=200,verbose_name="Address")
    user_state = models.TextField(max_length=200,verbose_name="State")
    ratings = models.IntegerField(max_length=200,verbose_name="Job Ratings", default=1.0)
    role = models.TextField(max_length=50,verbose_name="User role",default="client")
    walletBalance = models.FloatField(verbose_name="Balance",default=0.00)
    # account details
    account_name = models.TextField(max_length=150,verbose_name="Account Name",default="Null")
    account_number = models.TextField(max_length=150,verbose_name="Account Number",default="0000000000")
    bank_name = models.TextField(max_length=150,verbose_name="Bank Name",default="Null")

    # compliance with fida's rules
    profile_complete = models.BooleanField(default=False)
    terms_conditions = models.BooleanField(default=False)
    
    #notification toggle
    notification = models.BooleanField(default=False, verbose_name="Notification toggle")
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_id} - {self.firstname} - {self.lastname} - {self.user_phone} - {self.email} - {self.user_state} - {self.role} - {self.walletBalance}"

class Ads(models.Model):
    class Meta:
        db_table = "Ads_table"
    # Artisans Ads
    artisan_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name="Ad Title",blank=True)
    description = models.CharField(max_length=500,verbose_name="Ad Description",blank=True)
    duration = models.TextField(max_length=15,  null=True, verbose_name="Duration")
    min_budget = models.TextField(max_length=90, verbose_name="Minimum Budget")
    max_budget = models.TextField(max_length=200,verbose_name="Maximum Budget")
    location = models.TextField(max_length=200,verbose_name="Location")
    state = models.TextField(max_length=200,verbose_name="State")
    other_info = models.TextField(max_length=200,verbose_name="Other Information")
    no_of_views = models.IntegerField(verbose_name="No of Views", default=0)
    
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.artisan_id} - {self.title} - {self.min_budget} - {self.max_budget} - {self.state}- {self.no_of_views}"

class Orders(models.Model):
    class Meta:
        db_table = "Orders_table"
    # Client Orders
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name="Ad Title",blank=True)
    description = models.CharField(max_length=500,verbose_name="Ad Description",blank=True)
    duration = models.TextField(max_length=15,  null=True, verbose_name="Duration")
    min_budget = models.TextField(max_length=90, verbose_name="Minimum Budget")
    max_budget = models.TextField(max_length=200,verbose_name="Maximum Budget")
    location = models.TextField(max_length=200,verbose_name="Location")
    state = models.TextField(max_length=200,verbose_name="State")
    service_fee = models.TextField(max_length=200,verbose_name="Service fee")
    pitch = models.TextField(max_length=200,verbose_name="Pitch")
    noOfBidders = models.IntegerField(max_length=15,  default=0, verbose_name="No of Bidders")
    orderStatus = models.TextField(max_length=15,  default='pending', verbose_name="Order Status")
    winner_id = models.CharField(max_length=500,verbose_name="Bid Winner", null=True)
    winner_accept = models.BooleanField(default=False, verbose_name="Did Winner Accept Bid")
    from_ads = models.BooleanField(default=False, verbose_name="Order created from ads")
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.client_id} - {self.title} - {self.min_budget} - {self.max_budget} - {self.state} - {self.service_fee}"

class Verification(models.Model):
    class Meta:
        db_table = "Verification_table"
    # Verify Users
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField(max_length=20,verbose_name="Verification Code",blank=True)
    isVerified = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_id} - {self.code} - {self.isVerified}"

class Bids(models.Model): 
    class Meta:
        db_table = "Bids_table"
    # Bids
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    bidder = models.TextField(max_length=20,verbose_name="bidders", null=True)
    service_fee = models.TextField(max_length=200,verbose_name="Service fee", default="10")
    pitch = models.TextField(max_length=200,verbose_name="Pitch", default="hi")
    date_added = models.DateTimeField(default=timezone.now)
    declinedOffer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.order_id} - {self.bidder} - {self.service_fee} - {self.pitch}"

class Escrow(models.Model):
    class Meta:
        db_table = "Escrow_table"
    # Escrow 
    client_id = models.TextField(max_length=20,verbose_name="Client ID",null=True)
    artisan_id = models.TextField(max_length=20,verbose_name="Artisan ID",null=True)
    fees_agreed= models.CharField(max_length=500,verbose_name="Fees Agreed", null=True)
    project_id= models.TextField(max_length=500,verbose_name="Project ID", null=True)
    order_id= models.TextField(max_length=500,verbose_name="Order ID", null=True)
    commission = models.CharField(default=0,max_length=500, verbose_name="FIda's Commission",null=True)
    dispute = models.BooleanField(default=False, verbose_name="Did Client raise dispute")
    isPaid = models.BooleanField(default=False, verbose_name="Was payment made to Artisan")
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.client_id} - {self.artisan_id} - {self.fees_agreed} - {self.project_id} {self.dispute} - {self.isPaid}"

class Project_Gig(models.Model):
    class Meta:
        db_table = "Gig/Project Table"
    # Gigs/Projects
    order_id = models.TextField(max_length=20,verbose_name="Order ID",null=True)
    client_id = models.TextField(max_length=20,verbose_name="Client ID",null=True)
    artisan_id = models.TextField(max_length=20,verbose_name="Artisan ID",null=True)
    project_title= models.TextField(max_length=500,verbose_name="Project Title", null=True)
    canChat = models.BooleanField(default=False, verbose_name="Chat permission")
    projectStatus = models.TextField(max_length=15,  default='pending', verbose_name="Order Status")
    endProject = models.BooleanField(default=False, verbose_name="Was Projected ended")
    isCompleted = models.BooleanField(default=False, verbose_name="was Project completed") # sto be filled by artisan check options
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.order_id} - {self.client_id} - {self.artisan_id} - {self.project_title} - {self.canChat} {self.endProject} - {self.isCompleted}- {self.projectStatus}"

class Transaction(models.Model):
    class Meta:
        db_table = "Transaction Table"
    # Transactions
    from_id = models.TextField(max_length=20,verbose_name="Sending Party",null=True)
    to_id = models.TextField(max_length=20,verbose_name="Recieving Party",null=True)
    transaction_type = models.TextField(max_length=20,verbose_name="Type of Transaction",null=True)
    transaction_message= models.TextField(max_length=500,verbose_name="Message", null=True)
    projectCompleted = models.BooleanField(default=False, verbose_name="is Project completed")
    project_id = models.TextField(max_length=20,verbose_name="Project ID",null=True)
    amount = models.FloatField(verbose_name="Amount Sent",null=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.from_id} - {self.to_id} - {self.project_id} - {self.transaction_type} - {self.amount} {self.projectCompleted}"

class Chat(models.Model):
    class Meta:
        db_table = "Chat Table"
    # Chat
    from_id = models.TextField(max_length=20,verbose_name="Sending Party",null=True)
    to_id = models.TextField(max_length=20,verbose_name="Recieving Party",null=True)
    message= models.TextField(max_length=500,verbose_name="Message", null=True)
    projectCompleted = models.BooleanField(default=False, verbose_name="is Project completed")
    artisanRead = models.BooleanField(default=False, verbose_name="artisan has Read message")
    clientRead = models.BooleanField(default=False, verbose_name="client has Read message")
    project_id = models.TextField(max_length=20,verbose_name="Project ID",null=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.from_id} - {self.to_id} - {self.project_id} - {self.message} {self.projectCompleted}"