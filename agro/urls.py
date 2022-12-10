from unicodedata import name
from django.contrib import admin
from django.urls import path
from accounts import views as ac
from tables import views as tb


urlpatterns = [
    path('admin/', admin.site.urls),

    #accounts for normal user
    path('', ac.home, name='home'),
    path('register/', ac.registerPage, name='register'),
    path('login/', ac.loginPage, name='login'),
    path('logout/', ac.logoutuser, name='logout'),

    # accounts for expert
    path('exregister/', ac.registerexpert, name='expertregister'),
    path('exlogin/', ac.loginexpert, name='expertlogin'),


    #expert table
    path('issueexpert/', tb.issueexpert, name='issueexpert'),
    path('delexpertissue/<int:exissue_id>/', tb.delexpertissue, name='delexpertissue'),
    path('editexpertissue/<int:exissue_id>/', tb.editexpertissue, name='editexpertissue'),

    #tables
    #crop
    path('crudcrop/', tb.crudcrop, name='crudcrop'),
    path('deletecrop/<int:id>/', tb.deletecrop, name='deletecrop'),
    path('editcrop/<int:id>/', tb.editcrop, name='editcrop'), 

    #plot
    path('crudplot/', tb.crudplot, name='crudplot'),
    path('deleteplot/<int:plot_id>/', tb.deleteplot, name='deleteplot'),
    path('editplot/<int:plot_id>/', tb.editplot, name='editplot'),

    #plantation and harvesting
    path('crudplantationandharvesting/', tb.crudplantation, name='crudplantation'),
    path('editplantationandharvesting/<int:id>/',tb.editplantationandharvesting, name='editplantationandharvesting'),
    path('deleteplantationandharvesting/<int:id>/', tb.deleteplantationandharvesting , name='deleteplantationandharvesting'),

    #soil
    path('crudsoil/', tb.crudsoil, name='crudsoil'),
    path('deletesoil/<int:soil_id>/', tb.deletesoil, name='deletesoil'),
    path('editsoil/<int:soil_id>/', tb.editsoil, name='editsoil'),

    #tool
    path('crudtool/', tb.crudtool, name='crudtool'),
    path('deletetool/<int:tool_id>/', tb.deletetool, name='deletetool'),
    path('edittool/<int:tool_id>/', tb.edittool, name='edittool'),

    path('crudissue/', tb.crudissue, name='crudissue'),
    path('deleteissue/<int:issue_id>/', tb.deleteissue, name='deleteissue'),
    path('editissue/<int:issue_id>/', tb.editissue, name='editissue'),

    #otheruser accounr
    path('otherregister/', ac.otherregister, name='otherregister'),
    path('otherlogin/', ac.otherlogin, name='otherlogin'),

    path('otheruser/', tb.otheruser, name='otheruser'),

]