from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from notifications.models import Notification
from rest_framework import status

class NotificationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user, read=False).order_by('-timestamp')
        # Serialize notifications and send back
        # You can create a serializer for notifications as needed
        return Response({"notifications": notifications}, status=status.HTTP_200_OK)
