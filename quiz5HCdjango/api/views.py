
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Pacientes, Especialidades, Doctores, Citas, DoctoresEspecialidadeses
from .serializers import PacientesSerializer, EspecialidadesSerializer, DoctoresSerializer, CitasSerializer, DoctoresEspecialidadesesSerializer

class PacientesListCreateView(ListCreateAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer

class PacientesRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer
    
class EspecialidadesListCreateView(ListCreateAPIView):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer

class EspecialidadesRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer

class DoctoresListCreateView(ListCreateAPIView):
    queryset = Doctores.objects.all()
    serializer_class = DoctoresSerializer

class DoctoresRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Doctores.objects.all()
    serializer_class = DoctoresSerializer
    

class CitasListCreateView(ListCreateAPIView):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer
    
class CitasListRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

class DoctoresEspecialidadesesListCreateView(ListCreateAPIView):
    queryset = DoctoresEspecialidadeses.objects.all()
    serializer_class = DoctoresEspecialidadesesSerializer
    
class DoctoresListRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = DoctoresEspecialidadeses.objects.all()
    serializer_class = DoctoresEspecialidadesesSerializer
