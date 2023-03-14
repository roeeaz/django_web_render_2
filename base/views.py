from .models import Product, Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

@api_view(['GET'])
def index(request):
    return Response("test")

def test(request):
    return Response({"public":"a"})


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# register
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")


class MyModelView(APIView):
    def get(self, request, pk=-1):  # axios.get
        if int(pk) > -1:
            my_model = Product.objects.get(id=int(pk))
            serializer = ProductSerializer(my_model, many=False)
        else:
            my_model = Product.objects.all()
            serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):  # axios.post
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):  # axios.put
        my_model = Product.objects.get(pk=pk)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # axios.delete
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    def create(self, validated_data):
        user = self.context['user']
        print(user)
        return Student.objects.create(**validated_data,user=user)
    
@permission_classes([IsAuthenticated])
class student_Views(APIView):
    def get(self, request, pk=-1):  # axios.get
        if pk > -1:
            my_model = Student.objects.get(id=pk)
            serializer = StudentSerializer(my_model, many=False)
        else:
            # my_model = Student.objects.all()
            my_model = request.user.student_set.all()
            serializer = StudentSerializer(my_model, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):  # axios.post
        print(request.user)
        serializer = StudentSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):  # axios.put
        my_model = Student.objects.get(pk=pk)
        serializer = StudentSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # axios.delete
        my_model = Student.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
