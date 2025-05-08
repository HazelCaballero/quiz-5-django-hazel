from django.urls import path
from .views import PacientesListCreateView, PacientesRetrieveUpdateDestroyView, EspecialidadesListCreateView, EspecialidadesRetrieveUpdateDestroyView, DoctoresListCreateView, DoctoresRetrieveUpdateDestroyView, CitasListCreateView, CitasListRetrieveUpdateDestroyView, DoctoresEspecialidadesesListCreateView, DoctoresListRetrieveUpdateDestroyView

urlpatterns = [
    path('pacientes/', PacientesListCreateView.as_view(), name='pacientes-list-create'),
    path('pacientes/<int:pk>/', PacientesRetrieveUpdateDestroyView.as_view(), name='pacientes-retrieve-update-destroy'),
    path('especialidades/', EspecialidadesListCreateView.as_view(), name='pacientes-list-create'),
    path('especialidades/<int:pk>/', EspecialidadesRetrieveUpdateDestroyView.as_view(), name='pacientes-retrieve-update-destroy'),
    path('doctores/', DoctoresListCreateView.as_view(), name='doctores-list-create'),
    path('doctores/<int:pk>/', DoctoresRetrieveUpdateDestroyView.as_view(), name='doctores-retrieve-update-destroy'),
    path('citas/', CitasListCreateView.as_view(), name='citas-list-create'),
    path('citas/<int:pk>/', CitasListRetrieveUpdateDestroyView.as_view(), name='citas-retrieve-update-destroy'),
    path('doctores-especialidades/', DoctoresEspecialidadesesListCreateView.as_view(), name='doctores-especialidades-list-create'),
    path('doctores-especialidades/<int:pk>/', DoctoresListRetrieveUpdateDestroyView.as_view(), name='doctores-especialidades-retrieve-update-destroy')
]
