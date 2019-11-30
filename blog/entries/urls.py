from django.urls import path

from .views import HomeView, EntryView, CreteEntryView

urlpatterns = [
    path('', HomeView.as_view(), name = 'blog-home'),
    path('entry/<int:pk>/', EntryView.as_view(), name="entry-detail"),
    path('create_entry', CreteEntryView.as_view(success_url="/"), name="create-entry" )
]
