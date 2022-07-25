from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from .views import *
# Create your tests here.
class TestViews(TestCase):

    def test_index(self):
        #create new user with username and password
        user = User.objects.create(username='test')
        user.set_password('test1')
        user.save()

        # To login 
        client = Client()
        logged_in = client.login(username="test", password="test1")
        response = client.get(reverse(home))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_index_url(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)

    def test_case_url(self):
        url=reverse('customer_create')
        self.assertEquals(resolve(url).func,revie)

    def test_edit_url(self):
        url=reverse('name',args=['1'])
        self.assertEquals(resolve(url).func,ongoing)


class TestViews(TestCase):
    def test_delete(self):
        client=Client()
        c=revie.objects.create(
            description='textArea',
            rating='rate'
        )
        print("this")
        response=client.delete(reverse('revie_delete',args=[2]))

        self.assertEquals(response.status_code,302)


class TestUrls(TestCase):
    def test_login_page_url(self):
        url = reverse(login_page)
        print(url)
        self.assertEquals(resolve(url).func,login_page)

    def test_contact_url(self):
        url = reverse(contact)
        print(url)
        self.assertEquals(resolve(url).func,contact)

    def test_admin_home_url(self):
        url = reverse(admin_home)
        print(url)
        self.assertEquals(resolve(url).func,admin_home)

    
    
    def test_admin_home_Render(self):
        url = reverse(admin_home)
        print(url)
        self.assertEquals(resolve(url).func,admin_home)

User = get_user_model
class TestViews(TestCase):

    def test_admin_home_Render12(self):
        url = reverse(admin_home)
        response= self.assertEquals(resolve(url).func,admin_home)
        self.assertTemplateUsed(response, "admin/adminhome.html")
    
    
    def test_order(self):
        url = reverse(order)
        response= self.assertEquals(resolve(url).func,order)
        self.assertTemplateUsed(response, "admin/userorder.html")
    

    def test_user_display(self):
        url = reverse(user_display)
        response= self.assertEquals(resolve(url).func,user_display)
        self.assertTemplateUsed(response, 'admin/allusers.html')

      
    def test_admin_login(self):
        url = reverse(login_page)
        response= self.assertEquals(resolve(url).func,login_page)
        self.assertTemplateUsed(response, 'admin/admin_login.html')
    
          
    def test_contact(self):
        url = reverse(contact)
        response= self.assertEquals(resolve(url).func,contact)
        self.assertTemplateUsed(response, 'admin/admin_contact.html')
        
           
    def test_about(self):
        url = reverse(about)
        response= self.assertEquals(resolve(url).func,about)
        self.assertTemplateUsed(response, 'about.html')

          
    def test_main(self):
        url = reverse(main)
        response= self.assertEquals(resolve(url).func,main)
        self.assertTemplateUsed(response, 'main.html')

           
    def test_main(self):
        url = reverse(main)
        response= self.assertEquals(resolve(url).func,main)
        self.assertTemplateUsed(response, 'main.html')


    def test_product(self):
        url = reverse(orderPr)
        response= self.assertEquals(resolve(url).func,orderPr)
        self.assertTemplateUsed(response, 'checkout.html')